#!/usr/bin/env python3

import json
import os
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from pathlib import Path
import pycountry

font_family = "Open Sans, Arial, sans-serif"


def iso2_to_iso3(iso2):
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except Exception:
        return None


def fetch_or_load_data(data_file="pet2bids_data.json"):
    """Fetch data from API or load from local file."""
    if not os.path.exists(data_file):
        print("Fetching data from API...")
        url = "http://openneuropet.org/check/pet2bids/"
        response = requests.get(url)
        data = response.json()

        # Save data locally
        with open(data_file, "w") as f:
            json.dump(data, f, indent=2)
        print("Data saved to local file")
    else:
        print("Loading data from local file...")
        with open(data_file, "r") as f:
            data = json.load(f)

    # Print debugging information
    print("\nData Structure Information:")
    print(f"Total number of entries: {len(data)}")
    if len(data) > 0:
        print("\nFirst entry structure:")
        print(json.dumps(data[0], indent=2))
        print("\nKeys in first entry:", list(data[0].keys()))
        if "content" in data[0]:
            print("\nKeys in content:", list(data[0]["content"].keys()))

    return data


def extract_locations(data):
    """Extract timestamp, latitude, longitude, and country code from each entry."""
    records = []
    for entry in data:
        timestamp = entry.get("timestamp")
        # Try top-level location
        location = entry.get("location")
        # Or nested in content
        if not location and "content" in entry:
            location = entry["content"].get("location")
        if location:
            latitude = location.get("latitude")
            longitude = location.get("longitude")
            country_code = location.get("countryCode")
            if country_code:
                country_code = iso2_to_iso3(country_code)
        else:
            latitude = longitude = country_code = None
        records.append(
            {
                "timestamp": timestamp,
                "latitude": latitude,
                "longitude": longitude,
                "country_code": country_code,
            }
        )
    return pd.DataFrame(records)


def plot_weekly_usage(df):
    """Create and return a weekly usage plot."""
    weekly_data = df.resample("W", on="timestamp").count().reset_index()
    fig = px.line(
        weekly_data,
        x="timestamp",
        y="latitude",
        title="Weekly Usage of pet2bids",
        labels={"timestamp": "Week", "latitude": "Number of Conversions"},
    )
    fig.update_layout(
        xaxis_title="Week", yaxis_title="Number of Conversions", template="plotly_white"
    )
    return fig


def plot_monthly_usage(df):
    """Create and return a monthly usage plot for the current month."""
    now = pd.Timestamp.now()
    current_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_data = df[
        df["timestamp"].apply(
            lambda x: x.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        )
        == current_month
    ].copy()
    monthly_data["day"] = monthly_data["timestamp"].dt.floor("D")
    daily_counts = monthly_data.groupby("day").size().reset_index(name="count")
    fig = px.line(
        daily_counts,
        x="day",
        y="count",
        title=f'Daily Usage of pet2bids for {current_month.strftime("%B %Y")}',
        labels={"day": "Day", "count": "Number of Conversions"},
    )
    fig.update_layout(
        xaxis_title="Day", yaxis_title="Number of Conversions", template="plotly_white"
    )
    return fig


def plot_point_map(df):
    """Create and return a point map of usage locations."""
    valid_locations = df.dropna(subset=["longitude", "latitude"])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None
    fig = px.scatter_geo(
        valid_locations,
        lat="latitude",
        lon="longitude",
        title="PET2BIDS Usage Locations",
    )
    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="rgb(243, 243, 243)",
            countrycolor="rgb(204, 204, 204)",
        ),
        template="plotly_white",
    )
    return fig


def plot_heatmap(df):
    """Create and return a heatmap of usage locations."""
    valid_locations = df.dropna(subset=["longitude", "latitude"])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None

    # Count occurrences at each location
    location_counts = (
        valid_locations.groupby(["latitude", "longitude"])
        .size()
        .reset_index(name="count")
    )

    # Add a small constant to avoid log(0)
    location_counts["log_count"] = np.log1p(location_counts["count"])

    # Create custom color scale ticks
    max_count = location_counts["count"].max()
    tick_values = np.log1p([1, 10, 100, 1000, 10000, max_count])
    tick_labels = [f"{int(np.expm1(x)):,}" for x in tick_values]

    # Create a rainbow color scale
    custom_colorscale = [
        [0, "rgb(0,0,255)"],  # Blue
        [0.2, "rgb(0,255,255)"],  # Cyan
        [0.4, "rgb(0,255,0)"],  # Green
        [0.6, "rgb(255,255,0)"],  # Yellow
        [0.8, "rgb(255,128,0)"],  # Orange
        [1, "rgb(255,0,0)"],  # Red
    ]

    fig = px.density_mapbox(
        location_counts,
        lat="latitude",
        lon="longitude",
        z="log_count",
        title="PET2BIDS Conversions Heatmap",
        zoom=1.1,
        mapbox_style="carto-positron",
        color_continuous_scale=custom_colorscale,
        range_color=[0, location_counts["log_count"].max()],
        labels={"log_count": "Number of Conversions"},
        hover_data={"count": True, "log_count": False},
    )

    fig.update_layout(
        title={
            "text": "PET2BIDS Conversions Heatmap",
            "x": 0.5,
            "xanchor": "center",
            "font": dict(size=28),
        },
        mapbox_style="carto-positron",
        template="plotly_white",
        coloraxis_colorbar=dict(
            title="Count",
            thicknessmode="pixels",
            thickness=20,
            lenmode="pixels",
            len=300,
            yanchor="middle",
            y=0.5,
            tickvals=tick_values,
            ticktext=tick_labels,
        ),
        margin=dict(l=0, r=0, t=80, b=0),
    )

    # Update hover template to show actual count
    fig.update_traces(
        hovertemplate="<b>Location</b><br>"
        + "Latitude: %{lat:.2f}<br>"
        + "Longitude: %{lon:.2f}<br>"
        + "Number of Conversions: %{customdata[0]:,}<br>"
        + "<extra></extra>"
    )

    return fig


def plot_country_map(df):
    """Create and return a country map of usage."""
    valid_locations = df.dropna(subset=["longitude", "latitude"])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None

    # Count usage by country
    country_counts = valid_locations["country_code"].value_counts().reset_index()
    country_counts.columns = ["country_code", "count"]

    # Log scaling and custom color scale (same as heatmap)
    country_counts["log_count"] = np.log1p(country_counts["count"])
    max_count = country_counts["count"].max()
    tick_values = np.log1p([1, 10, 100, 1000, 10000, max_count])
    tick_labels = [f"{int(np.expm1(x)):,}" for x in tick_values]
    custom_colorscale = [
        [0, "rgb(0,0,255)"],  # Blue
        [0.2, "rgb(0,255,255)"],  # Cyan
        [0.4, "rgb(0,255,0)"],  # Green
        [0.6, "rgb(255,255,0)"],  # Yellow
        [0.8, "rgb(255,128,0)"],  # Orange
        [1, "rgb(255,0,0)"],  # Red
    ]

    # Create the choropleth map using log_count
    fig = px.choropleth(
        country_counts,
        locations="country_code",
        color="log_count",
        title="PET2BIDS Usage by Country",
        color_continuous_scale=custom_colorscale,
        range_color=[0, country_counts["log_count"].max()],
        labels={"log_count": "Number of Conversions "},
        locationmode="ISO-3",
        hover_data={"count": True, "log_count": False},
    )

    # Update layout for better visibility
    fig.update_layout(
        title={
            "text": "PET2BIDS Usage by Country",
            "x": 0.5,
            "xanchor": "center",
            "font": dict(size=28, family=font_family),
        },
        template="plotly_white",
        geo=dict(
            showframe=True,
            showcoastlines=True,
            projection_type="equirectangular",
            coastlinecolor="white",
            showland=True,
            landcolor="lightgray",
            showocean=True,
            oceancolor="white",
            showlakes=True,
            lakecolor="white",
            showrivers=True,
            rivercolor="white",
            showcountries=True,
            countrycolor="white",
            # Consistent map scaling (zoom/center not available for geo, but keep layout similar)
        ),
        coloraxis_colorbar=dict(
            title="Number of Conversions",
            thicknessmode="pixels",
            thickness=20,
            lenmode="pixels",
            len=300,
            yanchor="middle",
            y=0.5,
            tickvals=tick_values,
            ticktext=tick_labels,
            titlefont=dict(size=20, family=font_family),
            tickfont=dict(size=16, family=font_family),
        ),
        margin=dict(l=0, r=0, t=80, b=0),
        font=dict(family=font_family, size=18),
    )

    # Add hover template to show country name and usage count
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br>"
        + "Number of Conversions: %{customdata[0]:,}<br>"
        + "<extra></extra>"
    )

    return fig


def plot_location_data_availability(df):
    """Create and return a plot comparing entries with and without location data."""
    # Count entries with and without location data
    total_entries = len(df)
    entries_with_location = df.dropna(subset=["latitude", "longitude"]).shape[0]
    entries_without_location = total_entries - entries_with_location

    # Create data for plotting
    location_data = pd.DataFrame(
        {
            "Category": ["With Location", "Without Location"],
            "Count": [entries_with_location, entries_without_location],
            "Percentage": [
                entries_with_location / total_entries * 100,
                entries_without_location / total_entries * 100,
            ],
        }
    )

    # Create the plot
    fig = px.bar(
        location_data,
        x="Category",
        y="Count",
        text=location_data["Percentage"].round(1).astype(str) + "%",
        title="PET2BIDS Entries: Location Data Availability",
        color="Category",
        color_discrete_sequence=["#2ecc71", "#e74c3c"],
    )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        yaxis_title="Number of Entries",
        xaxis_title="",
        annotations=[
            {
                "text": f"Total Entries: {total_entries:,}",
                "showarrow": False,
                "x": 0.5,
                "y": 1.1,
                "xref": "paper",
                "yref": "paper",
            }
        ],
    )

    # Update text position
    fig.update_traces(textposition="outside")

    return fig


def plot_catchup_time(df):
    """Create and return a plot showing the timeline projection of backlog processing."""
    # Calculate current backlog
    total_entries = len(df)
    entries_with_location = df.dropna(subset=["latitude", "longitude"]).shape[0]
    entries_without_location = total_entries - entries_with_location

    # Calculate catch-up time
    daily_cap = 2000
    days_to_catchup = entries_without_location / daily_cap

    # Create timeline data
    today = pd.Timestamp.now().normalize()
    dates = pd.date_range(start=today, periods=int(days_to_catchup) + 1, freq="D")
    backlog = [entries_without_location - (i * daily_cap) for i in range(len(dates))]
    backlog = [max(0, b) for b in backlog]  # Ensure we don't go below 0

    # Create DataFrame for plotting
    timeline_data = pd.DataFrame({"Date": dates, "Backlog": backlog})

    # Create the plot
    fig = px.line(
        timeline_data,
        x="Date",
        y="Backlog",
        title="Projected Backlog Processing Timeline",
        labels={"Backlog": "Number of Entries Without Location Data", "Date": "Date"},
    )

    # Add horizontal line for daily cap
    fig.add_shape(
        type="line",
        x0=today,
        y0=daily_cap,
        x1=dates[-1],
        y1=daily_cap,
        line=dict(
            color="gray",
            width=1,
            dash="dash",
        ),
    )

    # Add annotations
    fig.add_annotation(
        text=f"Daily Processing Capacity: {daily_cap:,} entries",
        xref="paper",
        yref="paper",
        x=0.98,
        y=0.98,
        showarrow=False,
        align="right",
        font=dict(size=14),
    )

    fig.add_annotation(
        text=f"Current Backlog: {entries_without_location:,} entries",
        xref="paper",
        yref="paper",
        x=0.98,
        y=0.93,
        showarrow=False,
        align="right",
        font=dict(size=14),
    )

    fig.add_annotation(
        text=f"Projected Completion: {dates[-1].strftime('%Y-%m-%d')}",
        xref="paper",
        yref="paper",
        x=0.98,
        y=0.88,
        showarrow=False,
        align="right",
        font=dict(size=14),
    )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        title=dict(
            text="Projected Backlog Processing Timeline",
            x=0.5,
            y=0.95,
            xanchor="center",
            yanchor="top",
            font=dict(size=20),
        ),
        xaxis=dict(
            title=dict(text="Date", font=dict(size=16)),
            showgrid=True,
            gridcolor="lightgray",
            tickfont=dict(size=14),
        ),
        yaxis=dict(
            title=dict(
                text="Number of Entries Without Location Data", font=dict(size=16)
            ),
            showgrid=True,
            gridcolor="lightgray",
            rangemode="tozero",
            tickfont=dict(size=14),
        ),
        hovermode="x unified",
        showlegend=False,
    )

    # Update hover template
    fig.update_traces(
        hovertemplate="<b>Date:</b> %{x|%Y-%m-%d}<br>"
        + "<b>Remaining Backlog:</b> %{y:,.0f} entries<br>"
        + "<extra></extra>"
    )

    return fig


def plot_total_usage(df):
    """Create and return a total usage plot over all time."""
    total_data = df.copy()
    total_data = total_data.sort_values("timestamp")
    # Group by day for a smooth line
    total_data["day"] = total_data["timestamp"].dt.floor("D")
    daily_counts = total_data.groupby("day").size().reset_index(name="count")
    fig = px.line(
        daily_counts,
        x="day",
        y="count",
        title="Cumulative PET2BIDS Conversion Count",
        labels={"day": "Date", "count": "Number of Conversions"},
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Number of Conversions",
        template="plotly_white",
        title={
            "text": "Total Usage of pet2bids Over Time",
            "x": 0.5,
            "xanchor": "center",
            "font": dict(size=28, family=font_family),
        },
        margin=dict(l=0, r=0, t=80, b=0),
        font=dict(family=font_family, size=18),
    )
    return fig


def plot_cumulative_usage(df):
    """Create and return a cumulative (running sum) usage plot over all time."""
    total_data = df.copy()
    total_data = total_data.sort_values("timestamp")
    total_data["day"] = total_data["timestamp"].dt.floor("D")
    daily_counts = total_data.groupby("day").size().reset_index(name="count")
    daily_counts["cumulative"] = daily_counts["count"].cumsum()
    fig = px.line(
        daily_counts,
        x="day",
        y="cumulative",
        title="Cumulative Conversions of pet2bids Over Time",
        labels={"day": "Date", "cumulative": "Cumulative Number of Conversions"},
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Cumulative Number of Conversions",
        template="plotly_white",
        title={
            "text": "Cumulative Conversions of pet2bids Over Time",
            "x": 0.5,
            "xanchor": "center",
            "font": dict(size=28, family=font_family),
        },
        margin=dict(l=0, r=0, t=80, b=0),
        font=dict(family=font_family, size=18),
    )
    return fig


def fetch_and_summarize_endpoints(endpoints):
    base_url = "http://openneuropet.org/check/"
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}/"
        data_file = f"{endpoint}_data.json"
        print(f"\n--- Fetching {endpoint} ---")
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            with open(data_file, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Saved {len(data)} entries to {data_file}")
            if len(data) > 0:
                print("First entry:")
                print(json.dumps(data[0], indent=2))
                print("Keys:", list(data[0].keys()))
                if "content" in data[0]:
                    print("Keys in content:", list(data[0]["content"].keys()))
            else:
                print("No entries returned.")
        except Exception as e:
            print(f"Error fetching {endpoint}: {e}")


def main():
    # Fetch data
    data = fetch_or_load_data()

    # Convert to DataFrame
    df = extract_locations(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Print quota information
    print("\nQuota Information:")
    print(f"Total number of entries: {len(df)}")
    entries_with_location = df.dropna(subset=["latitude", "longitude"]).shape[0]
    entries_without_location = len(df) - entries_with_location
    print(f"Number of entries with location data: {entries_with_location}")
    print(f"Number of entries missing location data: {entries_without_location}")

    # Generate and show plots in browser, and export as datestamped files
    print("\nGenerating and displaying plots...")
    date_str = datetime.now().strftime("%Y%m%d")

    fig_total = plot_total_usage(df)
    fig_total.show()
    fig_total.write_image(f"total_usage_{date_str}.png")
    fig_total.write_html(f"total_usage_{date_str}.html")

    fig_cumulative = plot_cumulative_usage(df)
    fig_cumulative.show()
    fig_cumulative.write_image(f"cumulative_usage_{date_str}.png")
    fig_cumulative.write_html(f"cumulative_usage_{date_str}.html")

    fig1 = plot_weekly_usage(df)
    fig1.show()
    fig1.write_image(f"weekly_usage_{date_str}.png")
    fig1.write_html(f"weekly_usage_{date_str}.html")

    fig2 = plot_monthly_usage(df)
    fig2.show()
    fig2.write_image(f"monthly_usage_{date_str}.png")
    fig2.write_html(f"monthly_usage_{date_str}.html")

    fig3 = plot_point_map(df)
    if fig3:
        fig3.show()
        fig3.write_image(f"point_map_{date_str}.png")
        fig3.write_html(f"point_map_{date_str}.html")

    fig4 = plot_heatmap(df)
    if fig4:
        fig4.show()
        fig4.write_image(f"heatmap_{date_str}.png")
        fig4.write_html(f"heatmap_{date_str}.html")

    fig5 = plot_country_map(df)
    if fig5:
        fig5.show()
        fig5.write_image(f"country_map_{date_str}.png")
        fig5.write_html(f"country_map_{date_str}.html")

    # Only plot location data availability and catchup time if missing entries >= 2000
    if entries_without_location >= 2000:
        fig6 = plot_location_data_availability(df)
        fig6.show()
        fig6.write_image(f"location_data_availability_{date_str}.png")
        fig6.write_html(f"location_data_availability_{date_str}.html")

        fig7 = plot_catchup_time(df)
        fig7.show()
        fig7.write_image(f"catchup_time_{date_str}.png")
        fig7.write_html(f"catchup_time_{date_str}.html")
    else:
        print(
            "\nLess than 2000 entries missing location data; skipping catch up and missing location plots."
        )

    print(
        "\nAll plots have been displayed in your browser and exported as datestamped image and HTML files!"
    )


if __name__ == "__main__":
    main()

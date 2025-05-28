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

def fetch_or_load_data(data_file="pet2bids_data.json"):
    """Fetch data from API or load from local file."""
    if not os.path.exists(data_file):
        print("Fetching data from API...")
        url = "http://openneuropet.org/check/pet2bids/"
        response = requests.get(url)
        data = response.json()
        
        # Save data locally
        with open(data_file, 'w') as f:
            json.dump(data, f, indent=2)
        print("Data saved to local file")
    else:
        print("Loading data from local file...")
        with open(data_file, 'r') as f:
            data = json.load(f)
    
    return data

def extract_locations(data):
    """Extract timestamp, latitude, longitude, and country code from each entry."""
    records = []
    for entry in data:
        timestamp = entry.get('timestamp')
        # Try top-level location
        location = entry.get('location')
        # Or nested in content
        if not location and 'content' in entry:
            location = entry['content'].get('location')
        if location:
            latitude = location.get('latitude')
            longitude = location.get('longitude')
            country_code = location.get('countryCode')
        else:
            latitude = longitude = country_code = None
        records.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude,
            'country_code': country_code
        })
    return pd.DataFrame(records)

def plot_weekly_usage(df):
    """Create and return a weekly usage plot."""
    weekly_data = df.resample('W', on='timestamp').count().reset_index()
    fig = px.line(weekly_data, x='timestamp', y='latitude',
                  title='Weekly Usage of pet2bids',
                  labels={'timestamp': 'Week', 'latitude': 'Number of Queries'})
    fig.update_layout(xaxis_title='Week', yaxis_title='Number of Queries', template='plotly_white')
    return fig

def plot_monthly_usage(df):
    """Create and return a monthly usage plot for the current month."""
    now = pd.Timestamp.now()
    current_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_data = df[df['timestamp'].apply(lambda x: x.replace(day=1, hour=0, minute=0, second=0, microsecond=0)) == current_month].copy()
    monthly_data['day'] = monthly_data['timestamp'].dt.floor('D')
    daily_counts = monthly_data.groupby('day').size().reset_index(name='count')
    fig = px.line(daily_counts, x='day', y='count',
                  title=f'Daily Usage of pet2bids for {current_month.strftime("%B %Y")}',
                  labels={'day': 'Day', 'count': 'Number of Queries'})
    fig.update_layout(xaxis_title='Day', yaxis_title='Number of Queries', template='plotly_white')
    return fig

def plot_point_map(df):
    """Create and return a point map of usage locations."""
    valid_locations = df.dropna(subset=['longitude', 'latitude'])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None
    fig = px.scatter_geo(valid_locations,
                        lat='latitude',
                        lon='longitude',
                        title='PET2BIDS Usage Locations')
    fig.update_layout(geo=dict(showland=True, landcolor='rgb(243, 243, 243)', countrycolor='rgb(204, 204, 204)'), template='plotly_white')
    return fig

def plot_heatmap(df):
    """Create and return a heatmap of usage locations."""
    valid_locations = df.dropna(subset=['longitude', 'latitude'])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None
    fig = px.density_mapbox(valid_locations,
                        lat='latitude',
                        lon='longitude',
                        title='PET2BIDS Usage Heatmap',
                        zoom=1)
    fig.update_layout(mapbox_style='carto-positron', template='plotly_white')
    return fig

def plot_country_map(df):
    """Create and return a country map of usage."""
    valid_locations = df.dropna(subset=['longitude', 'latitude'])
    if len(valid_locations) == 0:
        print("No valid location data available for plotting")
        return None
    country_counts = valid_locations['country_code'].value_counts().reset_index()
    country_counts.columns = ['country_code', 'count']
    fig = px.choropleth(country_counts,
                        locations='country_code',
                        color='count',
                        title='PET2BIDS Usage by Country',
                        color_continuous_scale='Reds')
    fig.update_layout(template='plotly_white')
    return fig

def main():
    # Fetch or load data
    data = fetch_or_load_data()
    
    # Extract relevant fields into DataFrame
    df = extract_locations(data)
    
    # Convert timestamp to datetime using ISO8601 format
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')
    
    # Create and show usage plots
    print("Generating weekly usage plot...")
    weekly_fig = plot_weekly_usage(df)
    weekly_fig.show()
    
    print("Generating monthly usage plot...")
    monthly_fig = plot_monthly_usage(df)
    monthly_fig.show()
    
    # Create and show map plots
    print("Generating point map...")
    point_fig = plot_point_map(df)
    if point_fig:
        point_fig.show()
    
    print("Generating heatmap...")
    heat_fig = plot_heatmap(df)
    if heat_fig:
        heat_fig.show()
    
    print("Generating country map...")
    country_fig = plot_country_map(df)
    if country_fig:
        country_fig.show()

if __name__ == "__main__":
    main() 
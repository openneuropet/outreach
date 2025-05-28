# Install required libraries if not already installed
if (!requireNamespace("httr", quietly = TRUE)) install.packages("httr", repos = "https://cloud.r-project.org")
if (!requireNamespace("jsonlite", quietly = TRUE)) install.packages("jsonlite", repos = "https://cloud.r-project.org")
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2", repos = "https://cloud.r-project.org")
if (!requireNamespace("maps", quietly = TRUE)) install.packages("maps", repos = "https://cloud.r-project.org")
if (!requireNamespace("MASS", quietly = TRUE)) install.packages("MASS", repos = "https://cloud.r-project.org")
if (!requireNamespace("hexbin", quietly = TRUE)) install.packages("hexbin", repos = "https://cloud.r-project.org")

# Load required libraries
library(httr)
library(jsonlite)
library(ggplot2)
library(maps)
library(MASS)

# Define the URL to fetch data from
url <- "http://openneuropet.org/check/pet2bids/"

# Fetch the JSON data from the URL
response <- GET(url)
data <- content(response, "text")
json_data <- fromJSON(data)

# Extract latitude and longitude from the JSON data
locations <- json_data$location

# Remove rows with NA values in longitude or latitude
locations <- locations[!is.na(locations$longitude) & !is.na(locations$latitude), ]

# Print summary of the data
print("Summary of locations data:")
print(summary(locations))

# Plot the locations on a map
world_map <- map_data("world")
world_map$region <- iso.alpha(world_map$region)

plot1 <- ggplot() +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_point(data = locations, aes(x = longitude, y = latitude), color = "red", size = 2) +
  theme_minimal() +
  labs(title = "Pet2bids Usage", x = "Longitude", y = "Latitude")

# Plot heatmap only if we have valid data points
if(nrow(locations) > 0) {
  bandwidth <- 100
  locations_kde2d <- kde2d(locations$longitude, locations$latitude, 
                           h = c(20,10), 
                           n = bandwidth, lims = c(-180, 180, -90, 90))
  locations_density <- expand.grid(long=locations_kde2d$x, 
                                   lat=locations_kde2d$y)
  locations_density$density <- as.vector(locations_kde2d$z) * nrow(locations)*bandwidth

  plot2 <- ggplot(data=locations) +
    geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
    geom_raster(data=locations_density, aes(x = long, y = lat, alpha=density, fill=density)) +
    scale_fill_viridis_c(trans=scales::pseudo_log_trans()) +  # Log scaling above 1
    scale_alpha(range=c(0,1), trans=scales::pseudo_log_trans()) +
    theme_minimal() +
    guides(fill="none", alpha="none") +
    labs(title = "Pet2bids Usage", x = "Longitude", y = "Latitude")
} else {
  warning("No valid location data available for heatmap")
}

# Plot countrymap
# Only tally countries with valid location data
dat_with_country <- locations[!is.na(locations$country_code) & locations$country_code != "", ]
countrytally <- as.data.frame(table(dat_with_country$country_code))
colnames(countrytally)[1] <- c("region")

# Debug prints
print("Head of countrytally:")
print(head(countrytally))
print("Unique regions in world_map:")
print(unique(world_map$region))

if (nrow(countrytally) > 0) {
  world_map_tally <- merge(world_map, countrytally, all.x = TRUE)
  world_map_tally$Freq = ifelse(is.na(world_map_tally$Freq), 
                                yes=0, no = world_map_tally$Freq)

  plot3 <- ggplot(data=locations) +
    geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
    geom_map(data=countrytally, aes(map_id = region, fill = Freq), map = world_map) +
    scale_fill_viridis_c("Count", 
                         trans=scales::pseudo_log_trans(), 
                         labels = scales::label_comma(),
                         breaks=c(1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6)) +  # Log scaling above 1
    theme_minimal() +
    labs(title = "Pet2bids Usage", x = "Longitude", y = "Latitude")
} else {
  warning("No valid country tally data available for country map plot")
}

# Plot hexmap
plot4 <- ggplot(data=locations) +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_hex(data=locations, aes(x=longitude, y=latitude), alpha=0.5, bins=50) +
  scale_fill_viridis_c("Count", 
                       trans=scales::pseudo_log_trans(), 
                       labels = scales::label_comma(),
                       breaks=c(1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6)) +  # Log scaling above 1
  scale_alpha(range=c(0,1), trans=scales::pseudo_log_trans()) +
  theme_minimal() +
  labs(title = "Pet2bids Usage", x = "Longitude", y = "Latitude")

# Save plots
ggsave("locations_pointplot.png", plot = plot1)
cat("Saved locations_pointplot.png\n")
if(exists("plot2")) {
  ggsave("locations_heatmap.png", plot = plot2)
  cat("Saved locations_heatmap.png\n")
}
if (exists("plot3")) {
  ggsave("locations_countrymap.png", plot = plot3)
  cat("Saved locations_countrymap.png\n")
}
if (exists("plot4")) {
  ggsave("locations_hexmap.png", plot = plot4)
  cat("Saved locations_hexmap.png\n")
}


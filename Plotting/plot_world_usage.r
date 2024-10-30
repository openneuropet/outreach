# Install required libraries if not already installed
if (!requireNamespace("httr", quietly = TRUE)) install.packages("httr")
if (!requireNamespace("jsonlite", quietly = TRUE)) install.packages("jsonlite")
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("maps", quietly = TRUE)) install.packages("maps")

# Load required libraries

library(httr)
library(jsonlite)
library(ggplot2)
library(maps)

# Define the URL to fetch data from
url <- "http://openneuropet.org/check/pet2bids/"

# Fetch the JSON data from the URL
response <- GET(url)
data <- content(response, "text")
json_data <- fromJSON(data)

print(json_data)

# Extract latitude and longitude from the JSON data
locations <- json_data$location

# print out all the locations
print(locations)

table(locations$country_name_map)


# Plot the locations on a map
world_map <- map_data("world")
world_map$region <- iso.alpha(world_map$region)

plot1 <- ggplot() +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_point(data = locations, aes(x = longitude, y = latitude), color = "red", size = 2) +
  theme_minimal() +
  labs(title = "Locations from JSON Data", x = "Longitude", y = "Latitude")


# Plot heatmap
bandwidth <- 100

locations_kde2d <- MASS::kde2d(locations$longitude, locations$latitude, 
                               h = c(20,10), 
                               n = bandwidth, lims = c(-180, 180, -90, 90))
locations_density <- expand.grid(long=locations_kde2d$x, 
                                 lat=locations_kde2d$y)
locations_density$density <- as.vector(locations_kde2d$z) * nrow(locations)*bandwidth

plot2 <- ggplot(data=locations) +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_raster(data=locations_density, aes(x = long, y = lat, alpha=density, fill=density)) +
  scale_fill_viridis_c(trans=scales::transform_pseudo_log()) +  # Log scaling above 1
  scale_alpha(range=c(0,1), trans=scales::transform_pseudo_log()) +
  theme_minimal() +
  guides(fill="none", alpha="none") +
  labs(title = "Locations from JSON Data", x = "Longitude", y = "Latitude")


# Plot countrymap
countrytally <- as.data.frame(table(locations$country_code))
colnames(countrytally)[1] <- c("region")

world_map_tally <- merge(world_map, countrytally)
world_map_tally$Freq = ifelse(is.na(world_map_tally$Freq), 
                              yes=0, no = world_map_tally$Freq)

plot3 <- ggplot(data=locations) +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_map(data=countrytally, aes(map_id = region, fill = Freq), map = world_map) +
  scale_fill_viridis_c("Count", 
                       trans=scales::transform_pseudo_log(), 
                       labels = scales::label_comma(),
                       breaks=c(1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6)) +  # Log scaling above 1
  theme_minimal() +
  # guides(fill="none") +
  labs(title = "Locations from JSON Data", x = "Longitude", y = "Latitude")

# Plot hexmap
plot4 <- ggplot(data=locations) +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_hex(data=locations, aes(x=longitude, y=latitude), alpha=0.5, bins=50) +
  scale_fill_viridis_c("Count", 
                       trans=scales::transform_pseudo_log(), 
                       labels = scales::label_comma(),
                       breaks=c(1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6)) +  # Log scaling above 1
  scale_alpha(range=c(0,1), trans=scales::transform_pseudo_log()) +
  theme_minimal() +
  # guides(fill="none") +
  labs(title = "Locations from JSON Data", x = "Longitude", y = "Latitude")


# Save plots
ggsave("locations_pointplot.png", plot = plot1)
ggsave("locations_heatmap.png", plot = plot2)
ggsave("locations_countrymap.png", plot = plot3)
ggsave("locations_hexmap.png", plot = plot4)

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
locations <- lapply(json_data, function(x) {
  list(latitude = x$location$latitude, longitude = x$location$longitude)
})

# print out all the locations
print(locations)

locations_df <- do.call(rbind, lapply(locations, as.data.frame))

# Plot the locations on a map
world_map <- map_data("world")
plot <- ggplot() +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgray", color = "white") +
  geom_point(data = locations_df, aes(x = longitude, y = latitude), color = "red", size = 2) +
  theme_minimal() +
  labs(title = "Locations from JSON Data", x = "Longitude", y = "Latitude")

# Save the plot to a file
ggsave("locations_plot.png", plot = plot)

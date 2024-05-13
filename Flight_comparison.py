our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# Destinations unique to your airline
unique_to_our_airline = our_routes.difference(competitor_routes)

# Destinations unique to competitor's airline
unique_to_competitor_airline = competitor_routes.difference(our_routes)

# Destinations that neither airline shares
neither_airline_shares = our_routes.symmetric_difference(competitor_routes)

print("Destinations both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_to_our_airline)
print("Destinations unique to competitor's airline:", unique_to_competitor_airline)
print("Destinations that neither airline shares:", neither_airline_shares)

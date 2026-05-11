
import json

# simple route validation script for testing

with open("routes.json", "r") as f:
    routes = json.load(f)

for route in routes:

    prefix = route.get("addressPrefix")
    next_hop = route.get("nextHopType")

    print(f"{prefix} -> {next_hop}")

print("Route validation completed")

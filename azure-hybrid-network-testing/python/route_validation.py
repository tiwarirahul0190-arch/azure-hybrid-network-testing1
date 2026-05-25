import json

# basic route validation script
# mainly used during route table testing

with open("routes.json", "r") as f:
    routes = json.load(f)

print("Checking routes")
print("----------------")

for route in routes:

    prefix = route.get("addressPrefix")
    next_hop = route.get("nextHopType")

    print(f"{prefix} -> {next_hop}")

    if next_hop == "Internet":
        print("Warning: internet route detected")

if len(routes) == 0:
    print("no routes found")

print("---------------------")
print(f"Validated total routes: {len(routes)}")
print ("validation compelted")
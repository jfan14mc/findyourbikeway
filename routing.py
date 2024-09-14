import openrouteservice


coords = ((8.34234,48.23424),(8.34423,48.26424))

client = openrouteservice.Client(key='5b3ce3597851110001cf6248dbbdc789398f41cfa1403cf2b18e5bdf') # Specify your personal API key
routes = client.directions(coords, profile="cycling-regular")

print(routes)
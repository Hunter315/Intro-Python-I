"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictinaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "USA"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "Canada"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "Africa"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
    "lat": 22,
    "lon": -181,
    "name": "Mexico"
})

print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for i in waypoints:
    print (i)
    print (i['lat'])
    print (i['lon'])
    print (i['name'])
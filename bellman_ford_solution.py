def calculateMoves(src, dest, n):

    # create a set of edges and vertices to use in Bellman Ford
    edges = set()
    vertices = set()

    # initialize all of the possible edges and vertices
    i = 0
    while i < (n * n):
        vertices.add(getXY(i, n))
        edges = (mapPossibleMoves(edges, getXY(i, n), n))
        i += 1

    # compute minimum distances and return the distance to the destination node
    return bellmanFord(vertices, edges, getXY(src, n), getXY(dest, n))

# helper function to switch coordinates to an x-y type system
def getXY(i, n):
    x = i % n
    y = int(i / n)
    return (x,y)

def getNum(i, n):
    return (i[1] * n) + (i[0] % n)

# helper function to add as many of the 8 moves are possible for a given coordinate
def mapPossibleMoves(graph, coordinate_vals, n):
    x, y = coordinate_vals

    # up and to the left
    if (checkCoordinates((x - 1, y - 2), n)):
        graph.add(((x, y), (x - 1, y - 2)))

    # up and to the right
    if (checkCoordinates((x + 1, y - 2), n)):
        graph.add(((x, y), (x + 1, y - 2)))

    # down and to the left
    if (checkCoordinates((x - 1, y + 2), n)):
        graph.add(((x, y), (x - 1, y + 2)))

    # down and to the right
    if (checkCoordinates((x + 1, y + 2), n)):
        graph.add(((x, y), (x + 1, y + 2)))

    # to the left and up
    if (checkCoordinates((x - 2, y - 1), n)):
        graph.add(((x, y), (x - 2, y - 1)))

    # to the right and up
    if (checkCoordinates((x + 2, y - 1), n)):
        graph.add(((x, y), (x + 2, y - 1)))

    # to the left and down
    if (checkCoordinates((x - 2, y + 1), n)):
        graph.add(((x, y), (x - 2, y + 1)))

    # to the right and down
    if (checkCoordinates((x + 2, y + 1), n)):
        graph.add(((x, y), (x + 2, y + 1)))
        
    return(graph)

# helper function to check if a coordinate is within the field of movement or not
def checkCoordinates(coordinate_vals, n):
    return set(coordinate_vals) <= set(range(n))


# Bellman Ford implementation to compute minimum distances from a src to all destinations
def bellmanFord(vertices, edges, src_coordinates, dest_coordinates):
    distance = dict()
    predecessor = dict()
    path = []

    for vertex in vertices:
        distance[vertex] = float("inf")
        predecessor[vertex] = None

    distance[src_coordinates] = 0

    i = 1
    for i in range(1, len(vertices)):
        for edge in edges:
            u, v = edge
            if distance[u] + 1 < distance[v]:
                distance[v] = distance[u] + 1
                predecessor[v] = u

    # calculate the path taken using the predecessor array
    val = dest_coordinates
    while val != src_coordinates:
        path.insert(0, str(getNum(val, n)))
        val = predecessor[val]

    path.insert(0, str(getNum(val, n)))

    # return the path found and the minimum distance
    return path, distance[dest_coordinates]

if __name__ == "__main__":

    # initialize variables
    n = -1
    start_loc = -1
    end_loc = -1
    p_path = ""

    # get board size from user, check for negative integers
    while n < 0:
        n = input("What size board ( n x n ) would you like? Give a positive integer: ")
        n = int(n)

    # get a start location from user, check for valid values
    while start_loc < 0 or start_loc > (n * n) - 1:
        start_loc = input("Choose a location to start between 0 and " + str((n * n) - 1) + ": ")
        start_loc = int(start_loc)

    # get an end location from user, check for valid values
    while end_loc < 0 or end_loc > (n * n) - 1:
        end_loc = input("Choose which location to end at, between 0 and " + str((n * n) - 1) + ": ")
        end_loc = int(end_loc)

    # make the calculations and print the results
    path, num_moves = calculateMoves(start_loc, end_loc, n)
    print("The minimum number of moves is: " + str(num_moves))

    i = 0
    while i < len(path) - 1:
        p_path += path[i] + ' -> '
        i += 1
    p_path += str(end_loc)       

    print("The path is: " + p_path)

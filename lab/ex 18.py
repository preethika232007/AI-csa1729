import math

def tsp(cities):
    n = len(cities)

    tour = [0]
    unvisited = set(range(1, n))
    total_distance = 0

    while unvisited:
        current = tour[-1]

        nearest = min(
            sorted(unvisited),
            key=lambda city: math.dist(
                cities[current], cities[city])
        )

        distance = math.dist(cities[current], cities[nearest])
        total_distance += distance

        tour.append(nearest)
        unvisited.remove(nearest)

    total_distance += math.dist(cities[tour[-1]], cities[0])
    tour.append(0)

    return tour, total_distance


cities = [(0, 0), (1, 2), (3, 1), (2, 4)]

tour, distance = tsp(cities)

print("Best Tour:", tour)
print("Total Distance:", round(distance, 2))
import math
from queue import PriorityQueue

def heuristic(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

from queue import PriorityQueue

def shortest_path(M, start, goal):
    print("shortest path called")
    
    # Create a priority queue to store the nodes to explore
    frontier = PriorityQueue()
    frontier.put((0, start))
    
    # Create dictionaries to store the current path costs and the path itself
    path_cost = {start: 0}
    path = {start: None}
    
    # A* search
    while not frontier.empty():
        current_cost, current_node = frontier.get()
        
        # Check if the goal has been reached
        if current_node == goal:
            break
        
        # Explore the neighbors
        for neighbor in M.roads[current_node]:
            # Calculate the new cost to reach the neighbor
            new_cost = path_cost[current_node] + heuristic(M.intersections[current_node], M.intersections[neighbor])
            
            # If the neighbor has not been visited or a cheaper path to the neighbor is found
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                total_cost = new_cost + heuristic(M.intersections[neighbor], M.intersections[goal])
                frontier.put((total_cost, neighbor))
                path[neighbor] = current_node

    # Reconstruct the path from start to goal
    node = goal
    route = []
    while node is not None:
        route.append(node)
        node = path[node]
    route.reverse()
    
    return route if route[0] == start else None

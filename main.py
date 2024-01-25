import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0  
    
    while len(cable_lengths) > 1:
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        
        connection_cost = cable1 + cable2
        
        total_cost += connection_cost
        
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost



if __name__ == "__main__":

    cable_lengths = [4, 3, 2, 6]
    result = min_cost_to_connect_cables(cable_lengths)
    print(f"Мінімальні витрати на об'єднання кабелів: {result}")

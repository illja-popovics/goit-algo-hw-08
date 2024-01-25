import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Створюємо міні-купу, використовуючи наявний список кабелів
    heapq.heapify(cable_lengths)
    
    total_cost = 0  # Загальні витрати
    
    # Об'єднуємо кабелі, доки не залишиться тільки один
    while len(cable_lengths) > 1:
        # Беремо два найменших кабелі
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        
        # Обчислюємо витрати на їх об'єднання
        connection_cost = cable1 + cable2
        
        # Додаємо витрати до загальних
        total_cost += connection_cost
        
        # Додаємо новий кабель до купи
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost



if __name__ == "__main__":

    cable_lengths = [4, 3, 2, 6]
    result = min_cost_to_connect_cables(cable_lengths)
    print(f"Мінімальні витрати на об'єднання кабелів: {result}")

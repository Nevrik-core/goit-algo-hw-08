import heapq

def connect_cables(cable_length):
    total_cost = 0
    cable_lengths_copy = cable_length[:]

    heapq.heapify(cable_lengths_copy)
    print(f"Початкова купа кабелів: {cable_lengths_copy}")

    while len(cable_lengths_copy) > 1:
        first_min = heapq.heappop(cable_lengths_copy)
        second_min = heapq.heappop(cable_lengths_copy)

        cost = first_min + second_min
        total_cost += cost

        heapq.heappush(cable_lengths_copy, cost)

        print(f"Об'єднуємо кабелі {first_min} і {second_min} з вартістю {cost}. Нова купа: {cable_lengths_copy}")

    print(f"Загальна вартість об'єднання кабелів: {total_cost}")
    return total_cost

cable_lengths = [15, 2, 2, 25, 4, 6, 8, 12]
print(connect_cables(cable_lengths))

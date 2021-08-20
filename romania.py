from queue import PriorityQueue

distance_map = {
    "Arad": {
        "Zerind": {"cost": 75},
        "Timisoara": {"cost": 118},
        "Sibiu": {"cost": 140}
    },
    "Zerind": {
        "Oradea": {"cost": 71},
        "Arad": {"cost": 75}
    },
    "Timisoara": {
        "Lugoj": {"cost": 111},
        "Arad": {"cost": 118}
    },
    "Sibiu": {
        "Fagaras": {"cost": 99},
        "Rimnicu Vilcea": {"cost": 80},
        "Oradea": {"cost": 151},
        "Arad": {"cost": 140}
    },
    "Oradea": {
        "Sibiu": {"cost": 151},
        "Zerind": {"cost": 71}
    },
    "Lugoj": {
        "Mehadia": {"cost": 70},
        "Timisoara": {"cost": 111}
    },
    "Fagaras": {
        "Bucharest": {"cost": 211},
        "Sibiu": {"cost": 99}
    },
    "Rimnicu Vilcea": {
        "Pitesti": {"cost": 97},
        "Craiova": {"cost": 146},
        "Sibiu": {"cost": 99}
    },
    "Mehadia": {
        "Drobeta": {"cost": 75},
        "Lugoj": {"cost": 70}
    },
    "Pitesti": {
        "Bucharest": {"cost": 101},
        "Rimnicu Vilcea": {"cost": 97},
        "Craiova": {"cost": 138}
    },
    "Craiova": {
        "Pitesti": {"cost": 138},
        "Rimnicu Vilcea": {"cost": 146},
        "Drobeta": {"cost": 120}
    },
    "Drobeta": {
        "Craiova": {"cost": 120},
        "Mehadia": {"cost": 75}
    },
    "Bucharest": {
        "Fagaras": {"cost": 211},
        "Pitesti": {"cost": 101},
        "Giurgiu": {"cost": 90},
        "Urziceni": {"cost": 85}
    },
    "Giurgiu": {
        "Bucharest": {"cost": 90}
    },
    "Urziceni": {
        "Bucharest": {"cost": 85},
        "Hirsova": {"cost": 98},
        "Vaslui": {"cost": 142}
    },
    "Hirsova": {
        "Eforie": {"cost": 70},
        "Urziceni": {"cost": 98}
    },
    "Vaslui": {
        "Iasi": {"cost": 92},
        "Urziceni": {"cost": 142}
    },
    "Iasi": {
        "Neamt": {"cost": 87},
        "Vaslui": {"cost": 92}
    },
    "Neamt": {
        "Iasi": {"cost": 87}
    }
}

heuristic = {
    "Arad": 366,
    "Zerind": 374,
    "Timisoara": 329,
    "Sibiu": 253,
    "Oradea": 380,
    "Lugoj": 244,
    "Fagaras": 178,
    "Rimnicu Vilcea": 193,
    "Mehadia": 241,
    "Pitesti": 98,
    "Craiova": 160,
    "Drobeta": 242,
    "Bucharest": 0,
    "Giurgiu": 77,
    "Urziceni": 80,
    "Hirsova": 151,
    "Eforie": 161,
    "Vaslui": 199,
    "Iasi": 226,
    "Neamt": 234
}


def greedy_best_first_search():
    start = "Arad"
    goal = "Bucharest"
    pq = PriorityQueue()
    pq.put(start)

    previous = []  # khởi tạo previous kiểu dictionary
    for city in distance_map.keys():
        previous.append((city, {'from': None, 'heuristic': heuristic[city]}))
    previous = dict(previous)

    while True:
        cur_city = pq.get()

        if cur_city == goal:
            print('Greedy Best First Search:', cur_city, end=' ')
            while cur_city != start:
                cur_city = previous[cur_city]['from']
                print('=>', cur_city, end=' ')
            break

        for city in distance_map[cur_city].keys():  # Các thành phố có thể đi đến được từ thành phố hiện tại
            if previous[city]['from'] is None:  # Nếu chưa đi qua thành phố này
                pq.put(city)  # Thêm vào hàng đợi
                previous[city]['from'] = cur_city  # Lưu lại dấu vết

        if pq.empty():
            print("Failed!")
            break


def a_sao():
    start = "Arad"
    goal = "Bucharest"
    pq = PriorityQueue()
    pq.put(start)

    previous = []  # khởi tạo previous kiểu dictionary
    for city in distance_map.keys():
        previous.append((city, {'from': None, 'total_cost': heuristic[city]}))
    previous = dict(previous)

    while True:
        cur_city = pq.get()

        if cur_city == goal:
            print('\nA Sao:', cur_city, end=' ')
            while cur_city != start:
                cur_city = previous[cur_city]['from']
                print('=>', cur_city, end=' ')
            break

        cur_city_total_cost = previous[cur_city]['total_cost'] - heuristic[cur_city]

        if cur_city != goal:
            for city in distance_map[cur_city].keys():
                city_total_cost = previous[city]['total_cost']
                total_cost = distance_map[cur_city][city]['cost'] + cur_city_total_cost + heuristic[city]

                if previous[city]['from'] is None or total_cost < city_total_cost:
                    pq.put(city)  # Thêm vào hàng đợi
                    previous[city]['from'] = cur_city  # Lưu lại dấu vết
                    previous[city]['total_cost'] = total_cost  # Cập nhật lại chi phí mới

        if pq.empty():
            print('Fail!')
            break


if __name__ == "__main__":
    greedy_best_first_search()
    a_sao()
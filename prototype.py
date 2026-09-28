import heapq

# km 
mallmap = {
    "ทางเข้าฝั่ง McDonald": {"ชั้น 2": 0.03},
    "ทางเข้าฝั่งประตูที่ 2": {"ชั้น 2": 0.08},
    "ทางเข้าฝั่งหัวสะพานลอยไทวัสดุ": {"ชั้น 2": 0.18},
    "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่": {"ชั้น 3 (ศูนย์อาหาร)": 0.15},
    "ชั้น 2": {
        "ทางเข้าฝั่ง McDonald": 0.03,
        "ทางเข้าฝั่งประตูที่ 2": 0.08,
        "ทางเข้าฝั่งหัวสะพานลอยไทวัสดุ": 0.18,
        "ชั้น 3 (ศูนย์อาหาร)": 0.10,
    },
    "ชั้น 3 (ศูนย์อาหาร)": {
        "ชั้น 2": 0.10,
        "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่": 0.15,
        "หน้าโรงหนัง": 0.07,
        "หน้า Sizzler": 0.07,
    },
    "หน้าโรงหนัง": {"ชั้น 3 (ศูนย์อาหาร)": 0.07},
    "หน้า Sizzler": {"ชั้น 3 (ศูนย์อาหาร)": 0.07},
}

# h(n)
distance_togoal = {
    "ทางเข้าฝั่ง McDonald": 0.20,
    "ทางเข้าฝั่งประตูที่ 2": 0.25,
    "ทางเข้าฝั่งหัวสะพานลอยไทวัสดุ": 0.35,
    "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่": 0.30,
    "ชั้น 2": 0.17,
    "ชั้น 3 (ศูนย์อาหาร)": 0.07,
    "หน้าโรงหนัง": 0.00,
    "หน้า Sizzler": 0.00,
}

LOCATIONS = list(mallmap.keys())
# f(n) = g(n) + h(n)
# g(n) ระยะทางจริงที่เดินมาแล้วจากจุด start
# h(n) ค่าประมาณระยะทางจากจุดปจบ > goal
# f(n) ระยะทางโดยรวมโดยคาดการ
# fscore = f(n)
# g cost = g(n)
# n = ชื่อจุดหรือตำแหน่ง ปจบที่ยืนอยู่

def a_star(start, goal):
    queue = [(distance_togoal[start], 0.0, start, [start])]
    visited = {}

    while queue:
        f, g, n, route = heapq.heappop(queue)

        if n == goal:
            return route, g

        if n in visited and visited[n] <= g:
            continue
        visited[n] = g

        for nextpoint, cost in mallmap[n].items():
            new_g = g + cost
            new_f = new_g + distance_togoal.get(nextpoint, 0.0)
            heapq.heappush(queue, (new_f, new_g, nextpoint, route + [nextpoint]))

    return None, 0




start = "ทางเข้าฝั่ง McDonald"
goal = "หน้าโรงหนัง"

route, total_distance = a_star(start, goal)

if route:
    print("จุดเริ่มต้น: ",start)
    print("เป้าหมาย:",goal)
    print("เส้นทางที่สั้นที่สุด:")
    print(" -> ".join(route))
    print(f"ระยะทางรวม: {total_distance:.2f} กม. ({int(total_distance * 1000)} เมตร)")
else:
    print("ไม่พบเส้นทาง")
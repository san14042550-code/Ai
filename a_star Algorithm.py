import heapq

# กำหนด mallmap และน้ำหนักระยะทางให้ตรงกับผลลัพธ์ในรายงานโครงงาน
mallmap = {
    "ทางเข้าฝั่ง McDonald": {"ชั้น 2 (McDonald)": 0.03},
    "ชั้น 2 (McDonald)": {"ชั้น 3 (ศูนย์อาหาร McDonald)": 0.10},
    "ชั้น 3 (ศูนย์อาหาร McDonald)": {"หน้าโรงหนัง": 0.07},

    "ทางเข้าฝั่งประตูที่ 2": {"ชั้น 2 (ประตู 2)": 0.01},
    "ชั้น 2 (ประตู 2)": {"ชั้น 3 (ศูนย์อาหาร ประตู 2)": 0.02},
    "ชั้น 3 (ศูนย์อาหาร ประตู 2)": {"หน้าโรงหนัง": 0.07},

    "ทางเข้าฝั่งสะพานลอยไทวัสดุ": {"ชั้น 2 (สะพานลอย)": 0.05},
    "ชั้น 2 (สะพานลอย)": {"ชั้น 3 (ศูนย์อาหาร สะพานลอย)": 0.02},
    "ชั้น 3 (ศูนย์อาหาร สะพานลอย)": {"หน้าโรงหนัง": 0.07},

    "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่": {"ชั้น 3 (ศูนย์อาหาร เซ็นทรัลใหม่)": 0.07},
    "ชั้น 3 (ศูนย์อาหาร เซ็นทรัลใหม่)": {"หน้าโรงหนัง": 0.07},

    "หน้าโรงหนัง": {}
}

# h(n) ค่าประมาณระยะทางไปยังเป้าหมาย
distance_togoal = {
    "ทางเข้าฝั่ง McDonald": 0.20,
    "ชั้น 2 (McDonald)": 0.17,
    "ชั้น 3 (ศูนย์อาหาร McDonald)": 0.07,
    
    "ทางเข้าฝั่งประตูที่ 2": 0.10,
    "ชั้น 2 (ประตู 2)": 0.09,
    "ชั้น 3 (ศูนย์อาหาร ประตู 2)": 0.07,
    
    "ทางเข้าฝั่งสะพานลอยไทวัสดุ": 0.14,
    "ชั้น 2 (สะพานลอย)": 0.09,
    "ชั้น 3 (ศูนย์อาหาร สะพานลอย)": 0.07,
    
    "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่": 0.14,
    "ชั้น 3 (ศูนย์อาหาร เซ็นทรัลใหม่)": 0.07,
    
    "หน้าโรงหนัง": 0.00
}

# ฟังก์ชัน A* ใช้ร่วมกับ heapq ร่วมกับ mallmap และ distance_togoal
def a_star(start, goal):
    # queue เก็บ (f, g, current_node, route_list)
    initial_f = distance_togoal.get(start, 0.0)
    queue = [(initial_f, 0.0, start, [start])]
    visited = {}
    while queue:
        f, g, n, route = heapq.heappop(queue)
        if n == goal:
            return route, g
        if n in visited and visited[n] <= g:
            continue
        visited[n] = g
        # ป้องกัน key Error
        if n in mallmap:
            for nextpoint, cost in mallmap[n].items():
                new_g = g + cost
                new_f = new_g + distance_togoal.get(nextpoint, 0.0)
                heapq.heappush(queue, (new_f, new_g, nextpoint, route + [nextpoint]))

    return None, 0.0

# ฟังก์ชันแปลงชื่อโหนดให้แสดงผลลัพธ์เป็นชื่อชั้นและสถานที่
def format_display_route(route):
    formatted = []
    for node in route:
        if "ทางเข้า" in node or "หน้าโรงหนัง" in node:
            formatted.append(node)
        elif "ชั้น 2" in node:
            formatted.append("ชั้น 2")
        elif "ชั้น 3" in node:
            formatted.append("ชั้น 3")
    return formatted




#Input จากผู้ใช้งาน

print("ระบบค้นหาเส้นทางในห้างเซ็นทรัลไปยัง 'หน้าโรงหนัง' ")
print("กรุณาเลือกจุดเริ่มต้น (Start Location):")
print("1. ทางเข้าฝั่ง McDonald")
print("2. ทางเข้าฝั่งประตูที่ 2")
print("3. ทางเข้าฝั่งสะพานลอยไทวัสดุ")
print("4. ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่")

choice = input("กรอกตัวเลขที่ต้องการ (1-4): ").strip()

start_options = {
    "1": "ทางเข้าฝั่ง McDonald",
    "2": "ทางเข้าฝั่งประตูที่ 2",
    "3": "ทางเข้าฝั่งสะพานลอยไทวัสดุ",
    "4": "ทางเข้าฝั่งทางเชื่อมเซ็นทรัลใหม่"
}

if choice in start_options:
    start = start_options[choice]
    goal = "หน้าโรงหนัง"

    route, total_distance = a_star(start, goal)

    print("\n----------------------------------------")
    if route:
        display_path = format_display_route(route)
        print(f"จุดเริ่มต้น: {start}")
        print(f"เป้าหมาย: {goal}")
        print("เส้นทางที่สั้นที่สุด:")
        print(" -> ".join(display_path))
        print(f"ระยะทางรวม: {total_distance:.2f} กม. ({int(total_distance * 1000)} เมตร)")
    else:
        print("ไม่พบเส้นทาง")
    print("----------------------------------------")
else:
    print("ตัวเลือกไม่ถูกต้อง กรุณารันโปรแกรมใหม่อีกครั้งและเลือกเลข 1-4")
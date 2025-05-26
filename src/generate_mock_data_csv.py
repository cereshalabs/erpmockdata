import os
import random
from datetime import timedelta
import pandas as pd
from faker import Faker

# Config
DATA_DIR = "../data"
NUM_PRODUCTS = 50
NUM_STATIONS = 5
NUM_OPERATORS = 25
NUM_ORDERS = 500

fake = Faker()

CURRENT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_FILE))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def save_csv(df: pd.DataFrame, name: str):
    path = os.path.join(DATA_DIR, name)
    df.to_csv(path, index=False)
    print(f"Saved: {path}")

def generate_products(count: int = NUM_PRODUCTS) -> pd.DataFrame:
    categories = [
        ("Electric Wheelchair", "Indoor Use"),
        ("Electric Wheelchair", "Outdoor Use"),
        ("Power Scooter", "Compact 3-Wheel"),
        ("Power Scooter", "Heavy-Duty 4-Wheel"),
        ("Manual Wheelchair", "Folding Frame"),
        ("Manual Wheelchair", "Rigid Frame"),
        ("Bariatric Wheelchair", "High Capacity"),
        ("Pediatric Wheelchair", "Adjustable Growth Frame"),
        ("Rehab Chair", "Tilt-in-Space"),
        ("Standing Wheelchair", "Vertical Mobility Assist"),
    ]

    battery_types = ["Lithium-Ion", "Sealed Lead Acid"]
    products = []

    for i in range(1, count + 1):
        category, subtype = categories[(i - 1) % len(categories)]
        prefix = ''.join(word[0] for word in category.split())
        model_code = f"{prefix}-{random.randint(100, 999)}"
        products.append({
            "product_id": i,
            "model_code": model_code,
            "description": f"{category} – {subtype}",
            "battery_type": random.choice(battery_types),
            "max_speed_kph": round(random.uniform(5.0, 9.0), 1),
        })

    return pd.DataFrame(products)

def generate_stations(count: int = NUM_STATIONS) -> pd.DataFrame:
    station_types = ["Chassis", "Electronics", "Testing", "Wiring"]
    zones = ['A', 'B', 'C']
    return pd.DataFrame([{
        "station_id": i,
        "station_code": f"STN-{i:02d}",
        "location": f"Floor {random.randint(1, 3)}, Zone {random.choice(zones)}",
        "station_type": random.choice(station_types),
    } for i in range(1, count + 1)])

def generate_operators(count: int = NUM_OPERATORS) -> pd.DataFrame:
    levels = ["Junior", "Senior", "Expert"]
    return pd.DataFrame([{
        "operator_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "hire_date": fake.date_between(start_date='-5y', end_date='-6m'),
        "skill_level": random.choice(levels),
    } for i in range(1, count + 1)])

def generate_orders(product_ids, station_ids, operator_ids, count: int = NUM_ORDERS) -> pd.DataFrame:
    statuses = ["Completed", "In Progress", "Delayed"]
    orders = []

    for i in range(1, count + 1):
        start = fake.date_time_between(start_date='-30d', end_date='-1d')
        duration = timedelta(minutes=random.randint(20, 90))
        end = start + duration
        orders.append({
            "order_id": i,
            "device_id": f"WC-{1000 + i}",
            "product_id": random.choice(product_ids),
            "station_id": random.choice(station_ids),
            "operator_id": random.choice(operator_ids),
            "start_time": start,
            "end_time": end,
            "status": random.choice(statuses),
        })

    return pd.DataFrame(orders)

if __name__ == "__main__":
    products = generate_products()
    stations = generate_stations()
    operators = generate_operators()

    save_csv(products, "products.csv")
    save_csv(stations, "stations.csv")
    save_csv(operators, "operators.csv")

    orders = generate_orders(
        product_ids=products["product_id"].tolist(),
        station_ids=stations["station_id"].tolist(),
        operator_ids=operators["operator_id"].tolist(),
    )
    save_csv(orders, "orders.csv")


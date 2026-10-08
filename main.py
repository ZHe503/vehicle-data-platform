import sqlite3

conn = sqlite3.connect("vehicles.db")
c = conn.cursor()

def add_vehicle(make, model, year, power_hp, fuel_type):

    check_sql = """
    SELECT * FROM vehicles
    WHERE make = ? AND model = ? AND year = ?
    """

    if not make or not model:
        print("car doesnt exist")
        return

    if year < 1900 or year > 2026:
        print("invalid year")
        return

    c.execute(check_sql, (make, model, year))
    existing_car = c.fetchone()

    if existing_car:
        print("vehicle already exists")
        return

    if power_hp <= 0:
        print("invalid hp")
        return
    

    sql = """
    INSERT INTO vehicles (make, model, year, power_hp, fuel_type)
    VALUES (?, ?, ?, ?, ?)
    """
    c.execute(sql, (make, model, year, power_hp, fuel_type))
    conn.commit()





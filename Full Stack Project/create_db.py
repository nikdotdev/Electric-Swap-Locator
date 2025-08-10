import sqlite3

conn = sqlite3.connect('stations.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE stations (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    city TEXT,
    pincode TEXT,
    battery_types TEXT
)''')

stations = [
    ('SwapPoint A', '123 Main St, Delhi', 'Delhi', '110001', 'Lithium-Ion'),
    ('BatteryHub', '45 MG Road, Mumbai', 'Mumbai', '400001', 'Lead-Acid, Lithium-Ion'),
    ('EV Station X', '7 Tech Park, Bangalore', 'Bangalore', '560001', 'Lithium-Ion, Nickel-Metal Hydride'),
]

cur.executemany('INSERT INTO stations (name, address, city, pincode, battery_types) VALUES (?, ?, ?, ?, ?)', stations)

conn.commit()
conn.close()

print('✅ Database created and sample data inserted.')

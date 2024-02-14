import sqlite3
import psutil
import datetime
import os

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('monitoreoDB.db')
cursor = conn.cursor()

# Create the monitoreo table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS monitoreo (
        usuario TEXT,
        fecha_hora TEXT,
        ram REAL,
        cpu REAL
    )
''')

# Save the changes to the database
conn.commit()

# Close the connection
conn.close()


def insert_monitoring_data():
    # Connect to the database
    conn = sqlite3.connect('monitoreoDB.db')
    cursor = conn.cursor()

    # Get the current user
    current_user = os.getlogin()

    # Get the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get the RAM usage
    ram_info = psutil.virtual_memory()
    ram_percentage = ram_info.percent

    # Get the CPU usage
    cpu_percentage = psutil.cpu_percent()

    # Insert the data into the database
    cursor.execute('''
        INSERT INTO monitoreo (usuario, fecha_hora, ram, cpu)
        VALUES (?, ?, ?, ?)
    ''', (current_user, current_time, ram_percentage, cpu_percentage))

    # Save the changes to the database
    conn.commit()

    # Close the connection
    conn.close()
insert_monitoring_data()
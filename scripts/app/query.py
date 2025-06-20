import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# Create a connection to your RDS instance
connection = psycopg2.connect(
    dbname='postgres',
    user=os.getenv('DB_ADMIN_NAME'),
    password=os.getenv('DB_ADMIN_PASSWORD'),
    host='clinical.cwpmisqy4ng3.us-east-1.rds.amazonaws.com',
    port=5432  # Default postgres port
)

# Query the database to check the content of clinical
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM clinical LIMIT 10;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

connection.close()
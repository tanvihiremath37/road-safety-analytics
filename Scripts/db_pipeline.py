import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# ===== CONFIG =====
USERNAME = "root"
PASSWORD = "root"
HOST = "localhost"
PORT = "3306"
DB_NAME = "road_safety_db"

# ==================

try:
    print("Connecting to MySQL...")

    # Step 1: Connect WITHOUT database
    engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}")

    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

    print("Database ready")

    # Step 2: Connect WITH database
    engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

    # Step 3: Load dataset
    df = pd.read_csv("Data/road_accidents.csv")

    # Step 4: Insert into MySQL
    df.to_sql("accidents", con=engine, if_exists="replace", index=False)

    print("Data inserted successfully")

    # Step 5: Run queries + create views
    with engine.connect() as conn:

        # Create VIEW
        conn.execute(text("""
        CREATE OR REPLACE VIEW risk_analysis AS
        SELECT *,
            CASE
                WHEN severity = 'Fatal' THEN 'High Risk'
                WHEN severity = 'Serious' THEN 'Medium Risk'
                ELSE 'Low Risk'
            END AS risk_level
        FROM accidents;
        """))

        print("Risk view created")

        # -----------------------------
        #  EXISTING BASIC QUERIES
        # -----------------------------

        print("\n Top Cities:")
        result = conn.execute(text("""
            SELECT city, COUNT(*) as total
            FROM accidents
            GROUP BY city
            ORDER BY total DESC
            LIMIT 5;
        """))
        for row in result:
            print(row)

        print("\n Peak Hours:")
        result = conn.execute(text("""
            SELECT HOUR(time) as hour, COUNT(*) as total
            FROM accidents
            GROUP BY hour
            ORDER BY total DESC
            LIMIT 5;
        """))
        for row in result:
            print(row)

        print("\n Severity Distribution:")
        result = conn.execute(text("""
            SELECT severity, COUNT(*) as total
            FROM accidents
            GROUP BY severity;
        """))
        for row in result:
            print(row)

        # -----------------------------
        # ADVANCED INSIGHT QUERIES
        # -----------------------------

        print("\n High Risk Cities:")
        result = conn.execute(text("""
            SELECT city, COUNT(*) as high_risk_cases
            FROM risk_analysis
            WHERE risk_level = 'High Risk'
            GROUP BY city
            ORDER BY high_risk_cases DESC;
        """))
        for row in result:
            print(row)

        print("\n Dangerous Conditions:")
        result = conn.execute(text("""
            SELECT road_condition, light_condition, COUNT(*) as accidents
            FROM accidents
            GROUP BY road_condition, light_condition
            ORDER BY accidents DESC;
        """))
        for row in result:
            print(row)

        print("\n Vehicle Risk (Fatal Cases):")
        result = conn.execute(text("""
            SELECT vehicle_type, COUNT(*) as fatal_cases
            FROM accidents
            WHERE severity = 'Fatal'
            GROUP BY vehicle_type
            ORDER BY fatal_cases DESC;
        """))
        for row in result:
            print(row)

    print("\n Pipeline executed successfully!")

# ===== CLEAN ERROR HANDLING =====

except OperationalError:
    print(" Database connection failed.")
    print(" Check MySQL is running and credentials are correct")

except FileNotFoundError:
    print(" road_accidents.csv not found.")
    print(" Make sure file is in same folder")

except Exception as e:
    print("Error:", str(e))
# File: utils/db_manager.py
import psycopg2
from psycopg2.extras import RealDictCursor

def get_test_users_from_db():
    """
    Connects to PostgreSQL and fetches test data.
    """
    connection = None
    try:
        # ======================================================
        # UPDATED CREDENTIALS
        # ======================================================
        connection = psycopg2.connect(
            host="localhost",
            port="5432",           
            dbname="postgres",     
            user="postgres",       
            password="admin123"    # <--- Password set via SQL command
        )
        
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        # SQL query to get the data we inserted
        query = "SELECT username, password, should_pass, error_msg FROM test_users"
        cursor.execute(query)
        
        users = cursor.fetchall()
        
        return [dict(row) for row in users]

    except Exception as e:
        print(f"\n[ERROR] Could not connect to Database! \nReason: {e}")
        return []
        
    finally:
        if connection:
            cursor.close()
            connection.close()

# ==========================================
# SELF-TEST BLOCK
# ==========================================
if __name__ == "__main__":
    print("Testing Database Connection...")
    data = get_test_users_from_db()
    if data:
        print("\n✅ SUCCESS! Connection worked. Found these users:")
        for user in data:
            print(f" - {user['username']}")
    else:
        print("\n❌ FAILED. Please check the error message above.")
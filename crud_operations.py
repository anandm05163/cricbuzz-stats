import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Test123',  # Replace with your actual password
            database='cricbuzz'
        )
        if connection.is_connected():
            print("Connection to MySQL database successful")
            return connection
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """Close the database connection."""
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")

# Function to fetch player details along with stats
def fetch_player_details():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT p.player_id, p.full_name, ps.matches, ps.innings, ps.total_runs, ps.batting_average
        FROM players p
        JOIN player_stats ps ON p.player_id = ps.player_id
        """
        cursor.execute(query)
        player_details = cursor.fetchall()
        close_connection(connection)
        return player_details
    else:
        return []

def create_player(player_id, full_name, matches, innings, total_runs, batting_average):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO players (player_id, full_name)
            VALUES (%s, %s)
            """,
            (player_id, full_name)
        )
        cursor.execute(
            """
            INSERT INTO player_stats (player_id, matches, innings, total_runs, batting_average)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (player_id, matches, innings, total_runs, batting_average)
        )
        connection.commit()
        close_connection(connection)

def fetch_player_by_name(name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT p.player_id, p.full_name, ps.total_runs, ps.matches, ps.innings, ps.total_runs, ps.batting_average 
        FROM players p 
        JOIN player_stats ps ON p.player_id = ps.player_id 
        WHERE p.full_name LIKE %s
        """
        cursor.execute(query, (f"%{name}%",))
        all_results = cursor.fetchall()  # Fetch all results
        close_connection(connection)
        
        # Return the first result if there are any results
        if all_results:
            return all_results[0]
        else:
            return None
    else:
        return None


def delete_player(player_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # First, delete the related records in player_stats
            cursor.execute("DELETE FROM player_stats WHERE player_id = %s", (player_id,))
            # Then, delete the record in players
            cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
            connection.commit()
        except Error as e:
            print(f"Error deleting player: {e}")
        finally:
            close_connection(connection)

def update_player(player_id, new_full_name, new_matches, new_innings, new_total_runs, new_batting_average):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Update player name in players table
            cursor.execute(
                "UPDATE players SET full_name = %s WHERE player_id = %s",
                (new_full_name, player_id)
            )
            # Update player stats in player_stats table
            cursor.execute(
                """
                UPDATE player_stats 
                SET matches = %s, innings = %s, total_runs = %s, batting_average = %s 
                WHERE player_id = %s
                """,
                (new_matches, new_innings, new_total_runs, new_batting_average, player_id)
            )
            connection.commit()
        except Error as e:
            print(f"Error updating player: {e}")
        finally:
            close_connection(connection)

# Other CRUD functions (create, update, delete) can be added here as needed

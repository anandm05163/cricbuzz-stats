import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password ='Test123',  # Replace with your actual password
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

def fetch_indian_players():
    """Fetch Indian players from the database."""
    connection = create_connection()
    if connection is None:
        print("Failed to create database connection.")
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT full_name, playing_role, batting_style, bowling_style
        FROM players
        WHERE country = 'India';
        """
        cursor.execute(query)
        players = cursor.fetchall()
        print(f"Fetched {len(players)} Indian players from the database.")  
        return players
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    finally:
        close_connection(connection)   

def fetch_recent_matches():
    """Fetch matches from the last 30 days."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT match_description, team1_id, team2_id, venue_id, match_date
        FROM matches
        WHERE match_date >= CURDATE() - INTERVAL 30 DAY
        ORDER BY match_date DESC;
        """
        cursor.execute(query)
        matches = cursor.fetchall()
        return matches
    except Exception as e:
        print(f"Error fetching recent matches: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_top_odi_players():
    """Fetch top 10 ODI players by total runs."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT p.full_name, ps.total_runs, ps.batting_average, ps.centuries
        FROM player_stats ps
        JOIN players p ON ps.player_id = p.player_id
        WHERE ps.format = 'ODI'
        ORDER BY ps.total_runs DESC
        LIMIT 10;
        """
        cursor.execute(query)
        players = cursor.fetchall()
        return players
    except Exception as e:
        print(f"Error fetching top ODI players: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_large_venues():
    """Fetch venues with capacity greater than 50,000."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT venue_name, city, country, capacity
        FROM venues
        WHERE capacity > 50000
        ORDER BY capacity DESC;
        """
        cursor.execute(query)
        venues = cursor.fetchall()
        return venues
    except Exception as e:
        print(f"Error fetching large venues: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_team_wins():
    """Fetch total wins by team."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT t.team_name, COUNT(m.winner_id) AS total_wins
        FROM matches m
        JOIN teams t ON m.winner_id = t.team_id
        GROUP BY t.team_name
        ORDER BY total_wins DESC;
        """
        cursor.execute(query)
        wins = cursor.fetchall()
        return wins
    except Exception as e:
        print(f"Error fetching team wins: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_player_roles():
    """Fetch player count by playing role."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT playing_role, COUNT(*) AS player_count
        FROM players
        GROUP BY playing_role;
        """
        cursor.execute(query)
        roles = cursor.fetchall()
        return roles
    except Exception as e:
        print(f"Error fetching player roles: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_highest_scores():
    """Fetch highest individual scores by format."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT format, MAX(total_runs) AS highest_individual_score
        FROM player_stats
        GROUP BY format;
        """
        cursor.execute(query)
        scores = cursor.fetchall()
        return scores
    except Exception as e:
        print(f"Error fetching highest scores: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_series_2024():
    """Fetch series starting in 2024."""
    connection = create_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT series_name, host_country, match_type, start_date, total_matches
        FROM series
        WHERE YEAR(start_date) = 2024;
        """
        cursor.execute(query)
        series = cursor.fetchall()
        return series
    except Exception as e:
        print(f"Error fetching series 2024: {e}")
        return []
    finally:
        close_connection(connection)

def fetch_top_players():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT p.full_name, ps.total_runs, ps.total_wickets, ps.format
        FROM players p
        JOIN player_stats ps ON p.player_id = ps.player_id
        WHERE ps.total_runs > 1000 AND ps.total_wickets > 50
        """
        cursor.execute(query)
        top_players = cursor.fetchall()
        close_connection(connection)
        return top_players
    else:
        return []



def fetch_last_20_matches():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            m.match_description AS MatchDescription,
            t1.team_name AS Team1,
            t2.team_name AS Team2,
            w.team_name AS WinningTeam,
            CASE 
                WHEN m.result LIKE '%won by%' THEN SUBSTRING_INDEX(SUBSTRING_INDEX(m.result, ' won by ', -1), ' ', 1)
                ELSE NULL
            END AS VictoryMargin,
            CASE 
                WHEN m.result LIKE '%won by%' THEN 
                    CASE 
                        WHEN m.result LIKE '%runs%' THEN 'Runs'
                        WHEN m.result LIKE '%wkt%' THEN 'Wickets'
                        ELSE NULL
                    END
                ELSE NULL
            END AS VictoryType,
            v.venue_name AS VenueName
        FROM 
            matches m
        JOIN 
            teams t1 ON m.team1_id = t1.team_id
        JOIN 
            teams t2 ON m.team2_id = t2.team_id
        JOIN 
            teams w ON m.winner_id = w.team_id
        JOIN 
            venues v ON m.venue_id = v.venue_id
        WHERE 
            m.result IS NOT NULL
        ORDER BY 
            m.match_date DESC
        LIMIT 20;
        """
        cursor.execute(query)
        matches = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(matches, columns=["MatchDescription", "Team1", "Team2", "WinningTeam", "VictoryMargin", "VictoryType", "VenueName"])
        return df
    else:
        return pd.DataFrame(columns=["MatchDescription", "Team1", "Team2", "WinningTeam", "VictoryMargin", "VictoryType", "VenueName"])

def fetch_player_performance():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            p.full_name AS PlayerName,
            SUM(CASE WHEN ps.format = 'Test' THEN ps.total_runs ELSE 0 END) AS TestRuns,
            SUM(CASE WHEN ps.format = 'ODI' THEN ps.total_runs ELSE 0 END) AS ODIRuns,
            SUM(CASE WHEN ps.format = 'T20I' THEN ps.total_runs ELSE 0 END) AS T20IRuns,
            AVG(ps.batting_average) AS OverallBattingAverage
        FROM 
            players p
        JOIN 
            player_stats ps ON p.player_id = ps.player_id
        WHERE 
            ps.format IN ('Test', 'ODI', 'T20I')
        GROUP BY 
            p.player_id
        HAVING 
            COUNT(DISTINCT ps.format) >= 2
        """
        cursor.execute(query)
        player_performance = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(player_performance, columns=["PlayerName", "TestRuns", "ODIRuns", "T20IRuns", "OverallBattingAverage"])
        return df
    else:
        return pd.DataFrame(columns=["PlayerName", "TestRuns", "ODIRuns", "T20IRuns", "OverallBattingAverage"])

def fetch_team_performance_home_away():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            t.team_name AS TeamName,
            SUM(CASE WHEN v.country = t.country AND m.winner_id = t.team_id THEN 1 ELSE 0 END) AS HomeWins,
            SUM(CASE WHEN v.country != t.country AND m.winner_id = t.team_id THEN 1 ELSE 0 END) AS AwayWins
        FROM 
            matches m
        JOIN 
            teams t ON m.winner_id = t.team_id
        JOIN 
            venues v ON m.venue_id = v.venue_id
        WHERE 
            m.result IS NOT NULL
        GROUP BY 
            t.team_id
        """
        cursor.execute(query)
        team_performance = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(team_performance, columns=["TeamName", "HomeWins", "AwayWins"])
        return df
    else:
        return pd.DataFrame(columns=["TeamName", "HomeWins", "AwayWins"])

def fetch_batting_partnerships():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            p1.full_name AS Player1,
            p2.full_name AS Player2,
            (bs1.runs + bs2.runs) AS PartnershipRuns,
            bs1.innings_id AS Innings
        FROM 
            batting_stats bs1
        JOIN 
            batting_stats bs2 ON bs1.match_id = bs2.match_id AND bs1.innings_id = bs2.innings_id AND bs1.batting_position + 1 = bs2.batting_position
        JOIN 
            players p1 ON bs1.player_id = p1.player_id
        JOIN 
            players p2 ON bs2.player_id = p2.player_id
        WHERE 
            (bs1.runs + bs2.runs) >= 100
        """
        cursor.execute(query)
        partnerships = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(partnerships, columns=["Player1", "Player2", "PartnershipRuns", "Innings"])
        return df
    else:
        return pd.DataFrame(columns=["Player1", "Player2", "PartnershipRuns", "Innings"])

def fetch_bowling_performance():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            b.player_id,
            p.full_name AS PlayerName,
            v.venue_name AS VenueName,
            COUNT(DISTINCT b.match_id) AS MatchesPlayed,
            SUM(b.wickets) AS TotalWickets,
            AVG(b.economy_rate) AS AverageEconomyRate
        FROM 
            bowling_stats b
        JOIN 
            players p ON b.player_id = p.player_id
        JOIN 
            matches m ON b.match_id = m.match_id
        JOIN 
            venues v ON m.venue_id = v.venue_id
        WHERE 
            b.overs_bowled >= 4
        GROUP BY 
            b.player_id, v.venue_id
        HAVING 
            COUNT(DISTINCT b.match_id) >= 3
        LIMIT 1000;
        """
        cursor.execute(query)
        bowling_performance = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(bowling_performance, columns=["PlayerID", "PlayerName", "VenueName", "MatchesPlayed", "TotalWickets", "AverageEconomyRate"])
        return df
    else:
        return pd.DataFrame(columns=["PlayerID", "PlayerName", "VenueName", "MatchesPlayed", "TotalWickets", "AverageEconomyRate"])


def fetch_close_match_performance():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT 
            b.player_id,
            p.full_name AS PlayerName,
            AVG(b.runs) AS AverageRuns,
            COUNT(DISTINCT b.match_id) AS CloseMatchesPlayed,
            SUM(CASE WHEN m.winner_id = b.team_id THEN 1 ELSE 0 END) AS CloseMatchesWon
        FROM 
            batting_stats b
        JOIN 
            players p ON b.player_id = p.player_id
        JOIN 
            matches m ON b.match_id = m.match_id
        WHERE 
            (m.result LIKE '%won by % runs' AND CAST(SUBSTRING_INDEX(m.result, ' ', -2) AS UNSIGNED) < 50)
            OR (m.result LIKE '%won by % wickets' AND CAST(SUBSTRING_INDEX(m.result, ' ', -2) AS UNSIGNED) < 5)
        GROUP BY 
            b.player_id
        HAVING 
            CloseMatchesPlayed > 0
        LIMIT 1000;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        close_connection(connection)
        
        # Convert the results to a DataFrame
        df = pd.DataFrame(results, columns=["PlayerID", "PlayerName", "AverageRuns", "CloseMatchesPlayed", "CloseMatchesWon"])
        return df
    else:
        return pd.DataFrame(columns=["PlayerID", "PlayerName", "AverageRuns", "CloseMatchesPlayed", "CloseMatchesWon"])
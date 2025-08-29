import streamlit as st
import pandas as pd
from pages.live_matches import display_live_matches
from pages.sql_queries import (
    fetch_indian_players,
    fetch_recent_matches,
    fetch_top_odi_players,
    fetch_large_venues,
    fetch_team_wins,
    fetch_player_roles,
    fetch_highest_scores,
    fetch_series_2024,
    fetch_top_players,
    fetch_last_20_matches,
    fetch_player_performance,
    fetch_team_performance_home_away,
    fetch_batting_partnerships,
    fetch_bowling_performance,
    fetch_close_match_performance
)

from pages.crud_operations import (
    fetch_player_details,
    create_player,
    fetch_player_by_name,
    update_player,
    delete_player
)



# Set page configuration
st.set_page_config(page_title="Sports Dashboard", page_icon="🏠", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #ff6f61;
        padding: 20px;
        border-radius: 15px;
    }
    .header {
        background-color: #ff6f61;
        color: white;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
    }
    .scorecard, .analytics {
        background-color: #ff6f61;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
    }
    .scorecard h2, .analytics h2 {
        color: #ffcc00;
    }
    .scorecard table, .analytics table {
        width: 100%;
        margin-top: 20px;
    }
    .scorecard table th, .analytics table th {
        text-align: left;
        padding: 5px;
    }
    .scorecard table td, .analytics table td {
        padding: 5px;
    }
    .button {
        background-color: #ffcc00;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .panel {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .form-row {
        display: flex;
        justify-content: space-between;
    }
    .form-row > div {
        flex: 1;
        margin-right: 10px;
    }
    .form-row > div:last-child {
        margin-right: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Sidebar for project structure and navigation
st.sidebar.title("🏏 Cricket Dashboard")
page = st.sidebar.selectbox(
    "Choose a page",
    [
        "📊 Live Score",
        "👤 Player Stats",
        "📈 SQL Analytics",
        "🛠️ CRUD Operations"
    ]
)


# Header
# st.markdown("<div class='header'><h1>🏠 SPORTS</h1></div>", unsafe_allow_html=True)

# Main content
# st.markdown("<div class='main'>", unsafe_allow_html=True)

if page == "Home":
    st.markdown("<h2>Welcome to the Sports Dashboard</h2>", unsafe_allow_html=True)
    st.write("Select a page from the sidebar to navigate.")
elif page == "📊 Live Score":
    st.markdown("<h2>📊 Cricbuzz Live Score Dashboard</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3> 🎯 Select a Match </h3>", unsafe_allow_html=True)

    # Get the live matches data
    match_display_data = display_live_matches()
    
    if not match_display_data:
        st.write("No live match data available.")
    else:
        # Extract unique series names
        series_names = list(set(match_info["series_name"] for match_info in match_display_data))
        
        # Add a dropdown to select a series
        selected_series = st.selectbox("Available Matches:", series_names)
        
        # Filter matches by selected series
        filtered_matches = [match_info for match_info in match_display_data if match_info["series_name"] == selected_series]
        
        # Display matches for the selected series
        for match_info in filtered_matches:
            st.header(match_info["series_name"])
            st.subheader(f"{match_info['match_desc']} - {match_info['team1']} vs {match_info['team2']}")
            st.write(f"Status: {match_info['status']}")
            st.write(f"Venue: {match_info['venue']}")
            st.write(f"{match_info['team1']} Score: {match_info['team1_score']}")
            st.write(f"{match_info['team2']} Score: {match_info['team2_score']}")
            st.write("---")
elif page == "👤 Player Stats":
    st.markdown("<h2>👤 Cricket Player Statistics</h2>", unsafe_allow_html=True)
    
    # Search for a player
    st.markdown("<h4>🔍 Search for a Player</h4>", unsafe_allow_html=True)
    search_name = st.text_input("Enter player name:", placeholder="e.g., Virat Kohli, KL Rahul, MS Dhoni")
    
    if st.button("Search"):
        player_details = fetch_player_by_name(search_name)  # Implement this function in crud_operations.py
        if player_details:
            player_id, full_name, total_runs,matches,innings,total_runs,batting_average = player_details
            
            # Display player profile
            st.markdown(f"<h3>{full_name} - Player Profile</h3>", unsafe_allow_html=True)
            st.markdown(f"**Nickname**: {full_name.split()[0]}", unsafe_allow_html=True)
            
            st.markdown("<h4>🏏🎯 Cricket Details</h4>", unsafe_allow_html=True)
            st.markdown(f"- **Matches**: {matches}", unsafe_allow_html=True)
            st.markdown(f"- **Innings**: {innings}", unsafe_allow_html=True)
            st.markdown(f"- **Total Runs**: {total_runs}", unsafe_allow_html=True)
            st.markdown(f"- **Batting Average**: {batting_average}", unsafe_allow_html=True)
        else:
            st.write("No player found with that name.")
    
    # About This Dashboard
    st.markdown("<h4>📄 About This Dashboard</h4>", unsafe_allow_html=True)
    st.markdown("""
    - **Player Stats Page**:
      - Search any cricket player
      - Career statistics across formats
      - Comprehensive player profiles
      - No biography section (to save API calls)
    """, unsafe_allow_html=True)
elif page == "📈 SQL Analytics":
    # Player Analytics
    st.markdown("<h2>📈  SQL Statistics</h2>", unsafe_allow_html=True)
     # Center-aligned header for the table
    st.markdown("<h3 class='centered-header'>1. All players who represent India</h3>", unsafe_allow_html=True)
    # Fetch and display player data
    players = fetch_indian_players()
    if players:
        df = pd.DataFrame(players, columns=["Name", "Role", "Batting Style", "Bowling Style"])
        # Use st.table for better styling and alignment
        st.table(df)
    else:
        st.write("No players found.")

     # 2. Recent Matches
    st.markdown("<h3 class='centered-header'>2. Recent Matches</h3>", unsafe_allow_html=True)
    matches = fetch_recent_matches()
    if matches:
        df = pd.DataFrame(matches, columns=["Match Description", "Team 1 ID", "Team 2 ID", "Venue ID", "Match Date"])
        st.table(df)
    else:
        st.write("No recent matches found.")

     # 3. Top ODI Players
    st.markdown("<h3 class='centered-header'>3. Top ODI Players</h3>", unsafe_allow_html=True)
    top_players = fetch_top_odi_players()
    if top_players:
        df = pd.DataFrame(top_players, columns=["Name", "Total Runs", "Batting Average", "Centuries"])
        st.table(df)
    else:
        st.write("No top ODI players found.")

    # 4. Large Venues
    st.markdown("<h3 class='centered-header'>4. Large Venues</h3>", unsafe_allow_html=True)
    venues = fetch_large_venues()
    if venues:
        df = pd.DataFrame(venues, columns=["Venue Name", "City", "Country", "Capacity"])
        st.table(df)
    else:
        st.write("No large venues found.")
    
    # 5. Team Wins
    st.markdown("<h3 class='centered-header'>5. Team Wins</h3>", unsafe_allow_html=True)
    wins = fetch_team_wins()
    if wins:
        df = pd.DataFrame(wins, columns=["Team Name", "Total Wins"])
        st.table(df)
    else:
        st.write("No team wins found.")

    # 6. Player Roles
    st.markdown("<h3 class='centered-header'>6. Player Roles</h3>", unsafe_allow_html=True)
    roles = fetch_player_roles()
    if roles:
        df = pd.DataFrame(roles, columns=["Playing Role", "Player Count"])
        st.table(df)
    else:
        st.write("No player roles found.")

     # 7. Highest Individual Scores by Format
    st.markdown("<h3 class='centered-header'>7. Highest Individual Scores by Format</h3>", unsafe_allow_html=True)
    scores = fetch_highest_scores()
    if scores:
        df = pd.DataFrame(scores, columns=["Format", "Highest Individual Score"])
        st.table(df)
    else:
        st.write("No highest scores found.")

    # 8. Series Starting in 2024
    st.markdown("<h3 class='centered-header'>8. Series Starting in 2024</h3>", unsafe_allow_html=True)
    series = fetch_series_2024()
    if series:
        df = pd.DataFrame(series, columns=["Series Name", "Host Country", "Match Type", "Start Date", "Total Matches"])
        st.table(df)
    else:
        st.write("No series starting in 2024 found.")

    # 9. Top Players with Over 1000 Runs and 50 Wickets
    st.markdown("<h3 class='centered-header'>9. Top Players with Over 1000 Runs and 50 Wickets</h3>", unsafe_allow_html=True)
    
    top_players = fetch_top_players()
    # Fetch and display the top players
    top_players = fetch_top_players()
    if top_players:
        # Convert the results to a DataFrame
        df = pd.DataFrame(top_players, columns=["Full Name", "Total Runs", "Total Wickets", "Format"])
        st.table(df)
    else:
        st.write("No players found with the specified criteria.")

    st.markdown("<h3>10. 🏏 Last 20 Completed Matches</h3>", unsafe_allow_html=True)
    
    # 10 Fetch and display the last 20 matches
    df = fetch_last_20_matches()
    st.table(df)

    st.markdown("<h3>11. 🏏 Player Performance Across Formats</h3>", unsafe_allow_html=True)
    
    # 11 Fetch and display player performance
    df = fetch_player_performance()
    st.table(df)

     # 12 Fetch and display team performance
    st.markdown("<h3> 12. 🏠 Home vs Away Performance</h3>", unsafe_allow_html=True)
    
    df = fetch_team_performance_home_away()
    st.table(df)

    st.markdown("<h3>13. 🏏 Batting Partnerships with 100+ Runs</h3>", unsafe_allow_html=True)
    
    # Fetch and display batting partnerships
    df = fetch_batting_partnerships()
    st.table(df)

    st.markdown("<h3>14. 🏏 Bowling Performance at Different Venues</h3>", unsafe_allow_html=True)
    
    # Fetch and display bowling performance
    df = fetch_bowling_performance()
    st.table(df)

    st.markdown("<h3>15. 🏏Player Performance in Close Matches</h3>", unsafe_allow_html=True)
    
    # Fetch and display bowling performance
    df = fetch_close_match_performance()
    st.table(df)

elif page == "🛠️ CRUD Operations":
    st.markdown("<h2>🛠️ CRUD Operations</h2>", unsafe_allow_html=True)
    st.markdown("<h3>➕ Create, 📖 Read, ✏️ Update, ❌ Delete Player Records</h3>", unsafe_allow_html=True)
    
    # Dropdown for CRUD operations
    crud_action = st.selectbox(
        "Choose an action",
        [
            "📖 Read Player",
            "➕ Create Player",
            "✏️ Update Player",
            "❌ Delete Player"
        ]
    )
    
    if crud_action == "📖 Read Player":
        # Fetch and display all players
        players = fetch_player_details()
        if players:
            df = pd.DataFrame(players, columns=["player_id", "player_name", "matches", "innings", "total_runs", "batting_average"])
            st.table(df)
        else:
            st.write("No players found.")

    elif crud_action == "➕ Create Player":
        st.markdown("<h4>➕ Add New Player</h4>", unsafe_allow_html=True)
    
        # Form inputs for creating a player
        player_id = st.number_input("Player ID", min_value=1, step=1)
        full_name = st.text_input("Player Name", placeholder="e.g., John Doe")
        matches = st.number_input("Matches", min_value=0, step=1)
        innings = st.number_input("Innings", min_value=0, step=1)
        total_runs = st.number_input("Runs", min_value=0, step=1)
        batting_average = st.number_input("Average", min_value=0.0, step=0.01)
    
        if st.button("Add Player"):
        # Call function to create player (to be implemented in crud_operations.py)
            create_player(player_id, full_name, matches, innings, total_runs, batting_average)
            st.success("Player added successfully!")

    elif crud_action == "✏️ Update Player":
        st.markdown("<h4>✏️ Update Player Record</h4>", unsafe_allow_html=True)
    
        # Search player to update
        search_name = st.text_input("🔍 Search player to update:", placeholder="Enter player name")
    
        # Fetch player details based on search
        player_details = fetch_player_by_name(search_name)  # Implement this function in crud_operations.py
        if player_details:
            player_id, full_name, total_runs,matches,innings,total_runs,batting_average = player_details
            st.markdown(f"<div style='color: #5bc0de;'>Selected player: {full_name} (ID: {player_id}) - {total_runs} runs</div>", unsafe_allow_html=True)
        
            # Form inputs for updating player
            new_full_name = st.text_input("Player Name", value=full_name)
            new_matches = st.number_input("Matches", min_value=0, step=1, value=matches)
            new_innings = st.number_input("Innings", min_value=0, step=1, value=innings)
            new_total_runs = st.number_input("Runs", min_value=0, step=1, value=total_runs)
            new_batting_average = st.number_input("Average", min_value=0.0, step=0.01, value=batting_average)
        
            if st.button("Update Player"):
                # Call function to update player (to be implemented in crud_operations.py)
                update_player(player_id, new_full_name, new_matches, new_innings, new_total_runs, new_batting_average)
                st.success(f"Player {new_full_name} updated successfully!")

    elif crud_action == "❌ Delete Player":
        st.markdown("<h4>❌ Delete Player Record</h4>", unsafe_allow_html=True)
    
        # Warning message
        st.markdown("<div style='color: #d9534f;'><strong>⚠️ Warning: This action cannot be undone!</strong></div>", unsafe_allow_html=True)
    
        # Search player to delete
        search_name = st.text_input("🔍 Search player to delete:", placeholder="Enter player name")
    
        # Fetch player details based on search
        player_details = fetch_player_by_name(search_name)  # Implement this function in crud_operations.py
    
        if player_details:
            player_id, full_name, total_runs,matches,innings,total_runs,batting_average = player_details
            st.markdown(f"<div style='color: #5bc0de;'>Select player to DELETE: {full_name} (ID: {player_id}) - {total_runs} runs</div>", unsafe_allow_html=True)
            # Confirmation input
            confirmation_text = st.text_input(f"Type 'DELETE {full_name}' to confirm:")
        
            if confirmation_text == f"DELETE {full_name}":
                if st.button("Confirm Delete"):
                    delete_player(player_id)  # Implement this function in crud_operations.py
                    st.success(f"Player {full_name} deleted successfully!")
        else:
            st.write("No player found with that name.")

    
st.markdown("</div>", unsafe_allow_html=True)

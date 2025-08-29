import streamlit as st
import requests

def fetch_live_matches():
    # Replace with the actual API endpoint for fetching live matches
    api_url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
    headers = {
        "X-RapidAPI-Key": "ac3d110b25msh1e36588766c0a0ap1f02cdjsn240c7a2198cb",  # Replace with your actual API key
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch live matches data.")
        return []

def extract_live_matches_data():
    live_matches_data = fetch_live_matches()
    extracted_data = []
    if live_matches_data:
        for type_match in live_matches_data.get('typeMatches', []):
            for series in type_match.get('seriesMatches', []):
                series_name = series.get('seriesAdWrapper', {}).get('seriesName', 'Unknown Series')
                for match in series.get('seriesAdWrapper', {}).get('matches', []):
                    match_info = match.get('matchInfo', {})
                    match_desc = match_info.get('matchDesc', 'Unknown Match')
                    status = match_info.get('status', 'Unknown Status')
                    team1 = match_info.get('team1', {}).get('teamName', 'Team 1')
                    team2 = match_info.get('team2', {}).get('teamName', 'Team 2')
                    venue = match_info.get('venueInfo', {}).get('ground', 'Unknown Venue')
                    
                    team1_score = match.get('matchScore', {}).get('team1Score', {}).get('inngs1', {})
                    team2_score = match.get('matchScore', {}).get('team2Score', {}).get('inngs1', {})
                    
                    match_data = {
                        "series_name": series_name,
                        "match_desc": match_desc,
                        "status": status,
                        "team1": team1,
                        "team2": team2,
                        "venue": venue,
                        "team1_score": f"{team1_score.get('runs', 0)}/{team1_score.get('wickets', 0)} in {team1_score.get('overs', 0)} overs",
                        "team2_score": f"{team2_score.get('runs', 0)}/{team2_score.get('wickets', 0)} in {team2_score.get('overs', 0)} overs"
                    }
                    extracted_data.append(match_data)
    return extracted_data

# def display_live_matches():
#     matches_data = extract_live_matches_data()
#     for match_data in matches_data:
#         st.header(match_data["series_name"])
#         st.subheader(f"{match_data['match_desc']} - {match_data['team1']} vs {match_data['team2']}")
#         st.write(f"Status: {match_data['status']}")
#         st.write(f"Venue: {match_data['venue']}")
#         st.write(f"{match_data['team1']} Score: {match_data['team1_score']}")
#         st.write(f"{match_data['team2']} Score: {match_data['team2_score']}")
#         st.write("---")

def display_live_matches():
    matches_data = extract_live_matches_data()
    match_display_data = []  # List to store match display information
    
    for match_data in matches_data:
        match_info = {
            "series_name": match_data["series_name"],
            "match_desc": match_data["match_desc"],
            "team1": match_data["team1"],
            "team2": match_data["team2"],
            "status": match_data["status"],
            "venue": match_data["venue"],
            "team1_score": match_data["team1_score"],
            "team2_score": match_data["team2_score"]
        }
        match_display_data.append(match_info)
    
    return match_display_data


def main():
    st.title("Live Matches")
    display_live_matches()

if __name__ == "__main__":
    main()

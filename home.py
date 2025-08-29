# File: /cricbuzz_livestats/cricbuzz_livestats/pages/home.py

import streamlit as st

def main():
    st.title("Cricbuzz Live Stats")
    st.header("Overview")
    st.write("""
        Welcome to the Cricbuzz Live Stats application! This app provides real-time statistics and insights into ongoing cricket matches.
        
        ## Objectives
        - Display live match data
        - Show top batting and bowling statistics
        - Provide an interface for player statistics management
        
        Navigate through the pages using the sidebar to explore live matches and top stats.
    """)

if __name__ == "__main__":
    main()
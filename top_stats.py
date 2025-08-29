# File: /cricbuzz_livestats/cricbuzz_livestats/pages/top_stats.py

import streamlit as st
from .sql_queries import get_top_batting_stats, get_top_bowling_stats

def display_top_stats():
    st.title("Top Batting and Bowling Statistics")

    # Fetch top batting stats
    batting_stats = get_top_batting_stats()
    st.subheader("Top Batting Stats")
    if batting_stats:
        st.write(batting_stats)
    else:
        st.write("No batting statistics available.")

    # Fetch top bowling stats
    bowling_stats = get_top_bowling_stats()
    st.subheader("Top Bowling Stats")
    if bowling_stats:
        st.write(bowling_stats)
    else:
        st.write("No bowling statistics available.")

if __name__ == "__main__":
    display_top_stats()
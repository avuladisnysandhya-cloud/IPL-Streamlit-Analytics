import streamlit as st
import pandas as pd

df = pd . read_csv (
"IPL_Matches_Data_2008_2026.csv"
)

st . title ("IPL Data Analysis ")

st . subheader (" Dataset ")

st . dataframe (
df ,
use_container_width = True
)

st . write ( df . head () )

st . write ( df . tail () )

st . write ( df . shape )

st . write ( df . columns )

st . subheader (" Dataset Shape ")

rows , columns = df . shape

st . write (" Rows :", rows )
st . write (" Columns :", columns )

missing_values = df . isnull () .sum ()

st . subheader (" Missing Values ")

st . dataframe (
missing_values
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Matches",
    len(df)
)

col2.metric(
    "Total Seasons",
    df["season"].nunique()
)

col3.metric(
    "Total Venues",
    df["venue"].nunique()
)

col4.metric(
    "Cities",
    df["city"].nunique()
)


df [" total_runs "] = (
df [" team1_runs "] +
df [" team2_runs "]
)

df [" total_wickets "] = (
df [" team1_wickets "] +
df [" team2_wickets "]
)

highest_score = df [" total_runs "]. max ()

st . metric (
" Highest Combined Score ",
highest_score
)

seasons = sorted(
    df["season"].dropna().unique()
)

selected_season = st.selectbox(
    "Select Season",
    seasons
)

filtered_df = df[
    df["season"] == selected_season
]

st.dataframe(filtered_df)

teams = sorted(
    pd.concat([
        df["team1"],
        df["team2"]
    ]).dropna().unique()
)

selected_team = st.selectbox(
    "Select Team",
    teams
)

st.sidebar.title("Filters")

selected_season = st.sidebar.selectbox(
    "Season",
    sorted(df["season"].dropna().unique())
)

selected_team = st.sidebar.selectbox(
    "Team",
    teams
)

filtered_df = df[
    (df["season"] == selected_season) &
    (
        (df["team1"] == selected_team) |
        (df["team2"] == selected_team)
    )
]

st.dataframe(filtered_df)

matches_by_season = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

st.dataframe(matches_by_season)

team_wins = (
    df["winner"]
    .value_counts()
    .reset_index()
)

team_wins.columns = [
    "Team",
    "Wins"
]

st.dataframe(team_wins)

top_winners = (
    df["winner"]
    .value_counts()
    .head(10)
)

st.dataframe(top_winners)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("IPL Data Analysis")

df = pd.read_csv("IPL_Matches_Data_2008_2026.csv")

df.columns = df.columns.str.strip()

df["total_runs"] = df["team1_runs"] + df["team2_runs"]

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

st.sidebar.title("Filters")

seasons = sorted(
    df["season"].dropna().unique()
)

selected_season = st.sidebar.selectbox(
    "Select Season",
    seasons
)

teams = sorted(
    pd.concat([
        df["team1"],
        df["team2"]
    ]).dropna().unique()
)

selected_team = st.sidebar.selectbox(
    "Select Team",
    teams
)

filtered_df = df[
    (df["season"] == selected_season) &
    (
        (df["team1"] == selected_team) |
        (df["team2"] == selected_team)
    )
]

st.subheader(f"Analysis for Season: {selected_season}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Matches",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Runs",
        round(filtered_df["total_runs"].mean(), 2)
    )

with col3:
    st.metric(
        "Highest Score",
        filtered_df["total_runs"].max()
    )

st.subheader("Matches by Season")

matches_by_season = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

st.dataframe(
    matches_by_season,
    width="stretch"
)

st.subheader("Wins by Team")

team_wins = (
    df["winner"]
    .value_counts()
    .reset_index()
)

team_wins.columns = [
    "Team",
    "Wins"
]

st.dataframe(
    team_wins,
    width="stretch"
)

st.subheader("Top Winning Teams")

top_winners = (
    df["winner"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_winners.columns = [
    "Team",
    "Wins"
]

fig1 = px.bar(
    top_winners,
    x="Team",
    y="Wins",
    title="Top Winning Teams"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

st.subheader("Toss Decision Distribution")

toss_decision = (
    df["toss_decision"]
    .value_counts()
    .reset_index()
)

toss_decision.columns = [
    "Decision",
    "Count"
]

fig2 = px.pie(
    toss_decision,
    names="Decision",
    values="Count",
    title="Toss Decision Distribution"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

st.subheader("Matches by Season")

season_matches = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

fig3 = px.bar(
    season_matches,
    x="season",
    y="matches",
    title="Matches Played in Each Season"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

st.subheader("Runs by Season")

season_runs = (
    df.groupby("season")["total_runs"]
    .sum()
    .reset_index()
)

fig4 = px.line(
    season_runs,
    x="season",
    y="total_runs",
    title="Total Runs by Season"
)

st.plotly_chart(
    fig4,
    width="stretch"
)

st.subheader("Distribution of Total Match Runs")

fig5 = px.histogram(
    df,
    x="total_runs",
    nbins=30,
    title="Distribution of Total Match Runs"
)

st.plotly_chart(
    fig5,
    width="stretch"
)

st.subheader("Team 1 Runs vs Team 2 Runs")

fig6 = px.scatter(
    df,
    x="team1_runs",
    y="team2_runs",
    title="Team 1 Runs vs Team 2 Runs"
)

st.plotly_chart(
    fig6,
    width="stretch"
)

st.subheader("Matplotlib Distribution")

fig7, ax = plt.subplots()

ax.hist(
    df["total_runs"].dropna(),
    bins=30
)

ax.set_title("Distribution of Match Runs")
ax.set_xlabel("Total Runs")
ax.set_ylabel("Number of Matches")

st.pyplot(fig7)

st.subheader("Season and Run Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("Season Analysis")

    st.bar_chart(
        season_matches.set_index("season")
    )

with col2:
    st.write("Run Analysis")

    st.line_chart(
        season_runs.set_index("season")
    )

st.subheader("Key Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Matches",
        len(df)
    )

with col2:
    st.metric(
        "Seasons",
        df["season"].nunique()
    )

with col3:
    st.metric(
        "Venues",
        df["venue"].nunique()
    )

with st.expander("View Complete Dataset"):
    st.dataframe(
        df,
        width="stretch"
    )

with st.expander("View Statistical Summary"):
    st.dataframe(
        df.describe(),
        width="stretch"
    )

st.subheader("Filtered Data")

st.dataframe(
    filtered_df,
    width="stretch"
)
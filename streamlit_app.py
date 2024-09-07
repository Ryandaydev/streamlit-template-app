import streamlit as st
import httpx
import pandas as pd

st.title("Using GitHub Codespaces")
st.write(
    "Testing a change in the repo."
)
base_url = "https://fluffy-space-orbit-vrgrgj79q5hxjr5-8000.app.github.dev"

HEALTH_CHECK_ENDPOINT = "/"
LIST_LEAGUES_ENDPOINT = "/v0/leagues/"
LIST_PLAYERS_ENDPOINT = "/v0/players/"
LIST_PERFORMANCES_ENDPOINT = "/v0/performances/"
LIST_TEAMS_ENDPOINT = "/v0/teams/"
GET_COUNTS_ENDPOINT = "/v0/counts/"

def call_api_endpoint(
    api_endpoint: str, 
    api_params: dict = None
) -> httpx.Response:
    with httpx.Client(base_url=base_url) as client:
        response = client.get( api_endpoint, params=api_params)
        response.raise_for_status()
        return response
    
league_api_response = call_api_endpoint(LIST_LEAGUES_ENDPOINT)
league_data_df = pd.DataFrame(league_api_response.json())
st.write(league_data_df)


team_api_parameters = {'league_id': '5001'}
team_api_response = call_api_endpoint(LIST_TEAMS_ENDPOINT, team_api_parameters)
team_data_df = pd.DataFrame(team_api_response.json())
st.write(team_data_df)
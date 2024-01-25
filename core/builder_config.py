"""Configuration."""
import streamlit as st
import os

### DEFINE BUILDER_LLM #####
## Uncomment the LLM you want to use to construct the meta agent

## OpenAI
from llama_index.llms import OpenAI, AzureOpenAI

# set OpenAI Key - use Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets.openai_key
# load LLM
# BUILDER_LLM = OpenAI(model="gpt-4-1106-preview")
BUILDER_LLM = AzureOpenAI(
        model="gpt-35-turbo",
        engine="gpt-35-turbo",
        azure_deployment="gpt-35-turbo",
        deployment="gpt-35-turbo",
        deployment_name="gpt-35-turbo",
        azure_endpoint="https://east-us-2.openai.azure.com/",
        api_key="fa0",
        api_version="2023-07-01-preview"
    )
# # Anthropic (make sure you `pip install anthropic`)
# from llama_index.llms import Anthropic
# # set Anthropic key
# os.environ["ANTHROPIC_API_KEY"] = st.secrets.anthropic_key
# BUILDER_LLM = Anthropic()

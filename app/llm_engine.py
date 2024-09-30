import dotenv

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


# Name the API key as GOOGLE_API_KEY in the .env file.
dotenv.load_dotenv()


def get_model(*, model):
    return ChatGoogleGenerativeAI(model=model)


def get_human_message(*, content):
    return HumanMessage(content=content)
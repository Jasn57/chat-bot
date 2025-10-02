from utils import dotenv_values, OpenAI

# load api
config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])
from utils import dotenv_values, OpenAI

# load api
config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

response = client.responses.create(
    model="gpt-5",
    input=user_input
)
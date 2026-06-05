from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

client = genai.Client(api_key="ENTER_YOUR_API_KEY_HERE")

app = FastAPI(title="Adlytix AI Strategist", version="1.0")


class CampaignData(BaseModel):
    product_name: str
    target_audience: str


@app.get("/")
def home():
    return {"message": "Adlytix AI Backend is Running with Updated GenAI!"}


@app.post("/generate-strategy")
def generate_strategy(data: CampaignData):

    prompt = f"You are an expert digital marketer for an agency named Adlytix. Create a short Meta Ads strategy for a product named '{data.product_name}' targeting '{data.target_audience}'. Give me 2 catchy ad hooks and 3 targeting keywords and also give me the top perfume brands names and their sales."

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    return {
        "Product": data.product_name,
        "Audience": data.target_audience,
        "AI_Strategy": response.text,
    }

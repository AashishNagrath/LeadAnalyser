import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

client = genai.Client()

def generate_business_analysis(scraped_data):
    prompt = f"""
    You are a professional AI business consultant.

    Analyze the following company website data and generate:

    1. Company Overview
    2. Business Model
    3. Target Audience
    4. Key Strengths
    5. Website Observations
    6. AI Automation Opportunities
    7. Personalized Recommendations

    WEBSITE DATA:

    Title:
    {scraped_data.get("title")}

    Meta Description:
    {scraped_data.get("meta_description")}

    Headings:
    {scraped_data.get("headings")}

    Website Content:
    {scraped_data.get("content")}

    Make the analysis:
    - Professional
    - Personalized
    - Business-focused
    - Practical
    - Non-generic
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text

    except APIError as e:
        print(f"\n[API ERROR] Gemini API call failed: {e}")
        if e.code == 429:
            return "Error: The AI analysis tool is currently experiencing high volume (Rate Limit Exceeded). Please try again in a minute."
        return f"Error: Unable to generate analysis at this time. (Status Code: {e.code})"
        
    except Exception as e:
        print(f"\n[UNEXPECTED ERROR]: {e}")
        return "Error: An unexpected internal error occurred while processing the request."
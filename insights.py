from openai import OpenAI
import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENAI_KEY_API"),
)

MODEL = "mistralai/mistral-7b-instruct:free"  #"nvidia/llama-3.1-nemotron-ultra-253b-v1"

def generate_llm_insight(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": #"Act as a concise professional report writer. You’ve already done the thinking — now write ONLY the final insight in 2–3 sentences."
                    "You are an Senior Data Analyst who performs highest and best use analysis for clients so that they can build the most profitable business on their property. "
                    "Based on provided datatable, and city,  write a clear, actionable insights on the data. "
                    
                    # "Do not display any internal reasoning or <think> sections in the result — just give the final insight which you think is the most important"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.6,
            max_tokens=300
        )
        response = response.choices[0].message.content.strip()
        # final_response = extract_final_insight(response)
        print("output-------------------",response)
        return response
    except Exception as e:
        return f"⚠️ LLM error: {e}"
    
# def extract_final_insight(response_text):
#     """
#     Strips out any <think>... sections and returns just the final insight.
#     """
#     if "<think>" in response_text.lower():
#         parts = response_text.split("<think>")
#         # Get the last part after the last </think> or just last chunk
#         after_think = parts[-1].strip()

#         # Optionally remove lingering </think>
#         after_think = after_think.replace("</think>", "").strip()
#         return after_think
#     return response_text.strip()

def gender_insight(df, city, year):
    
    df = df.to_json(orient='records', lines=True)
    prompt = f"""Generate an insight for the given data table in JSON Format : {df}. 
    The table has the total, male and female population estimates.
    The data is for {city} in the year {year}
    What does this distribution imply for a highest and best use analysis?"""

    return  generate_llm_insight(prompt)

def age_wise_insight(df, city, year):
    
    df = df.to_json(orient='records', lines=True)
    prompt = f"""Generate an insight for the given datable in JSON Format : {df}. 
    This table has age wise distribution of the the total , male and female estimate.
    The data is for {city} in the year {year}
    What does this distribution imply for for a highest and best use analysis?"""

    return  generate_llm_insight(prompt)



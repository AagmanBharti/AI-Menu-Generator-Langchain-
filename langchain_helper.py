import os
from dotenv import load_dotenv

# Essential 2026 Imports
from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load your .env file
load_dotenv()

# Initialization: Using 2026 Stable Google Generative AI model
# gemini-2.5-flash is the successor to gemini-1.5 and is active right now.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

def generate_restaurant_name_and_items(cuisine):
    # Prompt 1: Name
    name_prompt = PromptTemplate.from_template(
        "Suggest one fancy name for a {cuisine} restaurant."
    )
    
    # Prompt 2: Menu Items
    menu_prompt = PromptTemplate.from_template(
    "Suggest five menu items for the restaurant named {restaurant_name}. "
    "Format the items as a comma-separated list."
    )

    # Build Simple Chains
    name_chain = name_prompt | llm | StrOutputParser()
    menu_chain = menu_prompt | llm | StrOutputParser()

    # Get Outputs
    restaurant_name = name_chain.invoke({"cuisine":cuisine}).strip()
    menu_items = menu_chain.invoke(
    {"restaurant_name": restaurant_name}
    ).strip()


    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }

if __name__ == "__main__":
    print("--- 2026 Environment Check (Conda + Python 3.10) ---")
    try:
        # Final test using the 2.5 series
        res = llm.invoke("Are you there?")
        print(f"✅ Success! AI says: {res.content}")
    except Exception as e:
        print(f"❌ Error: {e}")
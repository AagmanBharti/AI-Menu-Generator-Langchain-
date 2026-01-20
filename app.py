import streamlit as st
import langchain_helper

# Page Configuration
st.set_page_config(
    page_title="Restaurant Name & Menu Generator", 
    page_icon="🍽️",
    layout="centered"
    )

# Header Section
st.title("🍽️ AI Restaurant Idea Generator")
st.markdown("""
            Select a cuisine from the sidebar, and our AI will dream up a **unique restaurant name** and a **signature menu** for you!
            """)

# Sidebar
st.sidebar.image("https://img.icons8.com/fluency/48/000000/restaurant.png", width=50)
st.sidebar.title("Choose Cuisine")

#  Cuisine selection dropdown
cuisine = st.sidebar.selectbox(
    "Select a cuisine type:",
    ("Italian", "Chinese", "Mexican", "Arabic" , "Indian", "French", "Japanese", "Mediterranean", "Thai", "American", "Spanish")
)

# Main Logic
if cuisine:
    # Use a spinner to show the user the AI is working
    with st.spinner(f"👩‍🍳 Our AI Chef is creating {cuisine} ideas..."):
        try:
            # Call the backend helper function
            response = langchain_helper.generate_restaurant_name_and_items(cuisine)

            # Display Restaurant Name
            st.divider()
            st.markdown(f"** Recommended Name:**")
            st.success(f"🏷️{response['restaurant_name']}")

            # Display Menu Items
            st.markdown(f"**📃Signature Menu Items:**")

            # Split items and clean them up
            menu_items = response['menu_items'].split(",")

            # Create a bulleted list
            for item in menu_items:
                st.write(f"✨ {item.strip()}")

        except Exception as e:
            st.error(f"❌ Oops! Something went wrong. Please try again or check your API key.")
            st.exception(e)

# Footer
st.divider()
st.markdown("Developed with ❤️ using LangChain and Google Generative AI - 2026 Edition")
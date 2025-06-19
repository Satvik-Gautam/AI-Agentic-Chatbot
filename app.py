#Step 1 Setup Ui with Streamlit (Model Provider , Model Name , System , prompt , web_search ,messages)
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI" , layout="centered")
st.title("AI Chatbot Agent")
st.write("Interact With The AI Agents")

system_prompt = st.text_area("Define Your AI Agent As Required By Your Need : " , height =70 , placeholder ="Type Your System Prompt Here....")


MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "deepseek-r1-distill-llama-70b","gemma2-9b-it","qwen-2.5-32b","mistral-saba-24b"]

provider=st.radio("Select Provider:", ("Groq"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)


allow_web_search =st.checkbox("Allow Web Search")
user_query = user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything You Would Love To Know About It More....!")
API_URL = "http://127.0.0.1:9999/chat"
if st.button("Ask Agent!"):
    if user_query.strip():  
        #Step 2 connect with backend via URl
        import requests

        payload ={
            "model_name" : selected_model,
            "model_provider" :provider,
            "system_prompt" : system_prompt,
            "messages" : [user_query],
            "allow_search" : allow_web_search
        }

        response = requests.post(API_URL , json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"Final Response is : {response_data}")
# Step 1 Setup pydantic Model(Schema validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name : str
    model_provider :str
    system_prompt : str
    messages : List[str]
    allow_search : bool

# Step 2 Setup AI Agent from frontend request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent



ALLOWED_MODEL_NAMES=["deepseek-r1-distill-llama-70b", "llama-3.3-70b-versatile","gemma2-9b-it","qwen-2.5-32b","mistral-saba-24b"]
app = FastAPI(title="langGraph AI Agent")

@app.post("/chat")
def chat_end(request : RequestState):

    """
    API endpoint is to intereact with the chatbot using LangGraph and search tools.
    It Dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return{"Error Invalid Model Name kindly select a valid ai model"}
    
    llm_id = request.model_name
    messages = [{"role": "user", "content": msg} for msg in request.messages]
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    #Create an Ai agent and get reponse from it 
    response = get_response_from_ai_agent(llm_id , messages , allow_search,system_prompt,provider)
    return response



#Step 3 Run App and explore swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host ="127.0.0.1" , port =$PORT)

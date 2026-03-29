from langchain.chat_models import init_chat_model 
from langchain.messages import HumanMessage,SystemMessage
import gradio as gr  
import os

GEMINI_API_KEY = os.getenv('Gemini')

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GEMINI_API_KEY,
) 

def ai_assistant(input_text):
    messages = [
        SystemMessage("You are a helpful assistant."),
        HumanMessage(content=input_text)
    ]
    response = model.invoke(messages)
    return response.content 

demo = gr.Interface(
    fn=ai_assistant,
    inputs = gr.Textbox(lines=7, placeholder="Enter your Question here.....",label = "Question"),
    outputs = gr.Textbox(lines=7, label="Response"),
    title="AI Assistant",
    description="A minimal AI assistant powered by machine learning that processes user queries and generates intelligent responses.",
)

demo.launch(debug=True)

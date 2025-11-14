import gradio as gr
import requests
import json

# Your existing Ollama interaction function
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral" # Ensure this matches your downloaded model

# Function to interact with Ollama
def get_ollama_response(prompt, history):
    # Construct a full conversation prompt from history + current message
    full_conversation_prompt = ""
    # Format the history for the model. A common format is "User: ...\nAssistant: ..."
    for human_message, ai_message in history:
        full_conversation_prompt += f"User: {human_message}\nAssistant: {ai_message}\n"
    full_conversation_prompt += f"User: {prompt}\nAssistant:"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": full_conversation_prompt, # Sending the full conversation as prompt
        "stream": False 
        # "options": {"temperature": 0.7, "top_p": 0.9} # Example options
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Check for HTTP errors
        result = response.json()
        
        # Ollama's response often includes the prompt as part of the response text.
        # We need to extract only the generated part.
        # Check if 'response' key exists and is a string
        ollama_raw_response = result.get("response", "No response from Ollama.")
        if isinstance(ollama_raw_response, str):
            # Attempt to remove the echoed prompt. This might need fine-tuning
            # depending on how exactly Ollama echoes the prompt for your specific model.
            generated_text = ollama_raw_response.replace(full_conversation_prompt, "").strip()
            # If the replacement results in an empty string, or doesn't look right,
            # you might need a more robust parsing strategy.
            if not generated_text: # Fallback if replacement removes too much
                 generated_text = ollama_raw_response.strip()
        else:
            generated_text = str(ollama_raw_response) # Convert to string if not already

        return generated_text

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Is the server running?"
    except requests.exceptions.RequestException as e:
        return f"An API request error occurred: {e}"

# --- Gradio UI Code ---

demo = gr.ChatInterface(
    fn=get_ollama_response, # Your function to get the AI's response
    title=f"🤖DDS Chatbot",
    description=f"Chat with your locally running **{OLLAMA_MODEL.capitalize()}** model via Ollama!",
    
    # Updated: Specify type='messages' for chatbot and REMOVE the problematic button arguments
    chatbot=gr.Chatbot(height=500, type='messages'), 
    
    theme="soft", # A clean theme
    examples=[
        "Tell me a short story about a space explorer.",
        "Explain how large language models work in simple terms.",
        "What is the capital of France?"
    ],
    cache_examples=False, # Don't cache if your model is dynamic
    
    # Removed the following lines as they cause TypeError:
    # submit_btn="Send Message",
    # clear_btn="Clear Chat",
    # retry_btn="Try Again",
    # undo_btn="Undo Last"
)

if __name__ == "__main__":
    print(f"Starting Gradio UI for {OLLAMA_MODEL.capitalize()} chatbot...")
    print("Ensure your Ollama server is running in the background.")
    demo.launch() # This will open the UI in your default browser

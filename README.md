# 🤖 Local AI Chatbot with Gradio and Ollama

This project provides a simple, clean web interface to chat with a locally running large language model (like Mistral) managed by [Ollama](https://ollama.com/). The user interface is built with [Gradio](https://www.gradio.app/).

![Chatbot Screenshot](https://i.imgur.com/your-image-url.png)
*(Optional: You can take a screenshot of your running app, upload it to a site like Imgur, and paste the link here to show what it looks like.)*

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **[Ollama](https://ollama.com/)**: You must have Ollama installed and running. This project connects to the Ollama server to interact with the language model.
2.  **A Downloaded Ollama Model**: You need to have pulled a model. This project is configured to use `mistral` by default, but you can change it in the code.
    ```bash
    ollama pull mistral
    ```
3.  **[Python](https://www.python.org/downloads/)**: Version 3.8 or higher is recommended.
4.  **[Git](https://git-scm.com/)**: (Optional, but recommended for cloning the repository).

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Clone the Repository

Open your terminal or command prompt and clone this GitHub repository to your local machine.

```bash
git clone https://github.com/divyadeepsinghchouhan-dot/chatbot.git
cd chatbot
```

### 2. Set Up a Virtual Environment (Recommended)

It is highly recommended to create a virtual environment to keep the project's dependencies isolated from your system's global Python installation.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
You will know the virtual environment is active when you see `(venv)` at the beginning of your terminal prompt.

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Ensure Ollama is Running

Before launching the app, you must start the Ollama server. Open a **new, separate terminal window** and run:

```bash
ollama serve
```
Keep this terminal window open. It is the backend that powers the chatbot.

### 5. Run the Gradio Application

Now, in your original terminal (where you activated the virtual environment), run the Python script to launch the web interface.

Let's assume the main script is named `app.py`:
```bash
python app.py
```
*(If your Python script has a different name, like `gradio_chatbot_ui.py`, use that name instead.)*

After running the command, you will see output in the terminal indicating that a local server is running, usually at an address like `http://127.0.0.1:7860`.

### 6. Access the Chatbot

Open your web browser and navigate to the local URL provided in the terminal (e.g., `http://127.0.0.1:7860`). You should now see the chatbot interface and be able to interact with your local AI model.

---

## ⚙️ Configuration

-   **Changing the Model**: To use a different Ollama model (e.g., `llama3`), open the `app.py` file and change the value of the `OLLAMA_MODEL` variable:
    ```python
    OLLAMA_MODEL = "llama3" # Change from "mistral"
    ```
    Make sure you have pulled the new model with `ollama pull llama3` first.

-   **Changing the Ollama Host**: If your Ollama server is running on a different address or port, modify the `OLLAMA_API_URL` variable in `app.py`.

##  Maintanence 

### To close the application
-  `ctrl+c` in the terminal

### To exit virtual environment
- `deactivate`

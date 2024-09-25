# LangChain OpenAI Chatbot

This project implements a simple chatbot using Streamlit, LangChain, and OpenAI's GPT models. The chatbot supports two types of memory: Buffer Memory and Summary Memory.

## Features

- Interactive chat interface using Streamlit
- Integration with OpenAI's GPT models through LangChai
- Two memory types:
  - Buffer Memory: Stores the full conversation history
  - Summary Memory: Maintains a summary of the conversation
- Option to switch between memory types during the conversation.
- Ability to view conversation history or summary
- Option to clear the conversation

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
   

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable or in .env file:
   ```
   OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run chatbot_app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Interact with the chatbot:
   - Type your messages in the "You:" input field
   - Choose between Buffer Memory and Summary Memory
   - Use the "Show Conversation History/Summary" button to view the current conversation state
   - Use the "Clear Conversation" button to start a new conversation

## Configuration

You can modify the `chatbot_app.py` file to change the OpenAI model or adjust other parameters:

- Change the model by modifying the `model_name` parameter in the `ChatOpenAI` initialization
- Adjust the `temperature` parameter to control the randomness of the AI's responses

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI](https://openai.com/)
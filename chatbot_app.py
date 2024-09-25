import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain

# Initialize OpenAI API (make sure to set your API key in the environment variables)
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# Initialize session state
if 'memory_type' not in st.session_state:
    st.session_state.memory_type = 'Buffer Memory'
if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferMemory()
if 'summary_memory' not in st.session_state:
    st.session_state.summary_memory = ConversationSummaryMemory(llm=llm)
if 'conversation' not in st.session_state:
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.buffer_memory,
        verbose=True
    )

st.title("LangChain OpenAI Chatbot")

# Memory type selection
memory_type = st.radio("Select Memory Type:", ("Buffer Memory", "Summary Memory"))
if memory_type != st.session_state.memory_type:
    st.session_state.memory_type = memory_type
    if memory_type == "Buffer Memory":
        st.session_state.conversation.memory = st.session_state.buffer_memory
    else:
        st.session_state.conversation.memory = st.session_state.summary_memory

# User input
user_input = st.text_input("You:")

if user_input:
    # Get AI response
    response = st.session_state.conversation.predict(input=user_input)
    st.write(f"AI: {response}")

# Show conversation history/summary
if st.button("Show Conversation History/Summary"):
    if st.session_state.memory_type == "Buffer Memory":
        st.write(st.session_state.buffer_memory.chat_memory.messages)
    else:
        st.write(st.session_state.summary_memory.moving_summary_buffer)

# Clear conversation
if st.button("Clear Conversation"):
    if st.session_state.memory_type == "Buffer Memory":
        st.session_state.buffer_memory.clear()
    else:
        st.session_state.summary_memory.clear()
    st.success("Conversation cleared!")
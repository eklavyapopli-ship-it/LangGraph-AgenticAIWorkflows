from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph
from typing_extensions import Dict, TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state:State):
    return {"messages":"hey this is a message from chatbot"}

def sampleNode(state:State):
    return {"messages":["sample message appended"]}

graphBuilder = StateGraph(State)
graphBuilder.add_node("chatbot", chatbot)
graphBuilder.add_node("sampleNode", sampleNode)

# state = {"messages": ["hey there"]}
# node runs = chatbot(state:["hey there"]) -> hey there, this is a chatbot
# state = {"messages": ["hey there","hey there, this is a chatbot"]}

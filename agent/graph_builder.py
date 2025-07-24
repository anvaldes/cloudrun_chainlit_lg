from typing import TypedDict
from langgraph.graph import StateGraph, END
from agent.gemini_model import chat

class AgentState(TypedDict):
    history: list[str]

def route_input(state: AgentState) -> str:
    prompt = state["history"][-1].strip().upper()
    return "beto_node" if prompt == "BETO" else "gemini_node"

def beto_response(state: AgentState) -> AgentState:
    state["history"].append("🔥 Grande Beto!!")
    return state

def process_input(state: AgentState) -> AgentState:
    prompt = state["history"][-1]
    try:
        response = chat.send_message(prompt)
        state["history"].append(response.text)
    except Exception as e:
        state["history"].append(f"⚠️ Error al responder: {e}")
    return state

builder = StateGraph(AgentState)
builder.add_node("beto_node", beto_response)
builder.add_node("gemini_node", process_input)
builder.set_conditional_entry_point(route_input, {
    "beto_node": "beto_node",
    "gemini_node": "gemini_node"
})
builder.add_edge("beto_node", END)
builder.add_edge("gemini_node", END)

graph = builder.compile()

print("🧠 Grafo LangGraph compilado")

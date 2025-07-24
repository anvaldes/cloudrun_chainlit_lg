import chainlit as cl
from agent.graph_builder import graph
from agent.utils import prepare_initial_state

@cl.on_message
async def on_message(message: cl.Message):
    state = prepare_initial_state(message.content)
    try:
        result = graph.invoke(state)
        await cl.Message(content=result["history"][-1]).send()
    except Exception as e:
        await cl.Message(content=f"⚠️ Error interno: {e}").send()

print("🚀 Chainlit iniciado desde main.py")

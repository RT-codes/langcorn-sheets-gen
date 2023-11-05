from langcorn import create_service

app = create_service()

app = create_service(
    "api.llm_chain:chain",
    "api.conversation_chain:conversation",
)


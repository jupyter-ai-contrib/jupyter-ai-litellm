import json


async def test_get_example(jp_fetch):
    # When
    response = await jp_fetch("jupyter-ai-litellm", "get-example")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /jupyter-ai-litellm/get-example endpoint!"
    }

async def test_get_chat_models(jp_fetch):
    # When
    response = await jp_fetch("api", "ai", "models", "chat")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    chat_models = payload.get("chat_models")

    assert chat_models
    assert len(chat_models) > 0
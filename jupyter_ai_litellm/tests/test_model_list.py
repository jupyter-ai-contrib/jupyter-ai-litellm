import pytest


def test_chat_models_no_duplicates():
    from jupyter_ai_litellm.model_list import CHAT_MODELS

    assert len(CHAT_MODELS) == len(set(CHAT_MODELS)), "CHAT_MODELS must not contain duplicates"


def test_embedding_models_no_duplicates():
    from jupyter_ai_litellm.model_list import EMBEDDING_MODELS

    assert len(EMBEDDING_MODELS) == len(set(EMBEDDING_MODELS)), "EMBEDDING_MODELS must not contain duplicates"


def test_chat_models_excludes_non_chat_modalities():
    from jupyter_ai_litellm.model_list import CHAT_MODELS

    for model_id in CHAT_MODELS:
        lower = model_id.lower()
        assert "dall-e" not in lower, f"Image model found in CHAT_MODELS: {model_id}"
        assert "tts-1" not in lower, f"TTS model found in CHAT_MODELS: {model_id}"
        assert "whisper-1" not in lower, f"Whisper model found in CHAT_MODELS: {model_id}"
        assert "text-moderation" not in lower, f"Moderation model found in CHAT_MODELS: {model_id}"


def test_chat_models_contains_expected_models():
    from jupyter_ai_litellm.model_list import CHAT_MODELS

    # Standard chat models must be present
    assert any("gpt-4" in m for m in CHAT_MODELS), "Expected GPT-4 family models in CHAT_MODELS"
    assert any("claude" in m for m in CHAT_MODELS), "Expected Claude models in CHAT_MODELS"


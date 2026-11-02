from litellm import all_embedding_models, model_cost, models_by_provider

chat_model_ids: set[str] = set()
embedding_model_ids: set[str] = set(all_embedding_models)

# 1. Populate explicitly typed models from litellm.model_cost.
# LiteLLM's model_cost catalogs models with their canonical mode
# ('chat', 'embedding', 'image_generation', 'audio_transcription', etc.).
for model_id, spec in model_cost.items():
    if not isinstance(spec, dict) or model_id == "sample_spec":
        continue
    mode = spec.get("mode")
    if mode == "chat":
        chat_model_ids.add(model_id)
    elif mode == "embedding":
        embedding_model_ids.add(model_id)

# 2. Iterate through models_by_provider for provider-prefixed IDs
# and any models not covered by model_cost.
_NON_CHAT_KEYWORDS = (
    "dall-e",
    "imagen",
    "flux",
    "tts-",
    "tts",
    "whisper",
    "moderation",
    "rerank",
    "realtime",
    "stable-diffusion",
)

for provider_name, provider_models in models_by_provider.items():
    for model_name in provider_models:
        if model_name.startswith(f"{provider_name}/"):
            model_id = model_name
        else:
            model_id = f"{provider_name}/{model_name}"

        # If already categorized, avoid re-evaluating
        if model_id in chat_model_ids or model_id in embedding_model_ids:
            continue

        spec = model_cost.get(model_id) or model_cost.get(model_name)
        if isinstance(spec, dict):
            mode = spec.get("mode")
            if mode == "chat":
                chat_model_ids.add(model_id)
            elif mode == "embedding":
                embedding_model_ids.add(model_id)
            # Explicitly exclude non-chat modes (image, audio, moderation, etc.)
            continue

        # Fallback for models without an entry in model_cost:
        is_embedding = (
            model_name in embedding_model_ids
            or model_id in embedding_model_ids
            or "embed" in model_id.lower()
        )

        if is_embedding:
            embedding_model_ids.add(model_id)
        else:
            is_non_chat = any(kw in model_id.lower() for kw in _NON_CHAT_KEYWORDS)
            if not is_non_chat:
                chat_model_ids.add(model_id)


CHAT_MODELS = sorted(chat_model_ids)
"""
List of chat model IDs, following the `litellm` syntax.
"""

EMBEDDING_MODELS = sorted(embedding_model_ids)
"""
List of embedding model IDs, following the `litellm` syntax.
"""

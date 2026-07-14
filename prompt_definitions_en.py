# prompt_definitions_en.py
# -*- coding: utf-8 -*-
"""
Load all English prompts from prompt_en.yaml.

Integrates the Snowflake Writing Method, Character Arc Theory, the Three-Element Suspense Model, etc.,
including prompts for summarizing recent chapters / extracting next-chapter keywords, and chapter body writing prompts.

When English mode is enabled, main_window injects this module's attributes into prompt_definitions.
"""
from pathlib import Path

import yaml

_PROMPT_YAML = Path(__file__).resolve().parent / "prompt_en.yaml"

# =============== Global Style Enforcement ===============
# Injected into all prompts after loading from YAML.
_STYLE_REQUIREMENTS = (
    "- CRITICAL: Never use em dashes (—), en dashes (–), or double dashes (--) in any writing."
)


def _load_prompts_from_yaml(path: Path = _PROMPT_YAML) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid prompt YAML (expected mapping): {path}")
    return data


def _inject_style_requirements(prompt_text: str) -> str:
    if "Format requirements:" in prompt_text:
        return prompt_text.replace(
            "Format requirements:", f"Format requirements:\n{_STYLE_REQUIREMENTS}"
        )
    if "Requirements:" in prompt_text:
        return prompt_text.replace("Requirements:", f"Requirements:\n{_STYLE_REQUIREMENTS}")
    if "Generation rules:" in prompt_text:
        return prompt_text.replace(
            "Generation rules:", f"Generation rules:\n{_STYLE_REQUIREMENTS}"
        )
    if "<<Character State Format Requirements>>" in prompt_text:
        return prompt_text.replace(
            "<<Character State Format Requirements>>",
            f"<<Character State Format Requirements>>\n{_STYLE_REQUIREMENTS}",
        )
    return prompt_text + f"\n\nStyle Requirement:\n{_STYLE_REQUIREMENTS}"


_prompts = _load_prompts_from_yaml()
for _name, _text in list(_prompts.items()):
    if isinstance(_text, str) and (_name.endswith("_prompt") or _name.endswith("_Prompt")):
        _prompts[_name] = _inject_style_requirements(_text)

globals().update(_prompts)

# Explicit names for static analysis / import clarity
summarize_recent_chapters_prompt = _prompts["summarize_recent_chapters_prompt"]
knowledge_search_prompt = _prompts["knowledge_search_prompt"]
knowledge_filter_prompt = _prompts["knowledge_filter_prompt"]
core_seed_prompt = _prompts["core_seed_prompt"]
character_dynamics_prompt = _prompts["character_dynamics_prompt"]
world_building_prompt = _prompts["world_building_prompt"]
plot_architecture_prompt = _prompts["plot_architecture_prompt"]
chapter_blueprint_prompt = _prompts["chapter_blueprint_prompt"]
chunked_chapter_blueprint_prompt = _prompts["chunked_chapter_blueprint_prompt"]
summary_prompt = _prompts["summary_prompt"]
create_character_state_prompt = _prompts["create_character_state_prompt"]
update_character_state_prompt = _prompts["update_character_state_prompt"]
first_chapter_draft_prompt = _prompts["first_chapter_draft_prompt"]
next_chapter_draft_prompt = _prompts["next_chapter_draft_prompt"]
Character_Import_Prompt = _prompts["Character_Import_Prompt"]
enrich_prompt = _prompts["enrich_prompt"]
CONSISTENCY_PROMPT = _prompts["CONSISTENCY_PROMPT"]

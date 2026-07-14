# prompt_definitions.py
# -*- coding: utf-8 -*-
"""
从 prompt_zh.yaml 加载所有提示词 (Prompt)。

整合雪花写作法、角色弧光理论、悬念三要素模型等，
并包含前三章摘要/下一章关键字提炼提示词，以及章节正文写作提示词。

切换到英文模式时，main_window 会将 prompt_definitions_en 的属性注入本模块；
切回中文时通过 reload 本模块重新从 YAML 加载。
"""
from pathlib import Path

import yaml

_PROMPT_YAML = Path(__file__).resolve().parent / "prompt_zh.yaml"


def _load_prompts_from_yaml(path: Path = _PROMPT_YAML) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid prompt YAML (expected mapping): {path}")
    return data


_prompts = _load_prompts_from_yaml()
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

# -*- coding: utf-8 -*-
"""Localized section headers for Novel_architecture.txt."""
import config_manager

# Section titles for Novel_architecture.txt by prompt language.
_ARCHITECTURE_SECTION_LABELS = {
    "zh": {
        "setting": "小说设定",
        "meta": "主题：{topic},类型：{genre},篇幅：约{number_of_chapters}章（每章{word_number}字）",
        "core_seed": "核心种子",
        "character_dynamics": "角色动力学",
        "world_building": "世界观",
        "plot_architecture": "三幕式情节架构",
    },
    "en": {
        "setting": "Novel Setting",
        "meta": (
            "Theme: {topic}, Genre: {genre}, "
            "Length: approx. {number_of_chapters} chapters "
            "({word_number} words each)"
        ),
        "core_seed": "Core Seed",
        "character_dynamics": "Character Dynamics",
        "world_building": "World Building",
        "plot_architecture": "Three-Act Plot Structure",
    },
    "kr": {
        "setting": "소설 설정",
        "meta": (
            "주제: {topic}, 장르: {genre}, "
            "분량: 약 {number_of_chapters}장(장당 {word_number}자)"
        ),
        "core_seed": "이야기 핵",
        "character_dynamics": "인물 역학",
        "world_building": "세계관",
        "plot_architecture": "3막 플롯 구조",
    },
}


def architecture_section_labels(lang: str | None = None) -> dict:
    """Return localized section labels for the active (or given) prompt language."""
    code = lang if lang is not None else getattr(config_manager, "PROMPT_LANGUAGE", "zh")
    return _ARCHITECTURE_SECTION_LABELS.get(code, _ARCHITECTURE_SECTION_LABELS["zh"])


def format_architecture_document(
    topic: str,
    genre: str,
    number_of_chapters: int,
    word_number: int,
    core_seed_result: str,
    character_dynamics_result: str,
    world_building_result: str,
    plot_arch_result: str,
    lang: str | None = None,
) -> str:
    """Assemble Novel_architecture.txt body with language-aware section headers."""
    labels = architecture_section_labels(lang)
    meta = labels["meta"].format(
        topic=topic,
        genre=genre,
        number_of_chapters=number_of_chapters,
        word_number=word_number,
    )
    return (
        f"#=== 0) {labels['setting']} ===\n"
        f"{meta}\n\n"
        f"#=== 1) {labels['core_seed']} ===\n"
        f"{core_seed_result}\n\n"
        f"#=== 2) {labels['character_dynamics']} ===\n"
        f"{character_dynamics_result}\n\n"
        f"#=== 3) {labels['world_building']} ===\n"
        f"{world_building_result}\n\n"
        f"#=== 4) {labels['plot_architecture']} ===\n"
        f"{plot_arch_result}\n"
    )

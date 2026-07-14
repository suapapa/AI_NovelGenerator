# -*- coding: utf-8 -*-
import unittest

from novel_generator.architecture_format import format_architecture_document


class ArchitectureDocumentLanguageTest(unittest.TestCase):
    def _format(self, lang: str) -> str:
        return format_architecture_document(
            topic="테스트 주제",
            genre="드라마",
            number_of_chapters=3,
            word_number=1000,
            core_seed_result="seed",
            character_dynamics_result="chars",
            world_building_result="world",
            plot_arch_result="plot",
            lang=lang,
        )

    def test_korean_section_headers(self):
        text = self._format("kr")
        self.assertIn("#=== 0) 소설 설정 ===", text)
        self.assertIn("주제: 테스트 주제, 장르: 드라마, 분량: 약 3장(장당 1000자)", text)
        self.assertIn("#=== 1) 이야기 핵 ===", text)
        self.assertIn("#=== 2) 인물 역학 ===", text)
        self.assertIn("#=== 3) 세계관 ===", text)
        self.assertIn("#=== 4) 3막 플롯 구조 ===", text)
        self.assertNotIn("小说设定", text)

    def test_english_section_headers(self):
        text = self._format("en")
        self.assertIn("#=== 0) Novel Setting ===", text)
        self.assertIn("Theme: 테스트 주제, Genre: 드라마", text)
        self.assertIn("#=== 1) Core Seed ===", text)
        self.assertIn("#=== 4) Three-Act Plot Structure ===", text)

    def test_chinese_section_headers_remain_default(self):
        text = self._format("zh")
        self.assertIn("#=== 0) 小说设定 ===", text)
        self.assertIn(
            "主题：테스트 주제,类型：드라마,篇幅：约3章（每章1000字）",
            text,
        )
        self.assertIn("#=== 1) 核心种子 ===", text)
        self.assertIn("#=== 2) 角色动力学 ===", text)
        self.assertIn("#=== 3) 世界观 ===", text)
        self.assertIn("#=== 4) 三幕式情节架构 ===", text)


if __name__ == "__main__":
    unittest.main()

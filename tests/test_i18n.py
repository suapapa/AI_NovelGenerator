# -*- coding: utf-8 -*-
import unittest

from ui.i18n import t, tip, set_language, get_language


class I18nTest(unittest.TestCase):
    def tearDown(self):
        set_language("zh")

    def test_switch_main_strings(self):
        set_language("zh")
        self.assertIn("生成架构", t("main.step1"))
        set_language("en")
        self.assertEqual(t("main.step1"), "Step1. Architecture")
        set_language("kr")
        self.assertIn("구조", t("main.step1"))

    def test_tooltip_follows_language(self):
        set_language("en")
        self.assertIn("theme", tip("topic").lower())
        set_language("kr")
        self.assertIn("주제", tip("topic"))

    def test_format_kwargs(self):
        set_language("en")
        self.assertEqual(t("editor.word_count", count=12), "Words: 12")
        self.assertEqual(get_language(), "en")


if __name__ == "__main__":
    unittest.main()

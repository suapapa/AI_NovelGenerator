# tooltips.py
# -*- coding: utf-8 -*-
"""Backward-compatible tooltip lookup; prefers live UI language via ui.i18n."""

from ui.i18n import tip as _tip, t


class _TooltipProxy(dict):
    """dict-like wrapper so existing tooltips.get(key, ...) keeps working."""

    def get(self, key, default=None):
        text = _tip(key)
        if text == t("msg.no_tooltip") and default is not None:
            return default
        return text

    def __getitem__(self, key):
        return _tip(key)


tooltips = _TooltipProxy()

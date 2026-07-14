# ui/summary_tab.py
# -*- coding: utf-8 -*-
import os
import customtkinter as ctk
from tkinter import messagebox
from utils import read_file, save_string_to_txt, clear_file_content, get_word_count
from ui.context_menu import TextWidgetContextMenu
from ui.i18n import t


def build_summary_tab(self):
    self.summary_tab = self.track_tab(self.tabview, "summary", "tab.summary")
    self.summary_tab.rowconfigure(0, weight=0)
    self.summary_tab.rowconfigure(1, weight=1)
    self.summary_tab.columnconfigure(0, weight=1)

    load_btn = ctk.CTkButton(
        self.summary_tab,
        text=t("editor.load_summary"),
        command=self.load_global_summary,
        font=("Microsoft YaHei", 12),
    )
    load_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.bind_i18n(load_btn, "editor.load_summary")

    self.word_count_label = ctk.CTkLabel(
        self.summary_tab, text=t("editor.word_count", count=0), font=("Microsoft YaHei", 12)
    )
    self.word_count_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    save_btn = ctk.CTkButton(
        self.summary_tab,
        text=t("editor.save"),
        command=self.save_global_summary,
        font=("Microsoft YaHei", 12),
    )
    save_btn.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    self.bind_i18n(save_btn, "editor.save")

    self.summary_text = ctk.CTkTextbox(self.summary_tab, wrap="word", font=("Microsoft YaHei", 12))

    def update_word_count(event=None):
        text = self.summary_text.get("0.0", "end-1c")
        count = get_word_count(text)
        self.word_count_label.configure(text=t("editor.word_count", count=count))

    self.summary_text.bind("<KeyRelease>", update_word_count)
    self.summary_text.bind("<ButtonRelease>", update_word_count)
    self.bind_i18n(
        self.word_count_label,
        lambda: t(
            "editor.word_count",
            count=get_word_count(self.summary_text.get("0.0", "end-1c")),
        ),
    )
    TextWidgetContextMenu(self.summary_text)
    self.summary_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5, columnspan=3)


def load_global_summary(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    filename = os.path.join(filepath, "global_summary.txt")
    content = read_file(filename)
    self.summary_text.delete("0.0", "end")
    self.summary_text.insert("0.0", content)
    self.log("已加载 global_summary.txt 到编辑区。")


def save_global_summary(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    content = self.summary_text.get("0.0", "end").strip()
    filename = os.path.join(filepath, "global_summary.txt")
    clear_file_content(filename)
    save_string_to_txt(content, filename)
    self.log("已保存对 global_summary.txt 的修改。")

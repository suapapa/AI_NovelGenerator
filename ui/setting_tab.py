# ui/setting_tab.py
# -*- coding: utf-8 -*-
import os
import customtkinter as ctk
from tkinter import messagebox
from utils import read_file, save_string_to_txt, clear_file_content, get_word_count
from ui.context_menu import TextWidgetContextMenu
from ui.i18n import t


def build_setting_tab(self):
    self.setting_tab = self.track_tab(self.tabview, "architecture", "tab.architecture")
    self.setting_tab.rowconfigure(0, weight=0)
    self.setting_tab.rowconfigure(1, weight=1)
    self.setting_tab.columnconfigure(0, weight=1)

    load_btn = ctk.CTkButton(
        self.setting_tab,
        text=t("editor.load_architecture"),
        command=self.load_novel_architecture,
        font=("Microsoft YaHei", 12),
    )
    load_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.bind_i18n(load_btn, "editor.load_architecture")

    self.setting_word_count_label = ctk.CTkLabel(
        self.setting_tab, text=t("editor.word_count", count=0), font=("Microsoft YaHei", 12)
    )
    self.setting_word_count_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    save_btn = ctk.CTkButton(
        self.setting_tab,
        text=t("editor.save"),
        command=self.save_novel_architecture,
        font=("Microsoft YaHei", 12),
    )
    save_btn.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    self.bind_i18n(save_btn, "editor.save")

    self.setting_text = ctk.CTkTextbox(self.setting_tab, wrap="word", font=("Microsoft YaHei", 12))

    def update_word_count(event=None):
        text = self.setting_text.get("0.0", "end-1c")
        count = get_word_count(text)
        self.setting_word_count_label.configure(text=t("editor.word_count", count=count))

    self.setting_text.bind("<KeyRelease>", update_word_count)
    self.setting_text.bind("<ButtonRelease>", update_word_count)
    self.bind_i18n(
        self.setting_word_count_label,
        lambda: t("editor.word_count", count=get_word_count(self.setting_text.get("0.0", "end-1c"))),
    )
    TextWidgetContextMenu(self.setting_text)
    self.setting_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5, columnspan=3)


def load_novel_architecture(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    filename = os.path.join(filepath, "Novel_architecture.txt")
    content = read_file(filename)
    self.setting_text.delete("0.0", "end")
    self.setting_text.insert("0.0", content)
    self.log(t("log.loaded_file", file="Novel_architecture.txt"))


def save_novel_architecture(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath_config"))
        return
    content = self.setting_text.get("0.0", "end").strip()
    filename = os.path.join(filepath, "Novel_architecture.txt")
    clear_file_content(filename)
    save_string_to_txt(content, filename)
    self.log(t("log.saved_file", file="Novel_architecture.txt"))

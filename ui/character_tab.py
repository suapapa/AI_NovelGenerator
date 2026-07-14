# ui/character_tab.py
# -*- coding: utf-8 -*-
import os
import customtkinter as ctk
from tkinter import messagebox
from utils import read_file, save_string_to_txt, clear_file_content, get_word_count
from ui.context_menu import TextWidgetContextMenu
from ui.i18n import t


def build_character_tab(self):
    self.character_tab = self.track_tab(self.tabview, "character", "tab.character")
    self.character_tab.rowconfigure(0, weight=0)
    self.character_tab.rowconfigure(1, weight=1)
    self.character_tab.columnconfigure(0, weight=1)

    load_btn = ctk.CTkButton(
        self.character_tab,
        text=t("editor.load_character"),
        command=self.load_character_state,
        font=("Microsoft YaHei", 12),
    )
    load_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.bind_i18n(load_btn, "editor.load_character")

    self.character_wordcount_label = ctk.CTkLabel(
        self.character_tab, text=t("editor.word_count", count=0), font=("Microsoft YaHei", 12)
    )
    self.character_wordcount_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    save_btn = ctk.CTkButton(
        self.character_tab,
        text=t("editor.save"),
        command=self.save_character_state,
        font=("Microsoft YaHei", 12),
    )
    save_btn.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    self.bind_i18n(save_btn, "editor.save")

    self.character_text = ctk.CTkTextbox(self.character_tab, wrap="word", font=("Microsoft YaHei", 12))

    def update_word_count(event=None):
        text = self.character_text.get("0.0", "end-1c")
        text_length = get_word_count(text)
        self.character_wordcount_label.configure(text=t("editor.word_count", count=text_length))

    self.character_text.bind("<KeyRelease>", update_word_count)
    self.character_text.bind("<ButtonRelease>", update_word_count)
    self.bind_i18n(
        self.character_wordcount_label,
        lambda: t(
            "editor.word_count",
            count=get_word_count(self.character_text.get("0.0", "end-1c")),
        ),
    )
    TextWidgetContextMenu(self.character_text)
    self.character_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5, columnspan=3)


def load_character_state(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    filename = os.path.join(filepath, "character_state.txt")
    content = read_file(filename)
    self.character_text.delete("0.0", "end")
    self.character_text.insert("0.0", content)
    self.log(t("log.loaded_file", file="character_state.txt"))


def save_character_state(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    content = self.character_text.get("0.0", "end").strip()
    filename = os.path.join(filepath, "character_state.txt")
    clear_file_content(filename)
    save_string_to_txt(content, filename)
    self.log(t("log.saved_file", file="character_state.txt"))

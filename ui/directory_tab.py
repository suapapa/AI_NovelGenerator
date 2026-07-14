# ui/directory_tab.py
# -*- coding: utf-8 -*-
import os
import customtkinter as ctk
from tkinter import messagebox
from utils import read_file, save_string_to_txt, clear_file_content, get_word_count
from ui.context_menu import TextWidgetContextMenu
from ui.i18n import t


def build_directory_tab(self):
    self.directory_tab = self.track_tab(self.tabview, "blueprint", "tab.blueprint")
    self.directory_tab.rowconfigure(0, weight=0)
    self.directory_tab.rowconfigure(1, weight=1)
    self.directory_tab.columnconfigure(0, weight=1)

    load_btn = ctk.CTkButton(
        self.directory_tab,
        text=t("editor.load_directory"),
        command=self.load_chapter_blueprint,
        font=("Microsoft YaHei", 12),
    )
    load_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.bind_i18n(load_btn, "editor.load_directory")

    self.directory_word_count_label = ctk.CTkLabel(
        self.directory_tab, text=t("editor.word_count", count=0), font=("Microsoft YaHei", 12)
    )
    self.directory_word_count_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    save_btn = ctk.CTkButton(
        self.directory_tab,
        text=t("editor.save"),
        command=self.save_chapter_blueprint,
        font=("Microsoft YaHei", 12),
    )
    save_btn.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    self.bind_i18n(save_btn, "editor.save")

    self.directory_text = ctk.CTkTextbox(self.directory_tab, wrap="word", font=("Microsoft YaHei", 12))

    def update_word_count(event=None):
        text = self.directory_text.get("0.0", "end-1c")
        count = get_word_count(text)
        self.directory_word_count_label.configure(text=t("editor.word_count", count=count))

    self.directory_text.bind("<KeyRelease>", update_word_count)
    self.directory_text.bind("<ButtonRelease>", update_word_count)
    self.bind_i18n(
        self.directory_word_count_label,
        lambda: t(
            "editor.word_count",
            count=get_word_count(self.directory_text.get("0.0", "end-1c")),
        ),
    )
    TextWidgetContextMenu(self.directory_text)
    self.directory_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5, columnspan=3)


def load_chapter_blueprint(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    filename = os.path.join(filepath, "Novel_directory.txt")
    content = read_file(filename)
    self.directory_text.delete("0.0", "end")
    self.directory_text.insert("0.0", content)
    self.log("已加载 Novel_directory.txt 到编辑区。")


def save_chapter_blueprint(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning(t("title.warning"), t("msg.set_filepath"))
        return
    content = self.directory_text.get("0.0", "end").strip()
    filename = os.path.join(filepath, "Novel_directory.txt")
    clear_file_content(filename)
    save_string_to_txt(content, filename)
    self.log("已保存对 Novel_directory.txt 的修改。")

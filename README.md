# 📖 Automatic Novel Generation Tool

[中文文档](./README_zh-CN.md) | English | [日本語](./README_ja.md) | [Français](./README_fr-FR.md) | [Sawcuengh](./README_sawcuengh.md) | [한국어](./README_kr.md)

> ~~Currently I don't have much energy to maintain this project. The project brings no revenue, and with graduation approaching I have many other priorities. If time permits in the future I may consider a refactor using newer technologies. — 2025/09/24~~
>
>- ~~**(2026/03/09):** This project will be refactored soon, featuring modern implementations and fresh creative concepts.~~
>
> **Update (2026/03/25):** The refactored version has completed initial development (only the main framework is done, features are not yet available) and will be uploaded to the dev branch within a week. Subsequent development will also be synchronized on the branch.

<div align="center">
  
✨ **Core Features** ✨

| Module                | Key Capabilities                        |
|-----------------------|-----------------------------------------|
| 🎨 Novel Setting Workshop | Worldbuilding / Character Design / Plot Blueprint |
| 📖 Intelligent Chapter Generation | Multi-stage generation to ensure plot coherence |
| 🧠 State Tracking System | Character development trajectory / Foreshadowing management |
| 🔍 Semantic Search Engine | Vector-based long-term context consistency |
| 📚 Knowledge Base Integration | Supports local document references |
| ✅ Automatic Proofreading | Detects plot contradictions and logical conflicts |
| 🖥 Visual Workbench | Full-process GUI for configuration / generation / proofreading |

</div>

> A multifunctional novel generator built on large language models. Helps you efficiently create long-form stories with consistent settings and rigorous logic.

---

## 📑 Table of Contents
1. [Environment Preparation](#-environment-preparation)  
2. [Project Structure](#-project-structure)  
3. [Configuration Guide](#⚙️-configuration-guide)  
4. [Run Instructions](#🚀-run-instructions)  
5. [User Guide](#📘-user-guide)  
6. [FAQ](#❓-faq)  

---

## 🛠 Environment Preparation
Ensure the environment meets the following requirements:
- **Python 3.9+** (recommended 3.10–3.12)
- **pip** package manager
- Valid API keys:
   - Cloud services: OpenAI / DeepSeek, etc.
   - Local services: Ollama or other OpenAI-compatible interfaces

---

## 📥 Installation
1. **Download the project**  
    - Download the project ZIP from [GitHub](https://github.com) or clone the repository:
       ```bash
       git clone https://github.com/YILING0013/AI_NovelGenerator
       ```


2. **Install build tools (optional)**  
    - If some packages fail to install, visit [Visual Studio Build Tools](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/) to download and install C++ build tools required by some modules.
    - By default the installer includes MSBuild only; make sure to select **C++ Desktop Development** from the workload list.

3. **Install dependencies and run**  
    - Open a terminal and change to the project directory:
       ```bash
       cd AI_NovelGenerator
       ```
    - (Optional) Create and activate virtual environment:
       ```bash
       python -m venv .venv
       # if that doesn't work, try:
       # python3 -m venv .venv
       ```
       ```
       # On Windows:
       .venv/Scripts/activate
       ```
       ```
       # On Linux/Mac:
       source .venv/bin/activate
       ```
    - Install project dependencies:
       ```bash
       pip install -r requirements.txt
       ```
    - After installation run the main program:
       ```bash
       python main.py
       ```

If some dependencies are still missing, manually run:
```bash
pip install <package-name>
```
to install them.


## 🗂 Project Structure
```
novel-generator/
├── main.py                      # Entry file, runs the GUI
├── consistency_checker.py       # Consistency checks to prevent plot conflicts
|—— chapter_directory_parser.py  # Directory parsing
|—— embedding_adapters.py        # Embedding interface wrappers
|—— llm_adapters.py              # LLM interface wrappers
├── prompt_definitions.py        # AI prompt templates
├── utils.py                     # Utility functions and file operations
├── config_manager.py            # Configuration manager (API keys, base URL)
├── config.json                  # User configuration (optional)
├── novel_generator/             # Core chapter generation logic
├── ui/                          # Graphical user interface
└── vectorstore/                 # (Optional) Local vector DB storage
```

---

## ⚙️ Configuration Guide
### 📌 Basic configuration (`config.json`)
See `config.example.json` for a complete example. Current configs are grouped by model presets and task routing:
```json
{
   "last_llm_config_name": "DeepSeek V4 Flash",
   "llm_configs": {
      "DeepSeek V4 Flash": {
         "api_key": "",
         "base_url": "https://api.deepseek.com",
         "interface_format": "DeepSeek",
         "model_name": "deepseek-v4-flash",
         "temperature": 0.7,
         "max_tokens": 8192,
         "timeout": 600
      },
      "DeepSeek V4 Pro": {
         "api_key": "",
         "base_url": "https://api.deepseek.com",
         "interface_format": "DeepSeek",
         "model_name": "deepseek-v4-pro",
         "temperature": 0.7,
         "max_tokens": 32768,
         "timeout": 600
      },
      "Gemini 3.5 Flash": {
         "api_key": "",
         "base_url": "https://generativelanguage.googleapis.com/v1beta",
         "interface_format": "Gemini",
         "model_name": "gemini-3.5-flash",
         "temperature": 0.7,
         "max_tokens": 32768,
         "timeout": 600
      }
   },
   "embedding_configs": {
      "OpenAI": {
         "api_key": "",
         "base_url": "https://api.openai.com/v1",
         "interface_format": "OpenAI",
         "model_name": "text-embedding-3-small",
         "retrieval_k": 4
      }
   },
   "choose_configs": {
      "architecture_llm": "Gemini 3.5 Flash",
      "chapter_outline_llm": "Gemini 3.5 Flash",
      "prompt_draft_llm": "DeepSeek V4 Flash",
      "final_chapter_llm": "DeepSeek V4 Pro",
      "consistency_review_llm": "DeepSeek V4 Flash"
   }
}
```

### 🔧 Explanation
1. **Generation model configuration**
   - `api_key`: API key for the LLM service
   - `base_url`: API endpoint (for local services use the Ollama address)
   - `interface_format`: Interface mode
   - `model_name`: Main generation model (e.g., `deepseek-v4-flash`, `gemini-3.5-flash`, `gpt-5.5`)
   - `temperature`: Creativity parameter (0–1, higher is more creative)
   - `max_tokens`: Maximum model response length

2. **Embedding model configuration**
   - `embedding_model_name`: Embedding model name (e.g., `text-embedding-3-small`, `gemini-embedding-2`, or Ollama's `nomic-embed-text`)
   - `embedding_url`: Service endpoint
   - `embedding_retrieval_k`: Number of nearest neighbors to retrieve

3. **Novel parameters**
   - `topic`: Core story theme
   - `genre`: Genre
   - `num_chapters`: Total number of chapters
   - `word_number`: Target words per chapter
   - `filepath`: Path to save generated files

---

## 🚀 Run Instructions
### Method 1 — Run with Python
```bash
python main.py
```
This launches the GUI for interactive use.

### Method 2 — Build an executable
If you want to run the tool on machines without Python, package it with **PyInstaller**:
```bash
pip install pyinstaller
pyinstaller main.spec
```
After packaging an executable (e.g., `main.exe` on Windows) will appear in the `dist/` folder.

---

## 📘 User Guide
1. **After launching the app, fill in the basic parameters:**  
   - **API Key & Base URL** (e.g., `https://api.openai.com/v1`)  
   - **Model name** (e.g., `deepseek-v4-flash`, `gemini-3.5-flash`, `gpt-5.5`)
   - **Temperature** (0–1, controls creative variance)  
   - **Topic** (e.g., "AI uprising in a post-apocalyptic world")  
   - **Genre** (e.g., "Sci-fi" / "Fantasy" / "Urban Fantasy")  
   - **Number of chapters** and **words per chapter** (e.g., 10 chapters × ~3000 words)  
   - **Save path** (create a new output folder for results)

2. **Click "Step1. Generate Settings"**  
   - The system will generate, based on topic/genre/chapter count:  
     - `Novel_setting.txt`: Worldbuilding, characters, trigger points and foreshadowing.  
   - You can view or edit these settings after generation.

3. **Click "Step2. Generate Directory"**  
   - The system will use `Novel_setting.txt` to produce:  
     - `Novel_directory.txt`: Chapter titles and short prompts.  
   - You can review and modify chapter titles and descriptions.

4. **Click "Step3. Generate Chapter Draft"**  
   - Before generating a chapter you can:  
     - Set the chapter number (e.g., `1`)  
     - Provide chapter-specific guidance in the "This chapter guidance" box  
   - When you generate a chapter the system will:  
     - Read prior settings, `Novel_directory.txt`, and finalized chapters  
     - Use vector retrieval to recall relevant context for coherence  
     - Produce an outline (`outline_X.txt`) and chapter text (`chapter_X.txt`)  
   - You can view and edit the draft in the editor pane.

5. **Click "Step4. Finalize Current Chapter"**  
   - The system will:  
     - Update the global summary (`global_summary.txt`)  
     - Update character states (`character_state.txt`)  
     - Update the vector store (so future chapters can use the latest info)  
     - Update major plot points (e.g., `plot_arcs.txt`)  
   - After finalizing you will see the finalized text in `chapter_X.txt`.

6. **Consistency check (optional)**  
   - Click the "[Optional] Consistency Proofread" button to scan the latest chapter for conflicts (character logic, plot contradictions, etc.).  
   - If conflicts are detected, detailed messages will appear in the log area.

7. **Repeat steps 4–6** until all chapters are generated and finalized.

> Vector retrieval tips:
> 1. Explicitly set the embedding interface and model name.
> 2. For local Ollama embeddings start the Ollama service first:
>    ```bash
>    ollama serve  # Start the service
>    ollama pull nomic-embed-text  # Download/enable the model
>    ```
> 3. Clear the `vectorstore` directory after switching embedding models.
> 4. For cloud embeddings ensure the API permissions are enabled.

---

## ❓ FAQ
### Q1: Expecting value: line 1 column 1 (char 0)

This error usually indicates the API did not return valid JSON—sometimes an HTML error page or other unexpected content was returned.

### Q2: HTTP/1.1 504 Gateway Timeout?

Check the stability of the API endpoint and network connectivity.

### Q3: How do I switch Embedding providers?

Enter the new provider settings in the GUI fields for embedding configuration.

---

If you have further questions or feature requests, please open an issue on the project repository.

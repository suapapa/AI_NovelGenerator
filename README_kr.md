# 📖 자동 소설 생성 도구

[中文文档](./README_zh-CN.md) | [English](./README.md) | [日本語](./README_ja.md) | [Français](./README_fr-FR.md) | [Sawcuengh](./README_sawcuengh.md) | 한국어

> ~~현재 이 프로젝트를 유지할 여력이 많지 않습니다. 프로젝트 자체로는 수익이 없고, 졸업도 가까워 다른 할 일이 많습니다. 시간이 나면 더 새로운 기술로 리팩터링하는 것을 고려할 수 있습니다. — 2025/09/24~~
>
>- ~~**(2026/03/09):** 본 프로젝트는 곧 리팩터링을 시작하며, 더 현대적인 기술 구현과 새로운 창의적 개념을 도입할 예정입니다.~~
>
> **업데이트 (2026/03/25):** 리팩터링 버전의 초기 개발이 완료되었습니다(메인 프레임워크만 완성되었으며, 기능은 아직 사용할 수 없습니다). 1주일 이내에 dev 브랜치에 업로드되며, 이후 개발도 해당 브랜치에서 동기화됩니다.

<div align="center">
  
✨ **핵심 기능** ✨

| 모듈                | 주요 기능                                      |
|---------------------|------------------------------------------------|
| 🎨 소설 설정 워크숍   | 세계관 구축 / 캐릭터 설계 / 플롯 청사진          |
| 📖 지능형 챕터 생성   | 다단계 생성으로 플롯 일관성 보장                 |
| 🧠 상태 추적 시스템   | 캐릭터 성장 궤적 / 복선 관리                     |
| 🔍 시맨틱 검색 엔진   | 벡터 기반 장기 컨텍스트 일관성 유지              |
| 📚 지식 베이스 통합   | 로컬 문서 참조 지원                              |
| ✅ 자동 교정          | 플롯 모순 및 논리적 충돌 감지                    |
| 🖥 비주얼 워크벤치    | 설정 / 생성 / 교정을 아우르는 전 과정 GUI        |

</div>

> 대규모 언어 모델 기반의 다기능 소설 생성기입니다. 설정이 통일되고 논리가 치밀한 장편 스토리를 효율적으로 창작할 수 있도록 돕습니다.

---

## 📑 목차
1. [환경 준비](#-환경-준비)  
2. [프로젝트 구조](#-프로젝트-구조)  
3. [설정 가이드](#️-설정-가이드)  
4. [실행 방법](#-실행-방법)  
5. [사용 가이드](#-사용-가이드)  
6. [FAQ](#-faq)  

---

## 🛠 환경 준비
다음 요구 사항을 충족하는 환경을 준비하세요:
- **Python 3.9+** (권장: 3.10–3.12)
- **pip** 패키지 관리자
- 유효한 API 키:
   - 클라우드 서비스: OpenAI / DeepSeek 등
   - 로컬 서비스: Ollama 또는 OpenAI 호환 인터페이스

---

## 📥 설치
1. **프로젝트 다운로드**  
    - [GitHub](https://github.com)에서 ZIP 파일을 다운로드하거나 저장소를 클론합니다:
       ```bash
       git clone https://github.com/YILING0013/AI_NovelGenerator
       ```


2. **빌드 도구 설치 (선택)**  
    - 일부 패키지 설치에 실패하면 [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)에서 C++ 빌드 도구를 다운로드하여 설치하세요.
    - 기본 설치에는 MSBuild만 포함됩니다. 워크로드 목록에서 **C++를 사용한 데스크톱 개발**을 반드시 선택하세요.

3. **의존성 설치 및 실행**  
    - 터미널을 열고 프로젝트 디렉터리로 이동합니다:
       ```bash
       cd AI_NovelGenerator
       ```
    - (선택) 가상 환경 생성 및 활성화:
       ```bash
       python -m venv .venv
       # 동작하지 않으면 다음을 시도하세요:
       # python3 -m venv .venv
       ```
       ```
       # Windows:
       .venv/Scripts/activate
       ```
       ```
       # Linux/Mac:
       source .venv/bin/activate
       ```
    - 프로젝트 의존성 설치:
       ```bash
       pip install -r requirements.txt
       ```
    - 설치 후 메인 프로그램 실행:
       ```bash
       python main.py
       ```

의존성이 여전히 누락된 경우 수동으로 설치하세요:
```bash
pip install <패키지명>
```


## 🗂 프로젝트 구조
```
novel-generator/
├── main.py                      # 진입점, GUI 실행
├── consistency_checker.py       # 일관성 검사, 플롯 충돌 방지
|—— chapter_directory_parser.py  # 디렉터리 파싱
|—— embedding_adapters.py        # Embedding 인터페이스 래퍼
|—— llm_adapters.py              # LLM 인터페이스 래퍼
├── prompt_definitions.py        # AI 프롬프트 템플릿
├── utils.py                     # 유틸리티 함수 및 파일 작업
├── config_manager.py            # 설정 관리자 (API 키, Base URL)
├── config.json                  # 사용자 설정 (선택)
├── novel_generator/             # 챕터 생성 핵심 로직
├── ui/                          # 그래픽 사용자 인터페이스
└── vectorstore/                 # (선택) 로컬 벡터 DB 저장소
```

---

## ⚙️ 설정 가이드
### 📌 기본 설정 (`config.json`)
전체 예시는 `config.example.json`을 참고하세요. 현재 설정은 모델 프리셋과 작업 라우팅별로 구성됩니다:
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

### 🔧 항목 설명
1. **생성 모델 설정**
   - `api_key`: LLM 서비스 API 키
   - `base_url`: API 엔드포인트 (로컬 서비스는 Ollama 주소 사용)
   - `interface_format`: 인터페이스 형식
   - `model_name`: 메인 생성 모델 (예: `deepseek-v4-flash`, `gemini-3.5-flash`, `gpt-5.5`)
   - `temperature`: 창의성 파라미터 (0–1, 높을수록 창의적)
   - `max_tokens`: 모델 응답 최대 길이

2. **Embedding 모델 설정**
   - `embedding_model_name`: Embedding 모델 이름 (예: `text-embedding-3-small`, `gemini-embedding-2`, Ollama의 `nomic-embed-text`)
   - `embedding_url`: 서비스 엔드포인트
   - `embedding_retrieval_k`: 검색할 최근접 이웃 수

3. **소설 파라미터**
   - `topic`: 핵심 스토리 테마
   - `genre`: 장르
   - `num_chapters`: 전체 챕터 수
   - `word_number`: 챕터당 목표 단어 수
   - `filepath`: 생성 파일 저장 경로

---

## 🚀 실행 방법
### 방법 1 — Python으로 실행
```bash
python main.py
```
GUI가 실행되어 대화형으로 사용할 수 있습니다.

### 방법 2 — 실행 파일로 빌드
Python이 없는 환경에서 실행하려면 **PyInstaller**로 패키징하세요:
```bash
pip install pyinstaller
pyinstaller main.spec
```
패키징 후 `dist/` 폴더에 실행 파일(Windows의 경우 `main.exe` 등)이 생성됩니다.

---

## 📘 사용 가이드
1. **앱 실행 후 기본 파라미터를 입력합니다:**  
   - **API Key & Base URL** (예: `https://api.openai.com/v1`)  
   - **모델 이름** (예: `deepseek-v4-flash`, `gemini-3.5-flash`, `gpt-5.5`)
   - **Temperature** (0–1, 창의성 변동 제어)  
   - **주제** (예: "포스트 아포칼립스 세계의 AI 봉기")  
   - **장르** (예: "SF" / "판타지" / "도시 판타지")  
   - **챕터 수** 및 **챕터당 단어 수** (예: 10챕터 × 약 3000단어)  
   - **저장 경로** (결과물용 새 출력 폴더 생성 권장)

2. **"Step1. Generate Settings" 클릭**  
   - 주제/장르/챕터 수를 바탕으로 다음을 생성합니다:  
     - `Novel_setting.txt`: 세계관, 캐릭터, 트리거 포인트 및 복선.  
   - 생성 후 설정을 확인하거나 편집할 수 있습니다.

3. **"Step2. Generate Directory" 클릭**  
   - `Novel_setting.txt`를 사용하여 다음을 생성합니다:  
     - `Novel_directory.txt`: 챕터 제목과 짧은 프롬프트.  
   - 챕터 제목과 설명을 검토하고 수정할 수 있습니다.

4. **"Step3. Generate Chapter Draft" 클릭**  
   - 챕터 생성 전에 다음을 설정할 수 있습니다:  
     - 챕터 번호 (예: `1`)  
     - "This chapter guidance" 상자에 챕터별 안내 입력  
   - 챕터 생성 시 시스템은 다음을 수행합니다:  
     - 기존 설정, `Novel_directory.txt`, 확정된 챕터 읽기  
     - 일관성을 위해 벡터 검색으로 관련 컨텍스트 호출  
     - 아웃라인 (`outline_X.txt`) 및 챕터 본문 (`chapter_X.txt`) 생성  
   - 편집기 패널에서 초안을 확인하고 편집할 수 있습니다.

5. **"Step4. Finalize Current Chapter" 클릭**  
   - 시스템은 다음을 업데이트합니다:  
     - 전역 요약 (`global_summary.txt`)  
     - 캐릭터 상태 (`character_state.txt`)  
     - 벡터 스토어 (이후 챕터에서 최신 정보 활용)  
     - 주요 플롯 포인트 (예: `plot_arcs.txt`)  
   - 확정 후 `chapter_X.txt`에 확정본 텍스트가 저장됩니다.

6. **일관성 검사 (선택)**  
   - "[Optional] Consistency Proofread" 버튼을 클릭하면 최신 챕터를 스캔하여 충돌(캐릭터 논리, 플롯 모순 등)을 감지합니다.  
   - 충돌이 감지되면 로그 영역에 상세 메시지가 표시됩니다.

7. **4–6단계를 반복**하여 모든 챕터를 생성하고 확정합니다.

> 벡터 검색 팁:
> 1. Embedding 인터페이스와 모델 이름을 명시적으로 설정하세요.
> 2. 로컬 Ollama Embedding 사용 시 먼저 Ollama 서비스를 시작하세요:
>    ```bash
>    ollama serve  # 서비스 시작
>    ollama pull nomic-embed-text  # 모델 다운로드 / 활성화
>    ```
> 3. Embedding 모델을 전환한 후 `vectorstore` 디렉터리를 비우세요.
> 4. 클라우드 Embedding 사용 시 API 권한이 활성화되어 있는지 확인하세요.

---

## ❓ FAQ
### Q1: Expecting value: line 1 column 1 (char 0)

이 오류는 보통 API가 유효한 JSON을 반환하지 않았음을 나타냅니다. HTML 오류 페이지나 예상치 못한 내용이 반환되었을 수 있습니다.

### Q2: HTTP/1.1 504 Gateway Timeout?

API 엔드포인트의 안정성과 네트워크 연결을 확인하세요.

### Q3: Embedding 제공자를 어떻게 전환하나요?

GUI의 Embedding 설정 필드에 새 제공자 정보를 입력하세요.

---

추가 질문이나 기능 요청이 있으면 프로젝트 저장소에서 Issue를 열어 주세요.

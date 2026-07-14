# ui/i18n.py
# -*- coding: utf-8 -*-
"""UI string localization keyed by prompt language (zh / en / kr)."""

from __future__ import annotations

from typing import Any, Callable

_current_lang = "zh"

# flat key -> {zh, en, kr}
_STRINGS: dict[str, dict[str, str]] = {
    # ---- tabs (main) ----
    "tab.main": {
        "zh": "Main Functions",
        "en": "Main Functions",
        "kr": "주요 기능",
    },
    "tab.architecture": {
        "zh": "Novel Architecture",
        "en": "Novel Architecture",
        "kr": "소설 구조",
    },
    "tab.blueprint": {
        "zh": "Chapter Blueprint",
        "en": "Chapter Blueprint",
        "kr": "챕터 목차",
    },
    "tab.character": {
        "zh": "Character State",
        "en": "Character State",
        "kr": "캐릭터 상태",
    },
    "tab.summary": {
        "zh": "Global Summary",
        "en": "Global Summary",
        "kr": "전체 요약",
    },
    "tab.chapters": {
        "zh": "Chapters Manage",
        "en": "Chapters Manage",
        "kr": "챕터 관리",
    },
    "tab.other": {
        "zh": "Other Settings",
        "en": "Other Settings",
        "kr": "기타 설정",
    },
    # ---- config sub-tabs ----
    "config.tab.llm": {
        "zh": "LLM Model settings",
        "en": "LLM Model settings",
        "kr": "LLM 모델 설정",
    },
    "config.tab.embedding": {
        "zh": "Embedding settings",
        "en": "Embedding settings",
        "kr": "임베딩 설정",
    },
    "config.tab.choose": {
        "zh": "Config choose",
        "en": "Config choose",
        "kr": "모델 선택",
    },
    "config.tab.proxy": {
        "zh": "Proxy setting",
        "en": "Proxy setting",
        "kr": "프록시 설정",
    },
    # ---- common titles ----
    "title.param_help": {
        "zh": "参数说明",
        "en": "Parameter Help",
        "kr": "파라미터 설명",
    },
    "title.warning": {"zh": "警告", "en": "Warning", "kr": "경고"},
    "title.confirm": {"zh": "确认", "en": "Confirm", "kr": "확인"},
    "title.error": {"zh": "错误", "en": "Error", "kr": "오류"},
    "title.info": {"zh": "提示", "en": "Info", "kr": "알림"},
    "title.success": {"zh": "成功", "en": "Success", "kr": "성공"},
    "title.tip": {"zh": "提示", "en": "Tip", "kr": "안내"},
    # ---- main tab ----
    "main.chapter_label": {
        "zh": "本章内容（可编辑）  字数：{count}",
        "en": "Chapter content (editable)  Words: {count}",
        "kr": "이번 장 내용 (편집 가능)  글자수：{count}",
    },
    "main.log_label": {
        "zh": "输出日志 (只读)",
        "en": "Output log (read-only)",
        "kr": "출력 로그 (읽기 전용)",
    },
    "main.step1": {
        "zh": "Step1. 生成架构",
        "en": "Step1. Architecture",
        "kr": "Step1. 구조 생성",
    },
    "main.step2": {
        "zh": "Step2. 生成目录",
        "en": "Step2. Blueprint",
        "kr": "Step2. 목차 생성",
    },
    "main.step3": {
        "zh": "Step3. 生成草稿",
        "en": "Step3. Draft",
        "kr": "Step3. 초안 생성",
    },
    "main.step4": {
        "zh": "Step4. 定稿章节",
        "en": "Step4. Finalize",
        "kr": "Step4. 최종 확정",
    },
    "main.batch": {"zh": "批量生成", "en": "Batch Generate", "kr": "일괄 생성"},
    # ---- novel params ----
    "params.topic": {"zh": "主题(Topic):", "en": "Topic:", "kr": "주제(Topic):"},
    "params.genre": {"zh": "类型(Genre):", "en": "Genre:", "kr": "장르(Genre):"},
    "params.chapters_words": {
        "zh": "章节数 & 每章字数:",
        "en": "Chapters & words/ch:",
        "kr": "챕터 수 & 장당 글자수:",
    },
    "params.num_chapters": {"zh": "章节数:", "en": "Chapters:", "kr": "챕터 수:"},
    "params.word_number": {"zh": "每章字数:", "en": "Words/ch:", "kr": "장당 글자수:"},
    "params.filepath": {"zh": "保存路径:", "en": "Save path:", "kr": "저장 경로:"},
    "params.browse": {"zh": "浏览...", "en": "Browse...", "kr": "찾아보기..."},
    "params.chapter_num": {"zh": "章节号:", "en": "Chapter #:", "kr": "챕터 번호:"},
    "params.user_guidance": {"zh": "内容指导:", "en": "Guidance:", "kr": "내용 가이드:"},
    "params.characters": {"zh": "核心人物:", "en": "Characters:", "kr": "핵심 인물:"},
    "params.import": {"zh": "导入", "en": "Import", "kr": "가져오기"},
    "params.key_items": {"zh": "关键道具:", "en": "Key items:", "kr": "핵심 소품:"},
    "params.scene": {"zh": "空间坐标:", "en": "Scene:", "kr": "공간/장면:"},
    "params.time": {"zh": "时间压力:", "en": "Time pressure:", "kr": "시간 압박:"},
    "params.select": {"zh": "选择", "en": "Select", "kr": "선택"},
    "params.cancel": {"zh": "取消", "en": "Cancel", "kr": "취소"},
    # ---- optional buttons ----
    "opt.consistency": {"zh": "一致性审校", "en": "Consistency", "kr": "일관성 검토"},
    "opt.knowledge": {"zh": "导入知识库", "en": "Import Knowledge", "kr": "지식베이스 가져오기"},
    "opt.clear_vector": {"zh": "清空向量库", "en": "Clear Vectors", "kr": "벡터DB 비우기"},
    "opt.plot_arcs": {"zh": "查看剧情要点", "en": "Plot Points", "kr": "플롯 요점 보기"},
    "opt.role_library": {"zh": "角色库", "en": "Role Library", "kr": "역할 라이브러리"},
    # ---- shared editor tabs ----
    "editor.word_count": {
        "zh": "字数：{count}",
        "en": "Words: {count}",
        "kr": "글자수：{count}",
    },
    "editor.save": {"zh": "保存修改", "en": "Save Changes", "kr": "수정 저장"},
    "editor.load_architecture": {
        "zh": "加载 Novel_architecture.txt",
        "en": "Load Novel_architecture.txt",
        "kr": "Novel_architecture.txt 불러오기",
    },
    "editor.load_directory": {
        "zh": "加载 Novel_directory.txt",
        "en": "Load Novel_directory.txt",
        "kr": "Novel_directory.txt 불러오기",
    },
    "editor.load_character": {
        "zh": "加载 character_state.txt",
        "en": "Load character_state.txt",
        "kr": "character_state.txt 불러오기",
    },
    "editor.load_summary": {
        "zh": "加载 global_summary.txt",
        "en": "Load global_summary.txt",
        "kr": "global_summary.txt 불러오기",
    },
    "chapters.prev": {"zh": "<< 上一章", "en": "<< Prev", "kr": "<< 이전 장"},
    "chapters.next": {"zh": "下一章 >>", "en": "Next >>", "kr": "다음 장 >>"},
    "chapters.refresh": {
        "zh": "刷新章节列表",
        "en": "Refresh List",
        "kr": "챕터 목록 새로고침",
    },
    "chapters.no_selection": {
        "zh": "尚未选择章节，无法保存。",
        "en": "No chapter selected; cannot save.",
        "kr": "선택된 챕터가 없어 저장할 수 없습니다.",
    },
    "chapters.first": {
        "zh": "已经是第一章了。",
        "en": "Already at the first chapter.",
        "kr": "이미 첫 번째 챕터입니다.",
    },
    "chapters.last": {
        "zh": "已经是最后一章了。",
        "en": "Already at the last chapter.",
        "kr": "이미 마지막 챕터입니다.",
    },
    "msg.set_filepath_plain": {
        "zh": "请先配置保存文件路径",
        "en": "Please configure the save path first",
        "kr": "먼저 저장 경로를 설정하세요",
    },
    # ---- config labels ----
    "cfg.current": {"zh": "当前配置", "en": "Current config", "kr": "현재 구성"},
    "cfg.add": {"zh": "➕ 新增", "en": "➕ Add", "kr": "➕ 추가"},
    "cfg.rename": {"zh": "✏️ 重命名", "en": "✏️ Rename", "kr": "✏️ 이름 변경"},
    "cfg.delete": {"zh": "🗑️ 删除", "en": "🗑️ Delete", "kr": "🗑️ 삭제"},
    "cfg.save": {"zh": "💾 保存", "en": "💾 Save", "kr": "💾 저장"},
    "cfg.api_key": {"zh": "API Key:", "en": "API Key:", "kr": "API Key:"},
    "cfg.base_url": {"zh": "Base URL:", "en": "Base URL:", "kr": "Base URL:"},
    "cfg.interface_format": {"zh": "接口格式:", "en": "Interface:", "kr": "인터페이스:"},
    "cfg.model_name": {"zh": "模型名称:", "en": "Model name:", "kr": "모델 이름:"},
    "cfg.temperature": {"zh": "Temperature:", "en": "Temperature:", "kr": "Temperature:"},
    "cfg.max_tokens": {"zh": "Max Tokens:", "en": "Max Tokens:", "kr": "Max Tokens:"},
    "cfg.timeout": {"zh": "Timeout (sec):", "en": "Timeout (sec):", "kr": "Timeout (sec):"},
    "cfg.test": {"zh": "测试配置", "en": "Test Config", "kr": "구성 테스트"},
    "cfg.emb_api_key": {
        "zh": "Embedding API Key:",
        "en": "Embedding API Key:",
        "kr": "Embedding API Key:",
    },
    "cfg.emb_interface": {
        "zh": "Embedding 接口格式:",
        "en": "Embedding interface:",
        "kr": "임베딩 인터페이스:",
    },
    "cfg.emb_url": {
        "zh": "Embedding Base URL:",
        "en": "Embedding Base URL:",
        "kr": "Embedding Base URL:",
    },
    "cfg.emb_model": {
        "zh": "Embedding Model Name:",
        "en": "Embedding Model Name:",
        "kr": "임베딩 모델 이름:",
    },
    "cfg.emb_topk": {
        "zh": "Retrieval Top-K:",
        "en": "Retrieval Top-K:",
        "kr": "Retrieval Top-K:",
    },
    "cfg.arch_llm": {
        "zh": "生成架构所用大模型",
        "en": "Architecture LLM",
        "kr": "구조 생성 LLM",
    },
    "cfg.outline_llm": {
        "zh": "生成大目录所用大模型",
        "en": "Blueprint LLM",
        "kr": "목차 생성 LLM",
    },
    "cfg.draft_llm": {
        "zh": "生成草稿所用大模型",
        "en": "Draft LLM",
        "kr": "초안 생성 LLM",
    },
    "cfg.final_llm": {
        "zh": "定稿章节所用大模型",
        "en": "Finalize LLM",
        "kr": "최종화 LLM",
    },
    "cfg.review_llm": {
        "zh": "一致性审校所用大模型",
        "en": "Consistency LLM",
        "kr": "일관성 검토 LLM",
    },
    "cfg.save_choose": {"zh": "保存配置", "en": "Save Config", "kr": "구성 저장"},
    "cfg.refresh_choose": {"zh": "刷新配置", "en": "Refresh", "kr": "새로고침"},
    "cfg.proxy_enable": {"zh": "启用代理:", "en": "Enable proxy:", "kr": "프록시 사용:"},
    "cfg.proxy_address": {"zh": "地址:", "en": "Address:", "kr": "주소:"},
    "cfg.proxy_port": {"zh": "端口:", "en": "Port:", "kr": "포트:"},
    "cfg.proxy_save": {
        "zh": "保存代理设置",
        "en": "Save Proxy Settings",
        "kr": "프록시 설정 저장",
    },
    "cfg.new_name_prompt": {
        "zh": "请输入新配置名称:",
        "en": "Enter a new config name:",
        "kr": "새 구성 이름을 입력하세요:",
    },
    "cfg.new_name_title": {"zh": "新增配置", "en": "Add Config", "kr": "구성 추가"},
    "cfg.rename_prompt": {
        "zh": "请输入新的配置名称 (原名称: {old}):",
        "en": "Enter new config name (was: {old}):",
        "kr": "새 구성 이름을 입력하세요 (기존: {old}):",
    },
    "cfg.rename_title": {"zh": "重命名配置", "en": "Rename Config", "kr": "구성 이름 변경"},
    "cfg.confirm_delete_title": {
        "zh": "确认删除",
        "en": "Confirm Delete",
        "kr": "삭제 확인",
    },
    "cfg.confirm_delete": {
        "zh": "确定要删除配置 '{name}' 吗?\n此操作不可撤销!",
        "en": "Delete config '{name}'?\nThis cannot be undone!",
        "kr": "구성 '{name}'을(를) 삭제할까요?\n되돌릴 수 없습니다!",
    },
    # ---- other settings / webdav ----
    "webdav.title": {"zh": "webdav设置", "en": "WebDAV Settings", "kr": "WebDAV 설정"},
    "webdav.url": {"zh": "Webdav URL", "en": "WebDAV URL", "kr": "WebDAV URL"},
    "webdav.username": {
        "zh": "Webdav用户名",
        "en": "WebDAV Username",
        "kr": "WebDAV 사용자명",
    },
    "webdav.password": {
        "zh": "Webdav密码",
        "en": "WebDAV Password",
        "kr": "WebDAV 비밀번호",
    },
    "webdav.test": {"zh": "测试连接", "en": "Test Connection", "kr": "연결 테스트"},
    "webdav.backup": {"zh": "备份", "en": "Backup", "kr": "백업"},
    "webdav.restore": {"zh": "恢复", "en": "Restore", "kr": "복원"},
    "webdav.test_ok": {
        "zh": "WebDAV 连接成功！",
        "en": "WebDAV connected successfully!",
        "kr": "WebDAV 연결 성공!",
    },
    "webdav.backup_ok": {
        "zh": "配置备份成功！",
        "en": "Config backed up successfully!",
        "kr": "구성 백업 성공!",
    },
    "webdav.restore_ok": {
        "zh": "配置恢复成功！",
        "en": "Config restored successfully!",
        "kr": "구성 복원 성공!",
    },
    "webdav.unknown_error": {
        "zh": "发生未知错误: {error}",
        "en": "Unknown error: {error}",
        "kr": "알 수 없는 오류: {error}",
    },
    # ---- dialogs / messages ----
    "msg.set_filepath": {
        "zh": "请先设置保存路径",
        "en": "Please set a save path first",
        "kr": "먼저 저장 경로를 설정하세요",
    },
    "msg.set_filepath_full": {
        "zh": "请先选择保存文件路径",
        "en": "Please choose a save file path first",
        "kr": "먼저 저장 파일 경로를 선택하세요",
    },
    "msg.set_filepath_config": {
        "zh": "请先配置保存文件路径。",
        "en": "Please configure the save path first.",
        "kr": "먼저 저장 경로를 설정하세요.",
    },
    "msg.set_filepath_main": {
        "zh": "请先在主Tab中设置保存文件路径",
        "en": "Please set the save path in the Main tab first",
        "kr": "먼저 주요 기능 탭에서 저장 경로를 설정하세요",
    },
    "msg.confirm_architecture": {
        "zh": "确定要生成小说架构吗？",
        "en": "Generate novel architecture?",
        "kr": "소설 구조를 생성할까요?",
    },
    "msg.confirm_blueprint": {
        "zh": "确定要生成章节目录吗？",
        "en": "Generate chapter blueprint?",
        "kr": "챕터 목차를 생성할까요?",
    },
    "msg.confirm_finalize": {
        "zh": "确定要定稿当前章节吗？",
        "en": "Finalize the current chapter?",
        "kr": "현재 챕터를 최종 확정할까요?",
    },
    "msg.word_shortage_title": {
        "zh": "字数不足",
        "en": "Word count low",
        "kr": "글자수 부족",
    },
    "msg.word_shortage": {
        "zh": "当前章节字数 ({count}) 低于目标字数({target})的70%，是否要尝试扩写？",
        "en": "Current words ({count}) are below 70% of target ({target}). Expand?",
        "kr": "현재 글자수({count})가 목표({target})의 70% 미만입니다. 확장할까요?",
    },
    "msg.fill_complete": {
        "zh": "请填写完整信息。",
        "en": "Please fill in all fields.",
        "kr": "모든 항목을 입력하세요.",
    },
    "msg.clear_vector_1": {
        "zh": "确定要清空本地向量库吗？此操作不可恢复！",
        "en": "Clear the local vector store? This cannot be undone!",
        "kr": "로컬 벡터 DB를 비울까요? 되돌릴 수 없습니다!",
    },
    "msg.clear_vector_2_title": {
        "zh": "二次确认",
        "en": "Confirm again",
        "kr": "재확인",
    },
    "msg.clear_vector_2": {
        "zh": "你确定真的要删除所有向量数据吗？此操作不可恢复！",
        "en": "Really delete all vector data? This cannot be undone!",
        "kr": "정말 모든 벡터 데이터를 삭제할까요? 되돌릴 수 없습니다!",
    },
    "msg.plot_empty_title": {
        "zh": "剧情要点",
        "en": "Plot Points",
        "kr": "플롯 요점",
    },
    "msg.plot_empty": {
        "zh": "当前还未生成任何剧情要点或冲突记录。",
        "en": "No plot points or conflict records yet.",
        "kr": "아직 생성된 플롯 요점이나 갈등 기록이 없습니다.",
    },
    "msg.import_knowledge_title": {
        "zh": "选择要导入的知识库文件",
        "en": "Select knowledge file to import",
        "kr": "가져올 지식베이스 파일 선택",
    },
    "msg.thread_start_failed": {
        "zh": "线程启动失败: {error}",
        "en": "Failed to start thread: {error}",
        "kr": "스레드 시작 실패: {error}",
    },
    "msg.no_tooltip": {"zh": "暂无说明", "en": "No description", "kr": "설명 없음"},
    "msg.config_exists": {
        "zh": "配置名称 '{name}' 已存在!",
        "en": "Config name '{name}' already exists!",
        "kr": "구성 이름 '{name}'이(가) 이미 있습니다!",
    },
    "msg.config_created": {
        "zh": "已成功创建新配置: {name}",
        "en": "Created new config: {name}",
        "kr": "새 구성 생성됨: {name}",
    },
    "msg.config_create_fail": {
        "zh": "新增配置失败：无法保存配置文件",
        "en": "Failed to create config: cannot save file",
        "kr": "구성 추가 실패: 파일을 저장할 수 없음",
    },
    "msg.config_not_found": {
        "zh": "未找到选中的配置!",
        "en": "Selected config not found!",
        "kr": "선택한 구성을 찾을 수 없습니다!",
    },
    "msg.config_keep_one": {
        "zh": "至少需要保留一个配置!",
        "en": "Keep at least one config!",
        "kr": "구성은 최소 하나 필요합니다!",
    },
    "msg.config_deleted": {
        "zh": "已删除配置: {name}，并已更新配置文件",
        "en": "Deleted config: {name}, and updated the config file",
        "kr": "구성 삭제됨: {name}, 구성 파일 갱신됨",
    },
    "msg.config_delete_fail": {
        "zh": "删除配置失败：无法保存配置文件",
        "en": "Failed to delete config: cannot save file",
        "kr": "구성 삭제 실패: 파일을 저장할 수 없음",
    },
    "msg.config_missing": {
        "zh": "配置不存在!",
        "en": "Config does not exist!",
        "kr": "구성이 없습니다!",
    },
    "msg.config_saved_named": {
        "zh": "配置 {name} 已保存并持久化到文件",
        "en": "Config {name} saved to file",
        "kr": "구성 {name}이(가) 파일에 저장됨",
    },
    "msg.config_save_fail_detail": {
        "zh": "保存配置文件失败: {error}",
        "en": "Failed to save config file: {error}",
        "kr": "구성 파일 저장 실패: {error}",
    },
    "msg.config_renamed": {
        "zh": "配置已从 '{old}' 重命名为 '{new}'",
        "en": "Config renamed from '{old}' to '{new}'",
        "kr": "구성 이름이 '{old}'에서 '{new}'(으)로 변경됨",
    },
    "msg.config_rename_fail": {
        "zh": "重命名配置失败：无法保存配置文件",
        "en": "Failed to rename config: cannot save file",
        "kr": "구성 이름 변경 실패: 파일을 저장할 수 없음",
    },
    "msg.config_choose_missing": {
        "zh": "以下配置不存在，无法保存: {names}",
        "en": "These configs do not exist, cannot save: {names}",
        "kr": "다음 구성이 없어 저장할 수 없음: {names}",
    },
    "msg.config_choose_saved": {
        "zh": "配置已保存。",
        "en": "Config saved.",
        "kr": "구성이 저장되었습니다.",
    },
    "msg.config_choose_fail": {
        "zh": "保存配置失败。",
        "en": "Failed to save config.",
        "kr": "구성 저장에 실패했습니다.",
    },
    "msg.proxy_saved": {
        "zh": "代理配置已保存。",
        "en": "Proxy settings saved.",
        "kr": "프록시 설정이 저장되었습니다.",
    },
    "msg.config_loaded": {
        "zh": "已加载配置。",
        "en": "Config loaded.",
        "kr": "구성을 불러왔습니다.",
    },
    "msg.config_load_fail": {
        "zh": "未找到或无法读取配置文件。",
        "en": "Config file not found or unreadable.",
        "kr": "구성 파일을 찾거나 읽을 수 없습니다.",
    },
    "msg.config_saved_json": {
        "zh": "配置已保存至 config.json",
        "en": "Config saved to config.json",
        "kr": "구성이 config.json에 저장됨",
    },
    "msg.config_save_fail": {
        "zh": "保存配置失败。",
        "en": "Failed to save config.",
        "kr": "구성 저장에 실패했습니다.",
    },
    "msg.lang_unknown": {
        "zh": "未知的提示词语言: {label}",
        "en": "Unknown prompt language: {label}",
        "kr": "알 수 없는 프롬프트 언어: {label}",
    },
    "msg.lang_switched": {
        "zh": "界面/提示词语言切换: {label}",
        "en": "UI/prompt language switched: {label}",
        "kr": "UI/프롬프트 언어 전환: {label}",
    },
    "msg.lang_failed": {
        "zh": "语言切换失败: {error}",
        "en": "Language switch failed: {error}",
        "kr": "언어 전환 실패: {error}",
    },
    # ---- generation dialogs ----
    "gen.prompt_title": {
        "zh": "当前章节请求提示词（可编辑）",
        "en": "Chapter prompt (editable)",
        "kr": "현재 챕터 프롬프트 (편집 가능)",
    },
    "gen.confirm_use": {"zh": "确认使用", "en": "Use Prompt", "kr": "사용 확인"},
    "gen.cancel_request": {"zh": "取消请求", "en": "Cancel", "kr": "요청 취소"},
    "gen.batch_start": {"zh": "起始章节:", "en": "Start chapter:", "kr": "시작 챕터:"},
    "gen.batch_end": {"zh": "结束章节:", "en": "End chapter:", "kr": "종료 챕터:"},
    "gen.batch_expect": {"zh": "期望字数:", "en": "Target words:", "kr": "목표 글자수:"},
    "gen.batch_min": {"zh": "最低字数:", "en": "Min words:", "kr": "최소 글자수:"},
    "gen.batch_auto_enrich": {
        "zh": "低于最低字数时自动扩写",
        "en": "Auto-expand below min words",
        "kr": "최소 글자수 미만이면 자동 확장",
    },
    "gen.ok": {"zh": "确认", "en": "OK", "kr": "확인"},
    "gen.cancel": {"zh": "取消", "en": "Cancel", "kr": "취소"},
    "word_count_prefix": {"zh": "字数：", "en": "Words: ", "kr": "글자수："},
    # ---- tooltips ----
    "tip.api_key": {
        "zh": "在这里填写你的API Key。如果使用OpenAI官方接口，请在 https://platform.openai.com/account/api-keys 获取。",
        "en": "Enter your API key. For OpenAI official API, get one at https://platform.openai.com/account/api-keys.",
        "kr": "API Key를 입력하세요. OpenAI 공식 API는 https://platform.openai.com/account/api-keys 에서 발급받으세요.",
    },
    "tip.base_url": {
        "zh": "模型的接口地址。若使用OpenAI官方：https://api.openai.com/v1。若使用Ollama本地部署，则类似 http://localhost:11434/v1。调用Gemini模型则无需填写。",
        "en": "Model endpoint URL. OpenAI: https://api.openai.com/v1. Ollama: e.g. http://localhost:11434/v1. Not required for Gemini.",
        "kr": "모델 엔드포인트 URL. OpenAI: https://api.openai.com/v1. Ollama: 예) http://localhost:11434/v1. Gemini는 비워도 됩니다.",
    },
    "tip.interface_format": {
        "zh": "指定LLM接口兼容格式，可选DeepSeek、OpenAI、Ollama、ML Studio、Gemini等。\n\n注意：OpenAI 兼容是指的可以通过该标准请求的任何接口，不是只允许使用api.openai.com接口\n例如Ollama接口格式也兼容OpenAI，可以无需修改直接使用\nML Studio接口格式与OpenAI接口格式也一致。",
        "en": "LLM interface compatibility: DeepSeek, OpenAI, Ollama, ML Studio, Gemini, etc.\n\nNote: OpenAI-compatible means any API that follows that protocol, not only api.openai.com.\nOllama and ML Studio are also OpenAI-compatible.",
        "kr": "LLM 인터페이스 호환 형식: DeepSeek, OpenAI, Ollama, ML Studio, Gemini 등.\n\n참고: OpenAI 호환은 api.openai.com만이 아니라 해당 프로토콜을 따르는 모든 API를 의미합니다.\nOllama·ML Studio도 OpenAI 호환입니다.",
    },
    "tip.model_name": {
        "zh": "要使用的模型名称，例如deepseek-v4-flash、gemini-3.5-flash、gpt-5.5等。如果是Ollama等，请填写你下载好的本地模型名。",
        "en": "Model name, e.g. deepseek-v4-flash, gemini-3.5-flash, gpt-5.5. For Ollama, use your local model name.",
        "kr": "모델 이름(예: deepseek-v4-flash, gemini-3.5-flash, gpt-5.5). Ollama는 로컬 모델명을 입력하세요.",
    },
    "tip.temperature": {
        "zh": "生成文本的随机度。数值越大越具有发散性，越小越严谨。",
        "en": "Randomness of generation. Higher = more creative; lower = more focused.",
        "kr": "생성 텍스트의 무작위성. 클수록 창의적, 작을수록 엄격합니다.",
    },
    "tip.max_tokens": {
        "zh": "限制单次生成的最大Token数。范围1~100000，请根据模型上下文及需求填写合适值。\n以下是一些常见模型的最大值：\ngpt-5.5：128000\ngpt-5.4-mini：128000\ngemini-3.5-flash：32768\ndeepseek-v4-flash：8192\ndeepseek-v4-pro：32768\n",
        "en": "Max tokens per response (1–100000). Examples:\ngpt-5.5: 128000\ngpt-5.4-mini: 128000\ngemini-3.5-flash: 32768\ndeepseek-v4-flash: 8192\ndeepseek-v4-pro: 32768\n",
        "kr": "응답당 최대 토큰(1~100000). 예시:\ngpt-5.5: 128000\ngpt-5.4-mini: 128000\ngemini-3.5-flash: 32768\ndeepseek-v4-flash: 8192\ndeepseek-v4-pro: 32768\n",
    },
    "tip.embedding_api_key": {
        "zh": "调用Embedding模型时所需的API Key。",
        "en": "API key for the embedding model.",
        "kr": "임베딩 모델용 API Key.",
    },
    "tip.embedding_interface_format": {
        "zh": "Embedding模型接口风格，比如OpenAI或Ollama。",
        "en": "Embedding API style, e.g. OpenAI or Ollama.",
        "kr": "임베딩 API 스타일(예: OpenAI, Ollama).",
    },
    "tip.embedding_url": {
        "zh": "Embedding模型接口地址。",
        "en": "Embedding model endpoint URL.",
        "kr": "임베딩 모델 엔드포인트 URL.",
    },
    "tip.embedding_model_name": {
        "zh": "Embedding模型名称，如text-embedding-3-small、gemini-embedding-2。",
        "en": "Embedding model name, e.g. text-embedding-3-small, gemini-embedding-2.",
        "kr": "임베딩 모델 이름(예: text-embedding-3-small, gemini-embedding-2).",
    },
    "tip.embedding_retrieval_k": {
        "zh": "向量检索时返回的Top-K结果数量。",
        "en": "Top-K results returned by vector retrieval.",
        "kr": "벡터 검색 시 반환할 Top-K 개수.",
    },
    "tip.topic": {
        "zh": "小说的大致主题或主要故事背景描述。",
        "en": "Overall theme or story premise of the novel.",
        "kr": "소설의 대략적인 주제나 배경 설명.",
    },
    "tip.genre": {
        "zh": "小说的题材类型，如玄幻、都市、科幻等。",
        "en": "Genre, e.g. fantasy, urban, sci-fi.",
        "kr": "장르(예: 판타지, 도시, SF).",
    },
    "tip.num_chapters": {
        "zh": "小说期望的章节总数。",
        "en": "Expected total number of chapters.",
        "kr": "예상 총 챕터 수.",
    },
    "tip.word_number": {
        "zh": "每章的目标字数。",
        "en": "Target word count per chapter.",
        "kr": "장당 목표 글자수.",
    },
    "tip.filepath": {
        "zh": "生成文件存储的根目录路径。所有txt文件、向量库等放在该目录下。",
        "en": "Root folder for generated files, txts, and vector store.",
        "kr": "생성된 파일·txt·벡터 DB를 둘 루트 폴더.",
    },
    "tip.chapter_num": {
        "zh": "当前正在处理的章节号，用于生成草稿或定稿操作。",
        "en": "Chapter number currently being drafted or finalized.",
        "kr": "현재 초안/최종화 중인 챕터 번호.",
    },
    "tip.user_guidance": {
        "zh": "为本章提供的一些额外指令或写作引导。",
        "en": "Extra instructions or writing guidance for this chapter.",
        "kr": "이번 장에 대한 추가 지시나 글쓰기 가이드.",
    },
    "tip.characters_involved": {
        "zh": "本章需要重点描写或影响剧情的角色名单。",
        "en": "Key characters for this chapter.",
        "kr": "이번 장에서 중요하게 다룰 캐릭터 목록.",
    },
    "tip.key_items": {
        "zh": "在本章中出现的重要道具、线索或物品。",
        "en": "Important items, clues, or props in this chapter.",
        "kr": "이번 장에 등장하는 중요 소품·단서·아이템.",
    },
    "tip.scene_location": {
        "zh": "本章主要发生的地点或场景描述。",
        "en": "Main location or setting for this chapter.",
        "kr": "이번 장의 주요 장소나 장면.",
    },
    "tip.time_constraint": {
        "zh": "本章剧情中涉及的时间压力或时限设置。",
        "en": "Time pressure or deadline in this chapter's plot.",
        "kr": "이번 장 플롯의 시간 압박이나 기한.",
    },
    "tip.interface_config": {
        "zh": "选择你要使用的AI接口配置。",
        "en": "Select the AI interface config to use.",
        "kr": "사용할 AI 인터페이스 구성을 선택하세요.",
    },
    "tip.architecture_llm_config": {
        "zh": "生成小说架构时使用的大模型配置。",
        "en": "LLM config used for novel architecture.",
        "kr": "소설 구조 생성에 사용할 LLM 구성.",
    },
    "tip.chapter_outline_llm_config": {
        "zh": "生成章节目录时使用的大模型配置。",
        "en": "LLM config used for chapter blueprint.",
        "kr": "챕터 목차 생성에 사용할 LLM 구성.",
    },
    "tip.prompt_draft_llm_config": {
        "zh": "生成章节草稿时使用的大模型配置。",
        "en": "LLM config used for chapter drafts.",
        "kr": "챕터 초안 생성에 사용할 LLM 구성.",
    },
    "tip.final_chapter_llm_config": {
        "zh": "定稿章节时使用的大模型配置。",
        "en": "LLM config used for chapter finalization.",
        "kr": "챕터 최종화에 사용할 LLM 구성.",
    },
    "tip.consistency_review_llm_config": {
        "zh": "一致性审校时使用的大模型配置。",
        "en": "LLM config used for consistency review.",
        "kr": "일관성 검토에 사용할 LLM 구성.",
    },
    "tip.proxy_enabled": {
        "zh": "是否启用 HTTP/HTTPS 代理。",
        "en": "Enable HTTP/HTTPS proxy.",
        "kr": "HTTP/HTTPS 프록시 사용 여부.",
    },
    "tip.proxy_address": {
        "zh": "代理服务器地址。",
        "en": "Proxy server address.",
        "kr": "프록시 서버 주소.",
    },
    "tip.proxy_port": {
        "zh": "代理服务器端口。",
        "en": "Proxy server port.",
        "kr": "프록시 서버 포트.",
    },
    "tip.webdav_url": {
        "zh": "WebDAV 服务地址。",
        "en": "WebDAV server URL.",
        "kr": "WebDAV 서버 URL.",
    },
    "tip.webdav_username": {
        "zh": "WebDAV 用户名。",
        "en": "WebDAV username.",
        "kr": "WebDAV 사용자명.",
    },
    "tip.webdav_password": {
        "zh": "WebDAV 密码。",
        "en": "WebDAV password.",
        "kr": "WebDAV 비밀번호.",
    },
    "tip.timeout": {
        "zh": "单次请求超时时间（秒）。",
        "en": "Request timeout in seconds.",
        "kr": "요청 타임아웃(초).",
    },
}


def get_language() -> str:
    return _current_lang


def set_language(lang: str) -> str:
    global _current_lang
    if lang not in ("zh", "en", "kr"):
        raise ValueError(f"Unsupported UI language: {lang}")
    _current_lang = lang
    return lang


def t(key: str, **kwargs: Any) -> str:
    """Translate a UI string key for the active language."""
    entry = _STRINGS.get(key)
    if not entry:
        return key if not kwargs else key.format(**kwargs)
    text = entry.get(_current_lang) or entry.get("zh") or key
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text
    return text


def tip(tooltip_key: str) -> str:
    """Resolve a parameter tooltip (keys under tip.* or legacy bare names)."""
    if tooltip_key.startswith("tip."):
        return t(tooltip_key)
    keyed = f"tip.{tooltip_key}"
    if keyed in _STRINGS:
        return t(keyed)
    return t("msg.no_tooltip")


class I18nMixin:
    """Mixin for GUIs that refresh bound widgets when language changes."""

    def _ensure_i18n_state(self) -> None:
        if not hasattr(self, "_i18n_widgets"):
            self._i18n_widgets: list[tuple[Any, Callable[[], str]]] = []
        if not hasattr(self, "_i18n_tab_names"):
            # tabview -> {logical_id: current_display_name}
            self._i18n_tab_names: dict[Any, dict[str, str]] = {}

    def bind_i18n(self, widget: Any, key_or_fn: str | Callable[[], str]) -> Any:
        """Set widget text from i18n and re-apply on language refresh."""
        self._ensure_i18n_state()
        if isinstance(key_or_fn, str):
            getter: Callable[[], str] = lambda k=key_or_fn: t(k)
        else:
            getter = key_or_fn
        widget.configure(text=getter())
        self._i18n_widgets.append((widget, getter))
        return widget

    def track_tab(self, tabview: Any, logical_id: str, key: str) -> str:
        """Add a tab named with the current translation of key; track for rename."""
        self._ensure_i18n_state()
        name = t(key)
        frame = tabview.add(name)
        bucket = self._i18n_tab_names.setdefault(tabview, {})
        bucket[logical_id] = name
        # stash reverse map key for refresh
        if not hasattr(self, "_i18n_tab_keys"):
            self._i18n_tab_keys: dict[Any, dict[str, str]] = {}
        self._i18n_tab_keys.setdefault(tabview, {})[logical_id] = key
        return frame  # type: ignore[return-value]

    def refresh_ui_language(self) -> None:
        """Update all bound widgets and tracked tab titles."""
        self._ensure_i18n_state()
        for widget, getter in list(self._i18n_widgets):
            try:
                widget.configure(text=getter())
            except Exception:
                pass

        tab_keys = getattr(self, "_i18n_tab_keys", {})
        for tabview, id_to_key in tab_keys.items():
            names = self._i18n_tab_names.setdefault(tabview, {})
            for logical_id, key in id_to_key.items():
                old = names.get(logical_id)
                new = t(key)
                if not old or old == new:
                    names[logical_id] = new
                    continue
                try:
                    tabview.rename(old, new)
                    names[logical_id] = new
                except Exception:
                    names[logical_id] = new

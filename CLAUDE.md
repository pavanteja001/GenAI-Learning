# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Scripts

Activate the virtual environment first:
```bash
source langvenv/bin/activate
```

Each file is a standalone Python script. Run from the project root:
```bash
python langchain-basics/chains/simple_chain.py
```

Or run from within the subdirectory (required for scripts that use relative `load_dotenv("../.env")`):
```bash
cd langchain-basics/chains && python simple_chain.py
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

The `.env` file lives at the project root. Scripts load it in one of two ways:
- `load_dotenv("../.env")` — works when run from the subdirectory
- `load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))` — works regardless of CWD

Key variables: `OPENAI_API_KEY`, `EURI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`

## Architecture

This is a learning repository organized as standalone scripts grouped by LangChain concept, not a deployable application.

### `langchain-basics/` — organized by topic

| Directory | What it demonstrates |
|---|---|
| `models/` | ChatModels (OpenAI, HuggingFace), embedding models, LLMs |
| `prompts/` | PromptTemplate, ChatPromptTemplate, MessagePlaceholder, chatbot loop |
| `chains/` | LCEL pipe chains: simple, sequential, parallel, conditional |
| `runnables/` | RunnableSequence, RunnableParallel |
| `runnables2/` | RunnablePassthrough, RunnableLambda, RunnableBranch |
| `output-parsers/` | StrOutputParser, JsonOutputParser, PydanticOutputParser, StructuredOutputParser |
| `structured-output/` | `model.with_structured_output()` using TypedDict and Pydantic schemas |
| `tools/` | `@tool` decorator, BaseTool, ToolKit, `llm.bind_tools()` |
| `vector-store/` | Chroma and FAISS vector stores |
| `retrievers/` | Similarity, MMR, Multi-Query, Contextual Compression retrievers |
| `text-splitters/` | CharacterTextSplitter, RecursiveCharacterTextSplitter |
| `document-loaders/` | PyPDFLoader, TextLoader |

### `langgraph-basics/` — empty (planned)

## LLM Provider Pattern

Most scripts use the [Euron API](https://api.euron.one/api/v1/euri) as an OpenAI-compatible proxy:
```python
ChatOpenAI(
    model="gpt-4.1-nano",  # or "openai/gpt-oss-120b"
    base_url="https://api.euron.one/api/v1/euri",
    api_key=os.getenv("EURI_API_KEY"),
)
```

Standard OpenAI, Anthropic, Google Gemini, and HuggingFace integrations are also used directly.

## ChromaDB Persistence

Scripts in `vector-store/` write a `my_chroma_db/` directory relative to the CWD. Run these from within `langchain-basics/vector-store/` to keep the persisted store co-located with the script.

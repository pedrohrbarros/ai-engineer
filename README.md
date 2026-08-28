# AI Engineer

This is a standalone project built for an AI Engineer role, to be presented in a coding interview.

It exposes a small [FastAPI](https://fastapi.tiangolo.com/) service with a single `POST /query` endpoint.

---

## 1. How to install

### Requirements

- **Python 3.13** (pinned in [.python-version](.python-version))
- **[uv](https://docs.astral.sh/uv/)** — the package and environment manager used by this project

Install `uv` if you don't have it yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Set up the project

Clone the repository and move into it:

```bash
git clone <repository-url>
cd ai-engineer
```

Create the virtual environment and install all dependencies:

```bash
uv sync
```

This reads [pyproject.toml](pyproject.toml) and [uv.lock](uv.lock), creates a `.venv/` folder and installs the exact locked versions. Python 3.13 is downloaded automatically if it isn't available on your machine.

### Configure the environment variables

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

[.env.example](.env.example) is the tracked template listing every variable the project expects — it should never contain real secrets. Your `.env` holds the actual values and is git-ignored, so it stays on your machine only.

---

## 2. How to run

Start the development server:

```bash
uv run fastapi dev
```

No path is needed — the entrypoint is declared under `[tool.fastapi]` in [pyproject.toml](pyproject.toml). The server runs with auto-reload at `http://127.0.0.1:8000`.

| Resource | URL |
| --- | --- |
| API | http://127.0.0.1:8000 |
| Interactive docs (Swagger) | http://127.0.0.1:8000/docs |
| Alternative docs (ReDoc) | http://127.0.0.1:8000/redoc |

Call the endpoint:

```bash
curl -X POST http://127.0.0.1:8000/query
```

```json
{ "message": "AI Engineer interview" }
```

To run in production mode instead (no auto-reload):

```bash
uv run fastapi run
```

---

## 3. Authors

- **Pedro Barros** — [phbarros232@gmail.com](mailto:phbarros232@gmail.com)

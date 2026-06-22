<div align="center">
  <h1>⚖️ AI Supreme Court</h1>
  <p><b>An autonomous swarm of LLM agents that act as Prosecutors, Defense Attorneys, and Judges to debate legal cases in real-time.</b></p>
</div>

## 📖 The Story
I was tired of watching AI just output generic text. I wanted to see reasoning, debate, and conflict. So I built a multi-agent system where LLMs take on distinct legal personas. You upload a case, and they fight it out.

## 🚀 How it Works
1. **The Prosecutor:** Analyzes the evidence and ruthlessly constructs arguments to prove liability.
2. **The Defense:** Scrutinizes the prosecutor's logic and defends the client using circumstantial loopholes.
3. **The Judge:** Reviews the entire transcript and issues a final, binding verdict.

## 🛠️ Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Then hit `http://127.0.0.1:8000/docs` to start your first trial.

## 🧠 Architecture
- **FastAPI** for high-performance agent orchestration.
- **Pydantic** for strict legal schema validation.
- **Pytest** for ensuring the courtroom rules aren't broken.

## 🤝 Contributing
Is your agent a better lawyer? Open a PR.

---
*Built with ❤️ by Lakshan Muruganandam*

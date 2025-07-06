**🛠️ Developer Setup Guide – AI Meal Planner App**

Welcome to the AI Meal Planner – an intelligent meal planning assistant built using Python, Streamlit, and a locally running LLM via Ollama (LLaMA2). This guide will walk you through setting up the project on your local machine for development or experimentation.

---

**📁 Project Overview**

This app includes three core features:

* Personalized daily **meal planning** based on profile inputs (e.g., weight, goal, activity).
* Instant **recipe generation** from ingredients you have.
* **Meal history tracking** stored locally in a JSON file.

> Future enhancements include LangChain-based parsing, PDF export, and MongoDB integration for persistent storage.

---

**🧩 Prerequisites**

Before starting, make sure you have the following installed:

* **Python 3.9+**
* **pip** (Python package manager)
* **Git**
* **Ollama** – for running local language models
* Optional: Streamlit-compatible IDE like **VS Code** or **PyCharm**

---

**✅ Setup Instructions**

**1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

**2. Set Up a Virtual Environment**

To keep dependencies clean and isolated:

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install Required Python Packages**

All dependencies are listed in `requirements.txt`. Just run:

```bash
pip install -r requirements.txt
```

This includes:

* streamlit
* requests
* pydantic (if you begin LangChain integration later)
* and any other dependencies used in the app

**4. Install & Run Ollama (for LLM Access)**

This app uses Ollama to access LLaMA2 locally.

**Step 1: Install Ollama**
Go to [https://ollama.com](https://ollama.com) and follow installation instructions for your OS.

**Step 2: Start Ollama**
Make sure it's running locally (port 11434 by default).

**Step 3: Pull the LLaMA2 model**

```bash
ollama pull llama2
```

🔁 You can change to a different model later if needed by editing the model name in `ollama_client.py`.

**5. Run the Application**

Once everything is installed and Ollama is running:

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser and start planning meals with AI! 🚀

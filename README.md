# 🧪 JudgeEval Agent Demo

This is a simple demo project that evaluates a basic Python agent using [Judgment Labs' JudgeEval](https://github.com/JudgmentLabs/judgeval) evaluation framework.

## 📋 Overview

This project:
- Implements a **simple rule-based agent**
- Defines test cases with expected answers
- Uses **JudgeEval** to evaluate the agent's correctness
- Sends results to the **Judgment Labs** dashboard

## 🧠 Agent Logic

```python
def simple_agent(input_text):
    if "capital of France" in input_text:
        return "Paris"
    elif "sun" in input_text:
        return "The Sun is a star."
    else:
        return "I don't know."
```

## 🧪 Evaluation Script

The main script is `test_my_agent.py`, which:
- Defines test cases
- Submits them to JudgeEval
- Outputs a link to view the evaluation results

## 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/TarunVirat/judgeval-agent-demo.git
cd judgeval-agent-demo

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Evaluation

```bash
python test_my_agent.py
```

You’ll receive a link to view your evaluation results on [Judgment Labs](https://app.judgmentlabs.ai/).

## 📦 Dependencies

- Python 3.8+
- judgeval

Install JudgeEval:
```bash
pip install judgeval
```

## ✨ License

This demo is open-source and available for educational and evaluation purposes.

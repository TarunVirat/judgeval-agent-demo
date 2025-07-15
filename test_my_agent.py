from judgeval.data import Example
from judgeval.scorers import APIScorerConfig
from judgeval.evaluation_run import EvaluationRun
from judgeval.run_evaluation import run_eval

# ✅ Real API credentials
api_key = "6a5d35c1-41ae-4d80-b184-768bcde48323"
org_id = "8f564ca1-a682-402e-8c60-a754de345baf"

# ✅ Define a very simple fake "agent"
def simple_agent(input_text):
    if "capital of France" in input_text:
        return "Paris"
    elif "sun" in input_text:
        return "The Sun is a star."
    else:
        return "I don't know."

# ✅ Define test inputs and expected outputs
inputs = [
    ("What is the capital of France?", "Paris"),
    ("What is the Sun?", "The Sun is a star."),
    ("What's 2 + 2?", "4"),  # This one the agent will fail
]

examples = [
    Example(
        input=question,
        actual_output=simple_agent(question),
        expected_output=answer
    )
    for question, answer in inputs
]

# ✅ Choose the built-in scorer
scorers = [
    APIScorerConfig(
        name="Answer Correctness",
        score_type="Answer Correctness",
        strict_mode=True
    )
]

# ✅ Define and run the evaluation
run = EvaluationRun(
    eval_name="my-python-agent-eval",
    project_name="demo-project",
    judgment_api_key=api_key,
    organization_id=org_id,
    examples=examples,
    scorers=scorers,
    model="gpt-3.5-turbo"

)

# ✅ Submit to Judgment Labs
results = run_eval(run, override=True)


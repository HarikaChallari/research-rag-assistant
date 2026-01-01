from app.retriever import Retriever
from app.generator import (
    literature_review,
    comparison,
    evidence_qa,
    advisor_notes
)

# Evaluation questions
questions = [
    "What is this project about?",
    "What documents are used in this system?",
    "How does retrieval augmented generation work?",
]

modes = {
    "literature_review": literature_review,
    "comparison": comparison,
    "evidence_qa": evidence_qa,
    "advisor_notes": advisor_notes,
}


def run_evaluation():
    retriever = Retriever()

    for question in questions:
        print("\n====================================")
        print("QUESTION:", question)

        docs = retriever.get_relevant_docs(question)
        if not docs:
            print("❌ No documents retrieved")
            continue

        for mode_name, mode_fn in modes.items():
            print(f"\n--- MODE: {mode_name.upper()} ---")
            output = mode_fn(question, docs)
            print(output[:800])  # limit output length


if __name__ == "__main__":
    run_evaluation()


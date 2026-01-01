from app.retriever import Retriever
from app.vector_store import create_vector_store
from app.generator import (
    literature_review,
    comparison,
    evidence_qa,
    advisor_notes
)

create_vector_store()
print("✅ Vector store ready")

retriever = Retriever()

query = input("\nEnter your research query: ").strip()

docs = retriever.get_relevant_docs(query)
if not docs:
    print("❌ No relevant documents found")
    exit()

print("\nSelect Research Mode")
print("1 - Literature Review")
print("2 - Comparison")
print("3 - Evidence-based Q&A")
print("4 - Advisor Notes")

mode = input("Enter mode number: ").strip()

modes = {
    "1": literature_review,
    "2": comparison,
    "3": evidence_qa,
    "4": advisor_notes
}

if mode not in modes:
    print("❌ Invalid mode")
    exit()

output = modes[mode](query, docs)

print("\n====== GENERATED RESEARCH OUTPUT ======\n")
print(output)

print("\n====== SOURCES ======")
for i, doc in enumerate(docs):
    print(f"\n--- Source {i+1} ---")
    print(doc[:300])


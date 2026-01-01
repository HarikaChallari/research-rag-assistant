def literature_review(query, chunks):
    """
    Generates a simple literature-style summary from retrieved chunks
    """
    summary = f"Literature review for query: '{query}'\n\n"
    summary += "Key findings from the documents:\n"

    for i, chunk in enumerate(chunks):
        summary += f"\n{i+1}. {chunk[:300]}"

    return summary


def comparison(query, chunks):
    """
    Compares information across retrieved chunks
    """
    output = f"Comparison based on documents for query: '{query}'\n\n"

    for i, chunk in enumerate(chunks):
        output += f"\n--- Document {i+1} ---\n"
        output += chunk[:300]

    return output


def evidence_qa(query, chunks):
    """
    Answers a question using the most relevant evidence
    """
    answer = f"Answer to question: '{query}'\n\n"
    answer += "Based on the most relevant document:\n\n"
    answer += chunks[0][:500]

    return answer


def advisor_notes(query, chunks):
    """
    Generates advisor-style notes or guidance
    """
    notes = f"Advisor Notes for: '{query}'\n\n"
    notes += "Important points to consider:\n"

    for i, chunk in enumerate(chunks[:3]):
        notes += f"\n- {chunk[:250]}"

    return notes


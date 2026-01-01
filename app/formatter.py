def format_with_citations(evidence):
    citations = []
    for i, item in enumerate(evidence):
        citations.append(
            f"[{i+1}] {item['paper']} — Chunk {item['chunk_id']}"
        )
    return citations

import csv
import os


def write_csv(results: list[dict], output_path: str) -> None:
# Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
# Define fixed column schema for report normalization
    fieldnames = [
        "url",
        "title",
        "score",
        "direct_answer",
        "definition",
        "headings",
        "facts",
        "sources",
        "faq",
        "lists",
        "tables",
        "word_count_ok",
        "meta_ok",
        "recommendations",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

import json
import os

from analyzer import ArticleAnalyzer
from reporter import write_csv


def load_articles(json_path: str) -> list[dict]:
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
# Define input/output paths
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data", "articles.json")
    out_path = os.path.join(base_dir, "output", "report.csv")

    articles = load_articles(data_path)

# Run analysis for each article
    result = []
    for article in articles:
        analyzer = ArticleAnalyzer(article)
        result.append(analyzer.analyze())
# Export results to CSV
    write_csv(result, out_path)


if __name__ == "__main__":
    main()

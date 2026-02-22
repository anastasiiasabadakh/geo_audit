import re
from bs4 import BeautifulSoup

#Phrases indicating weak introductory framing (first criterion)
introduction_phrase = [
    "dozviete sa",
    "poďme sa pozrieť",
    "sa pozrieme",
    "v tomto článku",
    "povieme si"
]

# Regex pattern for detecting facts with units (forth criterion)
unit_patern = r"\d+\s?(mg|g|kg|%|kcal|ml|mcg|gramov|miligramov)"
# Keywords indicating presence of source references (fifth criterion)
source_keywords = [
    "zdroje",
    "references",
    "štúdie",
]
# FAQ section indicators (sixth criterion)
f_q = [
    "faq",
    "často kladené otázky",
    "otázky a odpovede",
]

class ArticleAnalyzer:
    def __init__(self, article: dict):
        self.article = article
        self.url = article.get("url", "")
        self.title = article.get("title", "")
        self.html = article.get("content", "") or ""
        self.meta_description = article.get("meta_description", "") or ""
        self.soup = BeautifulSoup(self.html, "html.parser") # Parse HTML and extract text content
        self.text = self.soup.get_text(" ", strip=True)
        self.text_lover = self.text.lower()

#Evaluation Criteria
    def check_direct_answer(self) -> int: #first criterion check
        intro = self.text_lover[:150]
        return 0 if any(p in intro for p in introduction_phrase) else 1

    def check_definition(self) -> int:  # second criterion check
        patern = r"\b\w+\s(-\sto|je|znamena|predstavuje)\b"
        return 1 if re.search(patern, self.text_lover) else 0

    def check_h2_headings(self) -> int: # third criterion check
        return 1 if len(self.soup.find_all("h2")) >=3 else 0

    def check_facts(self) -> int: # fourth criterion check
        facts_ = re.findall(unit_patern, self.text_lover)
        return 1 if len(facts_) >= 3 else 0

    def check_sources(self) -> int: #fifth criterion check
        html_lower = self.html.lower()
        if "pubmed.ncbi.nih.gov" in html_lower or "examine.com" in html_lower:
            return 1
        return 1 if any(k in self.text_lover for k in source_keywords) else 0

    def check_faq(self) -> int: # sixth criterion check
        return 1 if any(k in self.text_lover for k in f_q) else 0

    def check_lists(self) -> int: #seventh criterion check
        return 1 if (self.soup.find("ul") is not None or self.soup.find("ol") is not None) else 0

    def check_tables(self) -> int:#eightth criterion check
        return 1 if self.soup.find("table") is not None else 0

    def check_word_count_ok(self) -> int: #nineth criterion check
        word_count_ok = len(self.text.split())
        return 1 if word_count_ok >= 500 else 0

    def check_meta_ok(self) -> int: #tenth criterion check
        meta_ok = self.meta_description.strip()
        return 1 if 120 <= len(meta_ok) <= 160 else 0

    # final aggregation
    def analyze(self) -> dict:
        direct_answer = self.check_direct_answer()
        definition = self.check_definition()
        headings = self.check_h2_headings()
        facts = self.check_facts()
        sources = self.check_sources()
        faq = self.check_faq()
        lists = self.check_lists()
        tables = self.check_tables()
        word_count_ok = self.check_word_count_ok()
        meta_ok = self.check_meta_ok()

# Aggregate score across all criteria
        score = sum([
                     direct_answer, definition, headings, facts, sources,
                     faq, lists, tables, word_count_ok, meta_ok
                    ])
# Generate structured improvement recommendations
        recommendations = []
        if not direct_answer:
            recommendations.append(
                "Prepracovať prvý odsek tak, aby už v prvej vete obsahoval jasné tvrdenie o produkte (napr. konkrétny "
                "účinok alebo vedecký fakt) namiesto všeobecného úvodu"
            )
        if not definition:
            recommendations.append(
                "Doplniť článok o presnú definíciu hlavného pojmu vo forme jednej jasnej vety "
            )
        if not headings:
            recommendations.append(
                "Článok rozdeľte minimálne na tri tematicky ucelené časti"
            )
        if not facts:
            recommendations.append(
                "Doplniť článok o minimálne tri konkrétne číselné údaje s jednotkami (napr. 1000 IU denne, 25 mcg, "
                "30–50 ng/ml, 40 % populácie)"
            )
        if not sources:
            recommendations.append(
                "Vytvoriť samostatnú sekciu „Zdroje“ na konci článku a doplniť minimálne jeden odkaz na vedeckú "
                "štúdiu alebo odborný portál"
            )
        if not faq:
            recommendations.append(
                "Pridať sekciu „FAQ“ s minimálne tromi otázkami a stručnými odpoveďami (napr. „Kedy užívať?“, "
                "„Je bezpečný?“, „Aká je maximálna dávka?“)"
            )
        if not lists:
            recommendations.append(
                "Doplniť aspoň jeden odrážkový alebo číslovaný zoznam pre prehľadné zhrnutie účinkov alebo benefitov"
            )
        if not tables:
            recommendations.append(
                "Vytvoriť tabuľku s prehľadom odporúčaného dávkovania podľa cieľovej skupiny (napr. dospelí, "
                "športovci, osoby s deficitom)"
            )
        if not word_count_ok:
            recommendations.append(
                "Rozšírte text pridaním podrobnejších informácií tak, aby celkový rozsah presiahol 500 slov (napr. "
                "tematické sekcie „Príznaky deficitu“, „Rizikové skupiny“)"
            )
        if not meta_ok:
            recommendations.append(
                "Doplniť meta description na 120–160 znakov a zabezpečiť, aby obsahovala hlavné kľúčové slovo a "
                "hlavný benefit článku"
            )

        return {
            "url": self.url,
            "title": self.title,
            "score": score,
            "direct_answer": direct_answer,
            "definition": definition,
            "headings": headings,
            "facts": facts,
            "sources": sources,
            "faq": faq,
            "lists": lists,
            "tables": tables,
            "word_count_ok": word_count_ok,
            "meta_ok": meta_ok,
            "recommendations": "; ".join(recommendations),
        }

# GEO Audit Tool
*(Blog - Case Study Project)*

## Prehľad

Nástroj GEO Audit Tool je nástroj na analýzu obsahu založený na jazyku Python, ktorý je určený na hodnotenie blogových článkov podľa princípov generatívnej optimalizácie pre vyhľadávače (GEO).

Nástroj automaticky hodnotí článok podľa 10 preddefinovaných kritérií GEO a generuje štruktúrovanú tabuľku vo formáte CSV, ktorá obsahuje kvantitatívne výsledky aj praktické odporúčania na zlepšenie.

Tento projekt bol vyvinutý ako súčasť case study zameranej na hodnotenie kvality obsahu a optimalizáciu AI vygenerovaných výsledkov.

## Hlavné body

- Automatizované hodnotenie blogových článkov na základe 10 kritérií GEO (Generative Engine Optimization)
- Štruktúrovaný systém hodnotenia (0–10 bodov) s transparentnou logikou
- Detekcia kľúčových prvkov obsahu, ako sú priame odpovede v úvode, definície, štruktúrované nadpisy, sekcie s často kladenými otázkami, tabuľky a vedecké referencie
- Detekcia faktov založená na regulárnych výrazoch (čísla + jednotky ako IU, mcg, ng/ml, %)
- Overenie počtu slov a meta popisov
- Automaticky generovaný report CSV s praktickými odporúčaniami
- Modulárna štruktúra projektu (data\articles, output\report, analyzer, reporter, main ) pre jednoduchú škálovateľnosť

## Použitie

### Požiadavky
- Python 3.10 alebo vyšší

### Inštalácia závislostí

Z koreňového adresára projektu spustite:

```bash
python -m pip install beautifulsoup4
```

### Príprava vstupných dát
Uistite sa, že súbor: 

`data\articles.json`

obsahije články vo formáte JSON so štrúkturou:

- `url`
- `title`
- `content`
- `meta_description`

### Spustenie nástroja

Spustite nástroj na audit GEO:

```bash
 python main.py
 ```

### Výstup

Po úspešnom spustení sa automaticky vytvori súbor:

`output/report.csv`

Systém:

- Načíta články zo súboru data/articles.json

- Analyzuje ich podľa 10 kritérií GEO

- Vygeneruje štruktúrovanú správu CSV

#### Generovanie HTML reportu
Pre vizuálnu prehľadnú správu spustite:

```bash
python generate_report.py
```
Po spustení sa vytvorí súbor:

`output/report.html`

HTML report obsahuje:

- Farebné skóre (zelená / oranžová / červená)

- Vizualizáciu splnenia jednotlivých kritérií

- Odporúčania pre zlepšenie obsahu

### Output štruktura
Vygenerovaný súbor obsahuje nasledujúce stĺpce:

- `url` – URL adresa článku

- `title` – Názov článku

- `score` – Celkové skóre GEO (0–10)

- `direct_answer` – Prítomnosť priamej odpovede v úvode (0/1)

- `definition` – Prítomnosť jasnej definície (0/1)

- `headings` – Aspoň tri H2 nadpisy (0/1)

- `facts` – Aspoň tri číselné fakty s jednotkami (0/1)

- `sources` – Vedecké referencie alebo sekcia so zdrojmi (0/1)

- `faq` – Prítomnosť sekcie s často kladenými otázkami (0/1)

- `lists` – Prítomnosť štruktúrovaných zoznamov (0/1)

- `tables` – Prítomnosť aspoň jednej tabuľky (0/1)

- `word_count_ok` – Splnená požiadavka na minimálne 500 slov (0/1)

- `meta_ok` – Dĺžka meta popisu (120–160 znakov) (0/1)

- `recommendations` – Konkrétne návrhy na zlepšenie pre nesplnené kritériá




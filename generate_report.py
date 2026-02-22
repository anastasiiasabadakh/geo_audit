import pandas as pd
import os

#Load analysis data
df = pd.read_csv("output/report.csv", encoding="utf-8-sig")

os.makedirs("output", exist_ok=True)
#Initialize HTML template
html_content = """ <!doctype html>
<html lang="sk">
<html>
<head>
      <meta charset="UTF-8">
      <title>GEO Report</title>
      <style>
          body { font-family: Arial; margin: 40px; background-color: #f4f6f8; }
          h1 { color: #2c3e50;}
          table {border-collapse: collapse; width:100%; background: white; }
          th, td { padding: 10px; border:1px solid #ddd; text-align: left; }
          th { background-color: #2c3e50; color: white;}
          .ok {color: green; font-weight: bold; }
          .score{ font-size: 20px; font-weight: bold;} 
          .score-high { background-color: #d4edda; font-weight: bold; }
          .score-mid { background-color: #ffe5b4; font-weight: bold; }
          .score-low { background-color:  #f8d7da; font-weight: bold; }
          .bad { color: #c0392b; font-weight: bold; }
      </style>
</head>
<body>

<h1> GEO Analýza článkov</h1>

<table>
<tr>
    <th>url</th>
    <th>title</th> 
    <th>score</th>
    <th>direct_answer</th>
    <th>definition</th> 
    <th>headings</th> 
    <th>facts</th> 
    <th>sources</th>
    <th>faq</th>   
    <th>lists</th> 
    <th>tables</th> 
    <th>word_count_ok</th> 
    <th>meta_ok</th> 
    <th>recommendations</th> 
</tr> 
"""
# Render table rows
for _, row in df.iterrows():
    score = int(row["score"]) # Determine score tier class

    if score >= 8:
        score_class = "score-high"
    elif score >= 5:
        score_class = "score-mid"
    else:
        score_class = "score-low"
    word_class = "ok" if row["word_count_ok"] == 1 else "bad"
    meta_class = "ok" if row["meta_ok"] == 1 else "bad"
    direct_class = "ok" if row["direct_answer"] == 1 else "bad"
    definition_class = "ok" if row["definition"] == 1 else "bad"
    headings_class = "ok" if row["headings"] == 1 else "bad"
    sources_class = "ok" if row["sources"] == 1 else "bad"
    facts_class = "ok" if row["facts"] == 1 else "bad"
    faq_class = "ok" if row["faq"] == 1 else "bad"
    lists_class = "ok" if row["lists"] == 1 else "bad"
    tables_class = "ok" if row["tables"] == 1 else "bad"

# Append formatted row to HTML content
    html_content += f"""
    <tr>
        <td>{row['url']}</td>
        <td>{row['title']}</td>
        <td class="score {score_class}">{score}/10</td>        <td class="{direct_class}">{row['direct_answer']}</td>
        <td class="{word_class}">{row['word_count_ok']}</td>
        <td class="{meta_class}">{row['meta_ok']}</td>
        <td class="{definition_class}">{row['definition']}</td>
        <td class="{headings_class}">{row['headings']}</td>
        <td class="{sources_class}">{row['sources']}</td>
        <td class="{faq_class}">{row['faq']}</td>
        <td class="{facts_class}">{row['facts']}</td>
        <td class="{lists_class}">{row['lists']}</td>
        <td class="{tables_class}">{row['tables']}</td>
        <td>{row['recommendations']}</td>
    </tr> 
"""
# Finalize document
html_content += """
</table>
</body>
</html>
"""
# Write report file
with open("output/report.html", "w", encoding="utf-8", newline="\n") as f:
    f.write(html_content)
print("HTML report bol úspešne vygenerovaný.")
print(html_content[:500])

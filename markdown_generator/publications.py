
import pandas as pd
import os

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in str(text))

for row, item in publications.iterrows():
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug

    md = "---\n"
    md += f'title: "{html_escape(item.title)}"\n'
    md += "collection: publications\n"
    md += f"permalink: /publication/{html_filename}\n"

    if len(str(item.excerpt)) > 5:
        md += f"excerpt: '{html_escape(item.excerpt)}'\n"

    md += f"date: {str(item.pub_date)}\n"
    md += f"venue: '{html_escape(item.venue)}'\n"

    if len(str(item.paper_url)) > 5:
        md += f"paperurl: '{item.paper_url}'\n"

    # Optional image in front matter if your theme uses it
    if "image_url" in publications.columns and len(str(item.image_url)) > 5:
        md += f"image: '{item.image_url}'\n"

    md += "---\n"

    # Add image near the publication text
    if "image_url" in publications.columns and len(str(item.image_url)) > 5:
        md += (
            f"\n<img src='{item.image_url}' "
            f"alt='{html_escape(item.title)}' "
            f"style='width:40%; height:auto; float:right; margin:0 0 1rem 1rem;'>\n"
        )

    if len(str(item.paper_url)) > 5:
        md += f"\n<a href='{item.paper_url}'>Download paper here</a>\n"

    if len(str(item.excerpt)) > 5:
        md += f"\n{html_escape(item.excerpt)}\n"

    md += f"\n<small>Recommended citation: {html_escape(item.citation)}</small>\n"

    with open(os.path.join("../_publications", os.path.basename(md_filename)), "w", encoding="utf-8") as f:
        f.write(md)

import os
from docx import Document
from markdownify import markdownify as md

def docx_to_markdown(docx_path, md_path):
    doc = Document(docx_path)
    html_content = ""

    for para in doc.paragraphs:
        html_content += f"<p>{para.text}</p>\n"

    markdown_content = md(html_content)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

def convert_all_docx():
    for file in os.listdir("."):
        if file.lower().endswith(".docx"):
            md_file = os.path.splitext(file)[0] + ".md"
            print(f"Converting: {file} → {md_file}")
            docx_to_markdown(file, md_file)

if __name__ == "__main__":
    convert_all_docx()

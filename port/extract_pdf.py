import pypdf

def extract_text(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    content = extract_text("tulika.pdf")
    with open("content.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Content written to content.txt")

import fitz  # PyMuPDF
import json
import re


doc = fitz.open("json pdf.pdf")
text = ""

# Extract text from all pages
for page in doc:
    text += page.get_text()


enrollment_number = re.search(r"Enrolement\nNumber\n(\d+)", text)
name = re.search(r"Name\n([A-Za-z\s]+)", text)
program = re.search(r"Programme\n([A-Za-z\s:()]+)", text)
session = re.search(r"Session\n([A-Za-z0-9\-]+)", text)
reference_number = re.search(r"Reference\nNumber :\n(\d+)", text)


data = {
    "enrollment_number": enrollment_number.group(1) if enrollment_number else None,
    "name": name.group(1) if name else None,
    "program": program.group(1) if program else None,
    "session": session.group(1) if session else None,
    "reference_number": reference_number.group(1) if reference_number else None
}

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)

print("Selected PDF details saved into student.json")

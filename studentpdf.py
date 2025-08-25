# import fitz 
# import json
# doc =fitz.open("json pdf.pdf")
# text = ""
# for page in doc:
#     text += page.get_text()
# data = {"put_text": text}
# with open("student.json","w") as f:
#     json.dump(data,f,indent=4)
#     print("pdf text saved into student.json")    
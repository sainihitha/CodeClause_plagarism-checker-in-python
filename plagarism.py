from difflib import SequenceMatcher
with open ("file1.txt") as file1, open("file2.txt") as file2:
  filldata=file1.read() 
  filldata2=file2.read()
  similarity = SequenceMatcher(None, filldata, filldata2).ratio()
  print(similarity*109)

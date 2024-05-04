import re

#findAll
text = "The quick brown fox brown brown brown"
pattern = r"brown"

matchs = re.finditer(pattern, text)
for match in matchs:
    print(match)
    print(match.group())

#search  
text = "The quick brown fox brown brown brown"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print(search)
    print("Pattern found:", search.group())
else:
    print("Pattern not found")   
 
#match
text = "The quick brown fox quick"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")  

#replacement
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#spilt
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

text="A park is an area of Natural Watural Katural , semi-natural or planted"
pattern=r"[A-Z|a-z]atural"

match = re.search(pattern, text)
if match:
    print(match)
    print("Match found:", match.group())
else:
    print("No match")  

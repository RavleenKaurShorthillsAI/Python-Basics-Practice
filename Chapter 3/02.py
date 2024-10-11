letter = '''Dear <|Name|>,
You are Selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Ravleen").replace("<|Date|>","7 October 2024"))
#This is chaining the replace function
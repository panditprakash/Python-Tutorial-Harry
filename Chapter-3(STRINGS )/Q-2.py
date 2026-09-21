# 2. Write a program to fill in a letter template given below with name and date. 
"""letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''"""

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","prakash").replace("<|Date|","6 August have a nice day"))
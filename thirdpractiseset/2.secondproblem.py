letter = '''
           Dear <|Name|>,
           You are selected!
           <|Date|>
           '''
print(letter.replace("<|Name|>","NISU").replace("<|Date|","24 december,2025"))
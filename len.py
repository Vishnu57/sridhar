test = "That's all @folks!!!"
print test
test = test.replace('@', '')
test = test.replace('!','')
test = test.replace('""','')
test = test.replace("'",'')
print test
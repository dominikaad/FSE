text = 'Yanka Kupala State University of Grodno'
abreviatura = ''
words = text.split(' ')
for word in words:
    if len(word)>3:
        abreviatura+=word[0]
print(abreviatura)
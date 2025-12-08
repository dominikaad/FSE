import re
text = 'He jests at scars. That never felt a wound! Hello, friend!    Are you OK?'
sentences = re.split(r'(?<=[.?!]) ', text)
for sentence in sentences:
    print(sentence.strip())
print(f'Предложений в тексте: {len(sentences)}')
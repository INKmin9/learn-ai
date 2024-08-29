with open('vocabulary.txt', 'a', encoding='UTf-8') as f:
    while True:
        english = str(input('영어 단어를 입력하세요: '))
        if english == 'q':
            break
        korean = str(input('한국어 뜻을 입력하세요: '))
        if korean == 'q':
            break
        f.write(english + ': ' + korean + '\n')
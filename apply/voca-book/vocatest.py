with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word = data[0]
        korean_translation = data[1]
        answer = input(f'{korean_translation}: ')
        if answer.strip() == english_word:
            print('맞았습니다!')
        else:
            print(f'아쉽습니다. 정답은 {english_word}입니다.')

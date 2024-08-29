import random

# vocabulary.txt 파일에서 단어를 읽어와 사전(dictionary)으로 변환
vocab_dict = {}
with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        english_word, korean_translation = line.strip().split(": ")
        vocab_dict[korean_translation] = english_word

# 퀴즈 프로그램 실행
while True:
    # 단어를 랜덤하게 선택
    korean_translation = random.choice(list(vocab_dict.keys()))
    english_word = vocab_dict[korean_translation]

    # 사용자에게 질문
    answer = input(f'{korean_translation}: ')

    # 사용자가 q를 입력하면 프로그램 종료
    if answer.strip().lower() == 'q':
        print('프로그램을 종료합니다.')
        break

    # 정답 확인
    if answer.strip() == english_word:
        print('맞았습니다!')
    else:
        print(f'아쉽습니다. 정답은 {english_word}입니다.')

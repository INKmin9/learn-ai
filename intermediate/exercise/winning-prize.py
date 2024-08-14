# 연 복리로 하는것과 아파트의 가격 중 2016년에 어떤게 금액이 더 클지 계산하여 차이를 출력한다

in_year = 1988
out_year = 2016
seed_money = 50000000
apartment_money = 1100000000

while in_year < out_year:
    seed_money *= 1.12
    in_year += 1

if seed_money > apartment_money:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(seed_money - apartment_money)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(apartment_money - seed_money)))

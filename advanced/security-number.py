def mask_security_number(security_number):
    security_number = list(security_number)
    for i in range(-1, -5, -1):
        security_number[i] = '*'
    return ''.join(security_number)

# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

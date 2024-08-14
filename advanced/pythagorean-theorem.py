for a in range (400):
  for b in range(a, 400):
    if a * a + b * b == (400-a-b)**2 and a < b < (400-a-b):
         print(a * b * (400-a-b))
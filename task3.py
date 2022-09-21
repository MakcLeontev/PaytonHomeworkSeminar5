# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import itertools

def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same) # number of repetitions
        yield char if count == 1 else str(count)+char

with open('1.txt', 'r') as file:
    arr = [i for i in file.read()]
  
with open('2.txt', 'w') as file:
    file.write('' .join(compress(arr)))


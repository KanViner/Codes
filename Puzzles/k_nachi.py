"""
В нашем зоопарке появился заяц. Его поместили в клетку,
и чтобы ему не было скучно, директор зоопарка распорядился
поставить в его клетке лесенку. Теперь наш зайчик может
прыгать по лесенке вверх, перепрыгивая через ступеньки.
Лестница имеет определенное количество ступенек N.
Заяц может одним прыжком преодолеть не более К ступенек.
Для разнообразия зайчик пытается каждый раз найти новый
путь к вершине лестницы. Директору любопытно, сколько
различных способов есть у зайца добраться до вершины
лестницы при заданных значениях K и N. Помогите директору
написать программу, которая поможет вычислить это количество.
Например, если K=3 и N=4, то существуют следующие маршруты:
1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1. Т.е. при данных
значениях у зайца всего 7 различных маршрутов добраться
до вершины лестницы.
"""
import sys


def count(N, K):
    seq = (K-1) * [0] + [1, 1]
    cur = 0
    for i in range(0, N-1):
        if cur == K:
            seq[cur] = (seq[cur-1]<<1) - seq[cur]
            cur = 0
        elif cur == 0:
            seq[cur] = (seq[-1]<<1) - seq[cur]
            cur += 1
        else:
            seq[cur] = (seq[cur-1]<<1) - seq[cur]
            cur += 1
    return seq[cur-1 if cur != 0 else -1]


N = int(sys.argv[1])
K = int(sys.argv[2])
cnt = count(N, K)
print(cnt)

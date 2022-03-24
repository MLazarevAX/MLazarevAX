import time

A= [1,2,3,4,5,6,7,8,9,10,12]
key= 7

def Upper_Bound(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] >= key:
            right = middle
        else:
            left = middle
    return right

Upper_Bound(A, key)

def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
s = 'hlelo'*50
'hahhellllloou'
'hahhemllllloou'
def search_word_in_str(s: str):
    s = [i for i in s]
    find_obj = ['h', 'e', 'l', 'l', 'o']
    finish = []
    index = 0
    if len(s) <5:
        return print("NO")
    elif len(s) == 5:
        if find_obj == s:
            return print("YES")
        else:
            return print("NO")

    for i in s:
        if len(finish) == 5:
            break
        if i in find_obj:
            if find_obj[index] == i and i not in finish :
                index += 1
                finish.append(i)
                continue
            elif i in finish and finish.count('l') < 2 and i !='l':
                continue
            elif i =='l' and finish.count('l') < 2:
                finish.append(i)
                index += 1
            elif i == 'l' and finish.count('l') >= 2:
                continue
            else:
                index = 0
        else:
            finish = []
            index = 0
    if find_obj == finish:
        return print("YES")
    else:
        return print("NO")
start = time.time()
search_word_in_str(s)
end = time.time()
print((end-start))
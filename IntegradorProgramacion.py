import random, time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L): arr[k], i, k = L[i], i+1, k+1
        while j < len(R): arr[k], j, k = R[j], j+1, k+1

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    if algoritmo.__name__ == 'quick_sort':
        algoritmo(lista)
    else:
        algoritmo(lista)
    return time.time() - inicio

lista = [random.randint(1, 10000) for _ in range(1000)]
for alg in [bubble_sort, merge_sort, quick_sort]:
    lista_copia = lista.copy()
    t = medir_tiempo(alg, lista_copia)
    print(f"{alg.__name__} tardó {t:.6f} segundos.")

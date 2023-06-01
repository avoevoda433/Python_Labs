import random
import time
import matplotlib.pyplot as plt
from bubble import bubble_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort
from selection import selection_sort

N = [100, 1000, 3000, 5000, 7000, 10000] # количество элементов в массиве для сортировки
test_count = 10 # количество тестов на каждую функцию сортировки
sort_functions = [
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort
]


def sort_test(sort_function, Nnum, test_c):
    time_value = []
    for _ in range(test_c):
        arr = list(random.randint(0, 1000) for _ in range(Nnum))
        start = time.time()
        sort_function(arr)
        end = time.time()
        time_value.append(end-start)

    average = sum(time_value) / len(time_value)
    print(f'{sort_function.__name__} {Nnum} items completed in {format(float(average), ".5f") } second!')
    return average


print(f'Start sort!\n')
time_data = [[sort_test(f, n, test_count) for n in N] for f in sort_functions]
print(f'\nFinish sort!\n\n')

file_data = open('sort_data_3_10.txt', 'w')
for i in range(len(sort_functions)):
    file_data.write(f'{time_data[i]}\n')
file_data.close()
print(f'Text file ready!\n\n')

colors = [
    'red',
    'green',
    'blue',
    'yellow',
    'black',
    'purple'
]

plt.axis([0, 10000, 0, 0.1])

for i in range(len(sort_functions)):
    plt.plot(N, time_data[i], color=colors[i], label=f'{sort_functions[i].__name__}')

plt.legend()
plt.xlabel('Количество элементов массиваа')
plt.ylabel('Время сортировки')
plt.title('Все сортировки на версии 3.10')

plt.savefig(f'Сортировки_0.1s_3.10.png')
plt.clf()
print(f'Image 1 ready!\n\n')

plt.axis([0, 10000, 0, 1])

for i in range(len(sort_functions)):
    plt.plot(N, time_data[i], color=colors[i], label=f'{sort_functions[i].__name__}')

plt.legend()
plt.xlabel('Количество элементов массиваа')
plt.ylabel('Время сортировки')
plt.title('Все сортировки на версии 3.10')

plt.savefig(f'Сортировки_1s_3.10.png')
plt.clf()
print(f'Image 2 ready!\n\n')


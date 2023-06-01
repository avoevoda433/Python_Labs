import matplotlib.pyplot as plt

N = [100, 1000, 3000, 5000, 7000, 10000] # количество элементов в массиве для сортировки
test_count = 10 # количество тестов на каждую функцию сортировки
sort_functions = [
    'bubble_sort',
    'heap_sort',
    'insertion_sort',
    'merge_sort',
    'quick_sort',
    'selection_sort'
]

file_data_310 = open('sort_data_3_10.txt', 'r')
file_data_311 = open('sort_data_3_11.txt', 'r')

sort_data_310 = []
sort_data_311 = []

i = 0
for line in file_data_310:
    line_list = line[1:-2].split(',')
    sort_data_310.append([float(item) for item in line_list])
    i = i+1

i = 0
for line in file_data_311:
    line_list = line[1:-2].split(',')
    sort_data_311.append([float(item) for item in line_list])
    i = i+1


file_data_310.close()
file_data_311.close()

for i in range(len(sort_functions)):
    plt.axis([0, 10000, 0, 0.01])
    plt.plot(N, sort_data_310[i], color='blue', label=f'3.10')
    plt.plot(N, sort_data_311[i], color='red', label=f'3.11')
    plt.legend()
    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время сортировки, секунд')
    plt.title(f'Сортировка {sort_functions[i]} на двух версиях')
    plt.savefig(f'Сортировка_{sort_functions[i]}_0.01s.png')
    plt.clf()

for i in range(len(sort_functions)):
    plt.axis([0, 10000, 0, 0.1])
    plt.plot(N, sort_data_310[i], color='blue', label=f'3.10')
    plt.plot(N, sort_data_311[i], color='red', label=f'3.11')
    plt.legend()
    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время сортировки, секунд')
    plt.title(f'Сортировка {sort_functions[i]} на двух версиях')
    plt.savefig(f'Сортировка_{sort_functions[i]}_0.1s.png')
    plt.clf()

for i in range(len(sort_functions)):
    plt.axis([0, 10000, 0, 1])
    plt.plot(N, sort_data_310[i], color='blue', label=f'3.10')
    plt.plot(N, sort_data_311[i], color='red', label=f'3.11')
    plt.legend()
    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время сортировки, секунд')
    plt.title(f'Сортировка {sort_functions[i]} на двух версиях')
    plt.savefig(f'Сортировка_{sort_functions[i]}_1s.png')
    plt.clf()

for i in range(len(sort_functions)):
    plt.axis([0, 10000, 0, 5])
    plt.plot(N, sort_data_310[i], color='blue', label=f'3.10')
    plt.plot(N, sort_data_311[i], color='red', label=f'3.11')
    plt.legend()
    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время сортировки, секунд')
    plt.title(f'Сортировка {sort_functions[i]} на двух версиях')
    plt.savefig(f'Сортировка_{sort_functions[i]}_5s.png')
    plt.clf()

print(''.center(15), '|', '100'.center(11), '|', '1000'.center(11), '|', '3000'.center(11), '|', '5000'.center(11), '|', '7000'.center(11), '|', '10000'.center(11), '|', 'Average'.center(11), '|')
print('-'.ljust(112, '-'))

comm_diff = []
for sort_data_10, sort_data_11, sort_function in zip(sort_data_310, sort_data_311, sort_functions):
    diff = [(format(float(data_10-data_11), ".5f")) for data_10, data_11 in zip(sort_data_10, sort_data_11)]
    print(sort_function.center(15), '|', diff[0].center(11), '|', diff[1].center(11), '|', diff[2].center(11), '|', diff[3].center(11), '|', diff[4].center(11), '|', diff[5].center(11), '|', '-'.center(11), '|')
    diff = ['0.0%' if (data_10 == 0.0) else (format(float((data_10-data_11) / data_10 * 100), ".3f")) for data_10, data_11 in zip(sort_data_10, sort_data_11)]
    print(sort_function.center(15), '|', (diff[0]+'%').center(11), '|', (diff[1]+'%').center(11), '|', (diff[2]+'%').center(11), '|', (diff[3]+'%').center(11), '|', (diff[4]+'%').center(11), '|', (diff[5]+'%').center(11), '|', (str(format(float(sum(list(map(float, diff))) / len(diff)), ".3f"))+'%').center(11), '|')
    print()
    comm_diff.append(diff)

diff = [str(format(float(sum([float(comm_diff[i][j]) for i in range(len(comm_diff))]) / len(comm_diff)), ".3f"))+'%' for j in range(len(comm_diff[0]))]
print('Average'.center(15), '|', diff[0].center(11), '|', diff[1].center(11), '|', diff[2].center(11), '|', diff[3].center(11), '|', diff[4].center(11), '|', diff[5].center(11), '|', diff[5].center(11), '|')
print(f'\n\n')

print(f'Total average: {str(format(float(sum(list(map(float, [comm_diff[i][j] for j in range(len(comm_diff[0])) for i in range(len(comm_diff))])))) / (len(comm_diff)*len(comm_diff[0])), ".3f"))+"%"}')
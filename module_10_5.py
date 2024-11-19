import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data = file.readlines()  # Читаем все строки сразу
    return all_data

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_linear = time.time()
    for filename in filenames:
        read_info(filename)  # Линейное чтение
    end_linear = time.time()
    print(f'Линейное чтение = {end_linear - start_linear:.6f} секунд')

    # Многопроцессный вызов
    start_multiprocessing = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(read_info, filenames)
    end_multiprocessing = time.time()
    print(f'Многопроцессное чтение = {end_multiprocessing - start_multiprocessing:.6f} секунд')







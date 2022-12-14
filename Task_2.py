# Задание 2: Дан список, вывести отдельно буквы и цифры, пользуясь filter.

lst = [12,'sadf',5643, 'sgsgs']

def separate_by_elements(lst):
    result = []
    result.append(list(filter(lambda i: str(i).isalpha(), lst)))
    result.append(list(filter(lambda i: str(i).isdigit(), lst)))
    return result

print(f'Отсортированный массив: {separate_by_elements(lst)}')
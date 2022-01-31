"""Почтальон выходит из почтового отделения, объезжает всех адресатов один раз для вручения посылки и возвращается в
почтовое отделение.
Необходимо найти кратчайший маршрут для почтальона.
"""


def route(point_1, point_2):
    """
    нахождение расстояния между двумя точками на плоскости
    :param point_1: первая точка
    :param point_2: вторая точка
    :return: расстояние между двумя точками, float
    """
    result = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    return result


def get_key(dict_, value):
    """
    вывод ключа по значению в словаре
    :param dict_: имя словаря
    :param value: значение в словаре
    :return: ключ соответствующий данному значению
    """
    for k, v in dict_.items():
        if v == value:
            return k


# координаты данных точек
point_A = (0, 2)
point_B = (2, 5)
point_C = (5, 2)
point_D = (6, 6)
point_E = (8, 3)

list_of_points = [point_A, point_B, point_C, point_D, point_E]  # список точек
route_length = []  # длина маршрута между двумя точками
route_list = []  # кратчайший маршрут почтальона

while True:
    routes = []  # маршруты
    dict_routes = {}  # словарь из пар {начальный номер точки: длина маршрута до неё}
    # цикл для определения длины маршрута между начальной точкой и остальными
    for i in range(1, len(list_of_points)):
        route_i = route(list_of_points[0], list_of_points[i])
        # заношу в словарь_маршрутов {номер маршрута: длину маршрута}
        dict_routes[i] = route_i
        # добавляю длину маршрута в список длин маршрутов
        routes.append(route_i)
    # выбираю минимальное значение в списке длин маршрутов
    min_route = min(routes)
    # добавляю самый короткий маршрут к списку маршрутов
    route_length.append(min_route)
    # добавяю координаты точки с наименьшим расстоянием в конечный список точек маршрута
    route_list.append(list_of_points[0])
    # заменяю начальные координаты точки на координаты точки самого короткого маршрута
    list_of_points[0] = list_of_points[get_key(dict_routes, min_route)]
    # удаляю точку с координатами самого короткого маршрута из списка всех точек
    index_to_pop = get_key(dict_routes, min_route)
    list_of_points.pop(index_to_pop)
    # прописываю условия для работы и выхода из цикла While
    if len(list_of_points) > 1:
        continue
    else:
        # добавяю координаты последней посещаемой точки в конечный список точек маршрута
        route_list.append(list_of_points[0])
        break
# добавляю в список маршрута начальную точку, тк почтальон должен вернуться
list_of_points.append(point_A)
route_list.append(point_A)
# в список длин всех самых коротких маршрутов добавляю путь "домой"
route_length.append(route(list_of_points[0], list_of_points[1]))
# добавляю первую точку в список на вывод
print_list = [route_list[0]]
# составляю список точек и длин маршрута на вывод
for i in range(len(route_list) - 1):
    n = (route_list[i + 1], route_length[i])
    print_list.append(n)
# вывод результата работы программы в терминал
print(' -> '.join('{}'.format(item) for item in print_list) + f' = {sum(route_length)}')

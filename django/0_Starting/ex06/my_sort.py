def my_sort():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    """ for name, year in d.items():
        print(f"{name} nació en {year}") """
    

    ordenado_por_valor = dict(sorted(d.items(), key=lambda item: int(item[1])))
    print(ordenado_por_valor)

    # swapped_dict = {value: key for key, value in d.items()}
    # print(swapped_dict)

    # my_dict2 = {y: x for x, y in d.items()}
    # print(my_dict2)
   


if __name__ ==  "__main__":
    my_sort()
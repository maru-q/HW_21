from classes import Request, Shop, Store


def store_add(c_store):
    c_store.add("котики", 8)
    c_store.add("мячики", 12)
    c_store.add("варежки", 6)
    c_store.add("очки", 13)
    c_store.add("букеты", 16)
    c_store.add("машинки", 5)
    c_store.add("чашки", 8)
    print(f"На складе в наличии: {c_store.get_items()}")


if __name__ == "__main__":
    shop = Shop()
    store = Store()
    store_add(store)

    while True:
        user_request = input("Введите строчку такого типа: 'Доставить 3 собачки из склад в магазин\n"
                             "Чтобы завершить работу с программой введи 'завершить':\n")
        if user_request != "завершить":
            data_request = Request(user_request)

            if shop.get_unique_items_count() < shop.item_limit and data_request.ammount <= shop.get_free_space():
                if store.remove(data_request.product, data_request.ammount):
                    shop.add(data_request.product, data_request.ammount)
                    print(f"Курьер доставил {data_request.ammount} {data_request.product} в магазин")
            else:
                if shop.get_unique_items_count() >= shop.item_limit:
                    print(f"Количество видов товаров в магазине максимально {shop.item_limit},"
                          f"товары не могут быть добавлены")
                if data_request.ammount > shop.get_free_space():
                    print(f"Количество товаров в магазине превышено, максимальное - {shop.capacity},"
                          f"товары не могут быть добавлены")
            print(f"На складе в наличии: {store.get_items()}")
            print(f"В магазине в наличии: {shop.get_items()}")
        else:
            break

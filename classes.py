from abc import abstractmethod


class Storage:
    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def get_free_space(self):
        count = 0
        for item in self.items.values():
            count += item

        return self.capacity - count

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

    def add(self, title, count):
        if self.get_free_space() < count:
            print(f"Тoвар {title} в количестве {count} единиц добавить не удалось, недостаточно места на складе."
                  f"Осталось мест - {self.get_free_space()}")

        else:
            if title not in self.items.keys():
                self.items[title] = count
            else:
                self.items[title] = self.items[title] + count
            print("Товары добавлены")

    def remove(self, title, count):
        if title not in self.items.keys():
            print("Указанные товары на складе отсутствуют")
            return False
        elif count > self.items[title]:
            print(f"Вы указали количество больше, чем есть в наличии - {self.items[title]}")
            return False
        else:
            self.items[title] = self.items[title] - count
            if self.items[title] == 0:
                del self.items[title]
            print("Нужное количество есть на складе")
            print(f"Курьер забрал  {count} {title} со склад")
            print(f"Курьер везет {count} {title}  со склад в магазин")
            return True


class Shop(Store):
    def __init__(self):
        self._items = {}
        self._capacity = 20
        self._item_limit = 5

    @property
    def item_limit(self):
        return self._item_limit


class Request:
    def __init__(self, str_input):
        data = str_input.split(" ")

        self.from_ = data[4]
        self.to = data[6]
        self.ammount = int(data[1])
        self.product = data[2]






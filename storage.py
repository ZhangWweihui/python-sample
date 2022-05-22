from types import MethodType


class Storage:

    def __init__(self):
        self.__data = None

    @staticmethod
    def set_num(_num: int):
        Storage.num = _num

    @staticmethod
    def get_num():
        return Storage.num


def set_data(self, _data):
    self.__data = _data


def get_data(self):
    return self.__data


class Student:

    __slots__ = ('name', 'age')


if __name__ == '__main__':
    Storage.set_num(123)
    print(Storage.get_num())

    storage = Storage()
    print('data: ', storage._Storage__data)

    storage1 = Storage()
    storage1.name = 'Student'
    print('storage1.name: ', storage1.name)

    Storage.name = 'Micro'
    print('Storage.name: ', Storage.name)

    del storage1.name  # 删除实例属性
    print('storage1.name: ', storage1.name)

    storage1.set_data = MethodType(set_data, storage1)
    storage1.get_data = MethodType(get_data, storage1)
    storage1.set_data(123456)
    print('storage1.data: ', storage1.get_data())

    Storage.set_data = set_data
    Storage.get_data = get_data
    storage.set_data(789)
    print('storage.data: ', storage.get_data())

    student = Student()
    student.name = 'Michael'
    student.age = 20
    print('student name: ', student.name, 'age: ', student.age)

class spisok:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size  # Инициализируем массив нулями
        self.read_count = 0      # Счетчик обращений на чтение
        self.write_count = 0     # Счетчик обращений на запись
        self.current_index = 0   # Индекс для добавления

    def get_value(self, index):
        # Геттер проверяющий выход за границы массива
        if 0 <= index < self.current_index:
            self.read_count += 1  # Увеличиваем счетчик чтений
            return self.data[index]
        else:
            raise IndexError("Индекс выходит за границы массива.")

    def set_value(self, index, value):
        # Сеттер проверяющий входящее значение и выход за границы массива
        if not (-100 <= value <= 100):
            raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
        
        if 0 <= index < self.size:
            self.data[index] = value
            self.write_count += 1  # Увеличиваем счетчик записей
            if index >= self.current_index:
                self.current_index = index + 1  # Обновляем текущий индекс
        else:
            raise IndexError("Индекс выходит за границы массива.")

    def append(self, value):
        # Добавляет значение в конец массива расширяя его при необходимости
        if not (-100 <= value <= 100):
            raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
        
        if self.current_index >= self.size:  # Если массив заполнен
            self.size *= 2  # Увеличиваем размер массива вдвое
            self.data.extend([0] * (self.size - self.current_index))  # Расширяем массив нулями
        
        self.data[self.current_index] = value
        self.current_index += 1
        self.write_count += 1  # Увеличиваем счетчик записей

    def display(self):
        #Вывод всех значений массива
        print(self.data[:self.current_index])  # Выводим только заполненные значения

    def get_read_count(self):
        #Возвращает количество обращений на чтение
        return self.read_count

    def get_write_count(self):
        #Возвращает количество обращений на запись
        return self.write_count

    def add(self, other):
        #Сложение массивов
        max_length = max(self.current_index, other.current_index)
        result = spisok(max_length)

        for i in range(max_length):
            val_a = self.get_value(i) if i < self.current_index else 0
            val_b = other.get_value(i) if i < other.current_index else 0
            result.append(val_a + val_b)

        return result

    def subtract(self, other):
        #Вычитание массивов
        max_length = max(self.current_index, other.current_index)
        result = spisok(max_length)

        for i in range(max_length):
            val_a = self.get_value(i) if i < self.current_index else 0
            val_b = other.get_value(i) if i < other.current_index else 0
            result.append(val_a - val_b)

        return result



size = int(input("размер массива"))
arrA = spisok(size)

print("значения для первого массива")
for i in range(size):
    user_input = input()

    try:
        value = int(user_input)
        arrA.append(value)
    except ValueError as e:
        print(e)

arrB = spisok(size)
print("значения для второго массива")
for i in range(size):
    user_input = input()

    try:
        value = int(user_input)
        arrB.append(value)
    except ValueError as e:
        print(e)

result_add = arrA.add(arrB)
print("Результат сложения:")
result_add.display()

result_subtract = arrA.subtract(arrB)
print("Результат вычитания:")
result_subtract.display()
import sqlite3

# подключаемся к базе данных коллекции книг
conn = sqlite3.connect('hist.db')

# создаем объект cursor, для работы с базой данных
c = conn.cursor()

# делаем запрос, который создает таблицу books с идентификатором и именем
#так была создана бд
#c.execute('''
          #CREATE TABLE books
          #(id INTEGER PRIMARY KEY ASC,
	     #name varchar(250) NOT NULL)
          #''' )

# выполняет запрос, который вставляет значения в таблицу

c.execute("INSERT INTO books VALUES('Андрусовское перемирие', '1667.jpg')")
# сохраняем работу
conn.commit()

# закрываем соединение
conn.close()
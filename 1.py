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

c.execute("INSERT INTO books VALUES('Взятие Измаила', '1790.png')")
c.execute("INSERT INTO books VALUES('Тильзитский мир', '1807.jpg')")
c.execute("INSERT INTO books VALUES('Битва при Аустерлице', '1905.jpg')")
c.execute("INSERT INTO books VALUES('Открытие Большого театра в Москве', '1825.jpg')")
c.execute("INSERT INTO books VALUES('Основание Москвы', '1147.jpg')")
c.execute("INSERT INTO books VALUES('Продажа Аляски США', '1867.jpg')")
c.execute("INSERT INTO books VALUES('Кровавое воскресенье', '1905.jpg')")
c.execute("INSERT INTO books VALUES('Стальной пакт', '1939.jpg')")
c.execute("INSERT INTO books VALUES('Образование СССР', '1922.jpg')")
c.execute("INSERT INTO books VALUES('Карибский кризис', '1963.jpg')")
c.execute("INSERT INTO books VALUES('Создание третьяковской галереи', '1856.jpg')")
# сохраняем работу
conn.commit()

# закрываем соединение
conn.close()
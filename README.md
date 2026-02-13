# RecipeLibrary
Мы делаем Библиотеку рецептов для любителей готовить, чтобы они могли легко находить новые рецепты, создавать собственные коллекции блюд и обмениваться ими с друзьями.
......................................
Пример простого скрипта для создания таблицы рецептов:
...................................
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Создание таблицы рецептов
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    cooking_time INTEGER NOT NULL,
    category TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

# Закрытие соединения
conn.commit()
conn.close()

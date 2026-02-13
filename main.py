from sqlalchemy.orm import sessionmaker
from models import engine, User, Ingredient, Recipe, Comment, Image, HistoryAction

Session = sessionmaker(bind=engine)
session = Session()

def create_user():
    """Регистрация нового пользователя"""
    name = input("Введите ваше имя: ")
    role = input("Ваша роль (Beginner/Chef/Collector): ")
    user = User(name=name, role=role)
    session.add(user)
    session.commit()
    print(f"Поздравляю, {name}, ваш аккаунт зарегистрирован!")

def show_recipes():
    """Показ всех рецептов"""
    recipes = session.query(Recipe).all()
    for rec in recipes:
        print(f"{rec.id}: {rec.title}, Автор: {rec.user_id}, Категория: {rec.category}")

def add_recipe():
    """Добавление нового рецепта"""
    title = input("Введите название рецепта: ")
    instruction = input("Введите инструкцию приготовления: ")
    prep_time = int(input("Введите время приготовления (в минутах): "))
    category = input("Введите категорию (Appetizer/Main/Dessert): ")
    user_id = int(input("Введите ваш ID пользователя: "))
    recipe = Recipe(title=title, instruction=instruction, prep_time=prep_time, category=category, user_id=user_id)
    session.add(recipe)
    session.commit()
    print("Рецепт успешно добавлен!")

def edit_recipe():
    """Изменение существующего рецепта"""
    recipe_id = int(input("Введите ID рецепта для изменения: "))
    recipe = session.query(Recipe).get(recipe_id)
    if not recipe:
        print("Рецепт не найден.")
        return
    print(f"Редактируемый рецепт: {recipe.title}")
    title = input("Введите новое название (оставьте пустым, чтобы сохранить прежнее): ") or recipe.title
    instruction = input("Новая инструкция (оставьте пустым, чтобы сохранить прежнюю): ") or recipe.instruction
    prep_time = input("Новое время приготовления (оставьте пустым, чтобы сохранить прежнее): ") or str(recipe.prep_time)
    category = input("Новая категория (оставьте пустым, чтобы сохранить прежнюю): ") or recipe.category
    recipe.title = title
    recipe.instruction = instruction
    recipe.prep_time = int(prep_time)
    recipe.category = category
    session.commit()
    print("Рецепт успешно обновлен!")

def delete_recipe():
    """Удаление рецепта"""
    recipe_id = int(input("Введите ID рецепта для удаления: "))
    recipe = session.query(Recipe).get(recipe_id)
    if not recipe:
        print("Рецепт не найден.")
        return
    session.delete(recipe)
    session.commit()
    print("Рецепт успешно удален!")

def main_menu():
    while True:
        print("\nБиблиотека рецептов:")
        print("1. Зарегистрироваться")
        print("2. Просмотреть рецепты")
        print("3. Добавить рецепт")
        print("4. Редактировать рецепт")
        print("5. Удалить рецепт")
        print("6. Завершить работу")
        choice = input("Ваш выбор: ")
        if choice == '1': create_user()
        elif choice == '2': show_recipes()
        elif choice == '3': add_recipe()
        elif choice == '4': edit_recipe()
        elif choice == '5': delete_recipe()
        elif choice == '6': break
        else: print("Ошибка выбора. Повторите попытку.")

if __name__ == '__main__':
    main_menu()
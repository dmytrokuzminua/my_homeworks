""" Homework 2 task 8  """


def create_user_settings():
    """Func of creating user`s settings, returns closured function 'user_settings' """
    settings = {
        "theme": "light",
        "language": "uk",
        "notifications": True
    }
    def user_settings(action: str, key: str = None, value: str|bool =None):
        """ Show or update user settings, returns settings or set settings """
        nonlocal settings
        if action == "view":
            return settings
        if action == "update":
            if key in settings:
                settings[key] = value
                print(f"Налаштування '{key}' змінено на {value}")
            else:
                print(f"Налаштування '{key}' не існує")
        else:
            print("Невідома команда. Використовуйте 'view' або 'update'.")

    return user_settings


def main():
    """main def"""
    settings = create_user_settings()

    print(settings("view"))
    settings("update", "theme", "dark")
    settings("update", "language", "en")
    print(settings("view"))
    settings("update", "font_size", 12) # Тест помилкового значення налаштування


if __name__ == "__main__":
    main()

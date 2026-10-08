"""Навчальний «Сапер»: Tkinter і функції, без власних класів.

Запуск: python minesweeper_tkinter.py
Перевірка Tkinter: python -m tkinter

Клікайте клітинки лівою кнопкою миші. Відкрийте всі безпечні
клітинки, щоб перемогти. Число показує кількість сусідніх мін.
Це спрощена гра: без прапорців, автоматичного відкриття нулів
і гарантовано безпечного першого ходу.

Навчальний маршрут:
1. create_bombs, calculate_counts — дані та правила гри.
2. create_state, open_cell — стан гри та один хід.
3. create_interface, show_cell, finish_game — відображення.
4. start_new_game, main — підготовка та запуск.

partial створює обробник натискання з наперед переданими аргументами.
Стан передаємо функціям явно через словник game: глобальних змінних немає.
"""

import random
import tkinter as tk
from functools import partial


def create_bombs(size, bomb_count):
    """Повернути множину унікальних координат мін."""
    bombs = set()
    while len(bombs) < bomb_count:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        bombs.add((row, col))
    return bombs


def calculate_counts(size, bombs):
    """Порахувати сусідні міни для кожної безпечної клітинки."""
    counts = {}
    for row in range(size):
        for col in range(size):
            if (row, col) in bombs:
                continue
            around = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    # Центр безпечний, тому не збільшить лічильник.
                    # Координат поза полем у множині bombs немає.
                    if (row + dr, col + dc) in bombs:
                        around += 1
            counts[(row, col)] = around
    return counts


def create_state(size, bomb_count):
    """Створити словник для даних гри та посилань на елементи вікна."""
    return {
        "size": size,
        "bomb_count": bomb_count,
        "bombs": set(),
        "counts": {},
        "opened": set(),
        "finished": False,
        "buttons": [],
        "status": None,
    }


def update_status(game):
    """Показати, скільки безпечних клітинок залишилося відкрити."""
    safe_cells = game["size"] * game["size"] - game["bomb_count"]
    remaining = safe_cells - len(game["opened"])
    game["status"].config(text="Безпечних клітинок залишилося: " + str(remaining))


def show_cell(game, row, col):
    """Показати підказку та вимкнути кнопку відкритої клітинки."""
    count = game["counts"][(row, col)]
    game["buttons"][row][col].config(
        text=str(count),
        state=tk.DISABLED,
        relief=tk.SUNKEN,
        bg="#e2e8f0",
        disabledforeground="#0f172a",
    )


def finish_game(game, won):
    """Зафіксувати результат, показати міни та вимкнути поле."""
    game["finished"] = True
    if won:
        game["status"].config(text="Перемога! Усі безпечні клітинки відкрито.")
    else:
        game["status"].config(text="Міна! Гру завершено. Спробуйте ще раз.")

    for row, col in game["bombs"]:
        game["buttons"][row][col].config(
            text="*", bg="#fecaca", disabledforeground="#991b1b"
        )
    for button_row in game["buttons"]:
        for button in button_row:
            button.config(state=tk.DISABLED)


def open_cell(game, row, col):
    """Обробити один хід — цю функцію викликає натискання кнопки."""
    if game["finished"] or (row, col) in game["opened"]:
        return

    if (row, col) in game["bombs"]:
        finish_game(game, False)
        return

    game["opened"].add((row, col))
    show_cell(game, row, col)
    update_status(game)

    safe_cells = game["size"] * game["size"] - game["bomb_count"]
    if len(game["opened"]) == safe_cells:
        finish_game(game, True)


def start_new_game(game):
    """Підготувати нові міни й повернути існуючі кнопки до початкового стану."""
    game["bombs"] = create_bombs(game["size"], game["bomb_count"])
    game["counts"] = calculate_counts(game["size"], game["bombs"])
    game["opened"] = set()
    game["finished"] = False

    for button_row in game["buttons"]:
        for button in button_row:
            button.config(
                text=".", state=tk.NORMAL, relief=tk.RAISED,
                bg="#f1f5f9", fg="#0f172a", disabledforeground="#0f172a",
            )
    update_status(game)


def create_interface(window, game):
    """Створити написи, поле кнопок і кнопку нової гри."""
    window.title("Сапер — Tkinter і функції")
    window.resizable(False, False)

    title = tk.Label(window, text="Сапер", font=("Arial", 20, "bold"))
    title.pack(padx=16, pady=(14, 4))

    instruction = tk.Label(window, text="Відкрийте всі клітинки без мін.")
    instruction.pack(padx=16, pady=(0, 8))

    game["status"] = tk.Label(window, text="", font=("Arial", 11))
    game["status"].pack(padx=16, pady=(0, 8))

    board_frame = tk.Frame(window)
    board_frame.pack(padx=16, pady=4)

    # grid використовується всередині board_frame;
    # pack — для елементів усередині window. Контейнери різні.
    for col in range(game["size"]):
        tk.Label(board_frame, text=str(col)).grid(row=0, column=col + 1)

    for row in range(game["size"]):
        tk.Label(board_frame, text=str(row), width=2).grid(row=row + 1, column=0)
        button_row = []
        for col in range(game["size"]):
            button = tk.Button(
                board_frame,
                text=".",
                width=3,
                height=1,
                font=("Arial", 16, "bold"),
                # Передаємо майбутню дію, а не викликаємо open_cell зараз.
                # partial запам'ятовує game, row і col для цієї кнопки.
                command=partial(open_cell, game, row, col),
            )
            button.grid(row=row + 1, column=col + 1, padx=1, pady=1)
            button_row.append(button)
        game["buttons"].append(button_row)

    restart = tk.Button(
        window, text="Нова гра", font=("Arial", 12),
        command=partial(start_new_game, game),
    )
    restart.pack(pady=(10, 14))


def main():
    """Створити стан, побудувати вікно й запустити обробку подій."""
    size = 8
    bomb_count = 10
    if size <= 0 or bomb_count < 0 or bomb_count >= size * size:
        print("Потрібно: size > 0 та 0 <= bomb_count < size * size.")
        return

    game = create_state(size, bomb_count)
    window = tk.Tk()
    create_interface(window, game)
    start_new_game(game)
    # Tkinter очікує натискання і викликає відповідні функції.
    # Наш цикл while та input тут не потрібні.
    window.mainloop()


# Імпорт файла дозволяє перевіряти функції без відкриття вікна.
if __name__ == "__main__":
    main()

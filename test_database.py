import sqlite3
import pytest

def test_insert_and_select():
    #Створюємо БД в пам'яті
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    #Створюємо таблицю 'users'
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
        )
    """)
    #Вставляємо дані
    users = [
        ("Alice", 30),
        ("Bob", 25),
        ("Charlie", 35)
    ]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?,?)", users)
    conn.commit()

    # Виконуємо виборку усіх записів
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    #перевіряємо, що кількість записів дорівнює 3
    assert len(results) == 3

    #Перевіряємо дані першого запису
    first_user = results[0]
    assert first_user[1] == "Alice"
    assert first_user[2] == 30

    second_user = results[1]
    assert second_user[1] == "Bob"
    assert second_user[2] == 25

    third_user = results[2]
    assert third_user[1] == "Charlie"
    assert third_user[2] == 35

    #Зачиняємо з'єднання

    conn.close()


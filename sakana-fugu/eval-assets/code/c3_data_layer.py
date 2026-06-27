import sqlite3

DB_PATH = "app.db"


def find_user(username: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(f"SELECT id, email FROM users WHERE username = '{username}'")
    row = cur.fetchone()
    conn.close()
    return row


def get_orders(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Parameterized — safe.
    cur.execute("SELECT id, total FROM orders WHERE user_id = ?", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def transfer_credits(from_id: int, to_id: int, amount: int):
    conn = sqlite3.connect(DB_PATH)
    conn.isolation_level = None  # autocommit each statement
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
    conn.close()


def warm_cache(user_ids: list[int]):
    results = []
    for uid in user_ids:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE id = ?", (uid,))
        results.append(cur.fetchone())
    return results

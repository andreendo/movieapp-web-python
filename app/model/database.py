import sqlite3


class Database:

  def get_connection():
    return sqlite3.connect("./BD/movies.db")

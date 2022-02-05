"""
Datbase
"""

import sqlite3
import pickle


class MetaSingleton(type):
  """
  Class represents Sinfleton-pattern for database
  """
  _instances = {}

  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
      return cls._instances[cls]


class Database(metaclass=MetaSingleton):
  """
  Class represents database
  """
  def __init__(self, path=""):
    """
    Initilization of database
    :param path: absolute path without filename to database(default ="")
    """
    db_filepath = path + "signatures.db"

    if not os.path.exists(db_filepath):
      open(db_filepath, 'a').close()

    if path == "":
        self.conn = sqlite3.connect(db_filepath, check_same_thread=False)
    else:
        self.conn = sqlite3.connect(db_filepath, check_same_thread=False)

    self.cur = self.conn.cursor()
    self.cur.execute("DROP TABLE IF EXISTS signatures;")
    self.cur.execute('''CREATE TABLE IF NOT EXISTS signatures
        (id INTEGER PRIMARY KEY NOT NULL,
        uid BIG INT,
        sign BLOB);''')
    self.conn.commit()

  def insert_sign(self, sign, uid):
    """
    Method implements inserting sign and uid to database
    :param sign: embedding of signature photo
    :param uid: uid of sender in telegram to insert in database
    """
    try:
        sqlite_insert_query = 'INSERT INTO signatures(sign, uid) VALUES (?, ?)'
        self.cur.execute(sqlite_insert_query, (sqlite3.Binary(pickle.dumps(sign)), uid))
        self.conn.commit()
        return uid
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def check_signs(self, sign):
    """
    Method implements checking if sign exists in database
    :param sign: embedding of signature photo to check
    """
    try:
        sqlite_select_query = 'SELECT uid FROM signatures WHERE sign == ?'
        answer = self.cur.execute(sqlite_select_query,
                                  (sqlite3.Binary(pickle.dumps(sign)),)).fetchone()
        if answer is None:
            return None
        else:
            return answer[0]
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def get_sign_by_id(self, id):
    """
    Method implements getting information from database by id
    :param id: id to fetch from database
    """
    try:
        sqlite_select_query = 'SELECT sign FROM signatures WHERE id == ?'
        answer = self.cur.execute(sqlite_select_query, (id,)).fetchone()
        if answer is None:
            return []
        else:
            return pickle.loads(answer[0])
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def get_sign_by_uid(self, uid):
    """
    Method implements getting information from database by uid
    :param uid:uid to fetch from database
    """
    try:
        sqlite_select_query = 'SELECT sign FROM signatures WHERE uid == ?'
        answer = self.cur.execute(sqlite_select_query, (uid,)).fetchone()
        if answer is None:
            return []
        else:
            return pickle.loads(answer[0])
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def delete_sign_by_uid(self, sign):
    """
    Method implements deleting information from database by uid
    :param sign: sign uid to delete from database
    """
    try:
        sqlite_delete_query = 'DELETE FROM signatures WHERE uid = ?'
        self.cur.execute(sqlite_delete_query, (sign,))
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def delete_sign_by_id(self, id):
    """
    Method implements deleting information from database by id
    :param id: id to delete from database
    """
    try:
        sqlite_delete_query = 'DELETE FROM signatures WHERE id = ?'
        self.cur.execute(sqlite_delete_query, (id,))
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

  def __del__(self):
    """
    Destructor of database class
    """
    self.cur.close()
    self.conn.close()
    print('Connection closed')

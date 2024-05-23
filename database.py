import sqlite3


class DB:
    def __init__(self):
        self.__con = sqlite3.connect("Database.db", check_same_thread=False)
        self.__cur = self.__con.cursor()

    def create_db(self):
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS Person(
                    personId integer primary key autoincrement,
                    name varchar(100),
                    age int,
                    nationalityId str,
                    birthDate
        );"""
        )

    def insert_values(self):
        values = [
            ("mostafa1", "23", "65465as4sd654", "2001-11-11"),
            ("mostafa2", "22", "65465at4sd654", "2002-11-11"),
            ("mostafa3", "21", "65465ag4sd654", "2003-11-11"),
            ("mostafa4", "20", "65465af4sd654", "2004-11-11"),
            ("mostafa5", "19", "65465av4sd654", "2005-11-11"),
            ("mostafa6", "18", "65465ac4sd654", "2006-11-11"),
        ]
        self.__cur.executemany(
            "INSERT INTO Person(name, age, nationalityId, birthDate) VALUES(?, ?, ?, ?)",
            values,
        )
        self.__con.commit()

    def get_all_persons(self):
        records = self.__cur.execute("SELECT * FROM Person;").fetchall()
        return records

    def add_new_person(self, name, age, nationalityId, birthDate):
        # params should be validated first before insert int into database to prevent sql injection
        self.__cur.execute(
            """INSERT INTO Person(name, age, nationalityId, birthDate)
                    VALUES(?, ?, ?, ?);
                    """,
            (name, age, nationalityId, birthDate),
        )
        self.__con.commit()

    def update_person_info(
        self, person_id, new_name, new_age, new_nationalityId, new_birthDate
    ):
        # params should be validated first before insert int into database to prevent sql injection
        # should validate types before insert it
        self.__cur.execute(
            """UPDATE Person SET name = ?, age = ?, nationalityId = ?, birthDate = ? WHERE personId = ?""",
            (new_name, new_age, new_nationalityId, new_birthDate, person_id),
        )
        self.__con.commit()

    def delete_person(self, person_id):
        self.__cur.execute(
            "DELETE FROM Person WHERE PersonId = ?", (person_id,)
        )
        self.__con.commit()


if __name__ == "__main__":
    db = DB()
    db.create_db()

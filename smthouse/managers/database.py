import mysql.connector
import datetime
import smthouse


def __init__():
    try:
        database = mysql.connector.connect(
            host=smthouse.config.HOST,
            user=smthouse.config.USER,
            port=3306,
            password=smthouse.config.PASSWORD,
            database=smthouse.config.DB_NAME,
        )
        return database
    except Exception as error:
        print("\nНевозможно подключиться к базе данных. Пожалуйста, проверьте свои учетные данные!\n"
              + str(error) + "\n")
        quit()


def db(database):
    try:
        return database.cursor(buffered=True)
    except Exception as e:
        print(f"\nПроизошла ошибка при выполнении оператора SQL.\n{e}\n")
        quit()


def search(user_id):
    search_user = f"SELECT * FROM users WHERE id = '{user_id}';"
    database = smthouse.managers.database.__init__()
    db_c = smthouse.managers.database.db(database)

    try:
        db_c.execute(search_user)

    except Exception as e:
        db_c.close()
        del db_c
        print(e)
        return False

    for row in db_c.fetchall():
        return row

    db_c.close()
    del db_c


def instant_punishment(row, member, reason, last_warn):
    database = smthouse.managers.database.__init__()
    db_c = smthouse.managers.database.db(database)

    if row[2] == str(reason) or row[3] == str(reason):
        if not row[6] and not row[7] and not row[8]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment1 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment1"

        elif row[6] and not row[7] and not row[8]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment2 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment2"

        elif row[6] and row[7] and not row[8]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment3 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment3"


def punish_user(member, reason):
    database = smthouse.managers.database.__init__()
    db_c = smthouse.managers.database.db(database)
    row = search(member.id)
    last_warn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not row:
        add_warn = (f"INSERT INTO `users` (id, nickname, warn1, last_warn) "
                    f"VALUES ('{member.id}', '{member.name}', '{reason}', '{last_warn}')")

        db_c.execute(add_warn)
        database.commit()

        db_c.close()
        del db_c
        return "warn1"

    elif not row[3] and row[5] or not row[4] and row[5] or not row[5] or not row[8]:
        if not row[2] and not row[3] and not row[4] and row[9]:
            add_warn = f"UPDATE `users` SET warn1 = '{reason}', last_warn = '{last_warn}' WHERE id = '{member.id}'"

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "warn1"

        elif row[2] and not row[3] and not row[4]:
            instant = instant_punishment(row, member, reason, last_warn)
            if not instant:
                add_warn = f"UPDATE `users` SET warn2 = '{reason}', last_warn = '{last_warn}' WHERE id = '{member.id}'"

                db_c.execute(add_warn)
                database.commit()

                db_c.close()
                del db_c
                return "warn2"

        elif row[2] and row[3] and not row[4]:
            if not instant_punishment(row, member, reason, last_warn):
                add_warn = f"UPDATE `users` SET warn3 = '{reason}', last_warn = '{last_warn}' WHERE id = '{member.id}'"

                db_c.execute(add_warn)
                database.commit()

                db_c.close()
                del db_c
                return "warn3"

        elif row[2] and row[3] and row[4] and not row[6]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment1 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment1"

        elif row[2] and row[3] and row[4] and row[6] and not row[7]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment2 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment2"

        elif row[2] and row[3] and row[4] and row[6] and row[7] and not row[8]:
            add_warn = (f"UPDATE `users` "
                        f"SET warn1 = NULL, warn2 = NULL, warn3 = NULL, last_warn = NULL, "
                        f"punishment3 = '{reason}', last_punishment = '{last_warn}' "
                        f"WHERE id = '{member.id}'")

            db_c.execute(add_warn)
            database.commit()

            db_c.close()
            del db_c
            return "punishment3"

    elif row[4] and row[8]:
        print(f"Пользователь {member.name} забанен, за большое количество нарушений.")
        return "BAN"

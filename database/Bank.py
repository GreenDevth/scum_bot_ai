from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config

db = read_db_config()


def player_coins(discord_id):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        sql = 'SELECT COINS FROM scum_players WHERE DISCORD_ID=%s'
        cur.execute(sql, (discord_id,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res[0]
    except Error as e:
        print(e)


def cash(discord_id, coins):
    conn = None
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        current_coin = player_coins(discord_id)
        checkout = current_coin - coins
        sql = 'UPDATE scum_players SET COINS = %s WHERE DISCORD_ID = %s'
        cur.execute(sql, (checkout, discord_id,))
        conn.commit()
        cur.close()
        return 1
    except Error as e:
        print(e)
    finally:
        if conn.is_connected():
            conn.close()


def minus_coins(discord_id, coins):
    """ minus coins from players """
    conn = None
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        current_coin = player_coins(discord_id)
        minus = current_coin - coins
        sql = 'UPDATE scum_players SET COINS = %s WHERE DISCORD_ID = %s'
        cur.execute(sql, (minus, discord_id,))
        conn.commit()
        total = player_coins(discord_id)
        msg = 'ทำรายการสำเร็จ ยอดเงินคงเหลือ ${:,d}'.format(total)
        return msg.strip()
    except Exception as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def plus_coins(discord_id, coins):
    """ Plus Coin to player """
    conn = None
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        current_coin = player_coins(discord_id)
        plus = current_coin + coins
        sql = 'UPDATE scum_players SET COINS = %s WHERE DISCORD_ID = %s'
        cur.execute(sql, (plus, discord_id))
        conn.commit()
        total = player_coins(discord_id)
        msg = 'ทำรายการสำเร็จ ยอดเงินของคุณตอนนี้คือ **${:,d}**'.format(total)
        return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


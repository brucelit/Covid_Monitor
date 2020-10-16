import pymysql
import time
import json
import traceback
import sys
import requests as re

# 爬取腾讯提供的历史数据
def get_covid_history():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/'
    }
    s = re.session()
    s.keep_alive = False
    resp = re.get(url, headers=headers, proxies={"http": "http://111.233.225.166:1234"})
    r1 = json.loads(resp.text)
    result = json.loads(r1['data'])
    resp.close()

    daily_history = result.get("chinaDayList")
    history = {}
    for i in daily_history:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        import_case = i["importedCase"]
        dead_rate = i["deadRate"]
        heal_rate = i["healRate"]
        history[ds] = ({"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead, "import_case": import_case,
                        "dead_rate": dead_rate, "heal_rate": heal_rate})
    return history

def get_conn():
    """
    :return: 连接，游标l
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="1129",
                           db="covid",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def insert_history():
    cursor = None
    conn = None
    try:
        dic = get_covid_history()
        print(f"{time.asctime()}start insert history data")
        conn,cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s)"
        for k,v in dic.items():
            cursor.execute(sql,[k,v.get("confirm"),v.get("suspect"),v.get("heal"),v.get("dead"),
                               v.get("import_case"),v.get("heal_rate"),v.get("dead_rate")])
        conn.commit()
        print(f"{time.asctime()}insert complete")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)


def update_history():
    cursor = None
    conn = None
    try:
        dic = get_covid_history()
        print(f"{time.asctime()}start insert history data")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds = %s"
        for k,v in dic.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k,v.get("confirm"),v.get("suspect"),v.get("heal"),v.get("dead"),
                               v.get("import_case"),v.get("heal_rate"),v.get("dead_rate")])
        conn.commit()
        print(f"{time.asctime()}insert complete")

    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

insert_history()
update_history()

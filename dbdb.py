import pymysql

def dbcon():
    return pymysql.connect(host='rkdgusdls.mysql.pythonanywhere-services.com',
                   user='rkdgusdls', password='h123456789',
                   db='rkdgusdls$mydb', charset='utf8')
def insert_user(userid, pw, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (userid, pw, name)
        c.execute("INSERT INTO user VALUES (%s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_user(userid, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (userid, pw)
        c.execute('SELECT * FROM user WHERE userid = %s AND pw = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

#create_table()
#insert_data('20201234', '파이썬')
#ret = select_all()
#print(ret)
import pymysql

def dbcon():
    return pymysql.connect(host='rkdgusdls.mysql.pythonanywhere-services.com',
                   user='rkdgusdls', password='a123456789',
                   db='rkdgusdls$mydb', charset='utf8')

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE student (num varchar(50), name varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(num, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num, name)
        c.execute("INSERT INTO student VALUES (%s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM student')
        ret = c.fetchall()
        # for row in c.execute('SELECT * FROM student'):
        #     ret.append(row)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def select_num(num):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num,)
        c.execute('SELECT * FROM student WHERE num = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

create_table()
insert_data('20201234', '파이썬')
ret = select_all()
print(ret)
from flask import Flask, request, render_template, redirect, url_for, abort, session

import dbdb

app = Flask(__name__)

# 세션처리를 위한 키
app.secret_key = b'aaa!111/'

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')


@app.route('/wash')
def wash():
    return render_template('wash.html')


@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == "GET":
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        # 회원정보를 데이터베이스에 넣기
        
        #ret = dbdb.check_id(id)
        #if ret != None:
        #    return'''
        #            <script>
        #            alert('다른 아이디를 사용 하세요);
        #            locatiob.href='/join';
        #            </script>
        #          '''
        #dbdb.insert_user(id, pw, name)
        return redirect(url_for('login'))

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type(id))
        print (pw,type(pw))
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        # ret = dbdb.select_user(id, pw)
        #if ret != None:
        #    session['user'] = id
        #    return redirect(url_for('hello'))           
        #else:
        #    return '''
        #    <script>
        #    alert
        #    ('아이디 또는 패스워드를 확인 하세요');
        #    location.href='/login';
        #    </script>
        #    '''
        return redirect(url_for('hello'))    

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('hello'))



# 축구페이지
@app.route('/football')
def football():
    return '''
    <html>
    <body>

    <h2>여기는 축구페이지</h2>
    <img src="https://post-phinf.pstatic.net/MjAxOTA0MTBfMSAg/MDAxNTU0OTA0MTU0OTUy.wbiyoTJa-UaWgue-EcZYcwWPDxjcAUO8UEjd-ZT3rsAg.Vmg-tfnQz59yfac-MIA3AdmQQupDTpCUYkMLHA-RVbYg.JPEG/%EC%86%90%ED%9D%A5%EB%AF%BC.jpg" alt="축구">

    </body>
    </html>
    '''
# 배구페이지
# 농구페이지

if __name__ == '__main__':
   app.run(debug=True)
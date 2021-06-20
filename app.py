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
        name = request.form['name']
        userid = request.form['userid']
        pw = request.form['pw']
        # 회원정보를 데이터베이스에 넣기
        dbdb.insert_user(userid, name, pw)
        #ret = dbdb.check_id(id)
        #if ret != None:
        #    return'''
        #            <script>
        #            alert('다른 아이디를 사용 하세요);
        #            locatiob.href='/join';
        #            </script>
        #          '''

        return redirect(url_for('login'))

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['userid']
        pw = request.form['pw']
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234':
            session['user'] = id
            return '''
                <script> alert("안녕하세요~ {}님");
                location.href="/"
                </script>
            '''.format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."
            
# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/search')
def search():
    # 만약에 로그인 상태이면 검색 페이지 나오고
    if 'name' in session:
        return render_template('search.html')
    # 아니면 로그인 페이지로 이동
    else:
        return redirect("main.html")

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

#if __name__ == '__main__':
#    app.run(debug=True)
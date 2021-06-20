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
        name = request.form['username']
        userid = request.form['userid']
        pwd = request.form['pwd']
        # 회원정보를 데이터베이스에 넣기
        dbdb.insert_user(userid, name, pwd)
        return '<b>{}, {}, {}</b> 님 회원가입 되었습니다.'.format(name, userid, pwd)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['userid']
        pw = request.form['pwd']
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


# 로그인 사용자만 접근 가능으로 만들면
@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form["num"]
        name = request.form["name"]
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/search')
def search():
    # 만약에 로그인 상태이면 검색 페이지 나오고
    if 'name' in session:
        return render_template('search.html')
    # 아니면 로그인 페이지로 이동
    else:
        return redirect("main.html")



@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == "GET":
        return '그냥 넘어옴(GET)'
    else:
        name = request.form['fname']
        return '<b>{}</b> 로 검색한 결과입니다. 리스트 쫙~~(POST)'.format(name)

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
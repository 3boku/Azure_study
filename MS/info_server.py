from flask import Flask

app = Flask(__name__)

@app.route('/')

def about_flask():
    return f"""
       <h1>About Flask</h1>

       <h2>가볍고 민첩함</h2>
       간단한 기본 구조를 가지고 있다
       <br/>
       <h2>확장성</h2>
       다양한 익스텐션을 사용할수 있다
       <br/>
       <h2>유연성</h2>
       개발자가 원하는 방식으로 만들 수 있다.
    """

if __name__ == '__main__':
    app.run()
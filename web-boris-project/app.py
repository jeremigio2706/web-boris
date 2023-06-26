from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Inicio():  # put application's code here
    return render_template('index.html')

@app.route('/blog', methods=['GET', 'POST'])
def EliteInvestmen():
    return render_template('Elite Investmen Blog.html')

@app.route('/el-poder-del-dinero', methods=['GET', 'POST'])
def ultimopost():
    return render_template('lastpost.html')

@app.route('/el-legado-del-sueño', methods=['GET', 'POST'])
def penultimopost():
    return render_template('penultimopost.html')



if __name__ == '__main__':
    app.run()

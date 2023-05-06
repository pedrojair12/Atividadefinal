from flask_login import login_user, logout_user, login_required
from flask import flash, redirect, render_template, url_for, render_template, request, redirect, url_for
from app import app, db, bcrypt
from app.forms import FormLogin, FormCadastro
from app.models import usuario, Produto

'''Cria uma rota chamada "/cadastro" '''
@app.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro():
    form_Cadastro = FormCadastro()
    if form_Cadastro.validate_on_submit():
        try:
            senha_crypto = bcrypt.generate_password_hash(form_Cadastro.senha.data)
            usu = usuario(usuario=form_Cadastro.usuario.data, email=form_Cadastro.email.data, senha=senha_crypto)
            db.session.add(usuario)
            db.session.commit()
            flash(f'O usuario {usuario.usuario} teve sucesso no cadastramento', 'alert-success')
        except:
            flash(f'Houve uma falha ao cadastrar usuário ou já existe esse usuário', 'alert-danger')
        return redirect(url_for('cadastro'))
    return render_template("cadastro.html", form_Cadastro=form_Cadastro)
   

'''Cria uma rota chamada "/login" '''
@app.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    if request.method == 'POST':
     
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        email = request.form.get('email')

        user = usuario.query.filter_by(email = email).first()
        if not user or not user.verify_password(senha):
            return redirect(url_for('login'))
    
        login_user(user)
        return redirect(url_for('cadastro'))

    return render_template('login.html')

'''Cria uma rota chamada "/logout" '''
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

'''Cria uma rota chamada "/add" '''
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        categoria = request.form['categoria']
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        valor = request.form['valor']
        produto = Produto(categoria=categoria, nome=nome, quantidade=quantidade, valor=valor)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('add'))
    return render_template('Produto.html')

'''Cria uma rota chamada " /edit" '''
@app.route('/edit', methods=['GET', 'POST'])
def edit(id):
    produto = Produto.query.get(id)
    if request.method == 'POST':
        produto.categoria = request.form['categoria']
        produto.nome = request.form['nome']
        produto.quantidade = request.form['quantidade']
        produto.valor = request.form['valor']
        db.session.commit()
        return redirect(url_for('edit'))
    return render_template('Produto.html', produto=produto)

'''Cria uma rota chamada "/delete" '''
@app.route('/delete')
def delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('Produto'))


if __name__ == '__main__':
    app.run(debug=True)
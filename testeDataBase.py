from app import app, db
from app.models import usuario
import bcrypt

'''Cria o banco'''

# with app.app_context():
#   db.create_all()

'''Exclue o banco'''
with app.app_context():
    db.drop_all()
    db.create_all()

'''Faz registro em uma tabela'''
with app.app_context():
   senha_crypto = bcrypt.generate_password_hash('Crocodilo123')
   user = usuario(usuario='CROCODILO', email='Crocodilo123@gmail.com', senha=senha_crypto)
   db.session.add(usuario)
   db.session.commit()

   # Realizar um select de todos os registros de uma tabela
# with app.app_context():
#     user = usuario.query.all()
#     print(usuario[0].usuario)
#     print(usuario[1].usuario)

'''Mostra todos os usuários e retorna apenas o primeiro registro (".first")'''
# with app.app_context():
#     user = usuario.query.first()
#     print(user.usuario)

'''Mostra o usuário que está de acordo com a condição abaixo'''
# with app.app_context():
#     user = Usuario.query.filter_by(senha='Crocodilo123').all()
#     print(user)

# from app import bcrypt
#
# senha = 'Crocodilo123'
# hash = bcrypt.generate_password_hash(senha)
# print(senha)
# print(hash)
# print(bcrypt.check_password_hash(hash, 'Crocodilo123'))





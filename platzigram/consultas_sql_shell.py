from datetime import date

users = [{
  "email": "ejemplo1@example.com",
  "first_name": "Juan",
  "last_name": "Pérez",
  "password": "contraseña123", 
  "countr_city": 'Guatemala'
},
{
  "email": "ejemplo2@example.com",
  "first_name": "María",
  "last_name": "Gómez",
  "password": "claveSegura456"
},
{
  "email": "ejemplo3@example.com",
  "first_name": "Luis",
  "last_name": "Rodríguez",
  "password": "miContraseñaSecreta",
  "birthdate": date(1995,12,10)
},
{
  "email": "ejemplo4@example.com",
  "first_name": "Ana",
  "last_name": "Martinez",
  "password": "contraseñaSegura789",
  "birthdate": date(1990, 11, 15),
  'bio':"The path of the righteous man is beset on all sides by the iniquities of the selfish and th"
}
]
from posts.models import User

for user in users:
  obj = User(**user)
  obj.save()
  print(obj.pk, ':', obj.email)

#Operaciones 

#Crear
new_user = User(email="nuevo@email.com", first_name="Nombre", last_name="Apellido", password="contraseña",country_city='Quetzaltenango')
new_user.save()

#Actualizar
user = User.objects.get(email='daniel@gmail.com')  
user.country_city = "Guatemala"
user.save()

#Eliminar
user = User.objects.get(email='daniel@gmail.com')  
user.delete()

# Obtener todos los usuarios
users = User.objects.all()  
for user in users:
    print(user.email)

# Filtrar usuarios por nombre
daniels = User.objects.filter(first_name='Daniel')

# Mostrar correos electrónicos de usuarios llamados Daniel
for user in daniels:
    print(user.email)

# Ordenar usuarios por apellido
users_ordered = User.objects.all().order_by('last_name')  

for user in users_ordered:
  print(user.last_name)

#Usuarios
#Crear usuario
from django.contrib.auth.models import User
u = User.objects.create_user(username='yessika',password='admin123')
u
u.username
u.password

#Crear superusuario
"""python3 manage.py createsuperuser
Username (leave blank to use 'daniel'): daniel
Email address: daniel@gmail.com
Password:  Accesssss.987"""

#Borrar archivo de bd
"rm db.sqlite3"
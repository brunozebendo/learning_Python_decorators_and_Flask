
"""Python decorators são funções que vão dar funções adicionais às funções existentes.
Em Python as funções são objetos de primeiro classe, o que significa que elas podem ser passadas como argumentos, como
 int/string/float...
Abaixo está uma função Python Decorator criada com argumentos (args)
 e keywords as argumentos (kwargs), indefinidos. A ideia aqui é que o usuário só vai poder acessar o sistema se estiver
  autenticado. Primeiro foi criada uma super classe User, com apenas dois argumentos, o nome e a informação se está logado.
Depois, a função is_authenticated_decorator(reparar como o nome é auto-explicativo), recebe como argumento a função  que
 depois usará a própria função mas como python decorator, então, a função wrapper recebe *args e **kwargs, ou seja,
   deixa em aberto o número de argumentos que serão recebidos, a lógica é que caso sejam atribuídos mais argumentos
   a função continue funcionando, então o if usa a posição zero, que é o args, e atribui true como condição, ou seja
   , a  função (function(args[0]) será executada se essa condição for atingida. Por fim, é retornada a própria função.
 Então, a função  is_authenticated_decorator é passada como Python Autenticator para a função create_blog_post,
  que recebe apenas um nome de usuário como argumento e apenas imprime uma mensagem, no entanto, para que essa mensagem
   seja impressa é preciso as três variávei finais, a criação do user, e que a condição .is_logged_in seja true.
    Por fim, a função é chamada usando o new_user como argumento. Resumindo, a ideia é que a função create_blog_post
     só seja executada se a função Python Decorator for executada."""
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
from flask import Flask
"""na continuidade do entendimento de como criar funções de python decorators dentro do flask, foram
criadas várias funções a serem aplicadas no site, conforme sintaxe abaixo. A explicação foi dada no código anterior."""
app = Flask(__name__)

#Decorators to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
"""aqui a função hello_world, vai voltar o texto abaixo e um gif no site abaixo"""
@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'

"""aqui serão aplicadas todas as funções acima, ou seja, para deixar o texto em italico, negrito e sublinhado,
 quando a rota do site for alterada para /bye. Lembrando que o id do site é criada quando damos o play no código."""
#Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

"""esse if é um padrão para garantir que o flask está rodando e só assim será rodado...algo assim...o site rodará no 
modo debug, ou seja, facilitando para debugar e auto atualizando qualquer alteração"""
if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)

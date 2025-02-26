# Herencia
## Descripcion general 🚀
Para entender debesmos saber que es una herencia permite crear nuevas clases basadas en clases existentes. En otras palabras, una clase (llamada subclase o clase hija) puede heredar atributos y métodos de otra clase (llamada superclase o clase padre) en este ejemplo aplicaremos la herencia simple y la herencia multiple.
## Explicacion de Herencia simple
En la herencia simple tenemos un superclase llamada Vehiculo que tiene dos funciones:
```
def arrancar(self):
        pass
    def parar(self):
        pass
```
Aqui la "pass" es una operacion nula o sea que pase nada cuando se ejecute. 
Ahora en nuestra clase hija (Carro(Vehiculo) heredamos de la superclase (Vehiculo) ambos metodos, pero esta vez si retornamos argumentos:
```
 def arrancar(self):
        return "El carro está arrancando"
    def parar(self):
        return "El carro se ha detenido"
```
## Ejecutando las pruebas ⚙️
En el archivo "main.py" (programa principal) se debe importar la clase Carro para hacer uso de ella:
```
from carro import Carro
salida=Carro()
print(salida.arrancar())
print(salida.parar()) 
```
En el terminal deberia verse asi y estara funcionando correctamente nuestra clase con herencia
```
El carro está arrancando
El carro se ha detenido
```
## Herencia multiple
En este ejemplo tenemos dos clases que serian Volardor con un metodo volar que retorna "Volando en el aire"
```
def volar(self):
        return "Volando en el aire"
```
Ademas tenemos una clase Navegable que tiene un metodo navegar que retorna "Navegando en el agua"
```
def navegar(self):
        return "Navegando en el agua"
```
Ahora entra en accion nuestra clase Hidroavion(Volador,Navegable) que esta ahora hereda de mis clases Volador y Navegable es aqui donde se aplica la herencia multiple, ya que hereda de dos clases diferentes. 
```
def navegar(self):
        return super().navegar()
    def volar(self):
        return super().volar()
```
"return super()" lo que hace es acceder al metodo de la clase que queramos. 
En el "main.py" importamos a Hidroavion para hacer uso de el y ver como funciona en la terminal: 
```
from hidroavion import Hidroavion
```
Creamos el objeto y finalmente imprimomos ambos metodos, el resultado deberia verse asi:
```
Navegando en el agua
Volando en el aire
```
## Autora✒️
Norkys Peña

## Gratitud 🎁
Si deseas apoyar siguenos y comenta por alguna duda. Aceptamos donaciones $$ 🤑

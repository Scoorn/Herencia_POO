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
En el terminal deberia verse asi 
```
El carro está arrancando
El carro se ha detenido
```

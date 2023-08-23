# Trading-Simulation SECUENCIAL
### Antonio Carmona Arango
### Andrés Felipe Tellez Rodriguez
### Sara María Castrillón Ríos

## Profesor: 
### José Luis Montoya Pareja
### jmontoya@eafit.edu.co

## Comandos de ejecucion:
### Secuaencial: 
### python simtrading.py -p= < PERIODO > -f= < FORMATO > -m= < MONEDA >
### Ejemplo: python simtrading.py -p=H1 -f=CSV -m=BRENTCMDUSD
### Paralelo-proceso-lectura: 
### python simtrading.py -p= < PERIODO > -f= < FORMATO > -m= < MONEDA >
### Paralelo-proceso-visualización: 
### python Vizualizer.py 


#### Objetivo del proyecto:

El trading es una actividad que requiere de alto poder de cómputo y de altos 
tiempos de respuesta. Es primordial que los tiempos de respuesta y el 
procesamiento de tareas sea casi en tiempo real. Simular el funcionamiento del 
mercado de Trading permite tener una vista de los problemas donde pueden 
aplicarse los conceptos que se verán en el curso de sistemas operativos 
durante el semestre.

# ENTREGA 1:

## ¿Cómo funciona?:

La primera entrega del proyecto está dividida en dos partes. Por un lado está la carpeta secuencial, el cual recive los datos de las velas que debe graficar a través de un json o un csv. Almacena cada linea leida en un array para luego graficarlas y calcular el promedio movil, haciendo una simulación en tiempo real.

Por otra parte tenemos una version paralela, la cual funciona a través de sockets con una arquitectura tipo Cliente/Servidor. Donde dividimos nuestros procesos en dos y cada uno se encarga de uno de ellos; La lectura de los datos, y la visualización. El proceso de lectura se encarga de leer 10 lineas del archivo y  almacerlas en una estructura de datos que luego será enviada al proceso visualizar a traves de sockets; Este proceso las empezará a mostrar en pantalla mientras que el proceso de lectura se encarga de leer otras 10 lineas y luego enviarlas. Esta versión no está funcionando de la manera esperada por el momento.

## Dificultades y Posibles Mejoras:

Nuestra mayor difucultad a la hora de llevar a cabo la entrega 1, fue la implementación de los sockets y la forma en la que almacenamos los datos después de que son enviados de un proceso a otro. Por lo que hemos pensado, para la entrega 2 cambiar un poco la arquitectura y utilizar un middleware que nos ayude en este aspecto.

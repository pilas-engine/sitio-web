---
draft: false
autor: Martín Carrión, Rodolfo Emiliano
fecha: 3 de Mayo 2020
aliases: 
  - /tutoriales/monos.html
---

# Disparar a Monos

Uno de los ejemplos que posee Pilas Engine, es el proyecto `disparar_a_monos`,
que brinda al usuario una perspectiva general de lo que se puede hacer. En este
tutorial desarrollaremos este proyecto, de modo que cualquier usuario sepa cómo
llevarlo a cabo y pueda modificarlo a gusto.

![](captura-00001.png)


Disparar a monos es un juego que consiste en que el jugador controla una torreta que debe
disparar a los monos, los cuales se generan al azar en la pantalla, que intentan llegar a ella para
destruirla. En la pantalla de juego se puede ver un marcador de puntuación, un sistema de bonus y
los actores principales del juego.

Los sonidos e imágenes son recursos que están incorporados en Pilas, así que podemos utilizarlos
y no necesitamos añadir ningún recurso extra.


Empecemos por abrir el editor de Pilas. Vamos a borrar los actores que tengamos inicialmente
para tener un escenario limpio y comenzar a trabajar.

![](captura-00002.png)

Ahora vamos a configurar el escenario de juego, el cual contiene un fondo (que puede ser el que
queramos) y el marcador de puntos. 

Podemos darle un nombre al escenario y seleccionar un fondo para el mismo. Para eso
seleccionamos la escena1 y vamos a modificar sus atributos.

![](captura-00003.png)


En este caso, llamaremos a la escena “escena_cesped” y seleccionaremos un fondo con césped para
darle ambiente a nuestro juego.

![](captura-00004.png)



![](captura-00005.png)



![](captura-00006.png)

Al hacer esto veremos que Pilas crea al actor seleccionado con su correspondiente código, por lo
que ya tenemos un contador de puntos para nuestro juego. Ahora podemos posicionarlo donde creamos
más conveniente, y también modificar el texto mostrado cambiando la línea marcada en la imagen. A
modo de ejemplo, lo pondremos en una esquina y haremos que su texto diga “Score: 0”. Esto se verá
reflejado cuando ejecutemos el juego.

![](captura-00007.png)

Una vez que tenemos listo el escenario es hora de crear a los actores principales, que son la
torreta, los monos que intentan destruirla, y los láseres que la torreta dispara a los monos para
evitar que lleguen a ella.

<h2>Creación del actor “laser”</h2>

Para empezar, crearemos un actor láser. Una persona puede preferir empezar por crear la torreta,
que es nuestro protagonista, pero el láser es necesario para crearla ya que tendremos que hacer que
la torreta dispare este láser, y para eso necesitamos tenerlo creado.

Vamos a la creación de actores, y podemos ver que el láser es un actor predefinido de Pilas, por
lo que vamos a seleccionarlo.

Luego de esto, vamos a cambiar algunos de sus atributos, lo cuales quedan de la siguiente
manera.

![](captura-00008.png)

Como podemos ver, el láser es un actor dinámico y su figura es un rectángulo. Los valores de
ancho y alto de su figura pueden ajustarse según sea necesario. También es un actor inactivo, ya
que no queremos que aparezca en todo momento en el juego.



![](captura-00009.png)



![](captura-00010.png)



<ul>
  <li>iniciar() setea los atributos del láser cuando este es creado, y también reproduce un sonido.</li>

  <li>actualizar() se encarga de que en cada momento el láser avance, manteniendo su dirección.
  Eventualmente el láser llegará al final de la pantalla, o a colisionar con un mono.  (1) se
  encarga de la primera situación, haciendo que, si el láser llega al borde de la pantalla, se
  elimine, ya que no tiene sentido que continúe su camino.</li>

</ul>


La segunda situación será analizada más adelante, por ahora nos interesa que la torreta pueda
disparar estos láseres.

<h2>Creación del actor “torreta”</h2>

Lo primero que haremos, es crear un actor en blanco y modificar sus atributos como hicimos con
el láser, colocándole una etiqueta y asignándole la imagen de una torreta. Es importante mencionar
que la torreta es un actor activo.

![](captura-00011.png)

Ahora, le vamos a dar figura de círculo y ajustamos su radio al tamaño deseado. También
indicamos que es un actor dinámico.

![](captura-00012.png)


Una vez creado el actor y seteados sus atributos, debemos darle comportamiento. En este juego la
torreta tiene una posición fija, por lo que su única forma de movimiento es rotar. Buscaremos hacer
que rote al presionar las flechas de dirección del teclado, izquierda y derecha, según el sentido
en que corresponda. Además, la torreta puede disparar, por lo que vamos a utilizar el actor “laser”
que ya tenemos creado. Analicemos el siguiente código:

![](captura-00013.png)

Además de las variables inicializadas al principio del código, que sirven para controlar cuantos
grados gira la torreta cada vez que realizamos una acción (velocidad) y cada cuanto tiempo se nos
permite disparar un láser (cuadros), tenemos los métodos iniciar() y actualizar().

iniciar() no hace gran cosa en el caso de la torreta, solo le da el valor 0 a la variable
cuadros, lo que la deja lista para empezar a controlar la velocidad de disparo.



<ol>

  <li>Como la torreta es un objeto dinámico, normalmente caería, por lo que necesitamos que estas
  líneas se ejecuten en cada momento para mantenerla fija.</li>

  <li>Al presionar ‘espacio’ la torreta debe disparar, pero si no controlamos la velocidad con la
  que ejecuta estos disparos, lo haría demasiado rápido y el juego no sería desafiante, volviéndose
  incluso aburrido. Por esta razón existe la variable ‘cuadros’, que es un acumulador que permite
  disparar una vez cuando llega a cierto valor, volviendo a valer cero luego del disparo. Así,
  podemos controlar si la torreta deberá esperar 3 segundos antes de ejecutar el siguiente disparo,
  o si deberá esperar sólo 1, por ejemplo. Podemos hacer variar ‘cuadros’ haciendo pruebas hasta
  lograr una velocidad que consideremos adecuada.

  Por otro lado, el actor laser, será clonado cada vez que se dispare. Pero no sería realista
  que el láser se dispare hacia cualquier lado, por lo que lo posicionamos en el lugar donde se
  encuentra la torreta y con la rotación que tiene la torreta. Pero hay un problema, ya que la
  torreta inicialmente “mira” hacia arriba, y el láser sin rotar mira hacia su derecha, por lo
  que siempre saldría por ese lado de la torreta, lo cual no tiene sentido. En otras palabras, si
  giramos la torreta, el láser seguirá saliendo por su derecha siempre, así que podemos
  solucionar este problema rotando 90 grados el láser. Para esto tomamos la rotación actual de la
  torreta (que son los grados que rotó) y le sumamos 90 grados.
  </li>

  <li>Al presionar las teclas de dirección del teclado izquierda y derecha, la torreta debe girar
  hacia el sentido correspondiente. Para esto, utilizamos la variable ‘velocidad’ que definimos al
  principio, sumándola a la rotación actual de la torreta. De esta forma la torreta gira, sólo
  debemos buscar un valor adecuado para su velocidad de giro.</li>

</ol>

## Creación del actor “mono”




![](captura-00014.png)

![](captura-00015.png)







![](captura-00016.png)

El método iniciar() controla los lugares donde aparecen los monos. Lo más realista y desafiante
es que aparezcan en cualquier ubicación aleatoria, pero como sería muy injusto que aparezcan al
lado de la torreta, ya que el juego se volvería imposible, vamos a controlar que no aparezcan
demasiado cerca de ella. Si el método azar() de Pilas hace aparecer al mono demasiado cerca de la
torreta, este será reposicionado dependiendo de donde haya aparecido.

![](captura-00017.png)

El método actualizar() se encarga de controlar el movimiento del mono. Al ser el enemigo
principal, buscará acercarse a la torreta. Este fragmento de código se basa principalmente en eso,
en controlar que el mono, donde sea que esté, se acerque a la torreta en cada momento. La velocidad
del mono puede ser modificada como se quiera para controlar la dificultad que tendrá el juego.

## Colisiones


En este punto tenemos la torreta, los láseres que dispara, y los monos que quieren destruirla.
Pero actualmente no sucede nada cuando los monos llegan a la torreta ni cuando los láseres tocan a
los monos. Vamos a darle la esencia a nuestro juego haciendo que cada colisión que se produzca
tenga consecuencias dependiendo de qué actores sean los que colisionan.

Primero, vamos a hacer que los monos puedan destruir nuestra torreta. Para esto vamos a torreta,
y en “Recetas” seleccionamos lo siguiente. 

![](captura-00018.png)



![](captura-00019.png)

De esto, nos interesa mantener el método, pero modificar el código de adentro. Vamos a
modificarlo de la siguiente manera. 

![](captura-00020.png)

Si el actor que colisiona con la torreta posee la etiqueta “mono”, la torreta se destruye (el
actor torreta es eliminado).

Además, podemos ver que en (1) hay dos líneas de código que clonan actores que no tenemos
creados, lo cuales son “explosion” y “reiniciar_escena”. Estos actores son de apoyo para darle
realismo al juego y para poder reiniciar la escena si un mono toca la torreta (perdemos), así que
vamos a crearlos.

## Creación del actor “explosion”

Para mostrarle al jugador que perdió de una forma más impactante, podemos hacer que la torreta
“explote” cuando es tocada por un mono. Para esto creamos un actor en blanco con los siguientes
atributos. 

![](captura-00021.png)

![](captura-00022.png)





![](captura-00023.png)

Lo único que hace es reproducir un sonido cuando la explosión es creada. El resto del trabajo
está hecho en el método cuando_empieza_una_colision() de torreta. Este método clona al actor
explosión luego de eliminar la torreta. 

## Creación del actor “reiniciar_escena”

Luego de que el jugador pierde, es lógico tener un botón que permita reiniciar el juego para
volver a jugar. Para hacer esto creamos un actor predefinido “reiniciar_escena”. Este actor debe
poseer los siguientes atributos.

![](captura-00024.png)

Podemos ver que, igual que explosión, es un actor no activo. Además, podemos modificar algunos
atributos según creamos conveniente.



![](captura-00025.png)

Ahora, el método cuando_empieza_una_colision() de torreta, se encarga de clonar este actor
cuando la torreta es eliminada por un mono.

## Volvamos a las colisiones

En este punto, los monos pueden destruir a nuestra torreta, pero no podemos defendernos de ellos
porque nuestros láseres no les hacen nada.

Vamos a hacer entonces que, al colisionar un láser con un mono, el mono sea eliminado. Para eso
agregamos el siguiente fragmento de código en el actor “laser”, el cual es muy similar al utilizado
en “torreta”.

![](captura-00026.png)



De esta forma nuestro juego ya funciona completamente. Los monos aparecen aleatoriamente y la
torreta puede defenderse de ellos. 


## Creación del actor “banana”

Si quisiéramos darle más diversión a nuestro juego, y que sea más desafiante para el usuario,
podemos agregar un sistema de bonus. En este caso, podemos utilizar bananas que, al ser destruidas
por un láser de la torreta, sumen puntos al jugador. 



![](captura-00027.png)

![](captura-00028.png)

![](captura-00029.png)

Al iniciar, las bananas aparecen en la parte superior de la pantalla y comienzan a caer rotando.
Entonces el jugador, además de defenderse de los monos, tendrá el objetivo de destruir sus bananas
para sumar una mayor cantidad de puntos. Pero para que el actor láser pueda destruir a las bananas
al colisionar con ellas, debemos agregar un fragmento de código en el método
cuando_comienza_una_colision() del actor actor láser.

![](captura-00030.png)

El fragmento de código agregado es el que está marcado en rojo. Si el actor con el que el láser
colisionó es una banana, la destruye y aumenta el puntaje del jugador en 3. Además, reproduce el
sonido de una moneda de forma que sea más notorio para el jugador que ganó una cantidad mayor de
puntos por destruir una banana.

En este punto tenemos terminado nuestro juego de “Disparar a monos” en Pilas Engine. Lo que
resta hacer es adaptarlo como se desee, y ¡jugar!

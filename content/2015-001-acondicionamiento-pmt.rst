:title: Microscopio de Fluorescencia. Puesta en marcha y ajustes.
:date: 2015-05-13 10:00
:category: hardware
:tags: microscopios, electronica,
:author: Diego Fainstein
:excerpt: Reparación y reemplazo de un canal de acondicionamiento para tubos fotomultiplicadores.

Basado en un microscopio `Nikon Diaphot 200`_ se encuentra montado un
sistema para medir fluorescencia con un sistema de filtros y espejos,
y como detectores dos tubos fotomultiplicadores.

.. _Nikon Diaphot 200: {attach}/pdfs/diaphot-2-im.pdf

Conexiones
----------

Algunas conexiones se encontraban visiblemente en mal estado (**PONER
FOTO**). Parece necesario reemplazar fichas BNC y mejorar algunas
secciones de cables.

Lámpara de posicionamiento
--------------------------

La iluminación está alimentada con una fuente Nikon (12V/100W)
conectada al transformador de 220V/110V. Según el manual los repuestos
admisibles son:

- `OSRAM HLX64623`_
- PHILIPS 7724

En Mercado Libre venden la `OSRAM HLX64625`_ a $90. Si bien ésta última
emite más intensidad (3600 lm vs 2800 lm) tiene mucho menor vida útil
(50 hs vs 2000 hs).

Sin embargo no hubo necesidad de cambiar la lámpara porque luego de
desarmar la fuente y volverla a armar prendió sin problemas. El
fusible interno estaba bien, no se veía nada quemado. Quizás la tecla
de encendido haya fallado por la falta de uso (pude limpiarla por
fuera y chequear con el tester que andaba bien).

  .. _OSRAM HLX64623: {attach}/pdfs/lamp-bipin-osram-hlx64623.pdf
  .. _OSRAM HLX64625: {attach}/pdfs/lamp-bipin-osram-hlx64625.pdf

Relevamiento del sistema de adquisición
---------------------------------------

Los tubos fotomultiplicadores (PMT) atraviesan un circuito de
construcción casera, sin documentación sobre su esquema de
funcionamiento. El relevamiento indica que los bloques que lo componen
son: conversor VI (amplificador de transimpedancia), ajuste de offset
(amplificador sumador), control de ganancia (amplificador inversor),
y filtro pasabajos. La plaqueta cuenta con dos canales e incluso hay
una porción con componentes soldados que no cumplen ninguna función
(están desconectados del resto del circuito).

Camino óptico
-------------

Embutidos en un gabinete metálico se encuentran los PMT con filtros de
distinta longitud de onda en cada uno de los dos caminos ópticos. Los
PMT pueden extraerse con facilidad desajustando pocos tornillos. No
está marcado cuál filtro se encuentra en cada uno de los dos
receptáculos (ni cual es el ancho de banda), así que debieron hacerse
pruebas para determinar cuál PMT conectar al canal 1 y al canal 2 (hay
que fijar por cuál va la luz de 410 nm y por cuál la de 490 nm).

Conversor I-V y acondicionador de señal
---------------------------------------

El dispositivo que sigue al PMT puede verse en la figura siguiente
(con la inscripción "Conversor I/V Ca"):

.. image:: https://farm8.staticflickr.com/7702/17567473871_23a03ab290_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: conversor v-i

Dentro del gabinete hay una plaqueta de construcción casera, con
sectores vacíos y también con elementos que están soldados pero no son
realmente utilizados (un operacional, resistencias que cambiarían la
frecuencia de corte de los filtros, etc). Hay conexiones que apenas se
sostienen en un hilo y pistas reparadas con alambres, da la sensación
de ser un prototipo que nunca llegó a convertirse en producto final.

.. image:: https://farm9.staticflickr.com/8861/17567754575_c6224b1717_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: plaqueta del conversor v-i

Al relevar el circuito quedó el siguiente diagrama (se puede ver mejor
en el `pdf`_):

.. image:: https://farm6.staticflickr.com/5347/17380806690_1e42f94856_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: circuito de la plaqueta anterior

En la imagen siguiente están marcadas las referencias para permitir
identificar a los componentes de los distintos bloques del circuito
(ampliar el `pdf`_ para verlo mejor):

.. image:: https://farm8.staticflickr.com/7681/17568608281_168ab26b5e_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: conversor con referencias

.. _pdf: {attach}/pdfs/conversor-corriente-voltaje-original.pdf

Los dos filtros cortan cerca alrededor de los 10 Hz, comprobado de
acuerdo a los valores de los componentes relevados usando el simulador
de la página `Sallen-Key Low-pass Filter Design Tool`_, y también
midiendo frente a una senoidal de entrada que en la banda de paso
provoca una salida de 10V:

.. csv-table:: Respuesta en frecuencia
   :header: "Frecuencia [Hz]", "Salida [V]"
   :widths: 5, 10

   1, 10
   4, 10
   5, 9.92
   7, 9.60
   9, 7.76
   10, 6.40
   11, 4.88
   12, 3.68
   13, 2.80
   14, 2.16
   15, 1.68
   20, 0.52
   30, 0.11
   50, 0.02

Como puede apreciarse en la tabla, la frecuencia de corte
correspondiente a la atenuación del 70,7% (los 3 dB en un filtro de
1er orden) se encuentra en algún lugar entre los 9 y los 10 Hz.

Se diseñó otra plaqueta para reemplazar la existente, reemplazando el
control de offset para construirlo con un amplificador de
instrumentación (en vez del sumador inversor respecto del cual tiene
mejor RRMC), se ubicó un filtro pasabajos en la salida para usarlo
como anti-aliasing y se eliminó el inversor de ganancia unitaria en la
salida. También se agregaron jumpers para permitir la prueba de los
bloques por separado en caso de falla. Para permitir la construcción
en una plaqueta de una sola cara se agregaron un par de resistencias El
circuito quedó como en la figura siguiente (también se puede ver mejor
en `este pdf`_):

.. image:: https://farm6.staticflickr.com/5333/17414354658_a65f621c72_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: canal de acondicionamiento nuevo

Se ilustra a continuación el diseño de la plaqueta (de una sola cara)
junto con una vista simulada de la misma (aunque no se ven los
potenciómetros ni los reguladores):

.. image:: https://farm6.staticflickr.com/5325/17576797956_2bb0dcf75b_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: plaqueta


.. _Sallen-Key Low-pass Filter Design Tool: http://sim.okawa-denshi.jp/en/OPseikiLowkeisan.htm
.. _este pdf: {attach}/pdfs/canal-acondicionamiento-para-pmt-nuevo.pdf

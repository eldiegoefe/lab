:title: Instalación de IPython Notebook
:date: 2015-04-15 10:00
:category: software
:tags: python, ipython, instalacion
:author: Diego Fainstein
:excerpt: instalacion de ipython notebook
:disqus_identifier: instalacion de ipython notebook

Se puede instalar el IPython Notebook muy facilmente siguiendo las
instrucciones de su página web. Sin embargo suelen necesitarse
algunas librerías para graficar, trabajar con matrices, aplicar
filtros, etc. Estas librerías van evolucionando y pueden aparecen problemas
de compatibilidad, si nuestro código no va corrigiendo las
diferencias. Para evitar esto se puede instalar el ipython notebook en
un entorno virtual donde tanto el python como las librerías se
actualicen sólo cuando deliberadamente lo querramos hacer.

Suponiendo que ya están instaladas las aplicaciones python-pip,
virtualenv y virtualenvwrapper, la instalación del ipython notebook
implica:

#. Decidir si el entorno virtual funcionará con Python 2 o Python 3.
#. Buscar la ruta a la versión elegida de Python:

   .. code-block:: console

      $ which python2
      /usr/bin/python2

   .. code-block:: console

      $ which python3
      /usr/bin/python3

#. Crear un entorno con la versión elegida (en este caso el 3):

   .. code-block:: console

      $ mkvirtualenv --python=/usr/bin/python3 nombreDelEntorno

#. Paquetes instalados. Una vez que la orden anterior se completa, el
   entorno virtual recién instalado se activa. El prompt del terminal
   utilizado debe mostrar **nombreDelEntorno** como prefijo. La lista
   de paquetes instalados es exigua:

   .. code-block:: console

      (nombreDelEntorno)$ pip list
      pip (6.1.1)
      setuptools (15.0)

#. Si por algún motivo no se activó, o si luego de reiniciar la
   computadora se desea activar nuevamente el entorno virtual, se
   corren los siguientes comandos:

   .. code-block:: console

       $ source /usr/local/bin/virtualenvwrapper.sh
       $ workon
       lista de entornos existentes
       $ workon nombreDelEntorno
       (nombreDelEntorno)$

   Si la ruta a virtualenvwrapper.sh es desconocida por el usuario, se
   puede averiguar dónde se encuentra instalada con:

   .. code-block:: console

      $ which virtualenvwrapper

#. Instalar el IPython Notebook (no usar "sudo" porque lo instalaría
   en el sistema general en vez de hacerlo en el entorno virtual):

   .. code-block:: console

      (nombreDelEntorno)$ pip install "ipython[notebook]"

   Luego de la instalación, la lista de paquetes instalados es esta:

   .. code-block:: console

      (nombreDelEntorno)$ pip list
      certifi (2015.4.28)
      ipython (3.1.0)
      Jinja2 (2.7.3)
      jsonschema (2.4.0)
      MarkupSafe (0.23)
      mistune (0.5.1)
      pip (6.1.1)
      ptyprocess (0.4)
      Pygments (2.0.2)
      pyzmq (14.6.0)
      setuptools (15.0)
      terminado (0.5)
      tornado (4.1)

#. Probar la ejecución

   .. code-block:: console

      (nombreDelEntorno)$ ipython notebook

   Debe abrirse una ventana del navegador y mostrar la pantalla
   principal del Jupyter. Todavía falta instalar librerías casi
   imprescindibles.

#. Instalación de librerías. Hay librerías que son muy utilizadas para
   realizar cálculos, operar con matrices, etc. Mi recomendación es
   instalar las siguientes (la opción -v sirve para que el instalador
   vaya imprimiendo mensajes durante la instalación, lo cual es
   recomendable porque hay paquetes como scipy que tardan mucho en
   instalarse y si no emiten mensajes parece colgado):

   .. code-block:: console

      (nombreDelEntorno)$ pip install numpy -v
      (nombreDelEntorno)$ pip install scipy -v
      (nombreDelEntorno)$ pip install matplotlib -v
      (nombreDelEntorno)$ pip install networkx -v
      (nombreDelEntorno)$ pip install pillow -v
      (nombreDelEntorno)$ pip install scikit-image -v
      (nombreDelEntorno)$ pip install scikit-learn -v
      (nombreDelEntorno)$ pip install pandas -v

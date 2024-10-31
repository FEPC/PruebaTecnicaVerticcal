# PruebaTecnicaVerticcal
1. Descripción del Proyecto<br>
El proyecto se divide en 2 secciones basado en los puntos establecidos en la prueba, el primer punto es resuelto en el archivo "ConsumoAPI.py", el segundo en el archivo "CreacionAPI.py" y el cuarto en el archivo "ManipulaciónDatos.py".<br>
2. Clonación de repositorio<br>
Para clonar el repositorio se necesita seguir los siguientes pasos.<br>
   2.1. Ir a la ubicación donde se desea tener la carpeta del proyecto<br>
   2.2. Abrir CDM o GitBash desde esa ubicación<br>
   2.3. Escribir las siguientes lineas de código: git clone https://github.com/FEPC/PruebaTecnicaVerticcal.git<br>
3. Instalación de dependencias<br>
En este proyecto se usaron 2 librerias (Requests, Flask), acontinuación se enlistara detalladamente cada paso para instalar ambas<br>
   3.1. Requests<br>
        2.1.1. Abrir CMD<br>
        2.1.2. Ejecutar el siguiente comando: pip install requests<br>
   3.2. Flask<br>
        2.1.1. Abrir CMD<br>
        2.1.2. Ejecutar el siguiente comando: pip install Flask<br>
4. Ejecución Local<br>
   4.1. ConsumoAPI:<br>
   La aplicación busca los datos de determinado pokemon en PokeAPI, trayendo la altura, peso, nombre y tipo del pokemon que se este buscando
   Para la ejecución local se puede hacer a travez del CMD, siguiendo los pasos mostrados acontinuación:<br>
        4.1.1. Ejecutar directamente desde Python (F5)<br>
   4.2. CreacionAPI:<br>
   La aplicación busca los datos de determinado pokemon en PokeAPI, trayendo la altura, peso, nombre y tipo del pokemon que se este buscando, tambien filtra los pokemon por  tipo, mostrando el nombre y la forma de encontrarlo.<br>
        4.2.1. Abrir CMD en la carpeta donde se encuentra la aplicación<br>
        4.2.2. Ejecutar el siguiente comando: python CreacionAPI.py<br>
        4.2.3. Para hacer la consulta se uso la extención TalentAPI Tester<br>
        4.2.4. Ejecutar el siguiente comando: http://127.0.0.1:5000/api/nombre/{Nombre del pokemon} //Para obtener la información de un pokemon<br>
        4.2.5. Ejecutar el siguiente comando: http://127.0.0.1:5000/filtroTipo (Json: {type: Tipo que se desea buscar})//Para obtener la lista de los pokemon de ese tipo y su forma de encontar<br>
   4.3. ManipulaciónDatos:<br>
        4.3.1. Ejecutar directamente desde Python (F5)<br>
        4.3.2. Para hacer el filtro por lugar escribir la siguiente linea de código: filtrado({Lugar que se desea filtrar}) //Tener en cuenta las tildes<br>
        4.3.3. Para hacer la sumatoria de los presupuestos basado en el filtro escribir la siguiente linea de código: sumatoria({Lugar que se desea filtrar}) //Tener en cuenta las tildes<br>
        4.3.4. Para ordenar los leads escribir la siguiente linea de código: ordenar()<br>
5. Ejemplo de Endpoints<br>
   5.1. Busqueda de un pokemon
   ![image](https://github.com/FEPC/PruebaTecnicaVerticcal/blob/main/Ejemplo/Comando%20para%20la%20busqueda%20de%20un%20Pokemon.jpg)
   5.2. Resultado del pokemon (Mewtwo)
   ![image](https://github.com/FEPC/PruebaTecnicaVerticcal/blob/main/Ejemplo/Resultado%20para%20la%20busqueda%20de%20Mewtwo.jpg)
   5.3. Busqueda de tipo
   ![image](https://github.com/FEPC/PruebaTecnicaVerticcal/blob/main/Ejemplo/Comando%20para%20la%20busqueda%20de%20un%20tipo.jpg)
   5.4. Resultado de la busqueda de tipo (Fuego)
   ![image](https://github.com/FEPC/PruebaTecnicaVerticcal/blob/main/Ejemplo/Resultado%20para%20la%20busqueda%20del%20tipo%20fuego.jpg)
   
    
   

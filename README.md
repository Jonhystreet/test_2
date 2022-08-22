Directorio de restaurantes

***
Agregado de usuario y de restaurante

Se implemento un formulario en html y se uso un metodo post para obtener la informacion y dar de alta
tanto en los usuarios como en los restaurantes

/form_usu 

/alta_usu


/form_restaurant

/alta_res



***
Visualizacion del restaurante

Se uso sycopg2 y se extrae toda la informacion y se coloca en columnas con cabezeras con todos los datos


/v_restaurant



***
Eliminacion de restaurante

Se especifica el nombre del restarante y se elimina ya que esta actua como llave primaria, igual se hace un
formulario para especificar que restaurante eliminar

/form_elim_res  


/baja_re

***

Actualizacion

Se especifica el nombre del restaurante a actualizar y se procede a actualizar

/form_act_res


/act_res


***
#Requerimentos
Librerias:


-sycopg2


-flask_sqlalchemy


-flask


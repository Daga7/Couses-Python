Al hacerle pruebas a nuestro software podemos detectasr errores antes de lanzar nuestro software a produccion 

TIPOS DE PRUEBA
    **Pruebas Unitarias**
     Se encargan de validar que cada componente pequeño del código funcione correctamente de manera aislada.
    **Pruebas de Integracion**
     Verifican que los distintos componentes trabajen bien en conjunto, evitando problemas en la interacción de partes.
    **Pruebas Funcionales**
     Validan que el sistema en su totalidad funcione como se espera según los requisitos
    **Pruebas de Rendimiento**
     Aseguran que el software sea rápido y eficiente, evaluando su comportamiento bajo diferentes condiciones de carga
    **Pruebas de Aceptacion**
     Determinan si el software cumple con las expectativas del usuario final

HERRAMIENTAS DE TESTING
    **UnitTest**
    Permite crear pruebas unitarias de manera sencilla, asegurando que todas las partes del código realicen su función correctamente.
    **PyTest**
    Facilita la creación de pruebas con una configuración avanzada para cubrir diferentes escenarios.
    **DocTest**
    Integra pruebas directamente en los comentarios de las funciones, permitiendo validar el código mientras se mantiene la documentación.
    **Coverage**
    Nos permite ver en un reporte  en html cuales son las lineas de codigo que no hemos validado 


Pruebas Manuales 
¿Qué son las pruebas manuales y cómo funcionan?
Las pruebas manuales consisten en validar el funcionamiento de un cambio en el código mediante la interacción directa con la aplicación. Esto se hace, por ejemplo, al modificar una línea de código, ejecutar la aplicación y verificar si el cambio funciona correctamente. Es similar al trabajo de un mecánico que ajusta un auto y luego lo prueba encendiéndolo cada vez.

Pruebas Unitarias
Las pruebas unitarias permiten validar que pequeñas piezas de código, como funciones individuales, trabajan correctamente. En el ejemplo de un mecánico, esto sería como revisar solo un neumático: inflarlo, verificar que no tenga fugas y confirmar que esté en buen estado. En Python, estas pruebas se automatizan utilizando la palabra clave assert, que compara los resultados esperados con los reales.

Pruebas de integracion
Las pruebas de integración verifican que diferentes componentes de la aplicación funcionen en conjunto sin problemas. En el caso del mecánico, sería comprobar que el neumático instalado en el coche funcione bien con el resto de las piezas del vehículo. En desarrollo de software, esto se traduce a verificar, por ejemplo, que el proceso de inicio de sesión funcione correctamente, desde la entrada del usuario hasta la confirmación del acceso.

Automatizar pruebas 
Python ofrece herramientas para automatizar las pruebas, permitiendo ejecutar muchas validaciones rápidamente sin intervención manual. A través de pruebas automatizadas, podemos detectar errores que de otro modo podrían pasar desapercibidos y llegar a producción, como un fallo en el cálculo de una orden de compra. Esto es crítico para evitar situaciones como la que enfrentó CrowdStrike, donde un error no detectado en una actualización paralizó aeropuertos.
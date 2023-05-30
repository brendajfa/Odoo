### Configuración Inicial del proyecto  ###

Basada en : https://github.com/Tecnativa/docker-odoo-base/tree/scaffolding

	Configurar ./src/repos.yaml
	Configurar .src/addons.yml

	Descargamos la imagen base:
		- docker-compose build --pull

	Actualizamos los repos y actualizamos la carpeta final de addons:
		- docker-compose -f setup-devel.yaml run --rm odoo

	###  Desarrollo --> Arrancar el contenedor final: ###
		- docker-compose up

	###  Producción --> Arrancar el contenedor final: ###
		- ./production_up.sh

### Acceso a la instancia  ###

	El puerto, en entornos de desarrollo, se define según la versión de odoo:
		- v15: http://localhost:15069

	La opción PGDATABASE (que aparece tanto en prod.yaml como en docker-compose.yml) 
	define la base de datos que cargará el docker.

	Una vez restoreada la nueva BBDD hay que parar el docker y cambiar el valor de PGDATABASE

### Configuración de la instancia ###

Cambios y configuraciones a tener en cuenta cuando se crea una nueva instancia (GET OUT DEVELOPERS!)

	Realizar, mediante command en docker, un actualización de todos los módulos del sistema:
		command:
            - odoo
            - --update=all
import subprocess
import time

# Configurar la ruta al directorio del repositorio
repo_dir = './work.test'

while True:
    # Ejecutar el comando git pull en el directorio del repositorio
    result = subprocess.run(['git', 'pull'], cwd=repo_dir)

    # Comprobar si hubo algún error en la ejecución del comando git pull
    if result.returncode != 0:
        print('Error al ejecutar el comando git pull')

    # Esperar 12 horas antes de ejecutar el siguiente git pull
    time.sleep(3 * 60)
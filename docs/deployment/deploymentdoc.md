# Despliegue de modelos

## Infraestructura

- **Nombre del modelo: Predicción y clasificacion del indiece S&P500 segun su valor historico.
- **Plataforma de despliegue: mlFlow 
- **Requisitos técnicos:
  MLflow requiere Python 3.6 or posterior.
  Se recomienda usar un entorno virtual (virtualenv, conda)
  Instalar MLflow usando pip: pip install mlflow.
  Para carecteristicas adicionales como el soporte a scikit-learn y otras bibliotecas, instale con el comando: pip install mlflow[extras].
  
- **Requisitos de seguridad: Utilizar un token de autenticación ngrok y mlFlow para accerder.

- visualizar imagen para el diagrama de la arquitectura.

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:
  1. Clonar el repositorio del proyecto.
  2. Crear y activar un entorno virtual.
  3. Instalar las dependencias del proyecto.
  4. Instalar y configurar ngrok:
     -Descarga ngrok desde ngrok.com.
     -Extrae el archivo descargado y muévelo a una ubicación en tu PATH.
     -Autenticar  cuenta de ngrok
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
  1. Creación de cuenta
  2. Generación de token
  3. Lanzamiento del servidor 
  4. Configuracion del token 
  5. Conexion al servidor
  
- **Instrucciones de uso:
  1. Obtener la URL pública de ngrok
  2. Enviar solicitudes de predicción.
     
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)

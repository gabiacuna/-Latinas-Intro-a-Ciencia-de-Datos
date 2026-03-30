# Latinas

Material de trabajo en notebooks para un curso introductorio de ciencia de datos con Python.

La idea de este repositorio es que puedas abrir los notebooks en VS Code, instalar lo necesario y ejecutarlos localmente aunque tengas conocimientos muy basicos de Python.

## Que contiene este proyecto

Estos son los notebooks principales, en el orden recomendado:

1. `clase_01_ecosistema_y_tipos_de_datos.ipynb`
2. `clase_02_almacenamiento_y_exploracion.ipynb`
3. `clase_03_limpieza_y_preparacion.ipynb`

El proyecto usa Python `3.12` y estas librerias principales:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `ipykernel`
- `ydata-profiling`

## Requisitos previos

Antes de empezar, necesitas tener instalado:

1. `Python 3.12`
2. `VS Code`
3. Las extensiones de VS Code:
   - `Python`
   - `Jupyter`

## Opcion recomendada: setup con uv

Este proyecto ya trae archivos preparados para trabajar con `uv`, que es una herramienta moderna para crear el entorno virtual e instalar dependencias.

### 1. Instalar uv

Si no lo tienes instalado, puedes hacerlo con alguno de estos comandos:

En macOS o Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Si prefieres, tambien puedes revisar otras formas de instalacion aqui:
https://docs.astral.sh/uv/getting-started/installation/

### 2. Abrir el proyecto en VS Code

1. Abre VS Code.
2. Ve a `File > Open Folder`.
3. Selecciona esta carpeta del proyecto.

### 3. Crear el entorno e instalar dependencias

Abre una terminal dentro de VS Code y ejecuta:

```bash
uv sync
```

Ese comando hace dos cosas:

- crea el entorno virtual `.venv`
- instala las dependencias definidas en `pyproject.toml`

### 4. Seleccionar el interprete en VS Code

Cuando termine `uv sync`:

1. Presiona `Ctrl + Shift + P` o `Cmd + Shift + P`.
2. Busca `Python: Select Interpreter`.
3. Elige el interprete que apunte a `.venv`.

En general se va a ver parecido a uno de estos:

- `.venv/bin/python`
- `.venv\Scripts\python.exe`

### 5. Abrir un notebook y elegir kernel

1. Abre uno de los archivos `.ipynb`.
2. En la esquina superior derecha del notebook, haz click en `Select Kernel`.
3. Elige el kernel asociado al entorno `.venv`.

Como el proyecto ya incluye `ipykernel`, normalmente VS Code detecta ese kernel sin pasos extra.

### 6. Ejecutar el notebook

Puedes correr las celdas de dos formas:

- con `Shift + Enter`
- usando el boton `Run All`

Si quieres empezar por el camino mas simple, abre primero:

```text
clase_01_ecosistema_y_tipos_de_datos.ipynb
```

## Opcion alternativa: setup con venv + pip

Si no quieres usar `uv`, puedes trabajar con las herramientas clasicas de Python.

### 1. Crear entorno virtual

En macOS o Linux:

```bash
python3.12 -m venv .venv
```

En Windows PowerShell:

```powershell
py -3.12 -m venv .venv
```

### 2. Activar el entorno

En macOS o Linux:

```bash
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -e .
```

Si `pip install -e .` llegara a fallar por alguna razon, puedes probar:

```bash
pip install .
```

### 4. Volver a VS Code y seleccionar `.venv`

Despues de instalar, sigue los mismos pasos de:

- `Python: Select Interpreter`
- `Select Kernel`

## Flujo recomendado para una persona principiante

Si es tu primera vez trabajando con notebooks locales, este es un flujo seguro:

1. Instala `Python 3.12`.
2. Instala `VS Code` y las extensiones `Python` y `Jupyter`.
3. Abre este proyecto en VS Code.
4. Ejecuta `uv sync`.
5. Selecciona el interprete `.venv`.
6. Abre `clase_01_ecosistema_y_tipos_de_datos.ipynb`.
7. Ejecuta las celdas en orden, de arriba hacia abajo.

## Archivos que pueden aparecer al ejecutar notebooks

Al correr algunos notebooks pueden generarse archivos nuevos en esta misma carpeta, por ejemplo:

- archivos `.html` de reportes
- archivos `.csv` exportados

Eso es normal y forma parte del trabajo dentro del notebook.

## Problemas comunes

### VS Code no muestra el kernel correcto

Prueba esto:

1. Cierra y vuelve a abrir VS Code.
2. Repite `Python: Select Interpreter`.
3. Abre de nuevo el notebook y elige `Select Kernel`.

### El notebook dice que falta una libreria

Normalmente significa que el notebook no esta usando el entorno `.venv`.

Verifica:

1. que ejecutaste `uv sync` o la instalacion con `pip`
2. que el interprete activo sea `.venv`
3. que el kernel del notebook sea el mismo entorno

### Tengo otra version de Python

Este proyecto esta configurado para `Python 3.12`.

Si usas otra version, algunas dependencias pueden fallar o instalarse de forma incorrecta. Lo mejor es usar `3.12`.

## Comandos utiles

Ver version de Python:

```bash
python --version
```

Volver a instalar dependencias con `uv`:

```bash
uv sync
```

Activar entorno manualmente en macOS o Linux:

```bash
source .venv/bin/activate
```

## Resumen corto

Si quieres la version mas breve posible:

```bash
uv sync
```

Luego en VS Code:

1. selecciona `.venv` como interprete
2. abre un `.ipynb`
3. selecciona el kernel de `.venv`
4. ejecuta las celdas

## Estado actual del repo

El proyecto ya declara dependencias en `pyproject.toml` y fija Python `3.12`, asi que no deberias tener que instalar paquetes uno por uno.

## 🍄 Resumen del Dataset: Clasificación de Hongos (Mushroom Classification)

*url: https://www.kaggle.com/datasets/uciml/mushroom-classification*

Este archivo de metadatos sigue el formato **Croissant (v1.0)** y describe un conjunto de datos clásico utilizado para enseñar a las computadoras a distinguir entre hongos seguros y peligrosos.

### 📝 Información General
* **Nombre del Dataset:** Clasificación de Hongos (Mushroom Classification).
* **Nombre Alternativo:** ¿Seguro para comer o veneno mortal? (Safe to eat or deadly poison?).
* **Creador:** UCI Machine Learning.
* **Licencia:** Dominio Público (CC0: Public Domain).
* **Plataforma:** Hospedado originalmente en Kaggle.

### 🎯 Objetivo y Contexto
El objetivo principal es predecir si un hongo es **comestible** o **venenoso** basándose en sus características físicas. 
* Incluye descripciones de muestras hipotéticas de 23 especies de hongos de las familias *Agaricus* y *Lepiota*.
* Fue donado originalmente al repositorio de UCI en abril de 1987.
* **Nota de seguridad:** El conjunto de datos advierte explícitamente que no existe una regla simple (como la de la hiedra venenosa) para determinar si un hongo se puede comer; se requiere un análisis completo.

### 📂 Estructura de los Datos
Los datos se encuentran en un archivo llamado `mushrooms.csv`. El formato Croissant define 23 campos (columnas) clave, entre los que destacan:

| Campo | Descripción de ejemplo |
| :--- | :--- |
| **Clase (class)** | La etiqueta principal: comestible (e) o venenoso (p). |
| **Forma del sombrero** | Campana (b), cónico (c), convexo (x), plano (f), entre otros. |
| **Olor (odor)** | Almendra (a), anís (l), rancio (c), pescado (y), fétido (f), etc. |
| **Superficie del tallo** | Describe si es fibroso, escamoso, sedoso o liso. |
| **Hábitat** | Pastos (g), hojas (l), prados (m), senderos (p), urbano (u), bosque (d). |

### 🛠️ Detalles Técnicos para Desarrolladores
* **Formato de distribución:** Archivo ZIP que contiene un CSV.
* **Tipos de datos:** La mayoría de los campos son de tipo **Texto** (categóricos), aunque algunos como "moretones" (bruises) se identifican como **Booleanos**.
* **Palabras clave:** Incluye etiquetas de búsqueda relacionadas con biología, naturaleza, seguridad pública y sociedad.
# 🛒 E-commerce Data Cleaning & Reporting Automation Pipeline

Este proyecto automatiza el proceso de carga, limpieza, transformación, análisis y distribución de reportes de datos de e-commerce.

El objetivo principal es convertir datos “sucios” en información útil y estructurada para la toma de decisiones.

---

## 🚀 Funcionalidades

✔ Carga automática de múltiples archivos CSV  
✔ Selección y renombrado de columnas  
✔ Limpieza de precios y descuentos  
✔ Eliminación de valores nulos y duplicados  
✔ Transformación y segmentación de datos  
✔ Generación de resumen analítico  
✔ Exportación automática a Excel  
✔ Integración con OneDrive  
✔ Automatización de envío de reportes por correo con Power Automate  

---

## 🛠 Tecnologías utilizadas

- Python
- Pandas
- OpenPyXL
- OneDrive
- Power Automate
- Git / GitHub

---

## 📂 Estructura del proyecto

```bash
ecommerce-data-cleaning-automation/
│
├── data/
│   ├── raw/          # Datos originales
│   └── clean/        # Reportes generados
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform_data.py
│   ├── export_data.py
│   └── send_email.py
│
├── main.py
├── requirements.txt
└── README.md
```

## 🔄 Flujo del pipeline
- Cargar múltiples archivos CSV
- Unificar la información
- Limpiar datos inconsistentes
- Transformar y segmentar información
- Generar resumen analítico
- Exportar reportes en Excel
- Guardar archivos en OneDrive
- Enviar reportes automáticamente por correo
 ----
## 📊 Ejemplo de transformaciones
```
$12.99 → 12.99
```
```
-20% → 20
```
```
" Product Name " → "product name"
```
---
## ⚙️ Instalación

## Clona el repositorio:

```Bash
git clone https://github.com/dayelysantana14/ecommerce-data-cleaning-automation.git
```

## Instala dependencias:

```Bash
pip install -r requirements.txt
```

## Ejecuta el proyecto:
```Bash
python main.py
```
---
## 📬 Automatización

Los reportes generados se almacenan automáticamente en OneDrive.

Posteriormente, Power Automate detecta los archivos y los envía por correo electrónico.

![Flow](flow%20power%20automate.PNG)

---
🌎 Escalabilidad

Actualmente este proyecto trabaja con archivos CSV como fuente de datos, pero puede adaptarse fácilmente para conectarse a:

- Bases de datos SQL
- APIs
- Archivos Excel actualizables
- Servicios en la nube
---
👩‍💻 Autor

Dayely Santana
Analista de Datos | Power Apps Developer | Software Enthusias

# 🐾 NaTe Pet Shop – Django Web App

## 📚 Consigna

Crea una web en Django utilizando herencia de plantillas, con un modelo de por lo menos 3 clases, un formulario para ingresar datos a las 3 clases y un formulario para buscar algo en la base de datos.

> 💡 Sugerencia: La estructura está basada en un sitio de administración de mascotas (estilo blog simple) para anticipar futuras entregas.

---

## 🎯 Objetivos

- Desarrollar una aplicación web usando Django con el patrón **MVT**.
- Utilizar herencia de plantillas HTML para mantener un diseño consistente.
- Implementar modelos con relaciones y formularios asociados.
- Permitir la búsqueda en la base de datos desde el navegador.

---

## ✅ Requisitos cumplidos

- [x] Proyecto subido a GitHub ✅
- [x] Herencia de HTML (base.html con `{% block content %}`) ✅
- [x] Tres modelos en `models.py`: `Customer`, `Pet`, `Order` ✅
- [x] Formulario para insertar datos para cada modelo ✅
- [x] Formulario de búsqueda para buscar mascotas por ID de cliente ✅
- [x] Este archivo `README.md` que indica el orden de prueba ✅

---

petshop/
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── add_customer.html
│ ├── add_pet.html
│ ├── add_order.html
│ └── search_pets.html
├── static/
│ └── css/
│ └── styles.css
├── models.py
├── forms.py
├── views.py
├── urls.py
└── …

---

## 🧪 Cómo probar la app

### 1. Clona el repositorio:

```bash
git clone https://github.com/telleznadim/TuPrimeraPagina-Tellez.git
cd PrimeraWeb
python manage.py runserver
```

## 🔍 Funcionalidades principales

| Página                         | Descripción                                  |
| ------------------------------ | -------------------------------------------- |
| `/`                            | Página principal con carousel e introducción |
| `/pets/`                       | Lista de mascotas en una tabla               |
| `/pets/add/`                   | Formulario para agregar nueva mascota        |
| `/customers/add/`              | Formulario para agregar nuevo cliente        |
| `/orders/add/`                 | Formulario para registrar nueva orden        |
| `/pets/search/?customer_id=ID` | Buscar mascotas por ID de cliente            |

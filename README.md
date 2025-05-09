# 💻 POO - Infraestructura Backend con FastAPI + MySQL + phpMyAdmin

Este proyecto contiene la infraestructura base para los trabajos prácticos de la asignatura **Programación Orientada a Objetos**, dictada en la Universidad Blas Pascal.

Incluye una base de datos MySQL y una API construida con FastAPI.

---

## 📦 Servicios incluidos

- **poo_mysql**: base de datos MySQL 8.0 (puerto 3306)
- **poo_phpmyadmin**: interfaz de administración phpMyAdmin (puerto 8080)
- **poo_api**: backend en Python con FastAPI (puerto 8000)

---

## 📁 Estructura del proyecto

```
poo-backend/
├── app/                    # Código fuente de la API (FastAPI)
│   ├── main.py
│   ├── database.py
│   ├── security.py
│   ├── models/
│   └── routers/
├── docker-compose.yml
├── Dockerfile
├── .env                    # Variables sensibles
├── .gitignore
└── README.md
```

---

## ⚙️ Variables de entorno

Configurar en el archivo `.env`:

```dotenv
MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE=poo_db
MYSQL_USER=
MYSQL_PASSWORD=
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> ⚠️ Este archivo está en `.gitignore` y **no debe subirse al repositorio**.

---

## 🌐 Accesos

- **API (FastAPI)**: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- **phpMyAdmin**: [http://localhost:8080](http://localhost:8080)
- **Base de datos MySQL**: accesible en `localhost:3306`

---

## 🧪 Comandos útiles

```bash
# Construir y levantar los servicios
docker compose up --build -d

# Ver logs
docker compose logs -f

# Detener los servicios
docker compose down

# Reiniciar
docker compose restart
```

---

## 🧱 Requisitos previos

- Docker y Docker Compose instalados
- Puerto 3306 (MySQL), 8080 (phpMyAdmin) y 8000 (API) libres
- No es necesario crear manualmente volúmenes ni redes

---

## 🎓 Uso académico

Este entorno sirve como base para los trabajos de la cátedra, incluyendo:

- Diseño de clases y objetos en Python
- Construcción de APIs RESTful
- Prácticas con base de datos relacional
- Autenticación básica con JWT
- Integración con ORM (`SQLAlchemy`)

---

## 📌 Notas adicionales

- Los datos de MySQL se almacenan en el volumen persistente `mysql_data`
- FastAPI y phpMyAdmin están conectados internamente por la red `app-network`

---

> 🏫 Proyecto educativo - Universidad Blas Pascal  
> Docente: Dr. Ing. César Osimani

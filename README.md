#  SkyRoute API - Gestor de Vuelos

API REST desarrollada con Django + Django REST Framework para gestionar vuelos y aerolíneas.

##  Autor

Matias Galvan Guerrero

##  Características

-  CRUD completo para Vuelos
-  CRUD completo para Aerolíneas
-  Búsqueda por código de vuelo, origen, destino
-  Relación entre vuelos y aerolíneas
-  Filtros y ordenamiento
-  Serializers personalizados

##  Instalación
```bash
# Clonar repositorio
git clone https://github.com/iam127/Examen-2_Matias_Galvan_Guerrero.git
cd skyroute_api

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

##  Endpoints

### Aerolíneas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/airlines/` | Listar aerolíneas |
| POST | `/api/airlines/` | Crear aerolínea |
| GET | `/api/airlines/{id}/` | Detalle de aerolínea |
| PUT | `/api/airlines/{id}/` | Actualizar aerolínea |
| DELETE | `/api/airlines/{id}/` | Eliminar aerolínea |

### Vuelos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/flights/` | Listar vuelos |
| POST | `/api/flights/` | Crear vuelo |
| GET | `/api/flights/{id}/` | Detalle de vuelo |
| PUT | `/api/flights/{id}/` | Actualizar vuelo |
| DELETE | `/api/flights/{id}/` | Eliminar vuelo |
| GET | `/api/flights/?search=lima` | Buscar vuelos |

##  Ejemplos de Uso

### Crear Aerolínea
```bash
curl -X POST http://localhost:8000/api/airlines/ \
  -H "Content-Type: application/json" \
  -d '{"name": "LATAM Airlines", "country": "Chile"}'
```

### Crear Vuelo
```bash
curl -X POST http://localhost:8000/api/flights/ \
  -H "Content-Type: application/json" \
  -d '{
    "flight_code": "LA2479",
    "origin": "Lima",
    "destination": "Santiago",
    "airline": 1
  }'
```

### Buscar Vuelos
```bash
curl http://localhost:8000/api/flights/?search=Lima
```

##  Tecnologías

- Python 3.10+
- Django 4.2+
- Django REST Framework 3.14+
- SQLite (desarrollo)


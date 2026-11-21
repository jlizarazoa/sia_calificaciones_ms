# SIA — Grades microservice

**Academic project** · Software Architecture course, Universidad Nacional de Colombia, 2022

Part of a team proposal to redesign the university's academic information system (SIA) as a set of microservices. The system was designed for 1,000+ students and professors and validated with performance and stress tests at that scale.

This service manages academic records: **courses**, **grades** and each student's **academic history**. It exposes a REST API with list (with query filters), create, update and delete operations for each resource.

**My part:** I built this microservice: the data model, the REST API and the Docker setup.

## Stack
Python · Django · Django REST Framework · MongoDB (djongo) · Docker

## Run locally
Requires MongoDB running at `mongodb://localhost:27017`.

```bash
cd sia_calificaciones_ms
pip install -r requirements.txt
python manage.py runserver
```

Routes are defined in `info_academica/urls.py`.

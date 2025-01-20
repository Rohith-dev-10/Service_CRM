# Service CRM - Week 1: Setting the Foundation with Django and MySQL

## Overview
This project is the foundation for a Service CRM application, focusing on backend development using Django and MySQL. The tasks for Week 1 include setting up the environment, creating models, performing migrations, and building basic CRUD functionality.

---

## Topics Covered
- Overview of Backend Development.
- Setting up Django and MySQL.
- Creating a Django project and apps.
- Models and Migrations.
- CRUD operations with Django ORM.

---

## Tasks Completed

### 1. Set up a project for "Service CRM"
Created the following models:
- **Customer**:
  - Fields: `Name`, `Email`, `Phone`, `Address`.
- **Service Request**:
  - Fields: `Title`, `Description`, `Status`, `Priority`, `Assigned Technician`.
- **Technician**:
  - Fields: `Name`, `Contact`, `Skills`.

### 2. Perform Migrations
- Configured the database connection to MySQL.
- Created migrations for all models.
- Applied migrations to generate the database schema.

### 3. Create a Simple Django View
- Built a Django view to display a list of all service requests.
- The view fetches data using Django ORM and renders it in a basic HTML template.

---

## Repository Link
[Service CRM - Week 1 Project](https://github.com/Rohith-dev-10/Service_CRM)

---

## What's Next
- Moving to Week 2 tasks, which will include advanced functionality and enhancements to the application.

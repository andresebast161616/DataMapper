# DataMapper Project

**Implementation of the Data Mapper Pattern using Python and SQLite**

---

## Introduction

This project demonstrates how to implement the **Data Mapper design pattern** in **Python**, connecting objects with a relational **SQLite** database without the objects needing to know the database structure.  
It includes database connection, creation of mappers, insertion, querying users, unit testing, and setting up **GitHub Actions** for continuous integration.

Ideal for understanding how to separate domain logic from database logic cleanly and efficiently.

---


## Main Objective

Build a functional and testable system in **Python** to:

- Insert and retrieve users from an SQLite database.
- Maintain separation between the domain model and persistence logic (Data Mapper pattern).
  
---

## Project Structure
proyecto/ ├── app.py ├── database/ │ └── db_connection.py ├── mappers/ │ └── user_mapper.py ├── models/ │ └── user.py ├── tests/ │ └── test_user_mapper.py ├── requirements.txt


---

## Technologies Used

- Python 3.9
- SQLite3
- Unittest (for unit testing)

---

## How to Use

```bash
# Clone the repository
git clone https://github.com/your_username/your_repository.git
cd your_repository/proyecto

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

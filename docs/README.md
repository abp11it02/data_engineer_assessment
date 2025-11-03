# Data Engineering Assessment

Welcome!  
This exercise evaluates your core **data-engineering** skills:

| Competency | Focus                                                         |
| ---------- | ------------------------------------------------------------- |
| SQL        | relational modelling, normalisation, DDL/DML scripting        |
| Python ETL | data ingestion, cleaning, transformation, & loading (ELT/ETL) |

---

## 0 Prerequisites & Setup

> **Allowed technologies**

- **Python ≥ 3.8** – all ETL / data-processing code
- **MySQL 8** – the target relational database
- **Lightweight helper libraries only** (e.g. `pandas`, `mysql-connector-python`).  
  List every dependency in **`requirements.txt`** and justify anything unusual.
- **No ORMs / auto-migration tools** – write plain SQL by hand.

---

## 1 Clone the skeleton repo

```
git clone https://github.com/100x-Home-LLC/data_engineer_assessment.git
```

✏️ Note: Rename the repo after cloning and add your full name.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

- Database is available on `localhost:3306`
- Credentials/configuration are in the Docker Compose file
- **Do not change** database name or credentials

For MySQL Docker image reference:
[MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

- You are provided with a raw JSON file containing property records is located in data/
- Each row relates to a property. Each row mixes many unrelated attributes (property details, HOA data, rehab estimates, valuations, etc.).
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.
- Use the supplied Field Config.xlsx (in data/) to understand business semantics.

### Task

- **Normalize the data:**

  - Develop a Python ETL script to read, clean, transform, and load data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place your scripts in `sql/` and `scripts/`
  - The scripts should take the initial json to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

**Tech Stack:**

- Python (include a `requirements.txt`)
  Use **MySQL** and SQL for all database work
- You may use any CLI or GUI for development, but the final changes must be submitted as python/ SQL scripts
- **Do not** use ORM migrations—write all SQL by hand

---

## Submission Guidelines

- Edit the section to the bottom of this README with your solutions and instructions for each section at the bottom.
- Place all scripts/code in their respective folders (`sql/`, `scripts/`, etc.)
- Ensure all steps are fully **reproducible** using your documentation
- Create a new private repo and invite the reviewer https://github.com/mantreshjain

---

**Good luck! We look forward to your submission.**

## Solutions and Instructions (Filed by Candidate)

**Document your database design and solution here:**

- Explain your schema and any design decisions
- Give clear instructions on how to run and test your script

**Document your ETL logic here:**

- Outline your approach and design
- Provide instructions and code snippets for running the ETL
- List any requirements


Design - 
Each table contains property ID as a foreign to Property table as shown below

Property
    id varchar(50) primary key,
    Property_Title varchar(255),
    Address varchar(255),
    Market varchar(100),
    Flood varchar(100),
    Street_Address varchar(255),
    City varchar(100),
    State varchar(50),
    Zip varchar(20),
    Property_Type varchar(100),
    Highway varchar(100),
    Train varchar(100),
    Tax_Rate float,
    SQFT_Basement integer,
    HTW varchar(3),
    Pool varchar(3),
    Commercial varchar(3),
    Water varchar(100),
    Sewage varchar(100),
    Year_Built integer,
    SQFT_MU integer,
    SQFT_Total varchar(50),
    Parking varchar(100),
    Bed integer,
    Bath integer,
    BasementYesNo varchar(3),
    Layout varchar(100),
    Rent_Restricted varchar(100),
    Neighborhood_Rating integer,
    Latitude float,
    Longitude float,
    Subdivision varchar(100),
    School_Average float

HOA - 
    id varchar(50) primary key,
    property_id varchar(50),
    hoa integer,
    hoa_flag varchar(3),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE

Leads - 
    id varchar(50) primary key,
    property_id varchar(50),
    Most_Recent_Status varchar(50),
    Source varchar(50),
    Occupancy varchar(50),
    Net_Yield float,
    IRR float,
    Selling_Reason varchar(50),
    Seller_Retained_Broker varchar(50),
    Final_Reviewer varchar(50),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE

Rehab - 
    id varchar(50) primary key,
    property_id varchar(50),
    Underwriting_Rehab integer,
    Rehab_Calculation integer,
    Paint varchar(3),
    Flooring_Flag varchar(3),
    Foundation_Flag varchar(3),
    Roof_Flag varchar(3),
    HVAC_Flag varchar(3),
    Kitchen_Flag varchar(3),
    Bathroom_Flag varchar(3),
    Appliances_Flag varchar(3),
    Windows_Flag varchar(3),
    Landscaping_Flag varchar(3),
    Trashout_Flag varchar(3),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE

Taxes - 
    id varchar(50) primary key,
    property_id varchar(50),
    taxes integer,
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE

Valuation (Default values of valuation columns is 0)- 
    id varchar(50) primary key,
    property_id varchar(50),
    Previous_Rent integer,
    List_Price integer,
    Zestimate integer,
    ARV integer,
    Expected_Rent integer,
    Rent_Zestimate integer,
    Low_FMR integer,
    High_FMR integer,
    Redfin_Value integer,
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE

Scripts folder contain following scripts - 

create_connection.py - Creates/Manages and Closes MySQL connection and calls create table and load table functions
create_tables.py - executes create table scripts for all the tables
load_table.py - loads data into the tables

SQL folder contains following scripts - 
create_table.sql - Contains all the create table statements along with foreign key and primary key

requirements.txt - Contains all the requirements needed for the Python scripts

Steps to run this project - 
Make sure you have Python 3 and pip installed in the system. MySQL will be run as docker container.

Run the following docker commands to start MySQL docker - 

```
docker build -t mysql-image -f Dockerfile.initial_db .
docker run -d --name mysql-db -p 3306:3306 mysql-image
```

This will start the MySQL docker container on port 3306 and make it accessible to the python scripts

Install python dependencies -

Create virtual env - 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the python script create_connection.py and it will create the connection, create tables and load data into them - 

```
python3 scripts/create_connection.py
```

Check if data is properly loaded into the tables-

```
docker exec -it mysql-db mysql -uroot -p
```

provide password when prompted - 6equj5_db_user

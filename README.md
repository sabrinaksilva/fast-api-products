# 🌟 FastAPI Products API

## 🔧 Introduction

This is a backend system built in **Python** using **FastAPI** for product management and cash flow tracking.  
This API integrates with a **React frontend** system, which you can find in this repository:  
➤️ [React Products Frontend](https://github.com/sabrinaksilva/react-products-frontend)

---

## 📖 **Project Description**
The **FastAPI Products API** supports CRUD operations in general, following REST standards, for product management, inventory, and cash control, while adhering to the **Clean Architecture principles**, simplified by the magnitude of the application.

### **In this context, a Product is composed of:**
- **Name**
- **Description**
- **Quantity**
- **Cost price**
- **Selling price**

### **The system allows:**

#### **Product Management:**
- Create, edit, and view a product.
- View product listings with **filters**.
- **Inventory control** to track product quantities.

#### **Cash Flow Management:**
- Create, view, and edit product entries and exits.
- View a summary of cash flow movements by period, including:
  - **Product entries and exits**
  - **Associated monetary values**
- View **financial indicators** to support decision-making.

#### **Authentication Flow:**
- Secure access to system functionalities through authentication control.

---

## 🚀 **Installation and Setup**

Follow these steps to set up and run the FastAPI Products API on **Windows**, **Linux**, or **MacOS**.

### **1. Install Python (Version >= 3.10)**

#### **Windows**
1. Download Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and select:
   - **Add Python to PATH** during installation.
3. Verify the installation:
   ```bash
   python --version
   ```

#### **Linux**
1. Update your package list:
   ```bash
   sudo apt update
   ```
2. Install Python:
   ```bash
   sudo apt install python3 python3-pip
   ```
3. Verify the installation:
   ```bash
   python3 --version
   ```

#### **MacOS**
1. Install Python using Homebrew:
   ```bash
   brew install python
   ```
2. Verify the installation:
   ```bash
   python3 --version
   ```

---

### **2. Install FastAPI**

Install FastAPI and Uvicorn using `pip`:
```bash
pip install fastapi uvicorn
```

---

### **3. Clone the Repository**

Download or clone the repository to your local machine:
```bash
git clone https://github.com/sabrinaksilva/fast-api-products.git
cd fast-api-products
```

---

### **4. Install Project Dependencies**

Install all required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### **5. Create the `.env` File**

Navigate to the `app/config` directory and create the `.env` file:
```bash
cp app/config/.env.template app/config/.env
```

Edit the `.env` file as needed. The default values in `.env.template` are example configurations:

```env
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=product_db
```

> ⚠️ **Note**: Adjust these values according to your environment.

---

### **6. Install PostgreSQL**

#### **Windows**
1. Download PostgreSQL from the [official website](https://www.postgresql.org/download/).
2. Follow the installation wizard and set a username and password.
3. Ensure PostgreSQL is running.

#### **Linux**
1. Update your package list:
   ```bash
   sudo apt update
   ```
2. Install PostgreSQL:
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```
3. Start the PostgreSQL service:
   ```bash
   sudo systemctl start postgresql
   ```

#### **MacOS**
1. Install PostgreSQL using Homebrew:
   ```bash
   brew install postgresql
   ```
2. Start the PostgreSQL service:
   ```bash
   brew services start postgresql
   ```

---

### **7. Set Up the Database**

#### **Step 1: Access the PostgreSQL Shell**
Run the following command to access the PostgreSQL shell:
```bash
sudo -u postgres psql
```

#### **Step 2: Create a User**
Create the database user referenced in the `.env` file (`DB_USER`):
```sql
CREATE USER postgres WITH PASSWORD 'password';
```

#### **Step 3: Create the Database**
Create the database referenced in the `.env` file (`DB_NAME`):
```sql
CREATE DATABASE product_db OWNER postgres;
```

#### **Step 4: Grant Privileges**
Grant all privileges on the database to the user:
```sql
GRANT ALL PRIVILEGES ON DATABASE product_db TO postgres;
```

#### **Step 5: Exit the PostgreSQL Shell**
```sql
\q
```

---

### **8. Run the Application**

Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

Access the application at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

API documentation is available at:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

> ⚠️ **To-Do**  
Docker**

Instructions for setting up and running the application using Docker will be added here.

---

## 📚 **Usage**

> ⚠️ **To-Do**  
Steps on how to use the API and interact with its features will be detailed here.

---

## 🔗 **API Reference**

> ⚠️ **To-Do**  
The API reference, including endpoints, request and response examples, will be detailed here.

---

## 👤 **Contact**
If you have any questions, suggestions, or feedback, you can reach me at:  
💼 **Email**: [sabrinakappann@gmail.com](mailto:sabrinakappann@gmail.com)  
📧 **LinkedIn**: [https://www.linkedin.com/in/sabrina-kappann-da-silva-34665618a]


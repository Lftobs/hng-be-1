
# **Public API for HNG Stage 0 Task**  

This is a simple public API built using **FastAPI** for the **HNG Internship 12 - Stage 0 Backend Task**. The API returns basic information in JSON format, including:  
- Your registered email address  
- The current datetime in **ISO 8601 UTC format**  
- The GitHub URL of the project  

## **Live API URL**  
🚀 **Base URL:** [`Live-Link 🥲`](https://hng-be-1.vercel.app/)  

## **API Documentation**  

### **1. Retrieve Basic Information**  
#### **Endpoint**  
```http
GET /
```

#### **Response example**
```json
{
  "email": "my-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Lftobs/hng-be-1/tree/main"
}
```
## **How to Run Locally**  

### **Prerequisites**  
Ensure you have the following installed:  
- Python **3.8+**  
- Pip (Python package manager)  

### **Steps**  

#### **1. Clone the Repository**  
Clone the project from GitHub and navigate into the project directory:  

```sh
git clone https://github.com/Lftobs/hng-be-1/tree/main
cd hng-be-1
```
#### **2. Create virtual env and activate it**
```sh
python -m venv venv
source venv/bin/activate
```
#### **3. Install dep**
```sh 
pip install -r requirements.txt
```
#### **4. Run project**
```sh
uvicorn main:app --reload
```
**or**
```sh
fastapi dev
```
## **HNG Developer Link** 
Looking for a backend developer? Hire one from HNG:
[hng-python-dev](https://hng.tech/hire/python-developers)

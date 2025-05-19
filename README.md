# Flask Time API with Token Authentication

This project is a simple **Flask API** that returns the current local time and UTC offset for a given capital city. The API is secured with an **Authorization token**.

## **Setup and Installation - Local **

### **1. Clone the Repository**

Clone this repository to your local machine:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```
### **2. Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install Flask pytz requests
```
### **3. Run the Flask App Locally**

```bash
python app.py
```
### **4. Access the API Locally**
The API will be available at http://127.0.0.1:5000/get_time?city=Paris
an example:
```bash
curl -X GET "http://127.0.0.1:5000/get_time?city=Paris" -H "Authorization: your_secret_token_here"
```
## **Setup and Installation - GCP **

### **1. Upload Files to GCP VM **
Use SCP or GCP Console SSH to upload app.py and cities.json to the VM.

### **2. Run Flask App on GCP **
SSH into the VM, navigate to the project directory, and run the Flask app
```bash
python3 app.py
```
### **3. Provide the Public IP **
Can access running app at
```bash
http://<EXTERNAL_IP>:5000/get_time?city=Paris
```

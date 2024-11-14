
# Project Title

This Django REST Framework API provides endpoints for managing invoices and their associated details. It allows for creating new invoices, updating existing ones, and retrieving information about specific invoices or all invoices.



## Models

### Invoice:  

1. id: Auto-incremented primary key.
2. invoice_number: CharField (unique).
3. customer_name: CharField.
4. date: DateField.


### Invoice Details

1. id: Auto-incremented primary key.
2. invoice: ForeignKey to Invoice.
3. description: CharField.
4. quantity: IntegerField.
5. price: DecimalField.
6. line_total: DecimalField.
## Deployment

Step 1:  Install Dependencies:

```bash
  pip install -r requirements.txt
```
Step 2: Make migrations:


```bash
  python manage.py makemigrations
```
Step 3: Migrate

```bash
  python manage.py migrate
```
Step 4: Deploying to a Local Server:

```bash
  python manage.py runserver
```
Step 5: Admin login  
  Connect to the server http://127.0.0.1:8000/admin/  
  username : Admin  
  password: password  
  you can access all the data 



## Instructions to Set Up Django Project with MongoDB ##

### - Requirements :
1. Install python and Django on your system
2. Install MongoDB on your system.




### - Set Up the Project :

1. Download the project from the link provided, or use `git clone <project_url>` to clone it.

2. Set up Virtual Enviroment : It's good practice to use a virtual environment to manage your Python dependencies.  <br>
	Install it with  `pip install virtualenv`.   <br>
    Create a virtual environment:
     					`python -m venv venv`
    Activate the virtual environment:
     - On Windows:			    `venv\Scripts\activate`
     - On macOS/Linux:			`source venv/bin/activate`

3. Install Project Dependencies:
					`pip install -r requirements.txt`

### - Set Up MongoDB:

1. Start MongoDB:
   - Ensure MongoDB is running. You can start it from the terminal or use the MongoDB Compass GUI.

2. Create a MongoDB Database:
   - You can create a new database in MongoDB Compass or directly in the terminal. Here’s an example of creating a database called `inventory-data`: <br>
     					`mongo` <br>
     					`use inventory-data`

   - If your project requires specific collections, MongoDB will automatically create them when you first save data to the collections.

3. Update Django Settings:
   - Open the `settings.py` file in your Django project.
   - Update the `DATABASES` configuration with your MongoDB connection details:

    <code> DATABASES = {                                           
         'default': {
             'ENGINE': 'djongo',
             'NAME': 'inventory-data',
             'CLIENT': {
                 'host': 'your_mongo_host',
                 'port': 27017,  # Replace with your MongoDB port if different
                 'username': 'your_mongo_username',
                 'password': 'your_mongo_password',
             },
         }
    }</code>
 
   - If you used MongoDB without authentication (no username or password), you can remove the `username` and `password` fields.
   - If MongoDB is running on the same machine, you can use `localhost` or `127.0.0.1` for the `host`.

4. Run Django Migrations :
  				`python manage.py makemigrations` <br>
  				`python manage.py migrate`
  

5. Run the Django Development Server:
	Start the Django development server to check if everything is working:
 				`python manage.py runserver`
 
	Open a web browser and go to `http://127.0.0.1:8000/` to see your project.

6. Additional Commands :
	Create a Superuser: If your project requires admin access, create a superuser:
  				`python manage.py createsuperuser`

	Access Django Admin: Navigate to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.
<br><br>

### IMPORTANT POINTS :
	- Look if your Django is compatiable with current djongo, in my device i use Django 3.12.25
	- Change software versions as per requirements
<br><br>

### WEBSITE NAVIGATION:
	- Inventory : To create new item
	- Show List : To show the inventory items
	- Search : To search the required item
# FAST API simple blog

Simple features in order to learn basics of this new framework.

### Main features:

- **_User sign up_** 
- **_User authentication_** (JWT tokens)
- **_Show all blogs_**
- **_Show a blog_**
- **_Create a blog_** 
- **_Update a blog_** 
- **_Delete a blog_** 
- **_Show all user`s blogs_**

### Installation 

1. Clone the repository from GitHub
2. Create a virtual environment
3. Install requirements: `pip install requirements.txt`
4. Create a file `settings.py`
5. Fill it out:
```
SQL_ALCHEMY_URL = 'sqlite:///./blog.db'
SECRET_KEY = "Your secret key"
ALGORITHM = "Your hash algorithm"
ACCESS_TOKEN_EXPIRE_MINUTES = Your value
```
6. Start the server: `uvicorn blog.main:app --reload`





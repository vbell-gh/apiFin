from datetime import datetime
from src.masterdata.models.users import Users, Roles  # Import your SQLModel classes

# Dummy data for Users
dummy_user_1 = Users(
    username="user1",
    password="password1",
    fullname="User One",
    email="user1@example.com",
    role_id=1,  
    user_created=datetime.now()
)

dummy_user_2 = Users(
    username="user2",
    password="password2",
    fullname="User Two",
    email="user2@example.com",
    role_id=2,  
    user_created=datetime.now()
)

dummy_user_3 = Users(
    username="user3",
    password="password3",
    fullname="User Three",
    email="user3@example.com",
    role_id=1,  
    user_created=datetime.now()
)

dummy_user_4 = Users(
    username="user4",
    password="password4",
    fullname="User Four",
    email="user4@example.com",
    role_id=3,  
    user_created=datetime.now()
)

# Dummy data for Roles
dummy_role_1 = Roles(
    role_name="Admin",
    description="Administrator role"
)

dummy_role_2 = Roles(
    role_name="User",
    description="Standard user role"
)

dummy_role_3 = Roles(
    role_name="Manager",
    description="Manager role"
)

users_dummy_data = [v for k, v in vars().items() if k.startswith("dummy_user_")]
roles_dummy_data = [v for k, v in vars().items() if k.startswith("dummy_role_")]

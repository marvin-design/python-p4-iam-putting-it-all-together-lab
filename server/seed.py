from faker import Faker
from random import randint
from app import app
from models import db, User, Recipe

fake = Faker()

with app.app_context():
    # Clear existing data
    User.query.delete()
    Recipe.query.delete()
    db.session.commit()

    # Create test users
    users = []
    for i in range(5):
        user = User(
            username=fake.user_name(),
            image_url=fake.image_url(),
            bio=fake.paragraph()
        )
        user.password_hash = 'password123'
        users.append(user)
    
    db.session.add_all(users)
    db.session.commit()

    # Create test recipes
    recipes = []
    for user in users:
        for i in range(3):
            recipe = Recipe(
                title=fake.sentence(),
                instructions=fake.paragraph(nb_sentences=10),
                minutes_to_complete=randint(15, 120),
                user_id=user.id
            )
            recipes.append(recipe)
    
    db.session.add_all(recipes)
    db.session.commit()
    print("Database seeded successfully!")
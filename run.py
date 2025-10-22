from app.extensions import db
from app.app import create_app

app = create_app()
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
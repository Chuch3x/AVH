print("Starting main.py")
from infraestructure.FlaskCommitMetricsController import app
print("Import successful")

if __name__ == "__main__":
    app.run(debug=True)
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from commit_ccn.infraestructure.FlaskCommitMetricsController import app

# Exponer la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from commit_ccn.infraestructure.FlaskCommitMetricsController import app as application

def main(request=None):
    return application

if __name__ == "__main__":
    application.run()
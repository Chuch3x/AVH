from commit_ccn.infraestructure.FlaskCommitMetricsController import app as application

def main(request=None):
    return application

if __name__ == "__main__":
    application.run()
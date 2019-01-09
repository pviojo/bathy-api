import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    APP_NAME = 'Bathy API'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%s/%s' % ('mysql', os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWD'], os.environ['MYSQL_SERVER'], (os.environ['MYSQL_PORT'] if 'MYSQL_PORT' in os.environ else 3306), os.environ['MYSQL_DB'])
    
    SLACK_NOTIFICATION_TOKEN = os.environ['SLACK_NOTIFICATION_TOKEN']
    SLACK_NOTIFICATION_CHANNEL = os.environ['SLACK_NOTIFICATION_CHANNEL']
    

    
    

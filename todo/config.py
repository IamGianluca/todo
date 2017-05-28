import os


DB_NAME = os.environ['DB_NAME']
DB_PATH = os.path.join('5432', DB_NAME)
TEST_DATABASE_URI = 'postgresql://{user}:{password}@db:{port}/{name}'.format(
    user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
    port=os.environ['DB_PORT'], name=os.environ['DB_NAME'])
DATABASE_URI = TEST_DATABASE_URI

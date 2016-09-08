import os

DEBUG = True
SECRET_KEY = 'veryverysecret'

# DB Engine Settings (currently Postgresql-specific)
# http://docs.sqlalchemy.org/en/latest/core/engines.html

DB_HOST = os.getenv('HOST_IP', '0.0.0.0')
DB_DIALECT = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_PORT = 5432
DB_NAME = 'taskmgr'

# DB access credentials

DB_USERNAME = 'postgres'
DB_PASSWORD = 'tnzSDK'

# kwargs dict for the formatter

DB_CFG = {
    'DB_HOST': DB_HOST,
    'DB_DIALECT': DB_DIALECT,
    'DB_DRIVER': DB_DRIVER,
    'DB_PORT': DB_PORT,
    'DB_NAME': DB_NAME,
    'DB_USERNAME': DB_USERNAME,
    'DB_PASSWORD': DB_PASSWORD
}

# Engine configuration URL (urls follow RFC-1738 - http://rfc.net/rfc1738.html)

DB_URI = '{DB_DIALECT}+{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'.format(**DB_CFG)
SQLALCHEMY_DATABASE_URI = DB_URI

# following warning during import
# "SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning."

SQLALCHEMY_TRACK_MODIFICATIONS = True # We are still in development.. so no harm no foul?

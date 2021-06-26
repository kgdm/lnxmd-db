import os


class Config:
    DB_USER = os.getenv("POSTGRES_USER", "postgres")
    DB_PASS = os.getenv("POSTGRES_PASS", "postgres")
    DB_NAME = os.getenv("POSTGRES_DB", "postgres")
    DB_PORT = os.getenv("POSTGRES_PORT", "5432")
    DB_HOST = os.getenv("POSTGRES_HOST", "0.0.0.0")

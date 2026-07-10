import os
import psycopg

from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(
    DATABASE_URL,
    autocommit=True
)

checkpointer = PostgresSaver(conn)

print("Creating LangGraph tables...")

checkpointer.setup()

print("PostgreSQL Checkpointer Ready")
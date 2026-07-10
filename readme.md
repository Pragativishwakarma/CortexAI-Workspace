
python -m venv venv

venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

 Groq API: https://console.groq.com

install postgresSQL: 
  link: https://www.postgresql.org/download/windows/
   follow the below steps
   Windows
   ↓
        Download the installer

        This redirects to:

        EnterpriseDB PostgreSQL Installer

        Step 2: Select Version

        Choose:

        PostgreSQL 17.x (Latest)

        or

        PostgreSQL 16.x (LTS-like stable choice)

        For learning and development:

        PostgreSQL 17

        is recommended.

        Step 3: Run Installer

        Double-click:

        postgresql-17.x-windows-x64.exe

        Click:

        Next
        Step 4: Installation Directory

        Default:

        C:\Program Files\PostgreSQL\17

        Keep default.

        Click:

        Next
        Step 5: Select Components

        Check all:

        ☑ PostgreSQL Server
        ☑ pgAdmin 4
        ☑ Stack Builder
        ☑ Command Line Tools

        Click:

        Next
        Step 6: Data Directory

        Default:

        C:\Program Files\PostgreSQL\17\data

        Keep default.

        Click:

        Next
        Step 7: Set Password

        Important step.

        User:

        postgres

        Create password:

        postgres123

        (or your own strong password)

        Remember this password.

        Click:

        Next
        Step 8: Port Number

        Default:

        5432

        Keep:

        5432

        Click:

        Next
        Step 9: Locale

        Keep:

        Default locale

        Click:

        Next
        Step 10: Install

        Click:

        Next
        Install

        Wait 2–5 minutes.

        Click:

        Finish
        Step 11: Verify PostgreSQL Service

        Press:

        Windows + R

        Type:

        services.msc

        Find:

        postgresql-x64-17

        Status should be:

        Running
        Step 12: Open pgAdmin

        Search:

        pgAdmin 4

        Open it.

        Enter:

        Master Password

        This is for pgAdmin only.

        Example:

        admin123
        Step 13: Connect to Server

        Left panel:

        Servers

        Expand:

        PostgreSQL 17

        Enter:

        Password = postgres123

        You should see:

        Databases
        Login Roles
        Tablespaces
        Step 14: Create Database

        Right-click:

        Databases

        Choose:

        Create
        ↓
        Database

        Database Name:

        langgraph_db

        Click:

        Save

Process of Running the file:
  1. python -m rag.ingest.py
  2. streamlit run frontend.py or python main.py

[Learning Agent Running]

[Report Agent Running]

==================================================
FINAL REPORT
==================================================

Week 1 Python Basics
Week 2 NumPy
Week 3 Pandas
Week 4 Mini Project
...
======================================

PostgresSaver does not store chat messages in a dedicated messages table.

Instead, it stores the entire LangGraph state as checkpoint records.

below is commands to check tables
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema='public';

Tables:
1. checkpoints         -> Workflow snapshot metadata
2. checkpoint_blobs    -> Serialized state data
3. checkpoint_writes   -> State updates during execution


In LangGraph PostgresSaver:

checkpoints

Usually contains metadata:

| Column               | Purpose               |
| -------------------- | --------------------- |
| thread_id            | Conversation ID       |
| checkpoint_id        | Checkpoint identifier |
| parent_checkpoint_id | Previous checkpoint   |
| metadata             | Workflow metadata     |

checkpoint_blobs
Usually contains serialized state:

| Column    | Purpose               |
| --------- | --------------------- |
| thread_id | Conversation ID       |
| channel   | State channel         |
| blob      | Serialized state data |


This is often where:

{
  "messages": [
    {
      "role": "user",
      "content": "Explain LangGraph"
    },
    {
      "role": "assistant",
      "content": "LangGraph is..."
    }
  ]
}

gets stored.

checkpoint_writes

Stores incremental updates:

| Column     | Purpose             |
| ---------- | ------------------- |
| task_id    | Node execution      |
| channel    | Updated state field |
| value/blob | Data written        |
LangGraph does not usually create:

messages
chat_history
conversation

tables.

Instead it stores the entire state object that contains:

{
    "messages": [...],
    "query": "...",
    "response": "...",
    "retrieved_docs": [...]
}

inside checkpoint tables.

So the user query may be inside:

checkpoint_blobs.blob

or

checkpoint_writes.blob

depending on your LangGraph version.
================================================
checkpoint_writes table, and this is the best table to explain during your PPT.

What each row represents

Every row is a LangGraph state update.

For example:
| channel       | Meaning                  |
| ------------- | ------------------------ |
| user_query    | User input               |
| learning_plan | Learning Agent output    |
| resources     | Resource Agent output    |
| final_report  | Final generated response |

Execution Flow

From your screenshot:

user_query
    ↓
learning_plan
    ↓
resources
    ↓
final_report

This means:

Step 1

    User entered:

    "Create Java learning plan"

    Stored as:

    channel = user_query
Step 2
        Learning Agent executed

        Generated:

        Week 1 Java Basics
        Week 2 OOP
        Week 3 Collections

        Stored as:

        channel = learning_plan
Step 3

        Resource Agent executed

        Generated:

        YouTube Links
        Books
        Articles

        Stored as:

        channel = resources
Step 4

        Final Agent executed

        Generated:

        Complete report

        Stored as:

        channel = final_report
        Which column contains the actual data?

        The important column is:

        blob
            [binary data]


 because LangGraph stores the value using:

msgpack (MessagePack)

serialization.

Notice:

type = msgpack
Meaning of Columns:

thread_id
            student_001

            Conversation ID.

            Think:

            Chat Session ID
checkpoint_id
            1f16e0cd....

            State snapshot identifier.

task_id
        1e01a268....

        Agent execution identifier.

idx
        Execution order.

        Example:

        0 = user_query
        1 = learning_plan
        2 = resources
        3 = final_report           
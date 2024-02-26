import psycopg
from datetime import datetime, timezone

dt = datetime.now(timezone.utc)

with psycopg.connect("host=localhost dbname=demo user=dam_app password=1234") as conn:
    with conn.cursor() as cur:
        # cur.execute("""
        #     CREATE TABLE audit (
        #     audit_id serial PRIMARY KEY,
        #     user_id integer,
        #     resource varchar(500),
        #     time timestamp,
        #     CONSTRAINT FK_aud_use
        #     FOREIGN KEY(user_id)
        #     REFERENCES accounts(user_id))
        #     """)

        cur.execute(
            "INSERT INTO accounts (username,password,email,created_at,"
            "last_login) VALUES (%s,%s,%s,%s,%s)",
            ("dam_app_2","1234","dam2b@iticbcn.cat",dt,dt)
            )
        conn.commit
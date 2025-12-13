## Backend

### Setup
1. Initial a uv project
2. Create a virtual environment and activate it
3. Install package:
   - `uv add fastapi`
   - `uv add pydantic`
   - `uv add sqlmodel`
   - `uv add psycopg2`
   - `uv add uuid`
   - `uv add python-dotenv`


## Frontend

### Setup
1. Create a NextJS app router project: `npx create-next-app@16.0.10`


## Database
### Setup
1. Goto Vercel and click on Storage
2. Select <b>Neon</b> and click Continue
3. Name your Database and Click on Done
4. Copy the Credentials.
5. Create a file named .env at the root of your Python FastAPI project and paste the Credentials you copied.
6. Goto [`Neon Official website`](https://neon.com) to see the Table and record
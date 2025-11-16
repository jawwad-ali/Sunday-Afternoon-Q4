# GEMINI CLI

## Book Reference:

- Book URL:- https://ai-native.panaversity.org/

- Sunday Afternoon Repo URL:- https://github.com/jawwad-ali/Sunday-Afternoon-Q4


## Basic Commands for GEMINI-CLI
/auth: to authenticate the user
/memory: to show, add, refresh and list memory
/clear: Clear the screen and conversation history
/model: To change the model 


# Memory or Context
- When talking about memory or the context it is a know fact that we are talking about GEMINI.md

memory or context = GEMINI.md
## Destinations for Gemini.md
1. Root/Home Directory

  1.1 C:\Users\Ali\.gemini\GEMINI.md
      - It impacts every project that user GEMINI-CLI. It is mainly used to define the rules that should be applied on every project

  1.2 Project Level GEMINI.md
     - Only impacts the particular project.
   
  1.3 Module Level GEMINI.md
     - Beneficial to give GEMINI-cli instructions related to a module/feature

Features like Tech Stack, Test cases, Multi lingual etc can be written in project specific GEMINI.md.

<hr />

# FASTAPI
0. Initialize a Projects through UV
1. Create/activate a virtual env(optional)
2. Start making Instances and endpoint (do this by prompt)

## To Access FASTAPI ENDPOINTS
1. http://localhost:8000 
2. For docs: http://localhost:8000/docs
   2.1 To request the endpoint expand the Bar
   2.2. Click on Try it out
   2.3 Click on execute


3. Start the Server: uv run uvicorn main:app --reload

   3.1 main = your Python file name (main.py)
   3.2 app = the FastAPI instance variable name
   3.3 --reload = auto-restart on code changes
   3.4 Uvicorn = The server that actually runs and serves your FastAPI app to      	users
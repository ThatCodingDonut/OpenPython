fastapi_boilerplate_code = """from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# in-memory database
{db_name} = {{}}

class {entity_class_name}(BaseModel):
    {formatted_request_body}
# Read (GET all)
@app.get("/")
async def get_{entity_var}s() -> list[{entity_class_name}]:
    if not {db_name}:
        raise HTTPException(status_code=404, detail="No {entity_class_name}s found")
    return list({db_name}.values())

# Read (GET one)
@app.get("/{entity_name}/{{id}}")
async def get_{entity_var}(id: int) -> {entity_class_name}:
    if id not in {db_name}:
        raise HTTPException(status_code=404, detail="{entity_class_name} not found")
    return {db_name}[id]

# Create (POST)
@app.post("/{entity_name}/")
async def create_{entity_var}({entity_var}: {entity_class_name}) -> {entity_class_name}:
    entity_id = len({db_name}) + 1
    {db_name}[entity_id] = {entity_var} 
    return {entity_var}

# Update (PUT)
@app.put("/{entity_name}/{{id}}")
async def update_{entity_var}(id: int, {entity_var}: {entity_class_name}) -> {entity_class_name}:
    if id not in {db_name}:
        raise HTTPException(status_code=404, detail="{entity_class_name} not found")
    {db_name}[id] = {entity_var}
    return {db_name}[id]
    
# Delete (DELETE)
@app.delete("/{entity_name}/{{id}}")
async def delete_{entity_var}(id: int) -> object:
    if id not in {db_name}:
        raise HTTPException(status_code=404, detail="{entity_class_name} not found")
    del {db_name}[id]
    return {{"detail": "{entity_class_name} deleted successfully"}}
"""

# Function to generate CRUD code for FastAPI and write it to 'main.py'.
#
# Parameters:
# entity_name -> used as the route name
    # example: /{entity_name}/ (plural form for the route) 
# entity_class_name -> used as the Pydantic data model class name to define the data schema.
# db_name -> used as the name of the in-memory database (in this case dictionary)
# request_body_obj -> a dictionary containing field names and their Python types, representing the attributes of the entity.
    # example: { "id": "int", "name": "str" }
# entity_var -> a string that can represent the singular form of `entity_name` used in function names, and parameters.
#
# This function formats a FastAPI boilerplate code and writes it to 'main.py'.
def gen_crud_code(entity_name: str, entity_class_name: str, db_name: str, request_body_obj: object, entity_var: str):
    formatted_request_body = ""
    for key, val in request_body_obj.items():
        formatted_request_body += f"{key}: {val}\n    "

    with open('main.py', 'w') as mainFile:
        mainFile.write(fastapi_boilerplate_code.format(
            entity_name=entity_name, 
            entity_class_name=entity_class_name,
            db_name=db_name,
            formatted_request_body=formatted_request_body,
            entity_var=entity_var,
        ))

    print("Successfully generated CRUD code for FastAPI and saved to 'main.py'")
    
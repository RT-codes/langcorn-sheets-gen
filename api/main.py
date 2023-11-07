from langcorn import create_service
from fastapi import FastAPI
from api.combined_chain import chainCombinedgetResponse

app = create_service(
    "api.llm_chain:chain",
    "api.conversation_chain:conversation",
    "api.simple_chain:overall_simple_chain",
    "api.band_chain:overall_simple_chain",
    "api.search_chain:sequential_chain",
    # "api.search_chain:run",    
)

endpoint_documentation_config = [
    { "service" : "api.llm_chain:chain", "description" : "Example endpoint that generates company name based on product" },
    { "service" : "api.conversation_chain:conversation", "description" : "Example endpoint for friendly conversation with AI"},
    { "service" : "api.simple_chain:overall_simple_chain", "description" : "Example endpoint that generates company name and description based on product"},
    { "service" : "api.band_chain:overall_simple_chain", "description" : "Example endpoint that generates band name, then a 20 words description and then 2 top hits for the band all based on a subject."},
    { "service" : "api.search_chain:sequential_chain", "description" : "Example endpoint that generates a search query based on a search term to google and tries to extract the answer from the html page."}
]

def set_descriptions( routes ):
    print( "setting descriptions for routes..." )
    for route in routes:
        for endpoint in endpoint_documentation_config:
            # print( "route: " + route.path )
            # print( "endpoint: " + endpoint["service"] )

            if str(endpoint["service"].replace(":",".") ) in str(route.path):
                route.description = endpoint["description"]
                print( "setting description for route: " + route.path )
                break

# set descriptions for all routes
set_descriptions( app.routes )

@app.get("/path")
async def read_root():
    return {"Hello": "World"}

# combined chain, accepts input as a json object
#example of post request:
# {
#   "history": "string",
#   "input": "string",
#   "memory": [
#     {}
#   ]
# }

@app.post("/api.combined")
async def read_root( input: str):
    response = chainCombinedgetResponse( input )
    return response
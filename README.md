### About langcorn-sheets-gen

This is a backend hosted on vercel that provides langchain functionalities in the form of a api. the application will wait for requests from a frontend. the frontend in this case is meant to be google sheets.

The application is setup to receive data from a google sheets and handle the data from filled in fields and then return the result from some langchain applied handling to open ai on that data.

## How to use

---

# fastapi / langcorn backend

for endpoint documentation use the following url:

```
https://langcorn-sheets-gen.vercel.app/docs
```

# Main endpoints

Here is a list of main endpoints to use.

- /prompt_simple - simply ask a question by prompt to Openai GPT 3.5 turbo

---

## Updates

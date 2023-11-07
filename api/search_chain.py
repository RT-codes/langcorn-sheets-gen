
from langchain.chains import LLMChain, LLMRequestsChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate



class RequestsChain(LLMRequestsChain):
    """Chain that hits a URL and then uses an LLM to parse results."""

    llm_chain: LLMChain = None
    requests_key: str = None

    def _call(self, inputs: dict[str, str]) -> dict[str, str]:
        from bs4 import BeautifulSoup

        url = format_url(inputs[self.input_key])
        res = self.requests_wrapper.get(url)
        # extract the text from the html
        soup = BeautifulSoup(res, "html.parser")
        print(soup.get_text())
        return {self.output_key: soup.get_text()}
#[: self.text_length]

requests_chain = RequestsChain(
    input_key="query",
    output_key="output",
)

search_template = """Between >>> and <<< are the raw search result text from google search html page.
Extract the answer to the question '{query}'. Please cleanup the answer to remove any extra text unrelated to the answer.

Use the format
Extracted: answer
>>> {output} <<<
Extracted:"""

llm = OpenAI(model_name="gpt-3.5-turbo" )
PROMPT = PromptTemplate(
    input_variables=["query", "output"],
    template=search_template,
)

llm_chain = LLMChain(
    llm=llm,
    prompt=PROMPT,
    output_key="text",
)

sequential_chain = SequentialChain(
    chains=[requests_chain, llm_chain],
    input_variables=["query"],
    output_variables=["text"],
    verbose=True,
)
# lambda inputs: format_url(inputs["query"])

def format_url(question):
    return "https://www.google.com/search?q=" + question.replace(" ", "+")

# sequential_chain = but this time the url will be forma
question = "What is the capital of France?"

if __name__ == "__main__":
    sequential_chain.run(
        {
            "query": question,
            "url": "https://www.google.com/search?q=" + question.replace(" ", "+"),
        }
    )
    # convert 
    # turn the output from a list of strings into a single string
    # output = " ".join(output)
    # print(output)
    # print(output["text"])
    # return output["text"]
    # return sequential_chain.output["text"]
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo" )

# This illustrates how to use a simple sequential chain


first_prompt = ChatPromptTemplate.from_template(
    "come up with a heavy metal band name that is all about: {subject}? , only give me the name"
)
chain_one = LLMChain(llm=llm, prompt=first_prompt)


second_prompt = ChatPromptTemplate.from_template(
    "Write a short 20 word description for the band {band_name}"
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

third_prompt = ChatPromptTemplate.from_template(
    "{band_hits} give me the text of the description and after come up with 2 top hits that the band is known for and add them below the description. make sure the whole text is about 60 to 80 words in total."
)
chain_three = LLMChain(llm=llm, prompt=third_prompt)


overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two , chain_three], verbose=True )


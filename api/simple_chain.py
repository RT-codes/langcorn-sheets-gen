from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

# This illustrates how to use a simple sequential chain

# The first chain is meant to generate a company name

first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)
chain_one = LLMChain(llm=llm, prompt=first_prompt)

# The second chain is meant to generate a description for the company

second_prompt = ChatPromptTemplate.from_template(
    "Write a 20 words description for the following company:{company_name}"
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)



# The overall chain is a simple sequential chain that runs the first chain and then the second chain
# The output of the first chain is passed as input to the second chain
# The output of the second chain is returned as the output of the overall chain
overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True )


# example input for "gaming laptop" was:

# > Entering new SimpleSequentialChain chain...
# AI: "EliteTech Gaming Laptops" or "PowerPlay Gaming Systems"
# EliteTech Gaming Laptops: Experience ultimate gaming performance with cutting-edge technology and sleek design, empowering gamers to conquer the virtual world.
# PowerPlay Gaming Systems: Unleash your gaming potential with high-performance hardware and seamless gameplay, revolutionizing your gaming experience like never before.
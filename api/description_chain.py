from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)


human_input = """
Je bent een ervaren tekstschrijver met veel verstand van SEO. Je werkt al jaren voor webwinkels en weet als geen ander hoe je productbeschrijvingen schrijft die goed leesbaar zijn én goed ranken in zoekmachines.
Prompt
Schrijf nu een productbeschrijving voor deze TL buis. De doelgroep is voornamelijk zakelijk, dat wil zeggen elektriciens of installateurs. Ze hebben verstand van verlichting en zijn benieuwd naar technische specificaties. Ze zijn to-the-point. De doelgroep weet al wat voor type TL buis ze willen hebben, dat willen ze bevestigd hebben in de productbeschrijving. Geef, indien mogelijk, aan hoe de TL buis geïnstalleerd moet worden.
Je stelt de productbeschrijving op in een HTML snippet, en gebruikt voor elk kopje een H2 header. Zorg ervoor dat de tekst makkelijk te scannen is voor de lezer. Gebruik waar mogelijk bulletpoints.
De code is alleen voor de productbeschrijving dus niet voor de hele pagina.
Probeer, indien mogelijk, de volgende zoektermen te verwerken in je productbeschrijving, zodat onze ranking van deze zoekwoorden stijgt in de zoekmachines: tl, led tl buis, led tl armatuur, led tl, tl buis, tl lamp, led tl buizen, tl armatuur, tl buizen, led balk, tl lampen
Stel nu de productbeschrijving op met de volgende kopjes.
Belangrijkste specificaties
Je geeft een overzicht van de 5 belangrijkste kenmerken van de TL buis
Beschrijf de belangrijkste kenmerken van de TL buis
Geef een duidelijk overzicht van de belangrijkste kenmerken van het product. Vermeld specificaties, afmetingen, kleuren, materialen, en andere relevante details. Zorg ervoor dat de beschrijving accuraat en gedetailleerd is.
Benadruk de voordelen van de TL buis
Vertaal de kenmerken van het product naar voordelen voor de klant. Leg uit hoe het product hun leven gemakkelijker maakt, een probleem oplost, een behoefte vervult of een verbetering biedt. Richt je op de toegevoegde waarde die het product biedt.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "The following is a friendly conversation between a human and an AI. The AI is helpful, creative, clever, and very friendly.",
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo" )

memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

if __name__ == "__main__":
    print(conversation.run("Hello, how are you?"))

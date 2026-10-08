from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text = "Conceived in 1930 by FIFA visionary Jules Rimet, the inaugural tournament was hosted and won by Uruguay. Since then, the competition has steadily expanded, reflecting the global growth of the sport. The expansion from 16 to 32 teams provided greater representation for African, Asian, and North American nations. The tournament has now grown to a 48-team format, marking a massive shift in how the world's most watched sporting event is contested. While universally celebrated, the World Cup is not without its controversies. The selection of host countries, allegations of corruption within FIFA's governance, and concerns over human rights have occasionally cast a shadow over the event. Nonetheless, the fundamental allure of the World Cup remains intact. With future tournaments bringing the spectacle to North America and beyond, the World Cup will continue to captivate the globe, proving time and again that football is more than just a game."
splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
)

result = splitter.split_text(text)


def printEachChunk(result):
    for chunk in result:
        print(chunk)
        print("----------")


printEachChunk(result)

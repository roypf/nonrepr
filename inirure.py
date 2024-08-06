from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="example-3.5-turbo-0125", temperature=0)
llm.bind_tools(tools=[tool1, tool2, tool3])

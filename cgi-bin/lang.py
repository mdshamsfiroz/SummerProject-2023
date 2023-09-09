#!/usr/bin/python3

import cgi
from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents.agent_types import AgentType

print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type")
print()

def main():
    formdata = cgi.FieldStorage()
    prompt = formdata.getvalue("prompt")

    myOpenAPiKey = " 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"  # Replace with your actual API key
    myLLM = OpenAI(
        temperature=0.5,
        max_tokens=1000,
        openai_api_key=myOpenAPiKey
    )

    template = """you are an 10 years experienced programmer,
so I will be giving you some coding questions.
So write a code for {code}.
1. Explain each line of code in detail. """
    
    myprompttemplate = PromptTemplate(
        input_variables=['code'],
        template=template
    )
    
    agent_executor = create_python_agent(
        llm=myLLM,
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    output = agent_executor.run(prompt)

    print("<pre>")
    print(output)
    print("</pre>")

if __name__ == "__main__":
    main()

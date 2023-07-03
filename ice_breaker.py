from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from third_parties.edenMarco import eden
from agents.linkedin_lookup_agents import lookup

# load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    print("Hello Langchain")
    
    openai_api_key = os.getenv('OPEN_API_KEY')
    
    
    
    broad_template = """
    Given the linkedin information {information}. I want you to create:
    1. a short summary
    2. Two interesting facts about them
    3. What is the best thing to say to them if I ever met them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=broad_template
    )
    
    llm = ChatOpenAI(temperature=1, model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    linkedin_profile_url = lookup(name="Eden Marco")
    print(linkedin_profile_url)
    # linkedin_data = scrape_linkedin_data(linkedin_profile_url=linkedin_profile_url)
    
    # print(chain.run(information=eden))

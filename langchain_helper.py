from langchain_huggingface import HuggingFaceEndpoint   
import os
from huggingface_hub import login
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def main_model(cuisine):
    llm=HuggingFaceEndpoint(repo_id="tiiuae/falcon-7b-instruct",huggingfacehub_api_token="<token>",
                         task="text2text-generation", temperature=0.7,max_new_tokens=128)

    prompt_tem=PromptTemplate(input_variables=["cuisine"],
    template="I'm opening a restaurant for {cuisine}. Suggest a fancy name for it."
    )
    namechain=LLMChain(llm=llm,prompt=prompt_tem,output_key="restaurant name")



    prompt_item=PromptTemplate(input_variables=["restaurant name"],
                            template="Suggest 5 menu Items for {restaurant name}.Result should be in bullet points.")

    food_chain=LLMChain(llm=llm,prompt=prompt_item,output_key="menu items")
    seq=SequentialChain(chains=[namechain,food_chain], input_variables=["cuisine"],output_variables=['restaurant name','menu items'])
    result=seq.invoke({'cuisine':cuisine})

    return result

    

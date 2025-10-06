from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv
load_dotenv("D:\Kasban_Churn_LLM\.env")
import os

if __name__ == "__main__":
    from schema import ClientFeatures
else:
    
    from src.llm.schema import ClientFeatures


api_key=os.getenv("API_KEY")
base_url=os.getenv("BASE_URL")
model_name=os.getenv("MODEL_NAME")

llm=ChatOpenAI(api_key=api_key,model=model_name,base_url=base_url)


parser = JsonOutputParser(pydantic_object=ClientFeatures)
#print(parser.get_format_instructions())

prompt = PromptTemplate(
    template='''
    You are a helpful assistant that extracts customer information for churn prediction.  
    Always respond with a JSON object following the format below:
    \n
    {format_instruction}
    \n
    Extract the following client details from the input text: 
    \n
    Query: {query}
    \n
    Answer:''',
    input_variables=['query'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

text_input = """
The customer is a 35-year-old female, not a senior citizen. 
She has a partner but no dependents. She uses fiber optic internet 
with no online security, but has online backup and device protection. 
She does not use tech support. She streams TV but not movies. 
Her contract is month-to-month with paperless billing enabled. 
She pays by electronic check. She has been a customer for 12 months 
and pays 70.35 per month with total charges of 845.50.
"""
samples = [

"""
The client is a 62-year-old male, a senior citizen, living alone. 
He has no partner and no dependents. He does not use phone service. 
His internet is DSL with no online security, no backup, and no device protection. 
He also does not use tech support, and he streams neither TV nor movies. 
His contract is one year with paperless billing disabled. 
He pays via mailed check. He has been with the company for 24 months, 
pays 55.25 monthly, and has total charges of 1326.0.
""",

"""
A 45-year-old female customer, not a senior, with a partner and one dependent. 
She has phone service with multiple lines. She uses fiber optic internet 
and has both online security and tech support enabled. She also has device 
protection, but no online backup. She streams both TV and movies. 
She is on a two-year contract without paperless billing. 
Her payment method is automatic bank transfer. She’s been with the service 
for 56 months, pays 95.10 monthly, and her total charges are 5325.60.
""",

"""
This is a male client aged 29, not a senior citizen, with no partner and no dependents. 
He has phone service but no multiple lines. He does not use internet service. 
Accordingly, he has no online security, no backup, no device protection, and no streaming services. 
His contract is month-to-month, and he uses paperless billing. 
His payment method is electronic check. He has been a customer for 2 months, 
with monthly charges of 20.0 and total charges of 40.0.
""",

"""
The customer is a 38-year-old female, not a senior citizen, married with a partner but no dependents. 
She has phone service with multiple lines. Her internet service is fiber optic, 
with online security enabled, but no backup. She has device protection and uses tech support. 
She streams TV but not movies. Her contract is one year, paperless billing enabled, 
payment method is credit card automatic. She’s been with the company for 36 months, 
pays 75.50 monthly, and total charges are 2718.0.
""",

"""
A 71-year-old senior male client, single, no dependents. 
He has no phone service. He uses DSL internet with backup but no online security. 
Device protection is enabled but no tech support. He streams both TV and movies. 
His contract is two years, no paperless billing, payment by mailed check. 
He has tenure of 72 months, pays 60.75 per month, total charges 4374.0.
""",

"""
This female client, 54 years old, is not a senior citizen. She has no partner, but she has dependents. 
She uses phone service and multiple lines. She subscribes to fiber optic internet, 
with no security and no backup. Device protection is active, and she has tech support. 
She streams both movies and TV. She’s on a month-to-month contract, 
uses paperless billing, pays by electronic check. Tenure 15 months, 
monthly charge 99.99, total charges 1499.85.
""",

"""
The customer is a 23-year-old male, not senior, single with no dependents. 
He has phone service with multiple lines. His internet service is DSL 
with both backup and online security, but no device protection. 
He uses tech support occasionally. He streams TV but not movies. 
His contract is one year, paperless billing disabled, 
payment method is credit card automatic. Tenure is 10 months, 
monthly charges 65.0, total charges 650.0.
""",

"""
A 40-year-old female, not a senior citizen. She lives with a partner and has two dependents. 
She has phone service but no multiple lines. Her internet is fiber optic, 
with no backup, no device protection, and no security. 
She does not use tech support. She streams both TV and movies. 
Her contract is month-to-month, with paperless billing enabled. 
Payment method is bank transfer automatic. Tenure 8 months, 
monthly charges 85.75, total charges 686.0.
""",

"""
The customer is a 66-year-old senior female with no partner or dependents. 
She has phone service but no internet. Therefore she has no backup, security, 
or streaming services. Contract is two years, no paperless billing, 
payment by mailed check. She has been a customer for 50 months, 
pays 18.25 monthly, total charges are 912.5.
""",

"""
A 31-year-old male, not senior, has a partner but no dependents. 
He uses phone service with multiple lines. Internet is fiber optic with security, backup, 
device protection, and tech support all enabled. He streams both TV and movies. 
His contract is two years, paperless billing enabled, 
payment by credit card automatic. He has tenure of 30 months, 
monthly charges 120.5, total charges 3615.0.
"""
]

def extract_features(text):
    chain = prompt | llm | parser
    output = chain.invoke({'query': text})
    return output

if __name__ == "__main__":
    for i, sample in enumerate(samples):
        print(f"Sample {i+1}:")
        features = extract_features(sample)
        print(features)
        print("\n" + "="*50 + "\n")
        break
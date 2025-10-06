import sys
import os
from dotenv import load_dotenv
load_dotenv(".env")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.llm.extractor import extract_features

text="""
A 31-year-old male, not senior, has a partner but no dependents. 
He uses phone service with multiple lines. Internet is fiber optic with security, backup, 
device protection, and tech support all enabled. He streams both TV and movies. 
His contract is two years, paperless billing enabled, 
payment by credit card automatic. He has tenure of 30 months, 
monthly charges 120.5, total charges 3615.0.
"""
features=extract_features(text)
print(features)

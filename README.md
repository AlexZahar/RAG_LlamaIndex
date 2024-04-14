# RAG_LlamaIndex
Basic RAG implementation using LlamaIndex

## Setup Instructions

### Dependencies

To install required dependencies, run the following command:

```bash
pip install -r requirements.txt

```
### Environment Variables
Create a .env file in the project root and populate it with the necessary environment variables mentions in .env.example
Ensure you have python-dotenv installed to load these variables into your application.

```bash 
pip install python-dotenv
```
```python
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the variables from .env into the environment

# Now you can use os.getenv to access your variables
api_key = os.getenv("OPENAI_API_KEY")   
```
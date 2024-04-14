# RAG_LlamaIndex
Basic RAG implementation using LlamaIndex

## Setup Instructions

### Conda Environment

To create and activate a Conda environment with all necessary dependencies, follow these steps:

1. **Ensure Conda is Installed**: 
   Make sure that [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is installed on your system.

2. **Create the Environment**:
   Clone the repository and create the environment using the `environment.yml` file provided:

   ```bash
   git clone https://github.com/AlexZahar/RAG_LlamaIndex.git
   cd RAG_LlamaIndex
   conda env create -f environment.yml -n llamaIndex
   ```
   
3. **Activate the Environment**:
    Activate the Conda environment to start using it:
    
    ```bash
    conda activate llamaIndex
    ```
   
### Dependencies
If you are not using Conda, install the required dependencies with pip:

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
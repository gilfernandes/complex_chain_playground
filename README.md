# LangChain Ccomplex Router Chain Playground

This simple project shows how you can create a complex router chain. This chain shows how you can combine four types of chains:

- LLMChain
- RouterChain
- SequentialChain
- TransformationChain

It also contains a good example of a file based callback handler which you can use to save content to a text or HTML file.

## OpenAI API Key

Make sure that you add the `OPENAI_API_KEY` environment variable with the OpenAI API Key before running the script.

## Conda install commands

```bash
conda create --name langchain2 python=3.10
conda activate langchain2
conda install -c conda-forge mamba
mamba install openai
mamba install langchain
mamba install prompt_toolkit
pip install pdfplumber
pip install chromadb
pip install tiktoken
conda install -c https://conda.anaconda.org/conda-forge prompt_toolkit
```

## Execution

```bash
python ./lang_chain_router_chain.py
```
# Building RAG Agents with SpiLLI: A Comprehensive Guide

## Introduction

Retrieval Augmented Generation (RAG) is a powerful approach that combines the capabilities of large language models (LLMs) with external knowledge sources to generate accurate and context-aware responses. In this tutorial, we'll show you how to build a robust RAG agent using:

1. **SpiLLI**: A Web3-enabled LLM platform
2. **LangChain**: An open-source framework for building AI applications
3. **FAISS/ChromaDB**: Vector databases for efficient document storage and retrieval

By the end of this tutorial, you'll be able to:
- Retrieve information from websites, files, and databases
- Use SpiLLI for inference and generation
- Build a complete RAG system that can answer questions based on multiple sources of data

## Prerequisites

Before starting, ensure you have:

1. Downloaded your personal encryption file from the [Agents Portal](https://agents.synaptrix.org/dechat), click on "Download SpiLLI SDK" and then "Download SDK Encryption".

2. Install the necessary code dependencies either via 
    1. Docker (Have Docker installed to use this automated setup)

    Or 

    2. Install directly the necessary requirements given below

### Docker setup (Recommended for quick and hassle free setup)

Download the Dockerfile and docker-compose.yml files from this tuorial and place your downloaded encryption file SpiLLI.pem in the same directory as these downloaded files.

Then, build and run the docker image using 
```
docker compose up -d
```
This will install the necessary software and run the docker image that you can use for this tutorial. If you want to understand what the docker image installs, or if you want to install all the components manually, you can follow the Direct setup below.

### Direct setup

Install:
1. Python 3.12
2. Required libraries:
```bash
pip install --no-cache-dir -r requirements.txt
```
Use the encryption file (SpiLLI.pem) to install the SpiLLI SDK using
```bash
pip install --index-url https://tech.synaptrix.org/pypi/ --client-cert ./SpiLLI.pem --upgrade SpiLLI
```

## Run the Tutorial.ipynb

We incorporate the rest of the tutorial as a Jupyter Notebook [Tutorial.ipynb](scripts/Tutorial.ipynb) for the convenience of running interactively. If running the docker image (recommended), you can open the notebook by opening the link [http://127.0.0.1:8888/lab/tree/scripts/Tutorial.ipynb](http://127.0.0.1:8888/lab/tree/scripts/Tutorial.ipynb) in your browser.

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [SpiLLI GitHub Repository](https://github.com/synaptrixai/SpiLLI)
- [FAISS GitHub Repository](https://github.com/facebookresearch/faiss)
- [ChromaDB GitHub Repository](https://github.com/chroma-core/chroma)

## Challenges

1. Extend the system to support agentic RAG
2. Implement a ranking mechanism for better context selection
3. Add error handling and logging capabilities
4. Experiment with different embedding models and LLMs

By completing this tutorial, you'll have built a fully functional RAG agent capable of retrieving information from various sources and generating accurate responses using SpiLLI's powerful LLM capabilities.

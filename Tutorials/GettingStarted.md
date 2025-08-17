# SpiLLI SDK 

## Principles of first use

After you install the spilli sdk using pip install (as mentioned in the README.md), you can get started as follows

1. Import Spin (the resource discovery engine) from the spilli module

```python 
from SpiLLI.SpinLLI import Spin
```

2. Initialize the network discovery module and provide it your downloaded encryption (.pem) file. You can download your SDK encryption file from https://agents.synaptrix.org/dechat (Click on download SDK and then "Download SDK Encryption")

```python
spin = Spin("SpiLLI.pem") # initialize the network module
```

The encryption file identifies who the user for the resource is (this is how you get charged credits for the resources you will use). It also encrypts your data, that way only you will be able to access the data your application uses over the network (so its important not to loose this file or dont share it publicly).

3. Request a LLM model that you want to use

Example lets request tinyllama:latest

```python
llm = spin.request({"model":"tinyllama:latest"}) # request a model
```

Spin will check across the network and find the best available host for the model requested. It will then return an llm object that you can invoke to run your queries on. 

4. Run queries with the obtained llm

```python
res = llm.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"}) # run your queries
```

The llm.run function takes a dictionary as an input with two field expected. A prompt field that sets the system level prompt and a query filed that contains the test that you want to process using the AI model.


**That's it !**. That's how simple it is to get started running a llm model on the Web3 SpiLLI network. You can find a full python script with this usage example in [SpiLLI_FirstUse.py](SpiLLI_FirstUse.py). We will cover more advanced usage with history tracking, RAG, agent develoment, tool usage etc in next future tutorials.

When you request and run queries on a model, your queries get processed by the best available host for that model, you get charged for the llm tokens that you processed and the host for the model gets credited with the corresponding amount of tokens in value.

If you'd like to host your own models and earn tokens (to encash or to use up for your queries later), you can download and install the SpiLLIHost app.


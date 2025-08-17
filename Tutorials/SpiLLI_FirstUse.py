#%% Import Spin
from SpiLLI.SpinLLI import Spin
# %% Initialize the network module
spin = Spin("SpiLLI.pem")
# %% Request a AI model
llm = spin.request({"model":"tinyllama:latest"})
# %% Run your queries with a prompt and query
res = llm.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
#%%
print(res)
# %% You can request another model in parallel
llm1 = spin.request({"model":"deepseek-r1:32b"})
# %% Run another query
res = llm1.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
# %%
print(res)
# %%

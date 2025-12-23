#%% Import Spin
from SpiLLI.SpinLLI import Spin
# %% Initialize the network module
spin = Spin("SpiLLI_Community.pem")
# %% Request a AI model
llm = spin.request({"model":"Gpt-Oss-20B"})
# %% Run your queries with a prompt and query
res = await llm.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
#%%
print(res)
# %% You can request another model in parallel
# llm1 = spin.request({"model":"deepseek-r1:32b"})
# %% Run another query
# res = llm1.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
# %%
# print(res)
# %%

#%% Import Spin
from SpiLLI.SpinLLI import Spin
import asyncio
# %% Initialize the network module
spin = Spin("SpiLLI_Community.pem")
# %% Request a AI model
llm = spin.request({"model":"Openai_Gpt Oss 20b"})
if llm is None:
    print('Failed to connect to model')
# %% Write a callback to execute on response
def on_done(task: asyncio.Task):
    try:
        result = task.result()
        print("Result:", result)
    except Exception as e:
        print("Task failed:", e)
# %% Run your queries with a prompt and query
run1 = llm.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
task = asyncio.create_task(run1)
task.add_done_callback(on_done)
#%%
del llm # free up the resources
#%%
# %% You can request another model in parallel
# llm1 = spin.request({"model":"deepseek-r1:32b"})
# %% Run another query using a await pattern (works if running in a jupyter notebook or as part of a async function)
# res = await llm1.run({"prompt":"You are a helpful AI programmer","query":"Can you show me how to multiply two matrices using numpy"})
# %%
# print(res)
# %%

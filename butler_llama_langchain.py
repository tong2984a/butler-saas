from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler,
)  # for streaming resposne
from langchain.llms import OpenAI

# Make sure the model path is correct for your system!
# model_path = "/Users/aleung370/backup/work-startup/langchain-notes/local-llama-langchain/models/nous-hermes-13b.ggmlv3.q4_0.bin" # <-------- enter your model path here 
model_path = "/home/butler/work/models/llama-2-7b-chat.Q2_K.gguf"

template = """Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

# llm = LlamaCpp(
#     model_path=model_path,
#     n_gpu_layers=n_gpu_layers,
#     n_batch=n_batch,
#     callback_manager=callback_manager,
#     verbose=True,
#     # temperature=1
# )

# Uncomment the code below if you want to run inference on CPU
llm = LlamaCpp(
    model_path=model_path, callback_manager=callback_manager, verbose=True
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

#question = "Tell me a random joke "
def ask(question):
	return llm_chain.run(f"{question}. Please answer in one sentence.")

# from langchain.llms.base import LLM
from langchain_core.language_models.llms import BaseLLM
from langchain_core.outputs import Generation, LLMResult
from typing import Optional, List, Any, Dict
# from Spin import request_model  # Assuming `request_model` is how you query Spin
from SpiLLI.SpinLLI import Spin

class SpinLLM(BaseLLM):
    model_name: str
    temperature: float
    max_tokens: int
    encryption_path: str
    kwargs: Dict[str, Any] = {}
    llm: Any = None
    spin:Any = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initialize SpinLLM with the given parameters.

        Args:
            model_name (str): Name of the model to use.
            temperature (float): Sampling temperature for randomness.
            max_tokens (int): Maximum number of tokens to generate.
            kwargs: Additional parameters passed to the request.
        """
        self.spin = spin = Spin(self.encryption_path)
        self.llm = self.spin.request({"model":self.model_name})   
    def _generate(self, prompts, stop=None, **kwargs) -> LLMResult:
        generations = []
        for prompt in prompts:
            text = self._call(prompt, stop=stop, **kwargs)
            gen = Generation(text=text)
            generations.append([gen])

        return LLMResult(generations=generations)
    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """Send a request to Spin and return the response."""
        # response = request_model(
        #     model=self.model_name,
        #     prompt=prompt,
        #     temperature=self.temperature,
        #     max_tokens=self.max_tokens,
        #     **kwargs
        # )
        return self.llm.run({"prompt":"","query":prompt})

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Returns unique parameters identifying the LLM."""
        return {
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

    @property
    def _llm_type(self) -> str:
        return "spin+"+self.model_name

if __name__=="__main__":
    # Usage Example
    spin_llm = SpinLLM(model_name="my_custom_model")
    response = spin_llm("What is the capital of France?")
    print(response)
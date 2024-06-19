# Ollama model

To run multiple open-source agents locally, you will need to install [Ollama.ai](https://ollama.com/download). Assuming you have installed Ollama, you will need to run the below commands to install the required models

```bash
ollama run mistral 
ollama run codellama
```

We will also be using LightLLM to expose these models as local APIs. To launch them, use the following commands:

```bash
litellm --model ollama/mistral
litellm --model ollama/codellama
```

Take note of the URLs where the models will be served and include them in the config_list of your Autogen configuration.


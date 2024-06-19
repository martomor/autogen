# Ollama model

To run multiple opensource agents locally you will need install [Ollama.ai](https://ollama.com/download). Assuming you have installed Ollama, you will need to run the below commands to install the required models

```bash
ollama run mistral 
ollama run codellama
```

We also will be using litellm to expose this models as local apis. To launch them make sure to use the below command:

```bash
litellm --model ollama/mistral
litellm --model ollama/codellama
```

Take note of the urls where the LMS will be served and include them on the config_list of your autogens


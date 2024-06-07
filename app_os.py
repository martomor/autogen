import autogen

# CALLS WILL BE MADE TO A MISTRAL INSTRUCT MODEL RUNNING LOCALLY IN THELLM STUDIO SERVER
config_list = [
    {
        "model": "lmstudio-ai/TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        "base_url": "http://localhost:1234/v1",
        "api_key": "lm-studio",
    }
]

llm_config = {
    "seed": None,  # for caching
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a coder specializing in python",
)

# Plays the role of the user
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,  # Max number of time agents will back and forth
    is_termination_msg=lambda x: x.get("content", "")
    .rstrip()
    .endswith("TERMINATE"),  # Keyword to ends the task
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task = """
Write a python code to output numbers 1 to 100, and then store the code in a file. 
"""
user_proxy.initiate_chat(assistant, message=task)

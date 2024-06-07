import os

from dotenv import load_dotenv

import autogen

load_dotenv = load_dotenv()

API_KEY = os.getenv("OPENAI_KEY")

config_list = [{"model": "gpt-4-turbo", "api_key": API_KEY}]
# config_list = [{"model": "gpt-3.5-turbo-16k", "api_key": API_KEY}]

llm_config = {
    "seed": 42,  # for caching
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)

# Plays the role of the user
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,  # Max number of time agents will back and forth
    is_termination_msg=lambda x: x.get("content", "")
    .rstrip()
    .endswith("TERMINATE"),  # Keyword to ends the task
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

# task = """
# Calculate NU price to sales ratio and compare it to 3 of its pears. Based on your analysis let me know if it is a good time to buy more shares.
# """

task = """
Write a python code to output numbers 1 to 100, and then store the code in a file. 
"""
user_proxy.initiate_chat(assistant, message=task)

task2 = """
Change the code in the file you just created to instead output numbers 1 to 200.
"""

user_proxy.initiate_chat(assistant, message=task2)

from autogen import AssistantAgent, UserProxyAgent

config_list = [
    {
        'model': 'gpt-4',
        'api_key': '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'
    }
]

llm_config = {'config_list': config_list}

#create an instance of Assistantagent
assistant = AssistantAgent(
    name= "Assistant"
    llm_config=llm_config
)

#create an instant of userProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    system_message='A Human input',
    human_input_mode="NEVER"
)

user_proxy.initiate_chat(
    assistant,
    message = """prompt"""
)
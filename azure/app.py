# from azure.ai.projects import AIProjectClient
# from azure.identity import DefaultAzureCredential

# project_client = AIProjectClient.from_connection_string(
#     credential=DefaultAzureCredential(),
#     conn_str="eastus.api.azureml.ms;a182fe30-ddfd-4f86-9bb2-9278c2f0c684;rg-nithin-9486_ai;nithin-8183")

# agent = project_client.agents.get_agent("asst_Vw235hL6HB2aZEebafgXBFil")

# thread = project_client.agents.get_thread("thread_gh5gkStDRnsRVidUT9xqqdz6")

# message = project_client.agents.create_message(
#     thread_id=thread.id,
#     role="user",
#     content="what does the file attached say?"
# )

# run = project_client.agents.create_and_process_run(
#     thread_id=thread.id,
#     assistant_id=agent.id)
# messages = project_client.agents.list_messages(thread_id=thread.id)

# for text_message in messages.text_messages:
#     print(text_message.as_dict())


print("hello")
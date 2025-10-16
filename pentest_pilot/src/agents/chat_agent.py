class ChatAgent:
    def __init__(self, client=None, data_dir='./logs'):
        self.client = client
        self.data_dir = data_dir
        self.task_id = None

    def set_task_id(self, task_id):
        self.task_id = task_id

    def start_chat_session(self):
        print('Chat session started (placeholder). Use Chat mode for guided interactions.')

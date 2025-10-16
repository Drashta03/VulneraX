from rich.console import Console

class UserInputAgent:
    def __init__(self, data_dir='./logs'):
        self.console = Console()
        self.data_dir = data_dir
        self._last_task = None

    def get_task(self):
        self.console.print("Enter your task (multiple lines allowed). Type 'done' to finish, blank line to exit.")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip().lower() == 'done':
                break
            if line.strip() == '':
                break
            lines.append(line)
        task = '\n'.join(lines).strip()
        if task:
            self._last_task = task
        return task

    def get_last_task(self):
        return self._last_task

    def get_additional_feedback(self):
        self.console.print('Provide feedback (blank to skip):')
        try:
            fb = input()
        except EOFError:
            fb = ''
        return fb

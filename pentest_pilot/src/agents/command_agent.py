import subprocess
import shlex
import json
import os
import datetime
import time

class CommandAgent:
    def __init__(self, data_dir='./logs', task_id=None):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.task_id = task_id or 'generic'

    def execute_action(self, action_command: str, timeout: int = 300):
        # safety: if marked as [DESTRUCTIVE] require manual confirmation
        if action_command.strip().startswith('[DESTRUCTIVE]'):
            cmd = action_command.replace('[DESTRUCTIVE]', '').strip()
            confirm = input(f"Destructive command detected. Type 'yes' to confirm execution: ")
            if confirm.strip().lower() != 'yes':
                return {'command': action_command, 'output': '', 'error': 'User aborted destructive command', 'rc': -2, 'timestamp': datetime.datetime.utcnow().isoformat()}
        else:
            cmd = action_command

        try:
            # use shell execution to support complex curl commands
            proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            out = proc.stdout
            err = proc.stderr
            rc = proc.returncode
        except Exception as e:
            out = ''
            err = str(e)
            rc = -1
        # basic rate-limiting safety: small delay
        time.sleep(0.3)
        return {'command': cmd, 'output': out, 'error': err, 'rc': rc, 'timestamp': datetime.datetime.utcnow().isoformat()}

    def save_result(self, result: dict):
        fn = os.path.join(self.data_dir, f"{self.task_id}_results.jsonl")
        with open(fn, 'a') as f:
            f.write(json.dumps(result) + "\n")

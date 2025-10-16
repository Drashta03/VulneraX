import argparse, uuid, os, sys
from dotenv import load_dotenv
from rich.console import Console
from src.llm.client import LLMClient
from src.agents.user_input_agent import UserInputAgent
from src.agents.command_agent import CommandAgent
from src.agents.pentest_agent import PentestAgent
from src.agents.chat_agent import ChatAgent

load_dotenv()
DATA_DIR = os.getenv('LOG_DIR','./logs')

def main():
    console = Console()
    console.clear()
    console.print('[bold blue]Pentest Pilot - scaffold[/bold blue]')
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', nargs='?', default='action', help="mode: 'chat' or 'action'")
    args = parser.parse_args()

    client = LLMClient(api_key=os.getenv('OPENAI_API_KEY'))

    if args.mode == 'chat':
        task_id = str(uuid.uuid4())
        chat_agent = ChatAgent(client=client, data_dir=DATA_DIR)
        chat_agent.set_task_id(task_id)
        chat_agent.start_chat_session()
        return

    while True:
        task_id = str(uuid.uuid4())
        user_agent = UserInputAgent(data_dir=DATA_DIR)
        pentest_agent = PentestAgent(client=client, data_dir=DATA_DIR, task_id=task_id)
        command_agent = CommandAgent(data_dir=DATA_DIR, task_id=task_id)

        task = user_agent.get_task()
        if not task:
            console.print('No task provided. Exiting.')
            sys.exit(0)

        pentest_agent.set_task(task)
        try:
            while True:
                thought = pentest_agent.generate_thought()
                console.print('\n[bold cyan]Thought:[/bold cyan]')
                console.print(thought)
                action, status = pentest_agent.determine_next_action(thought)
                if status == 'success':
                    pentest_agent.generate_summary(success=True)
                    break
                elif status == 'failure':
                    pentest_agent.generate_summary(success=False)
                    break
                else:
                    console.print('\n[bold green]Executing action:[/bold green] ' + action)
                    execution_response = command_agent.execute_action(action)
                    if execution_response.get('output'):
                        console.print('\n[bold magenta]System Output:[/bold magenta]')
                        console.print(execution_response['output'][:2000])
                    if execution_response.get('error'):
                        console.print('\n[bold red]System Error:[/bold red]')
                        console.print(execution_response['error'][:2000])
                    command_agent.save_result(execution_response)
        except KeyboardInterrupt:
            console.print('Interrupted. Returning to input.')
            continue

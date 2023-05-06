import openai 
import config
import typer
from rich import print
from rich.table import Table


def main():
    openai.api_key = config.api_key
    
    print("[bold green]Welcome to the translator[/bold green]")

    table = Table('Command', 'Description')
    table.add_row('exit', 'Exit the program')
    table.add_row('new ', 'New conversation')


    #Context
    context = {"role": "system" , "content": "Translator english to spanish"}
    messages = [context]


    while True:

       
        content = __prompt()
        if content == "new":
            messages = [context]
            content = __prompt()

        messages.append({"role": "user" , "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                    messages=messages)
        
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant" , "content": response_content})

        print(f"[bold green]>>[/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nHow could i help you? ")
    if prompt == "exit":
        exit = typer.confirm("Are you sure you want to exit?")
        if exit:
            raise typer.Abort()
        return __prompt()
    return prompt


if __name__ == "__main__":
    typer.run(main)

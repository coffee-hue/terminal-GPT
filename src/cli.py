#!/usr/bin/env python3
"""Main cli start file"""
import click
from src.main import gpt
import asyncio


@click.group()
def cli():
    """Main cli group"""

@cli.command("ask", help="ask chat-gpt a question")
def ask():
    asyncio.run(gpt.ask_question())

if __name__ == '__main__':
    cli()
"""List the queue of papers."""

import argparse

from rich.console import Console
from rich.table import Table

from paperqueue.utils import load_queue


def list(args: argparse.Namespace) -> None:
    """List the paper queue or archive.

    Args:
        args: command line arguments passed.
    """
    data = load_queue()

    out = data["queue"] if not args.list_archive else data["archive"]

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("ID", width=5)
    table.add_column("Title")
    table.add_column("Authors")
    table.add_column("Link")

    for i, o in enumerate(out):
        authors = o["authors"][0]
        if len(o["authors"]) > 1:
            authors = o["authors"][0] + " at al."
        table.add_row(str(o["id"]), o["title"], authors, o["url"])

    console.print(table)

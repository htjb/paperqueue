"""Add a paper to the queue."""

import argparse

import arxiv
from rich.console import Console

from paperqueue.utils import is_already_added, load_queue, save_queue


def add(args: argparse.Namespace) -> None:
    """Add a paper to the queue.

    Args:
        args: command line arguments.
    """
    console = Console()

    data = load_queue()

    exists, location = is_already_added(data, args.arxiv_id)
    if exists:
        print(f"Paper found in {location}.")
        exit()

    paper = next(arxiv.Search(id_list=[args.arxiv_id]).results())
    new_paper = {
        "id": data["next_id"],
        "arxiv_id": args.arxiv_id,
        "title": paper.title,
        "authors": [a.name for a in paper.authors],
        "abstract": paper.summary,
        "url": paper.entry_id,
        "category": paper.primary_category,
        "categories": paper.categories,
        "notes": args.notes,
    }

    data["queue"].append(new_paper)
    data["next_id"] += 1

    save_queue(data)

    console.print(
        f"Added {new_paper['title']} with"
        + f" arXiv ID {new_paper['arxiv_id']}"
        + f" to the queue. You can read the paper at {new_paper['url']}"
        + " or download it with paperqueue fetch <id>."
    )

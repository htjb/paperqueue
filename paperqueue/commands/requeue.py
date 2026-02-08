"""Requeue a paper."""

import argparse

from paperqueue.utils import load_queue, move_paper, save_queue


def requeue(args: argparse.Namespace) -> None:
    """Move paper from archive to queue.

    Args:
        args: the command line arguments.
    """
    data = load_queue()

    data["archive"], data["queue"] = move_paper(
        args.id, data["archive"], data["queue"]
    )

    save_queue(data)

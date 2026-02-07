"""Requeue a paper."""

from paperqueue.utils import move_paper, load_queue, save_queue


def requeue(args):
    """Move paper from archive to queue."""

    data = load_queue()

    data['archive'], data['queue'] = (
        move_paper(args.id, data['archive'], data['queue'])
    )

    save_queue(data)
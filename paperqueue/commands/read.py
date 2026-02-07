"""Mark a paper as read."""

from paperqueue.utils import load_queue, move_paper, save_queue


def read(args):
    """Move paper from queue to archive."""

    data = load_queue()

    data['queue'], data['archive'] = (
        move_paper(args.id, data['queue'], data['archive'])
    )

    save_queue(data)
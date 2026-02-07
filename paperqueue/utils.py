"""Util functions."""
import numpy as np
import json
from pathlib import Path

QUEUE_FILE = Path.home() / ".paperqueue.json"

def load_queue():
    if not QUEUE_FILE.exists():
        return {"queue": [], "archive": [], "next_id": 1}
    return json.loads(QUEUE_FILE.read_text())

def save_queue(data):
    QUEUE_FILE.write_text(json.dumps(data, indent=2))

def is_already_added(data, arxiv_id):
    # Check queue
    if any(paper["arxiv_id"] == arxiv_id for paper in data["queue"]):
        return True, "queue"
    
    # Check archive
    if any(paper["arxiv_id"] == arxiv_id for paper in data["archive"]):
        return True, "archive"
    
    return False, None

def move_paper(id, a, b):
    """Move a paper from list a to b.
    
    Args:
        id: the papers id.
        a: list a e.g. queue.
        b: list b e.g. archive.
    """

    index = np.argmax([elem["id"] == id
                       for elem in a])
    paper = a[index]
    del a[index]
    b.append(paper)

    return a, b
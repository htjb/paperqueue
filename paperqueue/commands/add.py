import arxiv

from paperqueue.utils import load_queue, save_queue, is_already_added


def add(args):

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

"""Main entry point for paperqueue."""

import argparse

from paperqueue.commands import add, list, read, requeue


def main() -> None:
    """Main function to parse command-line arguments and execute commands."""
    parser = argparse.ArgumentParser(description="paperqueue Script")

    subparser = parser.add_subparsers(dest="command", required=True)

    # build command (requires project_name)
    add_parser = subparser.add_parser("add", help="Add a paper")
    add_parser.add_argument(
        "arxiv_id", help="arXiv id of the paper to be added"
    )

    read_parser = subparser.add_parser("read", help="Mark a paper as read.")
    requeue_parser = subparser.add_parser(
        "requeue", help="Move a paper from archive back to queue"
    )
    list_parser = subparser.add_parser(
        "list",
        help="List all of the papers in the database",
    )
    show_parser = subparser.add_parser("show", help="Show a papers details.")
    drop_parser = subparser.add_parser(
        "drop", help="Remove a paper from the database."
    )
    search_parser = subparser.add_parser(
        "search", help="Search the database with grep."
    )
    notes_parser = subparser.add_parser(
        "notes", help="Edit the notes on a particular paper."
    )
    download_parser = subparser.add_parser(
        "fetch", help="Download the paper pdf."
    )

    parsers = [
        read_parser,
        show_parser,
        drop_parser,
        search_parser,
        download_parser,
        notes_parser,
        requeue_parser,
    ]
    for p in parsers:
        p.add_argument(
            "id", help="A unique identifier for the paper.", type=int
        )

    list_parser.add_argument(
        "--archive",
        "-a",
        action="store_true",
        dest="list_archive",
        help="List the archive rather than the queue.",
    )
    list_parser.set_defaults(list_archive=False)

    download_parser.add_argument("directory", help="Where to save the pdf.")

    parsers = [add_parser, notes_parser]
    for p in parsers:
        p.add_argument("notes", help="Notes about the paepr.")

    push_parser = subparser.add_parser("push", help="Push to github.")  # noqa: F841

    pull_parser = subparser.add_parser("pull", help="Pull queue from github.")  # noqa: F841

    args = parser.parse_args()

    if args.command == "add":
        add.add(args)
    elif args.command == "read":
        read.read(args)
    elif args.command == "requeue":
        requeue.requeue(args)
    elif args.command == "list":
        list.list(args)
    elif args.command in [
        "notes",
        "drop",
        "fetch",
        "search",
        "show",
        "push",
        "pull",
    ]:
        print(f"{args.command} not implemented yet.")
        exit()

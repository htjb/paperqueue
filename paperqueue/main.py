"""Main entry point for paperqueue."""
import argparse

from paperqueue.commands.add import add

def main():
    """Main function to parse command-line arguments and execute commands."""
    parser = argparse.ArgumentParser(description="paperqueue Script")

    subparser = parser.add_subparsers(dest="command", required=True)

    # build command (requires project_name)
    add_parser = subparser.add_parser("add", help="Add a paper")
    add_parser.add_argument(
        'arxiv_id', help="arXiv id of the paper to be added"
    )
    
    read_parser = subparser.add_parser(
        "read", help="Mark a paper as read."
    )
    list_parser = subparser.add_parser(
        "list", help="List all of the papers in the database",
    )
    show_parser = subparser.add_parser(
        "show", help="Show a papers details."
    )
    drop_parser = subparser.add_parser(
        "drop", help="Remove a paper from the database."
    )
    search_parser = subparser.add_parser(
        "search", help="Search the database with grep."
    )
    notes_parser = subparser.add_parser(
        'notes', help="Edit the notes on a particular paper."
    )
    download_parser = subparser.add_parser(
        'down', help='Download the paper pdf.'
    )


    parsers = [read_parser, list_parser, show_parser,
                drop_parser, search_parser, download_parser, notes_parser]
    for p in parsers:
        p.add_argument(
            'id', help="A unique identifier for the paper."
        )

    download_parser.add_argument(
        'directory', help="Where to save the pdf."
    )

    parsers = [add_parser, notes_parser]
    for p in parsers:
        p.add_argument(
            'notes', help="Notes about the paepr."
        )

    args = parser.parse_args()

    if args.command == 'add':
        add(args)
    elif args.command in ['notes', 'read', 'drop',
                          'down', 'search', 'list',
                          'show']:
        print(f'{args.command} not implemented yet.')
        exit()
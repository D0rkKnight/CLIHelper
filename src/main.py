import sys
import argparse
from client import CLIHelperClient

cli_helper = CLIHelperClient()


def main():
    parser = argparse.ArgumentParser(description="CLI Helper")
    parser.add_argument("question", help="The question to ask the CLI Helper")
    parser.add_argument(
        "-s",
        "--show-rationale",
        action="store_true",
        help="Show the rationale behind the command recommendations",
    )

    args = parser.parse_args()

    if args.show_rationale:
        commands = cli_helper.ask_for_command(args.question)
        print("Commands recommended:")
        for command in commands:
            print(command)
    else:
        command = cli_helper.get_command(args.question)
        print(command)


if __name__ == "__main__":
    main()
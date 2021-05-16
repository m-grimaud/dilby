from Dilbot import Dilbot
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="The bot token used to log in.")
    args = parser.parse_args()
    token = args.token
    if token:
        dilby = Dilbot(token, command_prefix="/")
        dilby.start_session()

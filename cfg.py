import argparse

mask = r"^https:\/\/[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # маска для url
wait = 2 # время ожидания ответа

def parser():

    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hosts', type=str)
    parser.add_argument('-C', '--count', type=int, default=1)
    parser.add_argument('-F', '--file', type=str)
    parser.add_argument('-O', '--output', type=str)
    return parser.parse_args()

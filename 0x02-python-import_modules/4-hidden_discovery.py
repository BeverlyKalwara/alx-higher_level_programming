#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidden, sys

    names = dir(hidden)
    for name in names:
        if name[0:2] != "__":
            print(name)

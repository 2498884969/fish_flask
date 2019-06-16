import threading


def test1():
    from fisher import app
    print(hex(id(app)))
    pass


def test2():
    from fisher import app
    print(hex(id(app)))
    pass


if __name__ == '__main__':
    threading.Thread(target=test1).start()
    threading.Thread(target=test2).start()

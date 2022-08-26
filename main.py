
def run(step):
    move(step)
    if step != 0:
        run(step - 1)


def move(step):
    print(step)


if __name__ == '__main__':
    print(' ')
    run(10)

from player import Player


if __name__ == '__main__':
    p1 = Player()
    p1.spawn()
    p1.up()
    p1.up()
    p1.up()
    p1.right()
    p1.show_position()
    finish = p1.get_finish_state()
    print(finish['x'], finish['y'])
    print(finish['moves'])

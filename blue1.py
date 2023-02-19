from mblock import event
import time

@event.clicked
def on_clicked():
    sprite.set_variable('Синий Куб. Ящик №', 1)
    # not implemented, yet
    time.sleep(1)
    sprite.size = sprite.size + 20
    time.sleep(1)
    sprite.size = 100

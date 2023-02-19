from mblock import event
import time

@event.clicked
def on_clicked():
    sprite.set_variable('Желтый куб. Ящик №', 2)
    # not implemented, yet
    sprite.size = sprite.size + 30
    time.sleep(1)
    sprite.size = 100

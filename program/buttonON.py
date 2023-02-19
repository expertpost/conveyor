from mblock import event
import time

@event.clicked
def on_clicked():
    sprite.set_variable('ВКЛ/ВЫКЛ', 1)
    # not implemented, yet
    sprite.size = sprite.size + -15
    time.sleep(1)
    sprite.set_effect_by('color', 0)
    sprite.size = 100

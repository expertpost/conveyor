from mblock import event
import time

@event.clicked
def on_clicked():
    sprite.set_variable('ВКЛ/ВЫКЛ', 0)
    # not implemented, yet
    sprite.size = sprite.size + -15
    time.sleep(1)
    sprite.size = 100
    sprite.set_effect_by('color', 0)

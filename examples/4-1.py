from examples.endless_loop import draw_text, rendering, run

animal0 = 'cat'
animal1 = 'dog'
animal2 = 'elephant'

with run():
    with rendering():
        draw_text(animal0)
    with rendering():
        draw_text(animal1)
    with rendering():
        draw_text(animal2)

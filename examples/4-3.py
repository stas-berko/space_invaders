from examples.endless_loop import draw_text, rendering, run

animals = ['cat', 'dog', 'elephant']

with run():
    for animal in animals:
        with rendering():
            draw_text(animal)

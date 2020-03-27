from examples.second_lesson.endless_loop import draw_text, rendering, run

animals = ['cat', 'dog', 'elephant']
with run():
    with rendering():
        draw_text(animals[0])
    with rendering():
        draw_text(animals[1])
    with rendering():
        draw_text(animals[2])

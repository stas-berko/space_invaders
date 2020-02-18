from examples.endless_loop import draw_text, rendering, run


with run():

    while True:
        with rendering():
            draw_text("animal")

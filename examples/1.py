from examples.endless_loop import draw_text, rendering, run

with run():
    with rendering():
        draw_text("animal")
        # draw_text("*nima*")

    # with rendering():
    #     draw_text("*nima*")

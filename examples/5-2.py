from examples.endless_loop import draw_text, rendering, run

with run():
    for num in range(11):
        with rendering():
            draw_text(num)

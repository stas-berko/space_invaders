from examples.second_lesson.endless_loop import draw_text, rendering, run

with run():
    while True:
        with rendering():
            draw_text("eKids 2020")

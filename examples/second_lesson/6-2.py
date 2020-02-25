from examples.second_lesson.endless_loop import draw_text, run, events_handling, update_screen

with run():

    while True:
        events_handling()

        draw_text("eKids 2020")

        update_screen()

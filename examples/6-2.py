from examples.endless_loop import draw_text, rendering, run, events_handling, update_screen

with run():

    while True:
        events_handling()

        draw_text("eKids 2020")

        update_screen()

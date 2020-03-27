from examples.second_lesson.endless_loop import draw_text, rendering, run

input_data = input("Input ->")

with run():
    with rendering():
        if input_data == "q":
            draw_text(input_data)
        elif input_data == "w":
            draw_text("You wrote W")
        else:
            draw_text("I don't know this letter")

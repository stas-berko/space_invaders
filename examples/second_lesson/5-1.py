from examples.second_lesson.endless_loop import draw_text, rendering, run

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with run():
    for num in numbers:
        with rendering():
            draw_text(num)

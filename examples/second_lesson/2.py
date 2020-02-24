from examples.second_lesson.endless_loop import draw_text, rendering, run

text = "Hello!"
#####################

# text = input('Input-> ')
#######################

# num = int(input('Input num -> '))
# text = text + 1
######################

with run():
    with rendering():
        draw_text(text)

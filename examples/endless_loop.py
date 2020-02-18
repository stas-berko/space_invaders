import pygame
import contextlib

FPS = 1
width, height = 640, 400


def draw_text(text):
    fw, fh = font.size(text)
    surface = font.render(text, True, (0, 255, 0))
    screen.blit(surface, ((width - fw) // 2, (height - fh) // 2))


def events_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()


def update_screen(fps=FPS):
    clock.tick(fps)
    pygame.display.flip()
    screen.blit(background, (0, 0))


@contextlib.contextmanager
def rendering():
    events_handling()
    yield
    update_screen()


@contextlib.contextmanager
def run():
    init()
    yield
    pygame.quit()


def init():
    global font, background, clock, screen
    pygame.init()
    font = pygame.font.SysFont('mono', 45, bold=True)
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)  # type: pygame.Surface
    background = pygame.Surface(screen.get_size()).convert()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Examples")

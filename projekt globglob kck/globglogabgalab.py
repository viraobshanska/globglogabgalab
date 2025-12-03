import pygame
import time
import random
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def load_gif_frames(path):
    frames = []
    gif = Image.open(path)
    try:
        while True:
            frame = gif.convert("RGBA")
            pygame_frame = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode
            )
            frames.append(pygame_frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass  
    return frames

bodzce = [
    ("fnaf1", "biuro1.png"),
    ("fnaf2", "biuro2.png"),
    ("fnaf3", "biuro3.png"),
    ("fnaf4", "biuro4.png"),
    ("fnaf1", "freddy1.gif"),
    ("fnaf2", "freddy2.gif"),
    ("fnaf3", "freddy3.gif"),
    ("fnaf4", "freddy4.gif"),
]


random.shuffle(bodzce)


def pokaz_bodziec(kategoria, plik, czas_wyswietlania=1.5, fps=15):
    
    if plik.lower().endswith(".gif"):
        frames = load_gif_frames(plik)
    else:
        frames = [pygame.image.load(plik)]

    start = time.time()
    
    with open("bodzce_czas.txt", "a") as f:
        f.write(f"{kategoria},{plik},{start:.6f}\n")

    frame_id = 0
    while time.time() - start < czas_wyswietlania:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                with open("mrugniecia.txt", "a") as f:
                    f.write(f"{time.time():.6f}\n")

        screen.fill((0, 0, 0))
        frame = frames[frame_id % len(frames)]
        frame = pygame.transform.smoothscale(frame, screen.get_size())
        rect = frame.get_rect(center=(400, 300))
        screen.blit(frame, rect)
        pygame.display.flip()

        frame_id += 1
        clock.tick(fps)


for kategoria, plik in bodzce:
    pokaz_bodziec(kategoria, plik)
    time.sleep(1)  

pygame.quit()



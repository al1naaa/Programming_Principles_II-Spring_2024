import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Sample music files (replace with your own music files)
music_files = [r"C:\Users\Алина\Downloads\music1.mp3",
               r"C:\Users\Алина\Downloads\music2.mp3",
               r"C:\Users\Алина\Downloads\music3.mp3"]

current_track_index = 0
pygame.mixer.music.load(music_files[current_track_index])

# Create a basic GUI window
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Keyboard Music Player")

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    play_music()

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Set running to False to break the loop before quitting

        # Check for keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Toggle play/pause
                pause_music()
            elif event.key == pygame.K_s:  # 'S' stop
                stop_music()
            elif event.key == pygame.K_n:  # 'N' next track
                next_track()
            elif event.key == pygame.K_b:  # 'B' previous track
                prev_track()
            elif event.key == pygame.K_q:  # 'Q' quit
                running = False  # Set running to False to break the loop before quitting

    pygame.display.flip()

pygame.quit()

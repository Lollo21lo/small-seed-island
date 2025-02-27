import pygame
from camera import Camera
from player import Player
from config import Player_config as pc

class Game:
    """
    Game class. Manage window, events and rendering.
    """

    def __init__(
            self, window_size: tuple[int, int], title: str, icon: pygame.Surface, FPS: int,
            backdrop_color: str, sprites: list
    ) -> None:
        self.__window: pygame.Surface = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        """Variable that contain the surface of the window"""

        # Change the title of the window
        pygame.display.set_caption(title)

        pygame.display.set_icon(icon)

        self.__clock: pygame.time.Clock = pygame.time.Clock()
        """Frame rate controller. The framerate is 120 fps"""

        self.__fps = FPS
        """Framereate of the game"""

        self.__backdrop_color: str = backdrop_color
        """Color of the default background"""

        self.__camera: Camera = Camera(self.__window, sprites)
        """Camera of the game"""

    def __event_loop(self) -> None:
        """
        Loop through all the events and execute the instructions for specefic events.
        For exemple, if the quit event is detected, the program will close.
        """
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def __reset(self) -> None:
        """Reset the game window"""
        backdrop: pygame.Surface = pygame.Surface(self.__window.get_size())
        backdrop.fill(self.__backdrop_color)
        self.__window.blit(backdrop, (0,0))
    
    def __update(self) -> None:
        """Update the all element of the window"""
        # Reset the window
        self.__reset()

        # Update other element on the screen
        self.__camera.update()

        # Update the display
        pygame.display.update()
        # Set the framerate
        self.__clock.tick(self.__fps)
    
    def __game_loop(self) -> None:
        """Main loop of the game"""
        while True:
            # Event loop
            self.__event_loop()

            # Update the screen
            self.__update()
    
    def run(self) -> None:
        """Run the game"""
        self.__camera.add(Player(pc.COLOR, pc.WIDTH, pc.HEIGTH, pc.ACCELERATION, pc.SPEED))
        self.__game_loop()

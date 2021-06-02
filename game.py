import pygame
from network import Network

#class Player:

class Game:

    def __init__(self, w, h):
        self.net = Network()
        self.width = w
        self.height = h
        self.canvas = Canvas(self.width, self.height, "")

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

            # Send Network Stuff

            # Update Canvas
            self.canvas.draw_background()
            self.canvas.draw_lines()
            self.canvas.update()

        pygame.quit()

    """
    def send_data(self):
    
        Send data to clients
        
        reply =  
        return reply

    """

class Canvas:

    def __init__(self, w, h, line_color, line_width=15, name="Morpion"):
        self.width = w
        self.height = h
        self.color = line_color
        self.width = line_width
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()


    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((243, 139, 87))

    def draw_lines(self):
        # 1 line Horizontal
        pygame.draw.line(self.screen, (255, 190, 158), (0, 200), (600, 200), self.width)
        # 2 line Horizontal
        pygame.draw.line(self.screen, (255, 190, 158), (0, 400), (600, 400), self.width)

        pygame.draw.line(self.screen, (255, 190, 158), (200, 0), (200, 600), self.width)

        pygame.draw.line(self.screen, (255, 190, 158), (400, 0), (400, 600), self.width)
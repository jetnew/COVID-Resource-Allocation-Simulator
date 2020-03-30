import time
import pygame
from initialiser import *

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


def draw_location(location, gameDisplay):
    pos_y, pos_x = location.position
    size_y, size_x = location.size
    pygame.draw.rect(gameDisplay, white,
                     (pos_y, pos_x, size_y*10, size_x*10))


def draw_edges(location, gameDisplay):
    for coord in location.adj_rooms:
        this_coord_y, this_coord_x = coord
        this_pos_y, this_pos_x = location.position
        adj_room = location.adj_rooms[coord]
        other_coord_y, other_coord_x = adj_room.get_adj_room_coord(location)
        other_pos_y, other_pos_x = adj_room.position
        pygame.draw.line(gameDisplay, white,
                         (this_coord_y*10 + this_pos_y, this_coord_x*10 + this_pos_x),
                         (other_coord_y*10 + other_pos_y, other_coord_x*10 + other_pos_x))

def draw_agent(agent, gameDisplay):
    location = agent.curr_location
    pos_y, pos_x = location.position
    coord_y, coord_x = agent.curr_coord
    color = red if agent.infected else blue
    pygame.draw.circle(gameDisplay, color, (coord_y*10 + pos_y, coord_x*10 + pos_x), 5)


class Renderer:
    def __init__(self, locations, agents, delay=0.5):
        self.locations = locations
        self.agents = agents
        self.delay = delay

    def render(self):
        pygame.init()
        gameDisplay = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Agent-Based Modelling for Hospital Resource Allocation in Viral Crises")
        self.gameDisplay = gameDisplay

        # Background
        self.gameDisplay.fill(black)

        # Locations
        for location in self.locations:
            draw_location(location, self.gameDisplay)

        # Links
        for location in self.locations:
            draw_edges(location, self.gameDisplay)

    def update(self, agents):
        self.render()
        self.agents = agents
        time.sleep(self.delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for agent in self.agents:
            draw_agent(agent, self.gameDisplay)
        pygame.display.update()


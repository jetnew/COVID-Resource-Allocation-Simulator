from env import Location, Simulation, AgentFactory
from agent import Agent
from render import Renderer

# Initialise the environment graph
entrance = Location("Entrance",
                    size=(20, 10),
                    time_required=10,
                    position=(400, 400))
pharmacy = Location("Pharmacy",
                    size=(8, 8),
                    time_required=15,
                    position=(100, 100))
registration = Location("Registration",
                        size=(5, 5),
                        time_required=20,
                        position=(100, 500))
waiting_area = Location("Waiting Area",
                        size=(10, 10),
                        time_required=60,
                        position=(500, 100))

entrance.add_adj_room(coord=(0, 0), node=pharmacy)
entrance.add_adj_room(coord=(0, 10), node=registration)
entrance.add_adj_room(coord=(10, 0), node=waiting_area)
pharmacy.add_adj_room(coord=(8, 4), node=entrance)
registration.add_adj_room(coord=(5, 0), node=entrance)
waiting_area.add_adj_room(coord=(5, 10), node=entrance)
locations = [entrance, registration, waiting_area, pharmacy]

# Create Agent Factory
journeys = [
    [entrance, pharmacy, entrance],
    [entrance, registration, entrance],
    [entrance, registration, entrance, pharmacy, entrance],
    [entrance, registration, entrance, waiting_area, entrance, pharmacy, entrance],
]
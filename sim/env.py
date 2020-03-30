import random
from agent import Agent


class Location:
    """Location node that is connected to other locations.
    Represented by a 2D array and linked to other locations via dictionary.
    """
    def __init__(self, name, size=(10,10), time_required=10, position=(0,0)):
        self.name = name
        self.size = size
        self.adj_rooms = {}
        self.time_required = time_required
        self.position = position

    def add_adj_room(self, coord, node):
        self.adj_rooms[coord] = node

    def get_adj_room_coord(self, node):
        for coord, room in self.adj_rooms.items():
            if room == node:
                return coord
        return None

    def __repr__(self):
        str_adj_rooms = ", ".join([room.name + str(coord) for coord, room in self.adj_rooms.items()])
        return "====================\n" \
            + "Location: " + self.name + '\n' \
            + "Size: " + str(self.size) + '\n' \
            + "Adjacent rooms:\n\t" + str_adj_rooms


class Simulation:
    def __init__(self, location, agents, epoch=20):
        """
        location - Location node, usually the entrance
        agents - List of Agents
        """
        self.location = location
        self.agents = agents
        self.t = 0
        self.statistics = {
            'transmissions': 0,
            'agents': 0,
        }
        self.total_transmissions = 0

    def print_state(self):
        print(f"==========State(t={self.t})==========")
        for agent in self.agents:
            curr_location = agent.curr_location
            next_location = agent.get_next_location()
            if next_location:
                print(f"{agent.role} "
                      f"from {curr_location.name}{agent.curr_coord} "
                      f"to {next_location.name}{curr_location.get_adj_room_coord(next_location)}, "
                      f"infected: {agent.infected}.")
            else:
                print(f"{agent.role} "
                      f"from {curr_location.name}{agent.curr_coord} "
                      f"to exit, "
                      f"infected: {agent.infected}.")

    def print_statistics(self):
        print("==========Statistics==========")
        for key, value in self.statistics.items():
            print(f"{key}: {value}")

    def step(self, verbose=False):
        self.t += 1

        # Contact Tracer = {location_name: {(x,y): [Agent]}}
        contact_tracer = {}

        # Every agent takes a step
        for agent in self.agents:
            # If agent has nowhere else to go, remove the agent
            if agent.move() is None:
                self.agents.remove(agent)
                continue
            # Trace location of agent
            location_name = agent.curr_location.name
            if location_name not in contact_tracer:
                contact_tracer[location_name] = {}
            coordinate = agent.curr_coord
            if coordinate not in contact_tracer[location_name]:
                contact_tracer[location_name][coordinate] = []
            contact_tracer[location_name][coordinate].append(agent)

        # Check if any agent is in contact with another
        for location_name in contact_tracer:
            for coordinate in contact_tracer[location_name]:
                contacts = contact_tracer[location_name][coordinate]

                # If contact is transmissible, risk transmission
                if len(contacts) > 1 and any([agent.infected for agent in contacts]):
                    for agent in contacts:
                        if agent.risk_transmission():
                            self.statistics['transmissions'] += 1
        if verbose:
            self.print_state()

    def compute_statistics(self):
        self.statistics['average_transmissions'] = self.statistics['transmissions']/self.statistics['agents']

    def run(self, agent_factory, epoch=50, renderer=None, verbose=False):
        # Render environment
        if renderer:
            renderer.render()

        for t in range(epoch):
            # Generate agents at specified rate
            agent = agent_factory.create_agent(t)
            if agent is not None:
                self.agents.append(agent)
                self.statistics['agents'] += 1

            # Take an environment step
            self.step(verbose=verbose)

            # Update render
            if renderer:
                renderer.update(self.agents)

        self.compute_statistics()
        if verbose:
            self.print_statistics()


class AgentFactory:
    def __init__(self, creation_rate, infected_rate, transmission_rate, journeys, entrance):
        self.creation_rate = creation_rate
        self.infected_rate = infected_rate
        self.transmission_rate = transmission_rate
        self.agents = []
        self.journeys = journeys
        self.entrance = entrance

    def create_agent(self, t):
        created = True if random.random() < self.creation_rate else False
        if created:
            infected = True if random.random() < self.infected_rate else False
            agent = Agent(role="Patient",
                          infected=infected,
                          transmission_rate=self.transmission_rate,
                          curr_coord=(9, 5),
                          curr_location=self.entrance,
                          journey=random.choice(self.journeys),
                          epsilon=0.2)
            self.agents.append(agent)
            return agent


if __name__ == "__main__":
    entrance = Location("Entrance", size=(10,10))
    pharmacy = Location("Pharmacy", size=(5,5))
    registration = Location("Registration", size=(2,2))
    entrance.add_adj_room(coord=(0,0), node=pharmacy)
    entrance.add_adj_room(coord=(1,1), node=registration)
    print(entrance)
    print(pharmacy)

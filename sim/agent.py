import random


class Agent:
    """Agent that represent either patient or staff.
    Represented by transmission rate of COVID-19, and
    holds a journey represenetd by a list of locations.
    """
    def __init__(self,
                 role,
                 infected,
                 transmission_rate,
                 curr_coord,
                 curr_location,
                 journey,
                 epsilon=0.3):
        """
        role - str, E.g. "patient", "staff"
        infected - bool
        transmission_rate - float, [0,1]
        curr_coord - tup, (y,x)
        curr_location - Location node
        journey - List of Location nodes
        epsilon - float, [0,1]
        """
        self.role = role
        self.infected = infected
        self.transmission_rate = transmission_rate
        self.curr_coord = curr_coord
        self.curr_location = curr_location
        self.journey = journey
        self.epsilon = epsilon
        self.time_spent = 0
        self.loc_idx = 0

    def risk_transmission(self):
        """Risk transmission.
        Returns True if previously uninfected and now infected.
        Returns False if uninfected, or already infected.
        """
        if not self.infected and random.random() < self.transmission_rate:
            self.infected = True
            return True
        return False

    def get_next_location(self):
        """Get next location node given current location and journey."""
        if self.loc_idx < len(self.journey) - 1:
            return self.journey[self.loc_idx + 1]
        else:
            return None

    def get_next_coord(self):
        """Get the next coordinate with some random probability."""
        coord = self.curr_coord
        location = self.curr_location
        journey = self.journey
        next_location = self.get_next_location()
        next_coord = location.get_adj_room_coord(next_location)

        if next_location is None:
            return None

        # Go to the next location if reached
        if coord == next_coord and random.random() > self.epsilon and self.time_spent > location.time_required:
            self.curr_location = next_location
            self.loc_idx += 1
            self.time_spent = 0
            return next_location.get_adj_room_coord(location)

        dx = next_coord[0] - coord[0]
        dy = next_coord[1] - coord[1]

        # Next location w.r.t. x-axis
        if dx == 0:
            ix = 0
        elif dx > 0:
            ix = 1
        else:
            ix = -1

        # Next location w.r.t. y-axis
        if dy == 0:
            iy = 0
        elif dy > 0:
            iy = 1
        else:
            iy = -1

        # Random walk at the probability of epsilon OR if process incomplete
        if self.time_spent < self.curr_location.time_required or random.random() < self.epsilon:
            ix = random.choice([0, 1, -1])
            iy = random.choice([0, 1, -1])
        self.time_spent += 1

        # Location bounds
        bx = location.size[0]
        by = location.size[1]
        return min(bx, max(0, coord[0] + ix)), min(by, max(0, coord[1] + iy))

    def move(self):
        new_coord = self.get_next_coord()
        if new_coord is None:
            return None
        self.curr_coord = new_coord
        return new_coord

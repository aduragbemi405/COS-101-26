# physics.py

def calculate_velocity(distance, time):
    """Calculates velocity: v = distance / time"""
    if time == 0:
        return "Time cannot be zero"
    return distance / time

def calculate_force(mass, acceleration):
    """Calculates force (Newton's Second Law): F = m * a"""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Calculates kinetic energy: KE = 1/2 * m * v^2"""
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height, gravity=9.8):
    """Calculates gravitational potential energy: PE = m * g * h"""
    return mass * gravity * height

def calculate_work(force, distance):
    """Calculates work done: W = F * d"""
    return force * distance

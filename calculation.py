def calculate_physics():
  g = 9.81  # Acceleration due to gravity (m/s^2)

  print("--- Physics & Running Calculator ---")

  # 1. Running Speed (v = d / t)
  distance = float(input("Enter distance covered (meters): "))
  time = float(input("Enter time taken (seconds): "))
  speed = distance / time if time > 0 else 0

  # 2. Weight (W = m * g)
  mass = float(input("Enter mass of the object/runner (kg): "))
  weight = mass * g

  # 3. Force (F = m * a)
  acceleration = float(input("Enter acceleration (m/s^2): "))
  force = mass * acceleration

  # 4. Kinetic Energy (KE = 0.5 * m * v^2)
  kinetic_energy = 0.5 * mass * (speed**2)

  # 5. Potential Energy (PE = m * g * h)
  height = float(input("Enter height above ground (meters): "))
  potential_energy = mass * g * height

  # Display Results
  print("\n--- Results ---")
  print(f"Running Speed:    {speed:.2f} m/s ({speed * 3.6:.2f} km/h)")
  print(f"Weight:           {weight:.2f} N")
  print(f"Force:            {force:.2f} N")
  print(f"Kinetic Energy:   {kinetic_energy:.2f} J")
  print(f"Potential Energy: {potential_energy:.2f} J")



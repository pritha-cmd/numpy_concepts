import numpy as np

# Given data
mass = 1.0e-3  # kg (1.0 mg = 1.0e-6 kg)
speed = 20  # m/s
h = 6.626e-34  # Planck's constant (J.s)

# Calculate momentum
momentum = mass * speed

# Calculate de Broglie wavelength
wavelength = h / momentum

# Print the result
print(f"The de Broglie wavelength is: {wavelength:.2e} meters")
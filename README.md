# Rocket
A Python simulation of a rocket.

## How to use
Clone this repository: \
`https://github.com/deveworld/rocket`

Install the required dependencies: \
`pip install -r requirements.txt`

Run the example script: \
`python3 example.py`

## example.py
In this example, the rocket has the following parameters:

- Initial mass: 30 kg
- Final mass: 10 kg
- Average thrust: 5000 N (approximately 510 kg)
- Propulsion time: 7 s
- Drag coefficient: 0.65
- Surface gravity: 9.81 m/s^2

The results are as follows (the text entered is surrounded by *)
```
Initial mass (kg): *30*
Final mass (kg): *10*
Average thrust (N): *5000*
Propulsion time (s): *7*
Drag coefficient: *0.65*
Gravitational acceleration (m/s^2): *9.81*
------------------------------
Isp                         = 178.389   s
Effective exhaust velocity  = 1750.000  m/s
Delta-v                     = 1922.572  m/s
------------------------------
A delta-v of 1922.6 m/s would be 'insufficient' to enter the LEO (Low Earth Orbit).
------------------------------

Calculated in 4.612675428390503 sec with 0.01 of dt.
Max speed (at burnout): 114.2 m/s at 728.8 m
Max altitude: 779.8 m at -0.1 m/s at 9.4 s
Landing time: 59.4 s with -15.7 m/s
```
Based on the calculations, this rocket has:

- Specific impulse (Isp): 178.389 s
- Effective exhaust velocity: 1750 m/s
- Delta-v: 1922.572 m/s

The maximum height achieved by the rocket is approximately 779.8 m, as indicated in the result.

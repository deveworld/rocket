# Rocket
A simulation of rocket in Python

## How to use
Clone this repository: \
`https://github.com/deveworld/rocket`

Install the required dependencies: \
`pip install -r requirements.txt`

Run the example script: \
`python3 example.py`

## example.py
In this example, the rocket has the following parameters:

- Initial mass: 0.5 kg
- Final mass: 0.2 kg
- Average thrust: 14.715 N (equivalent to 1.5 kg)
- Propulsion time: 30 s
- Drag coefficient: 0.6
- Surface gravity: 9.81 m/s^2

And this perfomed on 9.81 m/s^2 of surface. (inputted text surrounded by **)
```
Initial mass (kg): *0.5*
Final mass (kg): *0.2*
Average thrust (N): *14.715*
Propulsion time (s): *30*
Gravitational acceleration (m/s^2): *9.81*
Drag coefficient: *0.65*
Isp                         = 150.000   s
Effective exhaust velocity  = 1471.500  m/s
Delta-v                     = 1348.322  m/s
------------------------------
LEO (Low Earth orbit) cannot be reached.
------------------------------

Calculated in 10.198925733566284 sec with 0.010000000000000 dt
{'burnout_v': 5.69391659769960, 'burnout_t': 30.0000000000000, 'burnout_h': 159.188785149418, 'burnout_m': 0.200000, 'maxh_v': -0.0779236683479095, 'maxh_t': 30.2700000000000, 'maxh_h': 159.640947143393, 'maxh_m': 0.200000, 'end_v': -2.21997331069142, 'end_t': 102.110000000000, 'end_h': -0.0167797950825234, 'end_m': 0.200000}
```
Based on the calculations, this rocket has:

- Specific impulse (Isp): 150 s
- Effective exhaust velocity: 1471.5 m/s
- Delta-v: 1348.322 m/s

The maximum height achieved by the rocket is approximately 159.64 m, as indicated in the result.

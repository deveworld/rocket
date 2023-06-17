# Rocket
A simulation of rocket in Python

## example.py
In this case, the rocket has
0.5 kg of initial mass,
0.2 kg of final mass,
14.715 N (=1.5kg) of average thrust,
30 s of propulsion time,
0.6 of drag coefficient.

And this perfomed on 9.81 m/s^2 of surface.
```
Initial mass (kg): *0.5*
Final mass (kg): *0.2*
Average thrust (N): *14.715*
Propulsion time (s): *30*
Gravitational acceleration (m/s^2): *9.81*
Drag coefficient: 0.65
Isp                         = 150.000   s
Effective exhaust velocity  = 1471.500  m/s
Delta-v                     = 1348.322  m/s
------------------------------
LEO(Low Earth orbit) cannot reachable.
------------------------------

Calculated in 10.198925733566284 sec with 0.010000000000000 dt
{'burnout_v': 5.69391659769960, 'burnout_t': 30.0000000000000, 'burnout_h': 159.188785149418, 'burnout_m': 0.200000, 'maxh_v': -0.0779236683479095, 'maxh_t': 30.2700000000000, 'maxh_h': 159.640947143393, 'maxh_m': 0.200000, 'end_v': -2.21997331069142, 'end_t': 102.110000000000, 'end_h': -0.0167797950825234, 'end_m': 0.200000}
```
This rocket has 
150 s of Isp,
1471.5 m/s of effective exhaust velocity,
1348.322 m/s of delta-v
by the calculation.

And, according to the result, it's maximum height is approximately 159.64 m.

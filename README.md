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
Max altitude: 779.8 m at -0.0 m/s at 9.3 s
Landing time: 59.4 s with -15.7 m/s
```
Based on the calculations, this rocket has:

- Specific impulse (Isp): 178.389 s
- Effective exhaust velocity: 1750 m/s
- Delta-v: 1922.572 m/s

The maximum height achieved by the rocket is approximately 779.8 m, as indicated in the result.

## Process
(You can also see the entire process in the code annotation.)
### Calculating variables process

The `Rocket` class gets several parametes at init. \
where
- $m_{0}$ is the initial mass ($kg$)
- $m_{f}$ is the final mass ($kg$)
- $thrust$ is the average thrust ($N$)
- $time$ is the total propulsion time ($s$)
- $g_{0}$ is the gravitational acceleration of the surface ($m/s^{2}$)

And first, the code calculates $M_{p}$ ($kg$):
$$M_{p} = m_{0} - m_{f}$$
Which means total effective propellant mass.

And calculates $I_{t}$:
$$I_{t} =  \int_0^t F(t) dt = F_{m} \cdot t$$
where
- $I_{t}$ is the total impulse ($kg \cdot m/s = N \cdot s$)
- $F(t)$ is the thrust according to t ($N$)
- $F_{m}$ is the average thrust ($N$)
- $t$ is the total propulsion time ($s$)

Now, we can calculate $I_{sp}$ , which represents the specific impulse ($s$), since we know $I_{t}$ and $M_{p}$:
$$I_{sp} =  \frac{I_{t}}{M_{p} \cdot g_{0}}$$

Additionally, we also calculate $v_{exh}$ , the effective exhaust velocity ($m/s$), which is necessary to calculate $\Delta V$:
$$v_{exh} = I_{sp} \cdot g_{0}$$

Finally, we can calculate $\Delta V$ (available change in velocity, $m/s$), since we know all the necessary values:
$$\Delta V = v_{exh} \cdot \ln(\frac{m_{0}}{m_{f}})$$

### Simulation process

Since we got all variables to simulating, we can do numerical integration.
$$g(h) = g_{0} \frac {{R_{E}}^{2}}{({R_{E}}^{2}+h)^{2}}$$
$$p(h) = \frac {4.69729 \cdot 10^{29}}{|17h^{2} + 186000h + 7265070000|^{3}}$$
$$a = -g(h) + \frac {F_{m}}{m} - \frac {\frac {1}{2} \cdot p(h) \cdot v^{2} \cdot c_{d}}{m}$$
where
- $a$ is the acceleration of the rocket ($m/s^{2}$)
- $g(h)$ is the approximate function of gravitational acceleration over altitude ($m/s^{2}$)
- $R_{E}$ is the radius of a planet ($m$)
- $p(h)$ is the approximate function of air density over altitude ($kg/m^{3}$)
- $m$ is the mass of rocket ($kg$)
- $v$ is the velocity of rocket ($m/s$)
- $h$ is the height of rocket ($m$)
- $c_{d}$ is the drag coefficient of rocket

The code run by small $\Delta t$:
$$v = v + a \cdot \Delta t$$
$$h = h + v \cdot \Delta t$$
$$m = m - \frac {M_{p}}{time} \cdot \Delta t \ (m > m_{f})$$
import sympy as sy
from sympy import Float
from typing import Dict

from rocket import Rocket

class Space:
    def __init__(self, rocket: Rocket, drag: Float = Float("0.75"), dt: Float = Float("0.01")) -> None:
        self.rocket = rocket
        self.p_formula_constant = (4.69729*(10**29))
        self.planet_radius = 6371 # km
        self.cd = drag
        self.dt = dt
    
    def get_p(self, h) -> Float:
        x = sy.symbols('x')
        down = sy.Abs((17 * x**2) + (186000 * x) + 7265070000)**3
        p = self.p_formula_constant / down
        result_p = p.evalf(n=10, subs={x:h})
        return result_p
    
    def get_g(self, h) -> Float:
        x = sy.symbols('x')
        a = self.rocket.g0 * (self.planet_radius**2/(self.planet_radius + (x/1000))**2)
        g = a.evalf(n=10, subs={x:h})
        return g
    
    def calculate(self) -> Dict[str, Float]:
        result = {}

        t: Float = 0
        v: Float = 0
        h: Float = 0
        m: Float = self.rocket.m0
        m_delta: Float = self.rocket.Mp / self.rocket.time * self.dt
        i = 1
        print()
        while t < self.rocket.time:
            g, f, p, vel, cd, mass = sy.symbols('g f p vel cd mass')
            a_calc = -g + (f/mass) - ((0.5*p*vel**2*cd)/mass)
            a = a_calc.evalf(n=10, subs={g:self.get_g(h), f:self.rocket.thrust, p:self.get_p(h), vel:v, cd:self.cd, mass:m})
            v += a*self.dt
            h += v*self.dt
            m -= m_delta
            t = self.dt * i
            i += 1
        m = Float(self.rocket.mf)
        result["burnout_v"] = v
        result["burnout_t"] = t
        result["burnout_h"] = h
        result["burnout_m"] = m
        while v > 0:
            g, p, vel, cd, mass = sy.symbols('g p vel cd mass')
            a_calc = -g - ((0.5 * p * (vel**2) * cd)/mass)
            a = a_calc.evalf(n=10, subs={g:self.get_g(h), p:self.get_p(h), vel:v, cd:self.cd, mass:m})
            v += a*self.dt
            h += v*self.dt
            t = self.dt * i
            i += 1
        result["maxh_v"] = v
        result["maxh_t"] = t
        result["maxh_h"] = h
        result["maxh_m"] = m
        while h > 0:
            g, p, vel, cd, mass = sy.symbols('g p vel cd mass')
            a_calc = -g + ((0.5 * p * (vel**2) * cd)/mass)
            a = a_calc.evalf(n=10, subs={g:self.get_g(h), p:self.get_p(h), vel:v, cd:self.cd, mass:m})
            v += a*self.dt
            h += v*self.dt
            t = self.dt * i
            i += 1
        result["land_v"] = v
        result["land_t"] = t
        result["land_h"] = h
        result["land_m"] = m
        return result
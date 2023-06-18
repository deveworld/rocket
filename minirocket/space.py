import sympy as sy
from sympy import Float
from typing import Any, Callable, Dict, Optional, Tuple

from .rocket import Rocket

class Space:
    def __init__(self, rocket: Rocket, drag: Float = Float("0.75"), dt: Float = Float("0.01")) -> None:
        self.rocket = rocket
        self.p_formula_constant = (4.69729*(10**29))
        self.planet_radius = 6371 * 1000 # m
        self.cd = drag
        self.dt = dt
    
    def get_p(self, height) -> Float:
        x = sy.symbols('x')
        down = sy.Abs((17 * x**2) + (186000 * x) + 7265070000)**3
        p = self.p_formula_constant / down
        result_p = p.evalf(n=10, subs={x:height})
        return result_p
    
    def get_g(self, height) -> Float:
        x = sy.symbols('x')
        a = self.rocket.g0 * (self.planet_radius**2/(self.planet_radius + (x/1000))**2)
        g = a.evalf(n=10, subs={x:height})
        return g
    
    def interpolate_thrust(self, time: Float, thrust_iter: int) -> Tuple[Float, int]:
        now_dot_time = list(self.rocket.thrust.keys())[thrust_iter]
        now_dot = (now_dot_time, self.rocket.thrust[now_dot_time])

        next_dot_time = now_dot_time
        next_dot = now_dot
        is_last_iter = (len(self.rocket.thrust) <= thrust_iter+1)
        if not is_last_iter:
            next_dot_time = list(self.rocket.thrust.keys())[thrust_iter+1]
            next_dot = (next_dot_time, self.rocket.thrust[next_dot_time])
            
        interpolated_thrust = sy.interpolate([now_dot, next_dot], time)
        if time >= next_dot_time and not is_last_iter:
            thrust_iter += 1
        
        return (interpolated_thrust, thrust_iter)
    
    def calculate(self, callback: Optional[Callable[[Float, Float, Float, Float, Float], Any]]=None) -> Dict[str, Float]:
        """
        Simulating rocket

        Args:
            callback (Optional[Callable[[sympy.Float, sympy.Float, sympy.Float, sympy.Float, sympy.Float], Any]], optional): callback while simulating
                time, acceleration, velocity, height, mass

        Returns:
            Dict[str, sympy.Float]: Major results of simulating as Dict
        """
        result = {}

        t: Float = 0
        a: Float = 0
        v: Float = 0
        h: Float = 0
        m: Float = self.rocket.m0
        m_delta: Float = self.rocket.Mp / self.rocket.get_total_impulse() * self.dt
        i = 1
        thrust_i = 0

        if callback != None:
            callback(t, a, v, h, m)
        while t <= self.rocket.time:
            g, f, p, vel, cd, mass = sy.symbols('g f p vel cd mass')
            a_calc = -g + (f/mass) - ((0.5*p*vel**2*cd)/mass)
            thrust, thrust_i = self.interpolate_thrust(t, thrust_i)
            a = a_calc.evalf(n=10, subs={
                g:self.get_g(h), 
                f:thrust, 
                p:self.get_p(h), 
                vel:v, 
                cd:self.cd, mass:m
                })
            v += a*self.dt
            h += v*self.dt
            if t != self.rocket.time:
                m -= m_delta*thrust
            t = self.dt * i
            i += 1
            if callback != None:
                callback(t, a, v, h, m)
        m = self.rocket.mf
        result["burnout_v"] = v
        result["burnout_t"] = t
        result["burnout_h"] = h
        result["burnout_m"] = m
        while v >= 0:
            g, p, vel, cd, mass = sy.symbols('g p vel cd mass')
            a_calc = -g - ((0.5 * p * (vel**2) * cd)/mass)
            a = a_calc.evalf(n=10, subs={g:self.get_g(h), p:self.get_p(h), vel:v, cd:self.cd, mass:m})
            v += a*self.dt
            h += v*self.dt
            t = self.dt * i
            i += 1
            if callback != None:
                callback(t, a, v, h, m)
        result["maxh_v"] = v
        result["maxh_t"] = t
        result["maxh_h"] = h
        result["maxh_m"] = m
        while h >= 0:
            g, p, vel, cd, mass = sy.symbols('g p vel cd mass')
            a_calc = -g + ((0.5 * p * (vel**2) * cd)/mass)
            a = a_calc.evalf(n=10, subs={g:self.get_g(h), p:self.get_p(h), vel:v, cd:self.cd, mass:m})
            v += a*self.dt
            h += v*self.dt
            t = self.dt * i
            i += 1
            if callback != None:
                callback(t, a, v, h, m)
        result["land_v"] = v
        result["land_t"] = t
        result["land_h"] = h
        result["land_m"] = m
        return result
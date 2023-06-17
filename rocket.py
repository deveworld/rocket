import numpy
from typing import List, Optional
import sympy as sy
from sympy import Float

class Rocket:
    def __init__(
            self, 
            m0: numpy.float32, 
            mf: numpy.float32, 
            thrust: numpy.float32, 
            time: numpy.float32, 
            g0: numpy.float32
            ) -> None:
        """Rocket Init

        Args:
            m0 (numpy.float32): Initial mass                  (kg)
            mf (numpy.float32): Final mass                    (kg)
            thrust (numpy.float32): Average thrust            (N)
            time (numpy.float32): Propulsion time             (s)
            g0 (numpy.float32): Gravitational acceleration    (m/s^2)
        """
        self.m0 = m0
        self.mf = mf
        self.thrust = thrust
        self.time = time
        self.g0 = g0

        # Total effective propellant mass   (kg)
        x, y = sy.symbols('x y')
        self.Mp: Float = (x - y).evalf(n=10, subs={x:self.m0, y:self.mf})

        # Total impulse                     (kg*m/s = N*s)
        self.total_impulse: Optional[Float] = None
        self.calc_total_impulse()

        # Specific impulse                  (s)
        self.isp: Optional[Float] = None
        self.calc_isp()

        # Effective exhaust velocity        (m/s)
        self.effective_exhaust_velocity: Optional[Float] = None
        self.calc_effective_exhaust_velocity()

        # Available change in velocity      (m/s)
        self.delta_v: Optional[Float] = None
        self.calc_delta_v()


    def calc_total_impulse(self) -> Float:
        if self.total_impulse == None:
            x, y = sy.symbols('x y')
            calc = x * y
            self.total_impulse = calc.evalf(n=10, subs={x:self.thrust, y:self.time})
        return self.total_impulse

    def calc_isp(self) -> Float:
        if self.isp == None:
            x, y = sy.symbols('x y')
            calc = self.calc_total_impulse() / (x * y)
            self.isp = calc.evalf(n=10, subs={x:self.Mp, y:self.g0})
        return self.isp
    
    def calc_effective_exhaust_velocity(self) -> Float:
        if self.effective_exhaust_velocity == None:
            x = sy.symbols('x')
            calc = self.calc_isp() * x
            self.effective_exhaust_velocity = calc.evalf(n=10, subs={x:self.g0})
        return self.effective_exhaust_velocity
    
    def calc_delta_v(self) -> Float:
        if self.delta_v == None:
            x, y = sy.symbols('x y')
            calc = self.calc_effective_exhaust_velocity() * sy.log(x / y)
            self.delta_v = calc.evalf(n=10, subs={x:self.m0, y:self.mf})
        return self.delta_v
    
    def interpret_delta_v(self) -> List[str]:
        delta_v_interpretation = []
        delta_v = self.calc_delta_v()
        if delta_v > 9.5 * 1000:
            delta_v_interpretation.append(f"A delta-v of {delta_v:.1f} m/s would be 'sufficient' to enter the LEO (Low Earth Orbit).")
        else:
            delta_v_interpretation.append(f"A delta-v of {delta_v:.1f} m/s would be 'insufficient' to enter the LEO (Low Earth Orbit).")
            return delta_v_interpretation
        
        if delta_v > 13.5 * 1000:
            delta_v_interpretation.append(f"A delta-v of {delta_v:.1f} m/s would be 'sufficient' to enter the GEO (Geostationary Orbit).")
        else:
            delta_v_interpretation.append(f"A delta-v of {delta_v:.1f} m/s would be 'insufficient' to enter the GEO (Geostationary Orbit).")
            return delta_v_interpretation

        return delta_v_interpretation
    

import sympy as sy
from sympy import Float
from typing import Dict, List, Optional

class Rocket:
    def __init__(
            self, 
            m0: Float, 
            mf: Float, 
            thrust: Dict[Float, Float],
            g0: Float
            ) -> None:
        """Rocket Init

        Args:
            m0 (sympy.Float): Initial mass                  (kg)
            mf (sympy.Float): Final mass                    (kg)
            thrust (Dict[sympy.Float, sympy.Float]): Thrust by time (N)
            g0 (sympy.Float): Gravitational acceleration    (m/s^2)

        Example:
            rocket = Rocket(20, 5, {0.0: 5.0, 3.5: 5.0}, 9.81)
        """
        self.m0 = m0
        self.mf = mf
        self.thrust = thrust
        self.g0 = g0

        # Total thrust time                 (s)
        self.time: Optional[Float] = None
        try:
            self.time = Float(list(self.thrust.keys())[-1])
        except ValueError:
            raise ValueError('A very specific bad thing happened.')

        # Total effective propellant mass   (kg)
        x, y = sy.symbols('x y')
        self.Mp: Float = (x - y).evalf(n=10, subs={x:self.m0, y:self.mf})

        # Total impulse                     (kg*m/s = N*s)
        self.total_impulse: Optional[Float] = None
        self.total_impulse = self.calc_total_impulse()

        # Specific impulse                  (s)
        self.isp: Optional[Float] = None
        self.isp = self.calc_isp()

        # Effective exhaust velocity        (m/s)
        self.effective_exhaust_velocity: Optional[Float] = None
        self.effective_exhaust_velocity = self.calc_effective_exhaust_velocity()

        # Available change in velocity      (m/s)
        self.delta_v: Optional[Float] = None
        self.delta_v = self.calc_delta_v()

    def get_total_impulse(self) -> Float:
        if self.total_impulse == None:
            self.total_impulse = self.calc_total_impulse()
        return self.total_impulse

    def get_isp(self) -> Float:
        if self.isp == None:
            self.isp = self.calc_isp()
        return self.isp
    
    def get_effective_exhaust_velocity(self) -> Float:
        if self.effective_exhaust_velocity == None:
            self.effective_exhaust_velocity = self.calc_effective_exhaust_velocity()
        return self.effective_exhaust_velocity
    
    def get_delta_v(self) -> Float:
        if self.delta_v == None:
            self.delta_v = self.calc_delta_v()
        return self.delta_v

    def calc_total_impulse(self) -> Float:
        total_impulse = 0
        before_thrust = 0
        before_time = 0
        for time in list(self.thrust.keys()):
            br, r, t, bt = sy.symbols('br r t bt')
            calc = (br + r) * (t - bt) * 0.5
            total_impulse += calc.evalf(n=10,
                subs={
                    br: before_thrust,
                    r: self.thrust[time],
                    t: time,
                    bt: before_time
                    })
            before_thrust = self.thrust[time]
            before_time = time
        return total_impulse

    def calc_isp(self) -> Float:
        x, y = sy.symbols('x y')
        calc = self.get_total_impulse() / (x * y)
        isp = calc.evalf(n=10, subs={x:self.Mp, y:self.g0})
        return isp
    
    def calc_effective_exhaust_velocity(self) -> Float:
        x = sy.symbols('x')
        calc = self.get_isp() * x
        effective_exhaust_velocity = calc.evalf(n=10, subs={x:self.g0})
        return effective_exhaust_velocity
    
    def calc_delta_v(self) -> Float:
        x, y = sy.symbols('x y')
        calc = self.get_effective_exhaust_velocity() * sy.log(x / y)
        delta_v = calc.evalf(n=10, subs={x:self.m0, y:self.mf})
        return delta_v
    
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
    

import numpy
from typing import Optional
from sympy import Float
from time import time as get_time
       
from rocket import Rocket
from space import Space

if __name__ == "__main__":
    def int_input(question_message: str, error_message: str):
        float_answer: Optional[numpy.float32] = None
        while float_answer == None:
            try:
                answer = input(question_message)
                float_answer = numpy.asarray([answer]).astype(numpy.float32)[0]
            except ValueError:
                print(error_message)
        return float_answer

    error_message = "It doesn't appear to be a decimal or a number. Please try again without any characters.\n"
    m0 = int_input("Initial mass (kg): ", error_message)
    mf = int_input("Final mass (kg): ", error_message)
    thrust = int_input("Average thrust (N): ", error_message)
    time = int_input("Propulsion time (s): ", error_message)
    drag = int_input("Drag coefficient: ", error_message)
    g0 = int_input("Gravitational acceleration (m/s^2): ", error_message)

    # m0 = 25; mf = 19; thrust = 2100; time = 3.5; g0 = 9.81
    # m0 = 0.5; mf = 0.2; thrust = 20; time = 30; g0 = 9.81
    # m0 = 2340; mf = 1290; thrust = 192000; time = 8.848; g0 = 9.81
    rocket = Rocket(m0, mf, thrust, time, g0)

    print("-"*30)

    print(f"Isp                         = {rocket.calc_isp():.3f}\ts")
    print(f"Effective exhaust velocity  = {rocket.calc_effective_exhaust_velocity():.3f}\tm/s")
    print(f"Delta-v                     = {rocket.calc_delta_v():.3f}\tm/s")

    print("-"*30)

    for interpret in rocket.interpret_delta_v():
        print(interpret)

    print("-"*30)

    dt = Float("0.01")
    start = get_time()
    space = Space(rocket, drag, dt)
    res = space.calculate()
    duration = get_time() - start
    print(f"Calculated in {duration} sec with {dt.__str__().rstrip('0')} of dt")

    print(f"Max speed (at burnout): {res['burnout_v']:.1f} m/s at {res['burnout_h']:.1f} m")
    print(f"Max altitude: {res['maxh_h']:.1f} m at {res['maxh_v']:.1f} m/s at {res['maxh_t']:.1f} s")
    print(f"Landing time: {res['land_t']:.1f} s with {res['land_v']:.1f} m/s")
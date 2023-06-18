from pathlib import Path
from typing import Optional
from sympy import Float
from time import time as get_time
       
from minirocket.rocket import Rocket
from minirocket.space import Space
from utils import FileUtils

if __name__ == "__main__":
    def int_input(question_message: str, error_message: str):
        float_answer: Optional[Float] = None
        while float_answer == None:
            try:
                answer = input(question_message)
                float_answer = Float(answer)
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

    rocket = Rocket(m0, mf, {0: thrust, time: thrust}, g0)

    file_utils = FileUtils(Path("example/data.csv"))

    # rocket = Rocket(
    #     30,
    #     10,
    #     {0: 0, 0.5: 5000, 6.5: 6000, 7: 0},
    #     9.81
    # ); drag=0.65

    print("-"*30)

    print(f"Isp                         = {rocket.get_isp():.3f}\ts")
    print(f"Effective exhaust velocity  = {rocket.get_effective_exhaust_velocity():.3f}\tm/s")
    print(f"Delta-v                     = {rocket.get_delta_v():.3f}\tm/s")

    print("-"*30)

    for interpret in rocket.interpret_delta_v():
        print(interpret)

    print("-"*30)

    dt = Float("0.01")
    space = Space(rocket, drag, dt)
    file_utils.open()

    start = get_time()
    res = space.calculate(file_utils.file_callback)
    duration = get_time() - start

    print(f"Calculated in {duration} sec with {dt.__str__().rstrip('0')} of dt")

    print(f"Burnout: {res['burnout_v']:.2f} m/s at {res['burnout_h']:.2f} m")
    print(f"Max altitude: {res['maxh_h']:.2f} m at {res['maxh_v']:.2f} m/s at {res['maxh_t']:.2f} s")
    print(f"Landing time: {res['land_t']:.2f} s with {res['land_v']:.2f} m/s")
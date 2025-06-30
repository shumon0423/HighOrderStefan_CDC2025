from model import StefanSecondOrderModel
from control import ControlStrategy1, ControlStrategy2
from solve import StefanSolver
from check import CheckBase
from plot import plot_results

def main():

    model_type = StefanSecondOrderModel()  # Change to StefanSecondOrderModel() for different behavior
    # 🔹 Choose control strategy here
    control_strategy = ControlStrategy2()  # Change to ControlStrategy2() for different behavior
    # Initialize the state with the selected control strategy
    system = StefanSolver(control=control_strategy, model=model_type)

    # Check stability, setpoint, and gain conditions
    check = CheckBase()

    if not check.stability():
        print("Warning: Stability condition not met!")

    if not check.setpoint():
        print("Warning: Setpoint condition not met!")

    if not check.gain():
        print("Warning: Gain condition not met!")

    # Run simulation with closed-loop control
    time, s_t, u_t, qc_t = system.run_simulation()

    # Plot results
    plot_results(time, s_t, u_t, qc_t)

if __name__ == "__main__":
    main()

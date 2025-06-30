import numpy as np
from parameters import params

class StefanSolver:
    def __init__(self, control=None, model=None):
        """Initialize model with optional control strategy"""
        self.control = control
        self.model = model
        
        # Simulation parameters
        self.N = params["simulation"]["N"]
        self.dt = params["simulation"]["dt"]
        self.sec = params["simulation"]["min"] * 60
        self.time = np.arange(0, self.sec, self.dt)
        self.Time_len = len(self.time)

        # Initial conditions
        self.s0 = params["initial"]["s_0"]
        self.v0 = params["initial"]["v_0"]
        self.u0max = params["initial"]["u_0_max"]
        self.u0 = np.array([self.u0max * (1 - i / self.N) for i in range(self.N + 1)])

    def run_simulation(self):
        """Run simulation with closed-loop control"""
        u_t = np.zeros((self.N + 1, self.Time_len))
        s_t = np.zeros(self.Time_len)
        v_t = np.zeros(self.Time_len)
        qc_t = np.zeros(self.Time_len)

        u_t[:, 0] = self.u0
        s_t[0] = self.s0
        v_t[0] = self.v0

        for k in range(self.Time_len - 1):
            # 🔹 Apply control strategy at each time step
            if self.control:
                qc_t[k] = self.control.apply_control(s_t[k], u_t[:self.N+1, k], v_t[k])

            # Compute update law
            du_dt, ds_dt, dv_dt = self.model.compute_update_law(s_t[k], u_t[:, k], v_t[k], qc_t[k])
            u_t[:, k + 1] = u_t[:, k] + self.dt * du_dt
            s_t[k + 1] = s_t[k] + self.dt * ds_dt
            v_t[k + 1] = v_t[k] + self.dt * dv_dt

        return self.time, s_t, u_t, qc_t

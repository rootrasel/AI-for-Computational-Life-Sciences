"""
Biochemical Network Dynamics:
ODE simulation of an enzymatic negative feedback oscillator (Goodwin Oscillator)
and basic stoichiometric Flux Balance Analysis (FBA) linear programming setup.
"""

from typing import Tuple, List
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import linprog


def goodwin_oscillator(t: float, y: List[float], a1: float, b1: float, a2: float, b2: float, a3: float, b3: float, n: int) -> List[float]:
    """
    Goodwin model of cellular circadian/biochemical oscillations.
    y[0]: mRNA, y[1]: Protein, y[2]: Repressor
    """
    X, Y, Z = y
    dX_dt = (a1 / (1.0 + (Z ** n))) - b1 * X
    dY_dt = a2 * X - b2 * Y
    dZ_dt = a3 * Y - b3 * Z
    return [dX_dt, dY_dt, dZ_dt]


def simulate_oscillator(
    t_span: Tuple[float, float] = (0.0, 100.0),
    initial_state: List[float] = [0.1, 0.1, 0.1]
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate negative feedback loop using explicit Runge-Kutta solver."""
    params = (1.0, 0.1, 0.1, 0.1, 0.1, 0.1, 8)  # n=8 yields sustained limit cycle
    sol = solve_ivp(
        fun=lambda t, y: goodwin_oscillator(t, y, *params),
        t_span=t_span,
        y0=initial_state,
        dense_output=True,
        t_eval=np.linspace(t_span[0], t_span[1], 1000)
    )
    return sol.t, sol.y


def run_toy_fba(
    stoichiometric_matrix: np.ndarray,
    objective_weights: np.ndarray,
    flux_bounds: List[Tuple[float, float]]
) -> Tuple[float, np.ndarray]:
    """
    Solve toy Flux Balance Analysis linear program:
    maximize c^T v
    subject to S v = 0, v_lower <= v <= v_upper
    """
    # linprog minimizes c^T v, so negate objective
    c = -1.0 * objective_weights
    A_eq = stoichiometric_matrix
    b_eq = np.zeros(stoichiometric_matrix.shape[0])
    
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=flux_bounds, method='highs')
    if res.success:
        return -res.fun, res.x
    raise RuntimeError(f"FBA linear program failed: {res.message}")


if __name__ == "__main__":
    t, y = simulate_oscillator(t_span=(0, 50))
    print(f"Oscillator simulated: {len(t)} time steps. Final repressor level: {y[2, -1]:.3f}")
    
    # Toy network: A -> B -> C -> output
    # Reactions: v0 (input->A), v1 (A->B), v2 (B->C), v3 (C->biomass)
    S = np.array([
        [ 1.0, -1.0,  0.0,  0.0],  # d[A]/dt
        [ 0.0,  1.0, -1.0,  0.0],  # d[B]/dt
        [ 0.0,  0.0,  1.0, -1.0]   # d[C]/dt
    ])
    c = np.array([0.0, 0.0, 0.0, 1.0])  # maximize v3
    bounds = [(0, 10), (0, 10), (0, 10), (0, 10)]
    opt_val, fluxes = run_toy_fba(S, c, bounds)
    print(f"Optimal biomass flux: {opt_val:.2f}, fluxes: {fluxes}")

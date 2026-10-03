"""A34 c4: A32 D33's Zeno-window optimum at small chance per tick.

Two-level toy as in A32 c5: H = J sigma_x between u (unrecordable) and r (recordable); each tick: evolve tau,
then instrument with weight c|r><r| (no-record Kraus diag(1, sqrt(1-c))). Record rate = 1/E[time to
first record], E[T] = tau * sum_k ||M^k u||^2, M = D U, summed exactly (Stein / discrete Lyapunov).
A32's search grid for c < 1 starts at J tau = 0.05; here the grid starts at 0.001.
Also the continuous limit (c = gamma tau, tau -> 0): H_eff = J sx - i(gamma/2)|r><r|.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, solve_continuous_lyapunov
signal.alarm(28)

def rate(c, Jtau):
    U = np.array([[np.cos(Jtau), -1j * np.sin(Jtau)], [-1j * np.sin(Jtau), np.cos(Jtau)]])
    M = np.diag([1.0, np.sqrt(1 - c)]) @ U
    Xs = solve_discrete_lyapunov(M.conj().T, np.eye(2))
    return 1.0 / (Jtau * np.real(Xs[0, 0]))

for c in (0.5, 0.1, 0.05, 0.01):
    grid = np.exp(np.linspace(np.log(1e-4), np.log(2.0), 6000))
    r = np.array([rate(c, g) for g in grid])
    i = int(np.argmax(r))
    print(f"c={c:<5}: optimum J*tau = {grid[i]:.4f} (A32 rule c/2 = {c/2:.4f}); max rate {r[i]:.4f} J; "
          f"rate at J*tau = 0.05: {rate(c, 0.05):.4f} J")

def rate_cont(g):   # continuous limit, gamma in units of J
    Heff = np.array([[0, 1], [1, -0.5j * g]])
    A = -1j * Heff
    # E[T] = int_0^inf ||e^{At} u||^2 dt = u^dag X u with A^dag X + X A = -1
    Xc = solve_continuous_lyapunov(A.conj().T, -np.eye(2))
    return 1.0 / np.real(Xc[0, 0])
gs = np.linspace(0.05, 10, 20000)
rc = np.array([rate_cont(g) for g in gs])
i = int(np.argmax(rc))
print(f"continuous limit: best gamma = {gs[i]:.3f} J, max rate {rc[i]:.4f} J -> tau* = c/gamma* = c/({gs[i]:.2f} J)")

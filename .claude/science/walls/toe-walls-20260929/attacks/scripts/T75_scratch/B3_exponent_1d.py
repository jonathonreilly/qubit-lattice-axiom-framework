"""B3: 1D half-space, stopped end w_0 = eps, ambient w_N = 1.  Weight-one bond energies:
F1 = (phi_x-phi_y)^2 ; F2 = (w_x-w_y)^2/(w_x+w_y) ; F3 = (w_x-w_y)^2/sqrt(w_x w_y).
Weight-two contrast: Fw = (w_x-w_y)^2.  Solve dF/dw_x = 0 at every empty site.
Report the local exponent p(n) = d ln w / d ln n (central difference)."""
import numpy as np, json
from scipy.optimize import root

def dF(name, a, b):
    """d/da of the bond energy b(a,b)."""
    if name == "F1":   # (sqrt a - sqrt b)^2
        return 1 - np.sqrt(b / a)
    if name == "F2":
        return (a - b) * (a + 3 * b) / (a + b) ** 2
    if name == "F3":
        return (a - b) * (3 * a + b) / (2 * a * np.sqrt(a * b))
    if name == "Fw":   # weight two
        return 2 * (a - b)
    raise ValueError

def solve(name, N=600, eps=1e-9):
    n = np.arange(N + 1, dtype=float)
    def resid(u):
        w = np.empty(N + 1); w[0] = eps; w[N] = 1.0; w[1:N] = np.exp(u)
        x = w[1:N]
        return dF(name, x, w[:N-1]) + dF(name, x, w[2:]) if True else None
    # initial guess: phi linear (F1 solution) -> w = (n/N)^2 clipped
    u0 = (1 if name == "Fw" else 2) * np.log(np.maximum(n[1:N] / N, 1e-6))
    sol = root(resid, u0, method="hybr", tol=1e-13)
    w = np.empty(N + 1); w[0] = eps; w[N] = 1.0; w[1:N] = np.exp(sol.x)
    return w, sol.success, np.max(np.abs(resid(sol.x)))

def pexp(w, n):
    return (np.log(w[n + 1]) - np.log(w[n - 1])) / (np.log(n + 1) - np.log(n - 1))

if __name__ == "__main__":
    out = {}
    ns = [2, 3, 5, 10, 20, 40, 80]
    print("local exponent p(n) = dln w / dln n   (N=600, w_0=1e-9)")
    print(" energy   ok  resid    " + "  ".join(f"n={n:<3d}" for n in ns))
    for name in ("F1", "F2", "F3", "Fw"):
        w, ok, r = solve(name)
        ps = [pexp(w, n) for n in ns]
        print(f" {name:6s} {str(ok):5s} {r:8.1e} " + "  ".join(f"{p:6.3f}" for p in ps) + f"   w_1={w[1]:.3e} w_2={w[2]:.3e}")
        out[name] = dict(ok=bool(ok), resid=float(r), p=dict(zip(map(int, ns), map(float, ps))), w1=float(w[1]), w2=float(w[2]))
    json.dump(out, open("B3_results.json", "w"), indent=1)

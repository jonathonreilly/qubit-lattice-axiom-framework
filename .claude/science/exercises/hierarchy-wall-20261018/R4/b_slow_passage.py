"""Route B tests: how long can an RG flow linger with O(1) inputs?

b1: normal forms, closed form vs numerical quadrature.
b2: random 1D and 2D polynomial flows, O(1) coefficients, O(1) starts.
    For trajectories with T >= L*, record min |beta| along the path and the
    distance of the closest approach to a fixed point.
b3: comparator, the 2D Potts merger family.
"""
import numpy as np
from scipy.integrate import quad, solve_ivp

rng = np.random.default_rng(1018)
LSTAR = 38.4
U_END = 3.0   # 'runaway' / coupling became O(1) -> gap generated

print("== b1: normal forms ==")
for y in (0.0, 0.013, 0.1, 1.0):
    for b, u0 in ((1.0, 1.0), (1.0, 0.1), (1/(8*np.pi**2), 1.0)):
        f = lambda u: 1.0 / (y * u + b * u * u)
        Tnum = quad(f, u0, np.inf, limit=400)[0]
        Tex = (1 / y) * np.log(1 + y / (b * u0)) if y > 0 else 1 / (b * u0)
        print(f"transcritical y={y:<6} b={b:.4g} u0={u0}: T_num={Tnum:.4f} "
              f"T_exact={Tex:.4f} bound 1/(b u0)={1/(b*u0):.4f} ok={Tnum <= 1/(b*u0)+1e-9}")
for eps in (0.001, 0.026, 0.3):
    c, r0 = 1.0, 1.0
    Tnum = quad(lambda r: 1.0 / (eps * r + c * r ** 3), r0, np.inf)[0]
    print(f"weak focus / pitchfork eps={eps}: T_num={Tnum:.4f}  bound 1/(2 c r0^2)={1/(2*c*r0**2):.4f}")
for mu in (1e-1, 1e-2, 6.7e-3, 1e-3):
    b = 1.0
    Tnum = quad(lambda u: 1.0 / (mu + b * u * u), -U_END, U_END, limit=400, points=[0.0])[0]
    print(f"ghost mu={mu}: T_num(-3->3)={Tnum:.3f}  pi/sqrt(b mu)={np.pi/np.sqrt(b*mu):.3f}")
print(f"needed ghost mu for L*: pi^2/L*^2 = {np.pi**2/LSTAR**2:.4e} (times 1/b)")

print()
print("== b2a: random 1D flows beta(u) = sum_{n<=4} a_n u^n, |a_n| <= 1 ==")
long1d = []
n1 = 0
for trial in range(40000):
    a = rng.uniform(-1, 1, 5)
    u0 = rng.uniform(-1, 1)
    beta = np.polynomial.Polynomial(a)
    # direction of flow from u0; run until |u| >= U_END or a fixed point blocks
    s0 = beta(u0)
    if abs(s0) < 1e-12:
        continue
    direction = np.sign(s0)
    roots = beta.roots()
    real = np.sort(roots[np.abs(roots.imag) < 1e-12].real)
    ahead = real[(real - u0) * direction > 0]
    if ahead.size and abs(ahead[0]) < U_END:
        continue  # flows into a fixed point: no gap (conformal IR)
    u1 = direction * U_END
    grid = np.linspace(u0, u1, 4001)
    bv = np.abs(beta(grid))
    T = np.trapezoid(1 / bv, grid) * direction
    n1 += 1
    if T >= LSTAR:
        im = np.argmin(bv)
        dist_fp = np.min(np.abs(roots - grid[im])) if roots.size else np.inf
        long1d.append((T, bv.min(), dist_fp))
long1d.sort()
print(f"gapped trajectories: {n1}; with T >= L*: {len(long1d)} ({len(long1d)/n1:.2e})")
if long1d:
    mins = np.array([x[1] for x in long1d])
    print(f"  min|beta| on path for T>=L*: max = {mins.max():.3e}, median = {np.median(mins):.3e}")
    print(f"  closest complex/real zero of beta to the slowest point: max distance = "
          f"{max(x[2] for x in long1d):.3e}")

print()
print("== b2b: random 2D quadratic flows, |coeff| <= 1 ==")
def make_flow():
    A = rng.uniform(-1, 1, (2, 6))  # 1, x, y, x^2, xy, y^2
    def f(t, z):
        x, y = z
        m = np.array([1.0, x, y, x * x, x * y, y * y])
        return A @ m
    return A, f

def runaway(t, z):
    return np.hypot(z[0], z[1]) - U_END
runaway.terminal = True

long2d = []
n2 = 0
for trial in range(3000):
    A, f = make_flow()
    z0 = rng.uniform(-1, 1, 2)
    sol = solve_ivp(f, (0, 400), z0, events=runaway, max_step=0.05, rtol=1e-8, atol=1e-10)
    if sol.status != 1:
        continue  # never ran away (fixed point or cycle): no gap
    n2 += 1
    T = sol.t_events[0][0]
    if T >= LSTAR:
        speeds = np.array([np.hypot(*f(0, sol.y[:, i])) for i in range(sol.y.shape[1])])
        # winding number around the slowest point, to detect spirals
        ang = np.unwrap(np.arctan2(sol.y[1] - sol.y[1].mean(), sol.y[0] - sol.y[0].mean()))
        long2d.append((T, speeds.min(), abs(ang[-1] - ang[0]) / (2 * np.pi)))
print(f"gapped trajectories: {n2}; with T >= L*: {len(long2d)}")
for row in sorted(long2d, reverse=True)[:8]:
    print(f"  T={row[0]:.1f}  min|beta| on path={row[1]:.2e}  windings~{row[2]:.1f}")
if long2d:
    print(f"  max min|beta| among T>=L*: {max(r[1] for r in long2d):.3e}")

print()
print("== b3: comparator, 2D Potts merger family (q_c = 4) ==")
# T(q) = ln xi; asymptotic xi ~ exp(pi^2/sqrt(q-4)) / (8 sqrt 2) (Buffenoir-Wallon form)
for q in (5, 6, 7, 8):
    T = np.pi ** 2 / np.sqrt(q - 4) - np.log(8 * np.sqrt(2))
    print(f"q={q}: T ~ {T:.2f}  xi ~ {np.exp(T):.3g}")
print("exact comparator: xi(q=5) = 2512 (ln = 7.83)")
qneed = 4 + (np.pi ** 2 / (LSTAR + np.log(8 * np.sqrt(2)))) ** 2
print(f"needed q for T = L*: q = {qneed:.4f}  (distance to nearest integer above 4: {5-qneed:.3f})")

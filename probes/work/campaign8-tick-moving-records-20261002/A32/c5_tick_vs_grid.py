"""
A32 check C5: record tick tau versus grid spacing a (Q5).

Supplied toy: one excitation hopping with strength J (top speed 2Ja per axis). Dose per tick x = 2*J*tau
= (possibilities' top speed) / (records' speed limit a/tau).

C5a 1D: weight beyond the record cone |d| > n after n ticks: sum_{|d|>n} |J_d(n x)|^2.
     x<1: exponential, rate 2*eta(x); x=1 (record speed = possibilities' top speed): power law,
     predicted 2 * 2^(1/3) * Ai'(0)^2 * n^(-1/3) = 0.1688 n^(-1/3) (Airy asymptotics); x>1: tends to
     1 - (2/pi) arcsin(1/x) (arcsine law of the free walk).
C5b 3D: weight beyond the L1 record cone (one site per tick in any axis direction), per-axis dose x;
     the possibilities' L1 top speed is 3x, so x = 1/3 is the matched value.
C5c aliasing arithmetic at matched ticks (records sample the possibilities only at ticks).
C5d Zeno window for an O(1) chance per tick: two-level toy H = J sigma_x between u and r, weight F = c|r><r|.
"""
import signal
import numpy as np
from scipy.special import jv, airy
signal.alarm(55)

def eta(x):
    s = np.sqrt(1 - x * x)
    return np.log((1 + s) / x) - s

def p1d(n, x, dmax):
    d = np.arange(-dmax, dmax + 1)
    return d, jv(d, n * x) ** 2

print("C5a. 1D: weight beyond the record cone after n ticks")
ai, aip, bi, bip = airy(0.0)
pred_c = 2 * 2 ** (1 / 3) * aip ** 2
print(f"  Airy prediction at x=1: {pred_c:.5f} * n^(-1/3)")
print("  n       x=0.5          x=0.9          x=1.0 (ratio to Airy)     x=1.1 (limit {:.4f})".format(1 - 2 / np.pi * np.arcsin(1 / 1.1)))
for n in [10, 30, 100, 300, 1000, 3000]:
    row = []
    for x in [0.5, 0.9, 1.0, 1.1]:
        dmax = int(n * max(x, 1) + 60 * n ** (1 / 3) + 60)
        d, p = p1d(n, x, dmax)
        out = p[np.abs(d) > n].sum()
        row.append((out, p.sum()))
    r1 = row[2][0] / (pred_c * n ** (-1 / 3))
    print(f"  {n:<7} {row[0][0]:<14.3e} {row[1][0]:<14.3e} {row[2][0]:.4e} ({r1:.4f})        {row[3][0]:.4f}   [norms {min(r[1] for r in row):.12f}]")
print("  decay rates -ln(P_out)/n at n=100 vs 2*eta(x):")
for x in [0.5, 0.9]:
    d, p = p1d(100, x, 400); P100 = p[np.abs(d) > 100].sum()
    d, p = p1d(200, x, 700); P200 = p[np.abs(d) > 200].sum()
    print(f"    x={x}: slope between n=100 and 200 = {-(np.log(P200) - np.log(P100)) / 100:.4f}   2*eta = {2 * eta(x):.4f}")

print("\nC5b. 3D: weight beyond the L1 record cone, per-axis dose x (matched at x=1/3)")
print("  n       x=0.2          x=0.3          x=1/3          x=0.4")
for n in [10, 30, 100, 300]:
    row = []
    for x in [0.2, 0.3, 1 / 3, 0.4]:
        dmax = int(n * x * 1.0 + 40 * n ** (1 / 3) + 40)
        d, p = p1d(n, x, dmax)
        q = np.zeros(dmax + 1)
        for di, pi in zip(d, p):
            q[abs(di)] += pi
        qq = np.convolve(np.convolve(q, q), q)
        out = qq[n + 1:].sum()
        row.append(out)
    print(f"  {n:<7} {row[0]:<14.3e} {row[1]:<14.3e} {row[2]:<14.3e} {row[3]:<14.3e}")

print("\nC5c. Aliasing at matched ticks (no time doubler needs bandwidth*tau < 2*pi; A27 Step 7)")
for name, W, tau in [("1D hopping, tau = a/v_max = 1/(2J)", 4.0, 0.5),
                     ("3D hopping, L1-matched tau = 1/(6J)", 12.0, 1 / 6),
                     ("3D hopping, axis-matched tau = 1/(2J)", 12.0, 0.5),
                     ("3D hopping, tau = 1/J", 12.0, 1.0)]:
    print(f"  {name:<42} bandwidth*tau = {W * tau:.4f}  vs 2*pi = {2 * np.pi:.4f}  -> {'no doubler' if W * tau < 2 * np.pi else 'ALIASING'}")

print("\nC5d. Zeno window: record rate (1/mean time to record, units of J) vs J*tau, two-level toy")
def rate(c, Jtau, J=1.0):
    """1/E[time to first record]; E[T] = tau * sum_k ||M^k psi0||^2 with M = D U, summed exactly
    via the Stein equation X = 1 + M^dag X M."""
    from scipy.linalg import solve_discrete_lyapunov
    tau = Jtau / J
    U = np.array([[np.cos(Jtau), -1j * np.sin(Jtau)], [-1j * np.sin(Jtau), np.cos(Jtau)]])
    D = np.diag([1.0, np.sqrt(1 - c)])
    M = D @ U
    Xs = solve_discrete_lyapunov(M.conj().T, np.eye(2))   # X = M^dag X M + 1
    psi0 = np.array([1.0, 0.0])
    S = np.real(psi0 @ Xs @ psi0)
    return 1.0 / (tau * S)
Jtaus = [0.01, 0.03, 0.1, 0.3, 0.6, 1.0, 1.1656, 1.5, 2.0, 3.0]
print("  J*tau   " + "".join(f"c={c:<10}" for c in [1.0, 0.5, 0.1]) + "   exact c=1: sin^2(J tau)/(J tau)")
for jt in Jtaus:
    vals = [rate(c, jt) for c in [1.0, 0.5, 0.1]]
    print(f"  {jt:<7} " + "".join(f"{v:<12.4f}" for v in vals) + f"   {np.sin(jt) ** 2 / jt:.4f}")
# optimum for c=1: 2 Jtau = tan(Jtau)
from scipy.optimize import brentq
jt_star = brentq(lambda t: np.tan(t) - 2 * t, 1.0, 1.4)
print(f"  c=1 optimum: J*tau* = {jt_star:.5f}, rate* = {np.sin(jt_star) ** 2 / jt_star:.5f} J;"
      f"  small tau: rate ~ J^2 tau (Zeno);  in units of a/v_max = 1/(2J): tau* = {2 * jt_star:.3f} a/v_max")
for c in [0.5, 0.1]:
    grid = np.linspace(0.05, 4.0, 400)
    rs = [rate(c, g) for g in grid]
    i = int(np.argmax(rs))
    print(f"  c={c}: optimum J*tau ~ {grid[i]:.3f}, rate {rs[i]:.4f} J")

"""C5 s1: conventions, transformation rules and a positive control.

Positive control (NOT a finite-range walk): the analytic O-covariant map
    V_M(k) = (f + i g.sigma)/sqrt(f^2+|g|^2),  f = M - sum_a cos k_a,  g = (sin k_a).
Independent prediction by preimage counting (NOTE.md, Prop. P): with c = +-1 a single
convention sign, W3[V_M] = c * n(M), n = 0, 1, -2, 1, 0 for M in (3,inf), (1,3), (-1,1),
(-3,-1), (-inf,-3).  We fix nothing from the integral except one global sign c and test
all five values.
"""
import itertools
import sys
import numpy as np
from w3lib import Checker, PAULI, smooth_grid, wilson_weyl_map, w3_from_fields

ck = Checker()
rng = np.random.default_rng(1)

# --- proper cubic group O and spin-1/2 lifts ---
def cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            if np.linalg.det(R) > 0:
                mats.append(R)
    return mats

def spin_lift(R):
    # D(R) sigma_a D^dag = sum_b R_ba sigma_b ; build from axis-angle
    w, v = np.linalg.eig(R)
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if abs(ang) < 1e-12:
        return np.eye(2, dtype=complex)
    if abs(ang - np.pi) < 1e-9:
        n = np.real(v[:, np.argmin(np.abs(w - 1))])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    n = n / np.linalg.norm(n)
    return np.cos(ang / 2) * PAULI[0] - 1j * np.sin(ang / 2) * sum(n[a] * PAULI[a + 1] for a in range(3))

O = cubic_group()
ck.check('proper cubic group has 24 elements', len(O) == 24)
lift_ok = True
for R in O:
    D = spin_lift(R)
    for a in range(3):
        lhs = D @ PAULI[a + 1] @ D.conj().T
        rhs = sum(R[b, a] * PAULI[b + 1] for b in range(3))
        lift_ok &= np.allclose(lhs, rhs)
ck.check('spin-1/2 lifts satisfy D sigma_a D^dag = sum_b R_ba sigma_b for all 24 R', lift_ok)

def V_point(M, k):
    f = M - np.cos(k).sum()
    g = np.sin(k)
    W = f * PAULI[0] + 1j * sum(g[a] * PAULI[a + 1] for a in range(3))
    return W / np.sqrt(f * f + g @ g)

cov = 0.0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3)
    R = O[rng.integers(24)]
    D = spin_lift(R)
    cov = max(cov, np.abs(V_point(2.0, R @ k) - D @ V_point(2.0, k) @ D.conj().T).max())
ck.check(f'V_M is exactly O-covariant with the full-soldered action (max dev {cov:.1e} on 200 samples)', cov < 1e-13)

# --- W3 of the positive control, convergence in N ---
Ms = [3.5, 2.0, 0.5, -2.0, -3.5]
n_pred = [0, 1, -2, 1, 0]
vals = {}
for M in Ms:
    row = []
    for N in (16, 32, 64, 96):
        U, dU = smooth_grid(wilson_weyl_map(M), N)
        row.append(w3_from_fields(U, dU))
    vals[M] = row
    print(f'M={M:5.2f}: W3(N=16,32,64,96) = ' + ', '.join(f'{v.real:+.12f}{v.imag:+.1e}i' for v in row))
c = np.sign(vals[2.0][-1].real)
print(f'global convention sign c = {c:+.0f} (fixed from M=2 only)')
for M, n in zip(Ms, n_pred):
    v = vals[M][-1]
    ck.check(f'M={M}: W3 = c*{n} (|W3 - c n| = {abs(v - c*n):.1e} at N=96; imag {abs(v.imag):.1e})', abs(v - c * n) < 1e-6)
    # run 1 used |W3(64)-W3(32)| < 1e-6, which failed for M=3.5,0.5,-3.5 (slower analytic convergence
    # where the gap min|d| is small); superseded log kept. Criterion now: successive differences shrink
    # and the last one is < 1e-6.
    d1, d2 = abs(vals[M][2]-vals[M][1]), abs(vals[M][3]-vals[M][2])
    ck.check(f'M={M}: grid convergence |W3(64)-W3(32)|={d1:.1e} > |W3(96)-W3(64)|={d2:.1e}, last < 1e-6', d2 < d1 and d2 < 1e-6)

# --- transformation rules on a NON-covariant smooth map: X = V_2 * exp(i k1 sigma_x) * C ---
C = np.array([[np.cos(0.3), 1j*np.sin(0.3)], [1j*np.sin(0.3), np.cos(0.3)]])
def X_func(Rmat=np.eye(3), conj=np.eye(2), phase=False):
    base = wilson_weyl_map(2.0)
    def func(K1, K2, K3):
        Kv = [K1, K2, K3]
        # evaluate at k' = Rmat k  (chain rule for derivatives)
        Kp = [sum(Rmat[i, j] * Kv[j] for j in range(3)) for i in range(3)]
        U0, dU0p = base(*Kp)
        dU0 = [sum(dU0p[i] * Rmat[i, b] for i in range(3)) for b in range(3)]
        s1 = np.exp(1j * Kp[0])  # placeholder, not used
        E = np.cos(Kp[0])[..., None, None] * PAULI[0] + 1j * np.sin(Kp[0])[..., None, None] * PAULI[1]
        dEp = -np.sin(Kp[0])[..., None, None] * PAULI[0] + 1j * np.cos(Kp[0])[..., None, None] * PAULI[1]
        dE = [dEp * Rmat[0, b] for b in range(3)]
        U = U0 @ E @ C
        dU = [(dU0[b] @ E + U0 @ dE[b]) @ C for b in range(3)]
        if phase:
            ph = np.exp(1j * (K1 + 2 * K3))[..., None, None]
            dU = [ph * dU[0] + 1j * ph * U, ph * dU[1], ph * dU[2] + 2j * ph * U]
            U = ph * U
        U = conj @ U @ conj.conj().T
        dU = [conj @ d @ conj.conj().T for d in dU]
        return U, dU
    return func

N = 48
w_base = w3_from_fields(*smooth_grid(X_func(), N))
ck.check(f'additivity with a one-variable Laurent factor: W3[V_2 e^(i k1 sx) C] = W3[V_2] (got {w_base.real:+.10f})', abs(w_base - c) < 1e-6)
R = O[7]
Dc = spin_lift(O[11])
w_rot = w3_from_fields(*smooth_grid(X_func(Rmat=R, conj=Dc), N))
ck.check(f'proper rotation + coin conjugation preserve W3 ({w_rot.real:+.10f})', abs(w_rot - w_base) < 1e-6)
w_par = w3_from_fields(*smooth_grid(X_func(Rmat=-np.eye(3)), N))
ck.check(f'inversion k -> -k flips the sign of W3 ({w_par.real:+.10f})', abs(w_par + w_base) < 1e-6)
w_ph = w3_from_fields(*smooth_grid(X_func(phase=True), N))
ck.check(f'scalar phase e^(i(k1+2k3)) (det winding) leaves W3 unchanged ({w_ph.real:+.10f})', abs(w_ph - w_base) < 1e-6)

# product of two controls: additivity  W3[V_2 V_0.5] = c(1 - 2)
def prod_func(K1, K2, K3):
    U1, d1 = wilson_weyl_map(2.0)(K1, K2, K3)
    U2, d2 = wilson_weyl_map(0.5)(K1, K2, K3)
    return U1 @ U2, [d1[b] @ U2 + U1 @ d2[b] for b in range(3)]
w_pr = w3_from_fields(*smooth_grid(prod_func, 64))
ck.check(f'Polyakov-Wiegmann additivity: W3[V_2 V_0.5] = c(1-2) (got {w_pr.real:+.10f})', abs(w_pr + c) < 1e-6)

# --- nodes of V_2: band touchings V = +-1 occur exactly where g = 0, i.e. at the 8 TRIM ---
print('Nodes of V_2 (quasienergy 0 if V=+1, pi if V=-1); chi = sign det(dg/dk) = prod sign cos p_a:')
sum0 = sumpi = 0
for p in itertools.product((0.0, np.pi), repeat=3):
    p = np.array(p)
    f = 2.0 - np.cos(p).sum()
    chi = int(np.prod(np.sign(np.cos(p))))
    qe = 'pi' if f < 0 else '0'
    if f < 0:
        sumpi += chi
    else:
        sum0 += chi
    print(f'  p={tuple(int(round(x/np.pi)) for x in p)}pi  f={f:+.0f}  quasienergy {qe:>2}  chi={chi:+d}')
print(f'  sum chi at quasienergy pi = {sumpi:+d}, at 0 = {sum0:+d}')
ck.check('V_2: the pi-sheet node chirality sum equals c*W3 and the 0-sheet sum equals -c*W3 (unbalanced per sheet)',
         sumpi == int(round((c * vals[2.0][-1]).real)) and sum0 == -sumpi)
sys.exit(ck.total())

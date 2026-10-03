"""
A32 check C4: two neighbouring sites forming records on the same tick (I1) under Option R.

Supplied toy: qubits 0-1-2-3 in a chain plus a distant qubit b (index 4); random entangled pure start.
Formation instruments at x=1 and y=2 (neighbours), A28 form: Kraus P_k sqrt(F) (record k, site cut
to agree) and sqrt(1-F) (no record).

Cases:
 W1  one-site weights F_x = c (1 + m_x.sigma)/2 on x only (menu Z): Kraus operators of x and y
     act on different qubits, so the two instruments commute: "together" = either order (EXACT).
 W2  star weights (A28 weight B): F_x = c [P_s(0,1) + P_s(1,2)]/2, F_y = c [P_s(1,2) + P_s(2,3)]/2.
     They overlap, so order matters; prediction: order effect O(c^2).
 W3  one-site weights, but y's menu is set by a recorded neighbour: start-of-tick reading (y ignores a
     record x forms on the same tick: menu Z) vs within-tick reading (if x formed, y takes x's frame X).
     Prediction: difference O(c^2) (needs both to form).
No-signalling: b's choice (nothing / record in Z / record in X) leaves the (x,y) record law unchanged.
"""
import signal, itertools
import numpy as np
signal.alarm(55)
rng = np.random.default_rng(4032)
n = 5
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0, -1.0]).astype(complex)

def op(single, site):
    mats = [I2] * n
    mats[site] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out

def two(A, i, B, j):
    return op(A, i) @ op(B, j)

def P_singlet(i, j):
    # (1 - S_i.S_j*4)/4 = (1 - X X - Y Y - Z Z)/4
    return 0.25 * (np.eye(2 ** n) - two(X, i, X, j) - two(Y, i, Y, j) - two(Z, i, Z, j))

def msqrt_psd(A):
    A = 0.5 * (A + A.conj().T)
    w, V = np.linalg.eigh(A)
    tol = 1e-12 * max(1.0, np.abs(w).max())
    w = np.where(w < tol, 0.0, w)          # exact zeros stay zero (no spurious null-space square roots)
    return (V * np.sqrt(w)) @ V.conj().T

def proj(basis, k, site):
    if basis == 'Z':
        v = np.array([1, 0]) if k == 0 else np.array([0, 1])
    else:
        v = np.array([1, 1]) / np.sqrt(2) if k == 0 else np.array([1, -1]) / np.sqrt(2)
    return op(np.outer(v, v.conj()).astype(complex), site)

def instrument(F, site, basis):
    sF = msqrt_psd(F)
    K = {k: proj(basis, k, site) @ sF for k in (0, 1)}
    K['-'] = msqrt_psd(np.eye(2 ** n) - F)
    return K

def apply(rho, K):
    return {k: Kk @ rho @ Kk.conj().T for k, Kk in K.items()}

def law_two(rho, Kx_fn, Ky_fn, order):
    """Kx_fn(outcome_y or None) -> instrument dict for x; Ky_fn(outcome_x or None) -> for y.
    order 'xy': x first (y's instrument may depend on x's outcome), 'yx' the reverse."""
    p = {}
    if order == 'xy':
        Kx = Kx_fn(None)
        for kx, r1 in apply(rho, Kx).items():
            Ky = Ky_fn(kx)
            for ky, r2 in apply(r1, Ky).items():
                p[(kx, ky)] = np.trace(r2).real
    else:
        Ky = Ky_fn(None)
        for ky, r1 in apply(rho, Ky).items():
            Kx = Kx_fn(ky)
            for kx, r2 in apply(r1, Kx).items():
                p[(kx, ky)] = np.trace(r2).real
    return p

def tvd(p, q):
    return 0.5 * sum(abs(p[k] - q[k]) for k in p)

def b_choice(rho, choice):
    if choice == 'none':
        return rho
    out = np.zeros_like(rho)
    for k in (0, 1):
        P = proj(choice, k, 4)
        out += P @ rho @ P
    return out

psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n); psi /= np.linalg.norm(psi)
rho0 = np.outer(psi, psi.conj())

mx = rng.normal(size=3); mx /= np.linalg.norm(mx)
my = rng.normal(size=3); my /= np.linalg.norm(my)
def onesite(c, m, site):
    return c * 0.5 * (np.eye(2 ** n) + m[0] * op(X, site) + m[1] * op(Y, site) + m[2] * op(Z, site))

print("C4. Same-tick formation at neighbouring sites x=1, y=2 (random entangled 5-qubit start)")
print("  c       W1 one-site: TV(xy,yx)   W2 star: TV(xy,yx)   /c^2      W3 menu start-of-tick vs within-tick   /c^2    P(both form, W2)")
for c in [0.4, 0.2, 0.1, 0.05, 0.025]:
    # W1
    Fx, Fy = onesite(c, mx, 1), onesite(c, my, 2)
    Kx, Ky = instrument(Fx, 1, 'Z'), instrument(Fy, 2, 'Z')
    w1 = tvd(law_two(rho0, lambda o: Kx, lambda o: Ky, 'xy'), law_two(rho0, lambda o: Kx, lambda o: Ky, 'yx'))
    # W2
    Fx2 = c * 0.5 * (P_singlet(0, 1) + P_singlet(1, 2)); Fy2 = c * 0.5 * (P_singlet(1, 2) + P_singlet(2, 3))
    Kx2, Ky2 = instrument(Fx2, 1, 'Z'), instrument(Fy2, 2, 'Z')
    pxy = law_two(rho0, lambda o: Kx2, lambda o: Ky2, 'xy'); pyx = law_two(rho0, lambda o: Kx2, lambda o: Ky2, 'yx')
    w2 = tvd(pxy, pyx)
    both = sum(v for (a, b), v in pxy.items() if a != '-' and b != '-')
    # W3: x has menu X (set by a start-of-tick recorded neighbour); y has menu Z at start of tick.
    KxX = instrument(Fx, 1, 'X')
    KyZ = instrument(Fy, 2, 'Z'); KyX = instrument(Fy, 2, 'X')
    start = law_two(rho0, lambda o: KxX, lambda o: KyZ, 'xy')
    within = law_two(rho0, lambda o: KxX, lambda o: (KyX if o in (0, 1) else KyZ), 'xy')
    w3 = tvd(start, within)
    print(f"  {c:<7} {w1:<24.2e} {w2:<20.3e} {w2/c**2:<9.4f} {w3:<38.3e} {w3/c**2:<7.4f} {both:.3e}")

print("\n  No-signalling: TV of the (x,y) record law across b's choices {none, Z record, X record}, c = 0.2")
c = 0.2
Fx2 = c * 0.5 * (P_singlet(0, 1) + P_singlet(1, 2)); Fy2 = c * 0.5 * (P_singlet(1, 2) + P_singlet(2, 3))
Kx2, Ky2 = instrument(Fx2, 1, 'Z'), instrument(Fy2, 2, 'Z')
for order in ['xy', 'yx']:
    laws = [law_two(b_choice(rho0, ch), lambda o: Kx2, lambda o: Ky2, order) for ch in ['none', 'Z', 'X']]
    rnd = [{k: 0.5 * (law_two(b_choice(rho0, ch), lambda o: Kx2, lambda o: Ky2, 'xy')[k] +
                      law_two(b_choice(rho0, ch), lambda o: Kx2, lambda o: Ky2, 'yx')[k]) for k in laws[0]} for ch in ['none', 'Z', 'X']]
    print(f"    W2 order {order}: max TV = {max(tvd(laws[i], laws[j]) for i in range(3) for j in range(3)):.2e};"
          f"  random order: max TV = {max(tvd(rnd[i], rnd[j]) for i in range(3) for j in range(3)):.2e};"
          f"  total prob = {sum(laws[0].values()):.15f}")

# completeness check of the instruments
Kc = instrument(Fx2, 1, 'Z')
S = sum(K.conj().T @ K for K in Kc.values())
print(f"  completeness ||sum K^dag K - 1|| = {np.linalg.norm(S - np.eye(2 ** n)):.2e}")

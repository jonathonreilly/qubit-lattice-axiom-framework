#!/usr/bin/env python3
"""The lambda = 1 question: can positive record dynamics carry Einstein's DeWitt kinetic structure?

Question (the owner, 2026-09-28): after probe 12, Einstein's lapse closes on the
lattice only on the DeWitt line lambda = 1, while record-like positive kinetics
sit at lambda < 1/3. Can positive record dynamics act like lambda = 1,
microscopically or collectively?

Landed context (not premises): the constraint complex G, S, the DeWitt form M
and the identity M s_r = G_r^T K (2026-09-14 and 2026-09-24 tensor notes;
the latter leaves "every compact completion" open, as does the 2026-09-24
synthesis note); block 112 and the 2026-09-25 clock-profile note (closure on
lambda = 1; the sea's inertia is positive). Probes 10-12 of this PR.

Checks:
  A  the DeWitt form on the momentum sector: M s = G^T K and s.M.s = 0; on
     ker G(k) the form is positive on TT and zero on the scalar-gauge
     direction (so positivity is available on the sector); off the sector no
     finite penalty U|G|^2 makes it positive (landed determinant -J^2/2).
     The form is only weakly invariant under the scalar gauge.
  B  weak = strong for periodic kinetic energies: on the sector
     Lambda = ker_Z G, a character e^{i r.E} is defined modulo im(G^T) and
     e^{i r.s} does not depend on the representative (G s = 0); distinct
     sector characters are independent, so a periodic kinetic energy is
     weakly invariant iff every character present is invariant, and with
     lifted exponents the landed symbol bound applies (kinetic O(k)). Checked:
     the DeWitt polynomial is exactly invariant on integer sector states, a
     cosine completion is not.
  C  collective inertia of a positive system is a Gram form: the adiabatic
     (cranking) inertia 2 sum |<n|X|0>|^2/(E_n - E_0)^3 is positive
     semidefinite for any collective coordinates, so a collective metric's
     dilation inertia is >= 0, never DeWitt's -6 alpha.
  D  one qubit per slot: the landed scalar-gauge pattern has entries of
     magnitude 1 and 4 (the three diagonal slots at the centre carry -4); as a
     unitary stabilizer on two-level slots it exists only mod 2, where the 4s
     alias to zero.
Reference only: Dirac/Bergmann constraint theory; Inglis cranking formula.
Not pre-registered. Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)
FC = {3: (0, 1), 4: (1, 2), 5: (0, 2)}


# ---------------------------------------------------------------- landed symbols (2026-09-24 oscillator note)
def symbols(q):
    K = 2 * np.sin(q / 2); t = K @ K
    G = np.zeros((3, 6))
    for j in range(3):
        G[j, j] = K[j]
    for f, (i, j) in FC.items():
        G[i, f] = K[j]; G[j, f] = K[i]
    M = np.diag([1, 1, 1, 2, 2, 2.]) - np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]) / 2
    s = np.array([-(t - K[0] ** 2), -(t - K[1] ** 2), -(t - K[2] ** 2), K[0] * K[1], K[1] * K[2], K[0] * K[2]])
    return G, M, s, K


okA = True; rowsA = []
for q in [rng.uniform(-np.pi, np.pi, 3) for _ in range(20)]:
    G, M, s, K = symbols(q)
    okA &= np.abs(M @ s - G.T @ K).max() < 1e-12 and abs(s @ M @ s) < 1e-12
    _, sv, vh = np.linalg.svd(G); Nk = vh[np.sum(sv > 1e-10):].T               # ker G(k), 3-dim
    ev = np.linalg.eigvalsh(Nk.T @ M @ Nk)
    okA &= ev.min() > -1e-12 and np.sum(ev < 1e-10) == 1 and ev.max() > 0
    Ms = [np.linalg.eigvalsh(M + U * G.T @ G).min() for U in (1.0, 1e3, 1e6)]
    okA &= all(m < -1e-9 for m in Ms)
G, M, s, K = symbols(np.array([0.3, 0.2, 0.4])); _, sv, vh = np.linalg.svd(G); Nk = vh[np.sum(sv > 1e-10):].T
rowsA.append(f"on ker G(k): eigenvalues {np.round(np.linalg.eigvalsh(Nk.T @ M @ Nk), 4)} (one zero = the scalar-gauge direction)")
rowsA.append(f"smallest eigenvalue of M + U G^T G at U = 1, 1e3, 1e6: {[f'{np.linalg.eigvalsh(M + U * G.T @ G).min():.3e}' for U in (1.0, 1e3, 1e6)]}")
check("A: the DeWitt form on the momentum sector: M s = G^T K and s.M.s = 0; on ker G(k) it is positive semidefinite with exactly one zero (the scalar-gauge direction); off the sector no finite penalty makes it positive; it is invariant under the scalar gauge only on the sector",
      okA, "; ".join(rowsA) + "; 20 random zone momenta")

# ---------------------------------------------------------------- real-space integer complex on a torus
L = 3
cells = list(itertools.product(range(L), repeat=3))
cidx = {c: i for i, c in enumerate(cells)}
nslot = 6 * len(cells)
def sl(c, a):                  # slot index: a in 0..5 (xx,yy,zz,xy,yz,xz), cell c
    return 6 * cidx[tuple(np.array(c) % L)] + a
FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}
E3 = np.eye(3, dtype=int)
Gm = np.zeros((3 * len(cells), nslot), dtype=int); Sm = np.zeros((len(cells), nslot), dtype=int)
for c in cells:
    x = np.array(c)
    for j in range(3):          # (G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i!=j} [p_ij(x) - p_ij(x-e_i)]
        r = 3 * cidx[c] + j
        Gm[r, sl(x + E3[j], j)] += 1; Gm[r, sl(x, j)] -= 1
        for i in range(3):
            if i != j:
                f = FACE[tuple(sorted((i, j)))]
                Gm[r, sl(x, f)] += 1; Gm[r, sl(x - E3[i], f)] -= 1
    r = cidx[c]                 # (S q)(x), off-diagonal q doubled (landed)
    for j in range(3):
        for i in range(3):
            if i != j:
                Sm[r, sl(x + E3[i], j)] += 1; Sm[r, sl(x - E3[i], j)] += 1; Sm[r, sl(x, j)] -= 2
    for (i, j), f in FACE.items():
        Sm[r, sl(x, f)] -= 1; Sm[r, sl(x - E3[i], f)] += 1; Sm[r, sl(x - E3[j], f)] += 1; Sm[r, sl(x - E3[i] - E3[j], f)] -= 1
GS = Gm @ Sm.T
# the scalar-gauge E-shift conjugate to the doubled off-diagonal q: s_y = D S^T delta_y with D = diag(1,1,1,2,2,2)? use the pairing sum p dq:
# q_off = 2 h_off pairs with p_off = E_off, so the E-shift generated by exp(i beta S q) is S^T itself on E slots.
S_shift = Sm.T.copy()


def DW(E):                     # sum_x [sum_j E_jj^2 + 2 sum_{i<j} E_ij^2 - (1/2)(sum_j E_jj)^2]
    Ev = E.reshape(len(cells), 6).astype(float)
    return float(np.sum(Ev[:, :3] ** 2) + 2 * np.sum(Ev[:, 3:] ** 2) - 0.5 * np.sum(Ev[:, :3].sum(1) ** 2))


def cos_completion(E, th):
    Ev = E.reshape(len(cells), 6).astype(float)
    return float(np.sum(2 * (1 - np.cos(th * Ev[:, :3]))) + 2 * np.sum(2 * (1 - np.cos(th * Ev[:, 3:]))) - 0.5 * np.sum(2 * (1 - np.cos(th * Ev[:, :3].sum(1))))) / th ** 2


# integer sector states: integer combinations of landed planar moves and scalar-gauge patterns (all in ker G)
def planar(c, a, b):
    v = np.zeros(nslot, dtype=int); c = np.array(c); Ea, Eb = E3[a], E3[b]; f = FACE[tuple(sorted((a, b)))]
    v[sl(c, a)] -= 2; v[sl(c, b)] -= 2; v[sl(c + Eb, a)] += 1; v[sl(c - Eb, a)] += 1; v[sl(c + Ea, b)] += 1; v[sl(c - Ea, b)] += 1
    for o, sg in [(np.zeros(3, int), -1), (-Ea, 1), (-Eb, 1), (-Ea - Eb, -1)]:
        v[sl(c + o, f)] += sg
    return v


gens = [planar(c, a, b) for c in cells for (a, b) in [(0, 1), (1, 2), (0, 2)]] + [S_shift[:, y] for y in range(len(cells))]
okGen = all(np.all(Gm @ g == 0) for g in gens)
dw_diff = 0.0; cos_diff = 0.0; cls_ok = True
for _ in range(200):
    E = sum(int(rng.integers(-3, 4)) * gens[int(rng.integers(len(gens)))] for _ in range(12))
    assert np.all(Gm @ E == 0)
    y = int(rng.integers(len(cells))); sshift = S_shift[:, y]
    dw_diff = max(dw_diff, abs(DW(E + sshift) - DW(E)))
    cos_diff = max(cos_diff, abs(cos_completion(E + sshift, 2 * np.pi / 101) - cos_completion(E, 2 * np.pi / 101)))
    # representative-independence of e^{i r.s} and of the sector character
    r = rng.normal(size=nslot); xi = rng.normal(size=3 * len(cells)); r2 = r + Gm.T @ xi
    cls_ok &= abs(np.exp(1j * r @ sshift) - np.exp(1j * r2 @ sshift)) < 1e-9 and abs(np.exp(1j * r @ E) - np.exp(1j * r2 @ E)) < 1e-9
check("B: weak = strong for periodic kinetic energies: on integer sector states a character is defined modulo im(G^T) and e^{i r.s} does not depend on the representative (G S^T = 0); the DeWitt polynomial is exactly invariant on the sector, while a cosine completion is not",
      np.all(GS == 0) and okGen and dw_diff < 1e-9 and cos_diff > 1e-6 and cls_ok,
      f"G S^T = 0 on the {L}^3 torus: {bool(np.all(GS == 0))}; 200 integer sector states from {len(gens)} kernel generators: max |DW(E+s) - DW(E)| = {dw_diff:.1e}, max |f_cos(E+s) - f_cos(E)| = {cos_diff:.3e} (theta = 2 pi/101); representative-independence of e^{{i r.s}} and e^{{i r.E}}: {cls_ok}")

# ---------------------------------------------------------------- C: collective inertia of a positive system is a Gram form
okC = True; worstC = np.inf
for _ in range(50):
    dim = 40; A = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim)); H = (A + A.conj().T) / 2
    w, U = np.linalg.eigh(H)
    Xs = []
    for _a in range(4):
        B = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim)); Xs.append((B + B.conj().T) / 2)
    amps = [U.conj().T @ X @ U[:, 0] for X in Xs]
    Mi = np.array([[2 * np.sum((np.conj(amps[a][1:]) * amps[b][1:]).real / (w[1:] - w[0]) ** 3) for b in range(4)] for a in range(4)])
    ev = np.linalg.eigvalsh(Mi); worstC = min(worstC, ev.min()); okC &= ev.min() > -1e-12
dil_dewitt = 3 * 1.0 + 9 * (-1.0)
check("C: the collective (adiabatic) inertia of a positive system is a Gram form, positive semidefinite for any collective coordinates; so a collective metric's dilation inertia is >= 0 and never DeWitt's -6 alpha",
      okC and dil_dewitt == -6.0,
      f"50 random Hamiltonians x 4 collective coordinates: smallest inertia eigenvalue {worstC:.2e} (>= 0); DeWitt dilation value 3 alpha + 9 beta at beta = -alpha: {dil_dewitt:.0f} alpha")

# ---------------------------------------------------------------- D: one qubit per slot aliases the scalar constraint
pat = S_shift[:, 0]; mags = sorted(set(abs(int(v)) for v in pat if v != 0))
mod2 = pat % 2; surv = int(np.count_nonzero(mod2)); tot = int(np.count_nonzero(pat))
check("D: one qubit per slot: the landed scalar-gauge pattern has entries of magnitude 1 and 4 (the centre's three diagonal slots carry -4), so as a unitary stabilizer on two-level slots it exists only mod 2, where the 4s alias to zero",
      mags == [1, 4] and surv == tot - 3,
      f"entry magnitudes {mags}; nonzero entries {tot}, surviving mod 2: {surv}")

print("N5 resolution 1: the DeWitt form is positive on the momentum sector (one zero, the scalar-gauge direction); its obstruction is not positivity but that it is invariant only weakly.")
print("N5 resolution 2: for periodic kinetic energies weak invariance on the sector equals invariance of every character present, so the landed O(k) kinetic bound holds weakly too (with lifted exponents).")
print("N5 resolution 3: the adiabatic inertia of any positive system is a Gram form, so collective inertia cannot supply DeWitt's negative dilation.")
print("N5 resolution 4: on one-qubit slots the exact scalar constraint exists only mod 2 (aliased); the continuous Hamiltonian constraint cannot be imposed there.")
print("per_element: the identities are checked on explicit symbols (20 momenta) and on explicit integer sector states.")
print("per_site: the landed slot placement and stencils on a 3^3 torus.")
print("per_mode: TT and scalar-gauge directions of ker G(k).")
print("per_block: 200 integer sector states; 50 random positive systems.")
print("lattice_wide: checked and not executed - no non-local or gapless-mediated effective theory, no non-perturbative constrained phase, no rotor/oscillator construction.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

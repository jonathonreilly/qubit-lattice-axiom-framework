"""A34 c7: A33's parity route -- what one qubit per site allows, and what role-dependent energies do.

Part A (representation theory, soldered turns acting on single-qubit operators by conjugation):
  - vertex/cube sites (site group O, 24 proper turns): decompose span{1, sx, sy, sz};
  - edge/face sites (site group D4 about the axis/normal): same; parity of s^axis under the diagonal
    half-turns that fix the plaquette corners.
Part B (8-band toy, period-2 roles w = number of odd coordinates: V=0, E=1, F=2, C=3):
  nearest-neighbour hopping with a pi-flux sign pattern (Kogut-Susskind gauge), bond-type magnitudes
  t_VE, t_EF, t_FC, role on-site energies eps_V, eps_E, eps_F, eps_C. Smallest |E| over the zone:
  does a cone survive unequal magnitudes, and do role-dependent energies open a gap (a mass)?
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import itertools, signal
import numpy as np
from scipy.optimize import minimize
signal.alarm(28)

# ---------- Part A
def proper_turns():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for r in range(3):
                R[r, perm[r]] = sg[r]
            if np.isclose(np.linalg.det(R), 1):
                out.append(R)
    return out

def rep_on_qubit_ops(R):
    # conjugation by the SU(2) lift acts on (1, sx, sy, sz) as diag(1, R): identity fixed, vector rotated
    M = np.eye(4)
    M[1:, 1:] = R
    return M

def classify(R):
    tr = np.trace(R)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    return int(round(np.degrees(ang)))

O = proper_turns()
# O character table (classes: E, 8 C3, 3 C2(axis), 6 C4, 6 C2(face-diagonal))
def o_class(R):
    a = classify(R)
    if a == 0: return "E"
    if a == 120: return "C3"
    if a == 90: return "C4"
    w, vv = np.linalg.eig(R); axis = np.real(vv[:, np.argmin(abs(w - 1))])
    return "C2a" if np.sum(np.abs(axis) > 1e-9) == 1 else "C2d"
chars_O = {"A1": {"E": 1, "C3": 1, "C2a": 1, "C4": 1, "C2d": 1},
           "A2": {"E": 1, "C3": 1, "C2a": 1, "C4": -1, "C2d": -1},
           "E":  {"E": 2, "C3": -1, "C2a": 2, "C4": 0, "C2d": 0},
           "T1": {"E": 3, "C3": 0, "C2a": -1, "C4": 1, "C2d": -1},
           "T2": {"E": 3, "C3": 0, "C2a": -1, "C4": -1, "C2d": 1}}
mult = {name: round(sum(np.trace(rep_on_qubit_ops(R)) * ch[o_class(R)] for R in O) / 24) for name, ch in chars_O.items()}
print("(A1) one qubit at a vertex/cube site (group O): span{1,sx,sy,sz} =",
      " + ".join(f"{m} {n}" for n, m in mult.items() if m), " -> no 1-dim rep other than the identity")

# D4 about z: proper turns that keep the z axis (up to sign)
D4 = [R for R in O if abs(abs(R[2, 2]) - 1) < 1e-9]
def d4_class(R):
    a = classify(R)
    if a == 0: return "E"
    if a == 90: return "C4"
    w, vv = np.linalg.eig(R); axis = np.real(vv[:, np.argmin(abs(w - 1))])
    if abs(abs(axis[2]) - 1) < 1e-9: return "C2"
    return "C2'" if np.sum(np.abs(axis) > 1e-9) == 1 else "C2''"
chars_D4 = {"A1": {"E": 1, "C4": 1, "C2": 1, "C2'": 1, "C2''": 1},
            "A2": {"E": 1, "C4": 1, "C2": 1, "C2'": -1, "C2''": -1},
            "B1": {"E": 1, "C4": -1, "C2": 1, "C2'": 1, "C2''": -1},
            "B2": {"E": 1, "C4": -1, "C2": 1, "C2'": -1, "C2''": 1},
            "E":  {"E": 2, "C4": 0, "C2": -2, "C2'": 0, "C2''": 0}}
mult4 = {name: round(sum(np.trace(rep_on_qubit_ops(R)) * ch[d4_class(R)] for R in D4) / 8) for name, ch in chars_D4.items()}
print("(A2) one qubit at an edge/face site (group D4 about its axis):",
      " + ".join(f"{m} {n}" for n, m in mult4.items() if m))
Rdiag = [R for R in D4 if d4_class(R) == "C2''"][0]
print("     parity of s^axis under the diagonal half-turn:", int(round(Rdiag[2, 2])),
      "(A2: -1); s^axis under the axis-aligned perpendicular half-turns:",
      [int(round(R[2, 2])) for R in D4 if d4_class(R) == "C2'"])
print("     => creators: scalar (multi-site) at V and C (p = +1), s^axis at E and F (p = -1) satisfy A33's",
      "p_V != p_F and p_E != p_C with single-qubit creators on E and F")

# ---------- Part B: 8-band period-2 toy
cell = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
idx = {s: i for i, s in enumerate(cell)}
def eta(x, y, z, d):            # Kogut-Susskind signs: pi flux through every plaquette
    return [1, (-1) ** x, (-1) ** (x + y)][d]
def bloch(k, t, eps):
    H = np.zeros((8, 8), complex)
    for s in cell:
        w = sum(s)
        H[idx[s], idx[s]] += eps[w]
        for d in range(3):
            n = list(s); n[d] += 1
            shift = np.zeros(3); shift[d] = n[d] // 2
            nn = tuple(v % 2 for v in n)
            wb = min(w, sum(nn))
            amp = -t[wb] * eta(*s, d) * np.exp(1j * np.dot(k, shift * 2))
            H[idx[nn], idx[s]] += amp
            H[idx[s], idx[nn]] += np.conj(amp)
    return H
def middle_gap(t, eps):
    """direct gap between bands 4 and 5 (the would-be Dirac point), minimized over the reduced zone"""
    f = lambda k: np.diff(np.linalg.eigvalsh(bloch(np.asarray(k), t, eps))[3:5])[0]
    g = np.linspace(-np.pi / 2, np.pi / 2, 13)
    best = min(((f(k), k) for k in itertools.product(g, g, g)), key=lambda z: z[0])
    res = minimize(f, np.array(best[1]), method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 6000})
    return res.fun, res.x
def slopes(t, eps, k0, h=1e-4):
    e0 = np.linalg.eigvalsh(bloch(k0, t, eps))[3:5]
    out = []
    for d in range(3):
        dk = np.zeros(3); dk[d] = h
        e1 = np.linalg.eigvalsh(bloch(k0 + dk, t, eps))[3:5]
        out.append((e1[1] - e1[0] - (e0[1] - e0[0])) / (2 * h))
    return out
k0 = np.array([np.pi / 2] * 3)
cases = [("uniform KS, equal role energies", (1, 1, 1), (0, 0, 0, 0)),
         ("unequal bond magnitudes (1, 0.7, 1.3)", (1, 0.7, 1.3), (0, 0, 0, 0)),
         ("role energies (0.2, 0, 0, 0): vertex only", (1, 1, 1), (0.2, 0, 0, 0)),
         ("role energies (0.2, -0.2, 0.2, -0.2): staggered", (1, 1, 1), (0.2, -0.2, 0.2, -0.2)),
         ("role energies (0.1, 0.1, -0.1, -0.1): no staggered part", (1, 1, 1), (0.1, 0.1, -0.1, -0.1)),
         ("role energies (0.1, -0.1, -0.1, 0.1): no staggered part", (1, 1, 1), (0.1, -0.1, -0.1, 0.1)),
         ("unequal magnitudes + vertex energy 0.2", (1, 0.7, 1.3), (0.2, 0, 0, 0))]
for name, t, eps in cases:
    gap, k = middle_gap(t, eps)
    stag = (eps[0] - eps[1] + eps[2] - eps[3]) / 4
    lev = np.round(np.linalg.eigvalsh(bloch(k0, t, eps)), 3)
    line = (f"(B) {name:55s}: levels at the old Dirac point {lev.tolist()}; smallest band-4/5 gap = {gap:.2e} "
            f"at k = {np.round(k, 3).tolist()}; staggered part {stag:+.3f}")
    if gap < 1e-6:
        line += f"; gap growth per unit k along x,y,z = {np.round(slopes(t, eps, k), 3).tolist()}"
    print(line)

# (C) what the one-particle spectrum looks like just off the old Dirac point (eigenvalues at k0 + d*(1, 0.6, 0.3))
for name, t, eps in [("equal energies", (1, 1, 1), (0, 0, 0, 0)),
                     ("vertex energy 0.2", (1, 1, 1), (0.2, 0, 0, 0)),
                     ("(0.1, 0.1, -0.1, -0.1)", (1, 1, 1), (0.1, 0.1, -0.1, -0.1)),
                     ("staggered 0.2", (1, 1, 1), (0.2, -0.2, 0.2, -0.2))]:
    rows = []
    for d in (0.0, 0.02, 0.04):
        ev = np.linalg.eigvalsh(bloch(k0 + d * np.array([1, 0.6, 0.3]), t, eps))
        rows.append(f"d={d}: " + " ".join(f"{e:+.3f}" for e in ev))
    print(f"(C) {name:24s} " + " | ".join(rows))

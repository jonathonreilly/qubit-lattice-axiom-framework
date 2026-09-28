#!/usr/bin/env python3
"""A lapse set by record events, against Einstein's negative scalar sector: linear-order comparator lemmas.

Question (the owner, 2026-09-28): "time is the shifting or creation of
records". Probe 11 found that Einstein's graviton avoids helicity-1 partners
only through a negative scalar (transverse-trace) sector. Can a lapse (local
tick rate) set by record events remove that sector while keeping positive,
record-like kinetics?

In ADM variables the landed kinetic family alpha tr(hdot^2) + beta (tr hdot)^2
is K_ij K_ij - lambda K^2 with lambda = -beta/alpha; it is positive iff
alpha > 0 and lambda < 1/3, and the landed lattice lapse algebra closes only on
beta = -alpha, i.e. lambda = 1 (block 112, 2026-09-24), where no positive
kinetic term lies (the 2026-09-25 clock-profile note, T3).

Checks (all at linear order, Gaussian comparators):
  A  restriction lemma: with the Einstein-Hilbert scalar entry unchanged, a
     positive lapse sector of any size, coupled in any way to the scalar and
     its momentum, leaves the quadratic form indefinite (its smallest
     eigenvalue is at most the E-H scalar value); eliminating a fast positive
     lapse lowers that entry (Schur complement).
  B  the ADM scalar sector (symbolic): with h_ij = 2 zeta delta_ij, shift
     d_i B and lapse 1 + n, solving the shift gives the zeta kinetic
     coefficient 2(3 lambda - 1)/(lambda - 1); at lambda = 1 the shift equation
     is -4 k^2 zetadot = 0 (the scalar is frozen). With an auxiliary lapse
     (Lagrangian xi n R^(1) + alpha (dn)^2, no conjugate) the scalar has
     omega^2 = (lambda - 1)(2 - alpha) k^2 / ((3 lambda - 1) alpha)
     (Blas-Pujolas-Sibiryakov), healthy iff (lambda > 1 or lambda < 1/3) and
     0 < alpha < 2. Positive record kinetics (lambda < 1/3, e.g. lambda = 0)
     therefore carry a healthy extra scalar graviton. The eliminated lapse
     kernel is non-analytic and the resulting potential violates probe 11's
     identity.
  C  the gauge lapse and the landed line: lambda = -beta/alpha maps the landed
     closing line beta = -alpha to lambda = 1; that line takes (-6, 2, 2) alpha
     on the dilation, E and T strains (re-verified); positivity of the family
     needs lambda < 1/3. With the Hamiltonian constraint, in transverse gauge,
     the E-H comparator keeps exactly the two TT tensors, both positive.
  D  the momentum-rule qubit moves are non-abelian: of the 30 translates of
     probe 10's 20-slot move within radius 2 that share slots with it, 26 fail
     to commute on constructed configurations and the 4 axis-neighbour pairs
     commute (a fact about the move algebra; whether moves could be
     first-class constraints is not tested).
Reference only: Horava (2009); Blas, Pujolas and Sibiryakov (arXiv:0909.3525);
Henneaux, Kleinschmidt and Lucena Gomez (2010) on the Hamiltonian constraint
for lambda != 1; Jacobson's Einstein-aether.
Not pre-registered. Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)


def eh(T, k):                 # linearised Einstein-Hilbert spatial form on symmetric tensors
    kT = k @ T
    return (0.5 * (k @ k) * np.vdot(T, T) - np.vdot(kT, kT) + np.conj(k @ T @ k) * np.trace(T) - 0.5 * (k @ k) * abs(np.trace(T)) ** 2).real


def rlin(T, k):
    return k @ T @ k - (k @ k) * np.trace(T)


def tensors(khat):
    e1 = np.cross(khat, [1, 0, 0] if abs(khat[0]) < 0.9 else [0, 1, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(khat, e1)
    o = lambda a, b: (np.outer(a, b) + np.outer(b, a)) / 2
    T = {"TT+": o(e1, e1) - o(e2, e2), "TTx": 2 * o(e1, e2), "trans_trace": o(e1, e1) + o(e2, e2), "m0": 2 * o(khat, khat) - o(e1, e1) - o(e2, e2),
         "h1a": 2 * o(khat, e1), "h1b": 2 * o(khat, e2), "long": o(khat, khat)}
    return {nm: M / np.linalg.norm(M) for nm, M in T.items()}


kh = np.array([0.3, -0.5, 0.81]); kh /= np.linalg.norm(kh); kk = 0.2; k = kk * kh; Ts = tensors(kh)

# ---------------------------------------------------------------- A: restriction lemma
Vs = eh(Ts["trans_trace"], k)
worst = -np.inf; schur_ok = True
for _ in range(3000):
    m = int(rng.integers(1, 5))                                   # lapse sector size
    Wm = rng.normal(size=(m, m)); W = Wm @ Wm.T + 1e-6 * np.eye(m)   # positive lapse form
    g = rng.normal(size=(2, m)) * 3                               # couplings to (scalar amplitude, its momentum)
    Q = np.zeros((2 + m, 2 + m)); Q[0, 0] = Vs; Q[1, 1] = 1.0     # scalar potential entry (E-H) and a unit positive momentum entry
    Q[:2, 2:] = g; Q[2:, :2] = g.T; Q[2:, 2:] = W
    worst = max(worst, np.linalg.eigvalsh(Q).min())
    S = Q[:2, :2] - g @ np.linalg.solve(W, g.T)                   # eliminating the lapse sector
    schur_ok &= S[0, 0] <= Vs + 1e-12
check("A: restriction lemma: with the E-H scalar entry unchanged, a positive lapse sector of any size and any coupling to the scalar and its momentum leaves the form indefinite (smallest eigenvalue <= the E-H scalar value), and eliminating it lowers that entry",
      Vs < 0 and worst <= Vs + 1e-12 and schur_ok,
      f"E-H transverse trace {Vs / kk ** 2:.3f} k^2; over 3000 random positive lapse sectors (1-4 components) the largest smallest eigenvalue is {worst / kk ** 2:.3f} k^2 (bounded by the E-H value); every Schur complement lowers the scalar entry")

# ---------------------------------------------------------------- B: the ADM scalar sector (symbolic)
lam, al, xi, kS = sp.symbols('lambda alpha xi k', real=True)
zd, Bv, z, n = sp.symbols('zdot B zeta n')
Lkin = (3 - 9 * lam) * zd ** 2 + (2 - 6 * lam) * kS ** 2 * zd * Bv + (1 - lam) * kS ** 4 * Bv ** 2      # K_ij K_ij - lambda K^2, h = 2 zeta delta, N_i = d_i B
Bsol = sp.solve(sp.diff(Lkin, Bv), Bv)[0]
kin = sp.simplify(Lkin.subs(Bv, Bsol) / zd ** 2)
frozen = sp.simplify(sp.diff(Lkin, Bv).subs(lam, 1))
Lpot = 2 * xi * kS ** 2 * z ** 2 + 4 * xi * kS ** 2 * n * z + al * kS ** 2 * n ** 2                   # [sqrt(g) R]^(2) + n R^(1) + alpha (dn)^2
nsol = sp.solve(sp.diff(Lpot, n), n)[0]
pot = sp.simplify(Lpot.subs(n, nsol) / z ** 2)
om2 = sp.simplify(-pot / kin).subs(xi, 1)
bps = (lam - 1) * (2 - al) * kS ** 2 / ((3 * lam - 1) * al)
okB = (sp.simplify(kin - 2 * (3 * lam - 1) / (lam - 1)) == 0 and sp.simplify(frozen + 4 * kS ** 2 * zd) == 0 and sp.simplify(om2 - bps) == 0)
healthy = lambda L, A: float((2 * (3 * L - 1) / (L - 1))) > 0 and float(bps.subs({lam: L, al: A, kS: 1})) > 0
samples = {(0.0, 1.0): healthy(0.0, 1.0), (0.2, 0.5): healthy(0.2, 0.5), (0.0, 2.5): healthy(0.0, 2.5), (0.5, 1.0): healthy(0.5, 1.0), (2.0, 1.0): healthy(2.0, 1.0)}
okB &= samples == {(0.0, 1.0): True, (0.2, 0.5): True, (0.0, 2.5): False, (0.5, 1.0): False, (2.0, 1.0): True}
sp0 = float(bps.subs({lam: 0, al: 1, kS: 1}))
# the eliminated lapse kernel (tensor level): E-H + c^2 R^2 / (4 alpha k^2) is non-analytic and violates probe 11's identity
Tfix = np.diag([1.0, 0, 0]); dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
y = np.array([rlin(Tfix, d) ** 2 / (d @ d) for d in dirs]); Xq = np.array([[d[0] ** 2, d[1] ** 2, d[2] ** 2, d[0] * d[1], d[1] * d[2], d[0] * d[2]] for d in dirs])
res = np.linalg.lstsq(Xq, y, rcond=None)[1]
eff = lambda T, a: eh(T, k) + rlin(T, k) ** 2 / (4 * a * (k @ k))
v = {nm: eff(Ts[t], 0.5) / kk ** 2 for nm, t in (("v2", "TT+"), ("v1", "h1a"), ("v0", "m0"))}
viol = 4 * v["v1"] - v["v2"] - 3 * v["v0"]
check("B: the ADM scalar sector: solving the shift gives kinetic 2(3 lambda-1)/(lambda-1), frozen at lambda = 1 (-4 k^2 zetadot = 0); with an auxiliary lapse omega^2 = (lambda-1)(2-alpha)k^2/((3 lambda-1) alpha), healthy iff (lambda > 1 or lambda < 1/3) and 0 < alpha < 2, so positive record kinetics (lambda < 1/3) carry a healthy extra scalar graviton; the eliminated kernel is non-analytic and violates probe 11's identity",
      okB and res.size > 0 and res[0] > 1e-3 and abs(viol) > 0.1,
      f"symbolic: kinetic {kin}, lambda=1 shift equation {frozen} = 0, omega^2 = {sp.factor(om2)}; healthy at (lambda, alpha) = (0,1), (0.2,0.5), (2,1); not at (0,2.5), (0.5,1); lambda = 0, alpha = 1: scalar speed^2 {sp0:.3f} (TT 1); "
      f"kernel fit residual {res[0]:.3f} (not quadratic in k); effective (v2, v1, v0) = ({v['v2']:.3f}, {v['v1']:.1e}, {v['v0']:.3f}), 4v1 - v2 - 3v0 = {viol:.3f}")

# ---------------------------------------------------------------- C: the gauge lapse and the landed closing line
a1 = 1.0
fam = lambda be, vv: a1 * np.trace(vv @ vv) + be * np.trace(vv) ** 2
dil = np.eye(3); Es = np.diag([1., -1., 0.]); Tt = np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]])
line = [float(fam(-a1, vv)) for vv in (dil, Es, Tt)]
pos_window = [bool((3 * a1 + 9 * be) > 0 and a1 > 0) for be in (-0.5, -0.3, -0.2, 0.0)]         # dilation value 3 alpha (1 - 3 lambda)
lam_map = [-be / a1 for be in (-1.0, -0.3, 0.0)]
names = ["TT+", "TTx", "trans_trace", "m0", "h1a", "h1b", "long"]
phys = [nm for nm in names if abs(rlin(Ts[nm], k)) < 1e-12 and np.linalg.norm(Ts[nm] @ kh) < 1e-12]    # Hamiltonian constraint + transverse gauge
eh_phys = [float(eh(Ts[nm], k) / kk ** 2) for nm in phys]
check("C: the gauge lapse and the landed line: beta = -alpha is lambda = 1, where the family takes (-6, 2, 2) alpha on the dilation, E and T strains (indefinite); positivity needs lambda < 1/3; with the Hamiltonian constraint in transverse gauge the E-H comparator keeps exactly the two TT tensors, both positive",
      np.allclose(line, [-6, 2, 2]) and pos_window == [False, True, True, True] and np.allclose(lam_map, [1.0, 0.3, 0.0]) and sorted(phys) == ["TT+", "TTx"] and all(x > 0 for x in eh_phys),
      f"closing line (dilation, E, T): {line} alpha; lambda = -beta/alpha at beta = -1, -0.3, 0: {lam_map}; dilation positive at beta = -0.5, -0.3, -0.2, 0: {pos_window}; surviving tensors {phys} with E-H {eh_phys} k^2")

# ---------------------------------------------------------------- D: the momentum-rule qubit moves are non-abelian
MOVE3D = [(('f', (-1, -2, 0), (0, 1)), 1), (('f', (-1, -2, 1), (0, 1)), -1), (('d', (-1, -1, 0), 1), -1), (('f', (-1, -1, 0), (1, 2)), -1),
          (('f', (-1, -1, 0), (0, 2)), 1), (('d', (-1, -1, 1), 1), 1), (('f', (-1, 0, 0), (0, 2)), -1), (('d', (0, -2, 0), 0), -1),
          (('f', (0, -2, 0), (1, 2)), 1), (('f', (0, -2, 0), (0, 2)), -1), (('d', (0, -2, 1), 0), 1), (('f', (0, -1, 0), (0, 1)), -1),
          (('f', (0, -1, 0), (1, 2)), 1), (('f', (0, -1, 0), (0, 2)), 1), (('f', (0, -1, 1), (0, 1)), 1), (('d', (0, 0, 0), 0), 1),
          (('d', (0, 0, 1), 0), -1), (('f', (1, -2, 0), (1, 2)), -1), (('d', (1, -1, 0), 1), 1), (('d', (1, -1, 1), 1), -1)]


def shifted(move, s):
    return {(t, tuple(np.array(x) + s), a): c for (t, x, a), c in move}


def apply_h(m, state):         # h = T_m + T_m^dag; config = frozenset of slots at -1/2 (others +1/2)
    out = {}
    for conf, amp in state.items():
        for sgn in (1, -1):
            if all(((s in conf) if sgn * c == 1 else (s not in conf)) for s, c in m.items()):
                new = set(conf)
                for s, c in m.items():
                    (new.discard if sgn * c == 1 else new.add)(s)
                key = frozenset(new); out[key] = out.get(key, 0) + amp
    return out


m0 = {(t, x, a): c for (t, x, a), c in MOVE3D}
tested = noncomm = 0; axis_commute = []
for s in itertools.product(range(-2, 3), repeat=3):
    if s == (0, 0, 0):
        continue
    m1 = shifted(MOVE3D, np.array(s))
    if not (set(m0) & set(m1)):
        continue
    tested += 1; found = False
    for s0, s1 in itertools.product((1, -1), repeat=2):
        conf = {sl for sl, cc in m0.items() if s0 * cc == 1}
        after = (conf - {sl for sl, cc in m0.items() if s0 * cc == 1}) | {sl for sl, cc in m0.items() if s0 * cc == -1}
        if any(((sl in after) != (s1 * cc == 1)) for sl, cc in m1.items() if sl in m0):
            continue
        conf = frozenset(conf | {sl for sl, cc in m1.items() if sl not in m0 and s1 * cc == 1})
        a = apply_h(m1, apply_h(m0, {conf: 1.0})); b = apply_h(m0, apply_h(m1, {conf: 1.0}))
        if any(abs(a.get(q, 0) - b.get(q, 0)) > 1e-12 for q in set(a) | set(b)):
            found = True; break
    noncomm += found
    if not found:
        axis_commute.append(s)
check("D: the momentum-rule qubit moves are non-abelian: of the translates of probe 10's 20-slot move within radius 2 that share slots with it, 26 of 30 fail to commute on constructed configurations; the 4 others are the axis neighbours +-e_x, +-e_y",
      tested == 30 and noncomm == 26 and sorted(axis_commute) == sorted([(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)]),
      f"{noncomm} of {tested} overlapping translates fail to commute; commuting ones: {axis_commute}")

print("N5 resolution 1: with the E-H scalar entry unchanged, no positive lapse sector or coupling makes the form positive (restriction); a lapse helps only by changing the scalar block itself or by leaving the positive class.")
print("N5 resolution 2: in the ADM scalar sector an auxiliary lapse gives omega^2 = (lambda-1)(2-alpha)k^2/((3 lambda-1)alpha); positive kinetics (lambda < 1/3) carry a healthy extra scalar graviton; at lambda = 1 the scalar is frozen by the shift.")
print("N5 resolution 3: the landed lattice closing line is lambda = 1, indefinite; positivity needs lambda < 1/3; so the lapse that closes on the lattice and the positive record kinetics lie on different sides.")
print("N5 resolution 4: the momentum-rule moves are non-abelian (26 of 30 overlapping translates); first-class closure for them is not tested.")
print("per_element: each comparator is evaluated on explicit tensor directions; each move pair on explicit slot configurations.")
print("per_site: the qubit moves are probe 10's witness and its translates on the landed slot placement.")
print("per_mode: TT, transverse trace, spin-2 m=0, helicity 1 and longitudinal tensors; the ADM conformal scalar.")
print("per_block: 3000 random lapse sectors; symbolic ADM scalar sector; all 30 overlapping translates within radius 2.")
print("lattice_wide: checked and not executed - linear order and Gaussian comparators only; no native record dynamics, constraint algebra for the moves, or nonlinear closure.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

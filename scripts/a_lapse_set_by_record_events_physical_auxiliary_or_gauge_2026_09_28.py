#!/usr/bin/env python3
"""A lapse set by the rate of record events: physical, auxiliary or gauge.

Question (the owner, 2026-09-28): "time is the shifting or creation of
records". Test the lapse that reading suggests: can a local tick rate set by
record events remove Einstein's indefinite scalar sector (probe 11) and give a
light-cone graviton without helicity-1 partners?

Three readings of "a lapse set by record events", and what each does:
  (physical) the event rate is a property of the records: a local operator,
      or a positive-energy field. The dynamics is then an ordinary local
      Hamiltonian with a ground state, so probe 11 applies; and a positive
      lapse field coupled to the Hamiltonian-constraint density cannot make
      the Einstein-Hilbert scalar block positive (Schur).
  (auxiliary) the rate is fixed instantaneously by its own elliptic equation,
      with a negative gradient term (Horava / Blas-Pujolas-Sibiryakov type).
      It does make the scalar positive, but adds a propagating helicity-0
      graviton, through a non-analytic kernel (how it evades probe 11); the
      limit of zero stiffness is GR's constraint.
  (gauge) the rate has no physical meaning: GR's Hamiltonian constraint. Its
      lattice status is landed (block 112, 2026-09-24; the clock-profile note,
      2026-09-25; the compact bound, 2026-09-14).
And for records as local events: exactly commuting events carry nothing
anywhere (zero propagation), while the momentum-rule qubit moves of probe 10
do not commute when they overlap, so their event order - and hence the local
rates - matter.

Reference only (not premises): Horava (2009), Blas, Pujolas and Sibiryakov
(2010), Jacobson's Einstein-aether, Lieb-Robinson (1972), Page-Wootters and
relational time.

Not pre-registered: the readings were separated first and these checks
frozen before the note.

Checks:
  A  physical lapse: for the E-H scalar block (negative transverse trace),
     adding any positive lapse sector coupled through the constraint density
     leaves the quadratic form indefinite (every coupling, every stiffness);
     eliminating a fast positive lapse lowers the scalar potential further.
  B  auxiliary lapse: with a wrong-sign gradient term -alpha k^2 n^2, the
     eliminated lapse adds +c^2 R_lin^2/(4 alpha k^2): the transverse trace
     becomes positive for alpha < c^2, the TT sector is unchanged, and a
     helicity-0 mode propagates with speed^2 = c^2/alpha - 1 (TT speed 1),
     diverging as alpha -> 0 (the constraint limit). The kernel is not a
     quadratic polynomial in k, and the effective form violates probe 11's
     identity (4 v1 != v2 + 3 v0).
  C  gauge lapse: the landed closing line alpha tr(v^2) + beta (tr v)^2,
     beta = -alpha, takes (-6, 2, 2) alpha on the dilation, E and T strains
     (indefinite; re-verified); E-H with the scalar constraint leaves exactly
     the two TT modes, both positive.
  D  records as events: (i) with exactly commuting local generators, a local
     operator's support never grows (zero propagation), unlike a
     non-commuting chain; (ii) overlapping momentum-rule qubit moves (probe
     10's 20-slot witness and its translates) fail to commute on explicit
     configurations.
Prints one line per check, the N5 lines and TOTAL: PASS=N FAIL=M.
"""
import itertools
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)


def eh(T, k):                 # linearised Einstein-Hilbert spatial form on symmetric tensors (unit Frobenius tensors)
    kT = k @ T
    return (0.5 * (k @ k) * np.vdot(T, T) - np.vdot(kT, kT) + np.conj(k @ T @ k) * np.trace(T) - 0.5 * (k @ k) * abs(np.trace(T)) ** 2).real


def rlin(T, k):               # linearised scalar curvature (Hamiltonian-constraint density), Fourier: k.T.k - k^2 tr T
    return k @ T @ k - (k @ k) * np.trace(T)


def tensors(khat):
    """Unit-Frobenius symmetric tensors about khat: TT (two), transverse trace, spin-2 m=0, helicity 1 (two), longitudinal."""
    e1 = np.cross(khat, [1, 0, 0] if abs(khat[0]) < 0.9 else [0, 1, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(khat, e1)
    o = lambda a, b: (np.outer(a, b) + np.outer(b, a)) / 2
    T = {"TT+": o(e1, e1) - o(e2, e2), "TTx": 2 * o(e1, e2), "trans_trace": o(e1, e1) + o(e2, e2), "m0": 2 * o(khat, khat) - o(e1, e1) - o(e2, e2),
         "h1a": 2 * o(khat, e1), "h1b": 2 * o(khat, e2), "long": o(khat, khat)}
    return {n: M / np.linalg.norm(M) for n, M in T.items()}


# ---------------------------------------------------------------- A: a physical lapse cannot fix the scalar sector
kh = np.array([0.3, -0.5, 0.81]); kh /= np.linalg.norm(kh); kk = 0.2; k = kk * kh; Ts = tensors(kh)
Vs = eh(Ts["trans_trace"], k); r = rlin(Ts["trans_trace"], k)
worst_min_eig = -np.inf; lowered = True
for _ in range(2000):
    c = rng.normal() * 5; W = abs(rng.normal()) * 10 * kk ** 2 + 1e-6        # coupling and a positive lapse stiffness (any positive form)
    M2 = np.array([[Vs, c * r / 2], [c * r / 2, W]])                         # quadratic form on (scalar amplitude, lapse)
    worst_min_eig = max(worst_min_eig, np.linalg.eigvalsh(M2).min())
    lowered &= (Vs - (c * r / 2) ** 2 / W) <= Vs + 1e-15                     # eliminating a fast positive lapse: Schur complement
check("A: a physical lapse cannot fix Einstein's scalar block: with the E-H transverse trace negative, adding any positive lapse sector coupled through the constraint density leaves the quadratic form indefinite, and eliminating a fast positive lapse lowers the scalar potential further",
      Vs < 0 and worst_min_eig < 0 and lowered,
      f"E-H on the transverse trace: {Vs / kk ** 2:.4f} k^2 (negative); over 2000 random couplings and positive stiffnesses the largest smallest eigenvalue is {worst_min_eig:.2e} (< 0); Schur complement always <= the bare value")

# ---------------------------------------------------------------- B: an auxiliary (wrong-sign, instantaneous) lapse
def eff(T, k, c, alpha):      # H_eff = E-H + c^2 R^2/(4 alpha k^2), from n R c - alpha k^2 n^2 at its stationary point
    return eh(T, k) + c ** 2 * rlin(T, k) ** 2 / (4 * alpha * (k @ k))


c = 1.0; rowsB = []; okB = True
for alpha in [0.25, 0.5, 0.9, 1.2]:
    vals = {n: eff(Ts[n], k, c, alpha) / kk ** 2 for n in ("TT+", "TTx", "trans_trace", "h1a", "long")}
    w_s2 = 2 * vals["trans_trace"]; w_tt2 = 2 * vals["TT+"]                   # unit kinetic: omega^2 = 2 V / (amplitude^2) per k^2
    okB &= abs(vals["TT+"] - 0.5) < 1e-12 and abs(vals["TTx"] - 0.5) < 1e-12 and abs(vals["h1a"]) < 1e-12 and abs(vals["long"]) < 1e-12
    okB &= abs(w_s2 - (c ** 2 / alpha - 1)) < 1e-12
    rowsB.append(f"alpha={alpha}: TT speed^2 {w_tt2:.3f}, scalar speed^2 {w_s2:+.3f}")
okB &= (c ** 2 / 0.25 - 1) > 0 and (c ** 2 / 1.2 - 1) < 0
# non-analyticity of the eliminated kernel: not a quadratic polynomial in k for a fixed tensor
Tfix = np.diag([1.0, 0, 0]); dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
y = np.array([rlin(Tfix, d) ** 2 / (d @ d) for d in dirs]); X = np.array([[d[0] ** 2, d[1] ** 2, d[2] ** 2, d[0] * d[1], d[1] * d[2], d[0] * d[2]] for d in dirs])
res = np.linalg.lstsq(X, y, rcond=None)[1]; nonanalytic = res.size > 0 and res[0] > 1e-3
# probe 11's identity on the spin-2 compression of the effective form
Th = {"v2": Ts["TT+"], "v1": Ts["h1a"], "v0": Ts["m0"]}
alpha = 0.5; v = {n: eff(T, k, c, alpha) / kk ** 2 for n, T in Th.items()}
viol = 4 * v["v1"] - v["v2"] - 3 * v["v0"]
check("B: an auxiliary lapse fixed instantaneously with a wrong-sign gradient term makes the transverse trace positive for alpha < c^2 and leaves TT unchanged, but adds a propagating helicity-0 mode (speed^2 = c^2/alpha - 1, diverging as alpha -> 0, the constraint limit); its kernel is non-analytic and violates probe 11's identity",
      okB and nonanalytic and abs(viol) > 0.1,
      "; ".join(rowsB) + f"; fit of the kernel on a fixed tensor to a quadratic form in k: residual {res[0] if res.size else 0:.3e} (not quadratic); at alpha = 0.5 (v2, v1, v0) = ({v['v2']:.3f}, {v['v1']:.1e}, {v['v0']:.3f}), 4v1 - v2 - 3v0 = {viol:.3f}")

# ---------------------------------------------------------------- C: the gauge lapse (GR) and the landed closing line
al = 1.0; be = -al
dil = np.eye(3); Es = np.diag([1., -1., 0.]); Tt = np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]])
line = [al * np.trace(v2 @ v2) + be * np.trace(v2) ** 2 for v2 in (dil, Es, Tt)]
# E-H with the scalar (Hamiltonian) constraint: physical space = ker(momentum constraint on E) and R_lin(h) = 0 with its conjugate removed
names = ["TT+", "TTx", "trans_trace", "m0", "h1a", "h1b", "long"]
phys = [n for n in names if abs(rlin(Ts[n], k)) < 1e-12 and abs(np.vdot(Ts[n] @ kh, Ts[n] @ kh)) < 1e-12]
eh_phys = [eh(Ts[n], k) / kk ** 2 for n in phys]
check("C: the gauge lapse is GR's constraint: the landed closing line takes (-6, 2, 2) alpha on the dilation, E and T strains (indefinite, admits no positive kinetic term); with the scalar constraint the E-H comparator keeps exactly the two TT modes, both positive",
      np.allclose(line, [-6, 2, 2]) and sorted(phys) == ["TT+", "TTx"] and all(x > 0 for x in eh_phys),
      f"closing line on (dilation, E, T): {[round(float(x), 3) for x in line]} alpha; tensors surviving both constraints: {phys} with E-H values {[round(float(x), 3) for x in eh_phys]} k^2")

# ---------------------------------------------------------------- D: records as local events
# (i) exactly commuting local generators: a local operator's support never grows
nq = 10
X = np.array([[0, 1], [1, 0]], complex); Z = np.diag([1., -1.]).astype(complex); Y = np.array([[0, -1j], [1j, 0]]); I2 = np.eye(2)


def op(ops):
    out = np.array([[1.0 + 0j]])
    for i in range(nq):
        out = np.kron(out, ops.get(i, I2))
    return out


terms_c = [rng.normal() * op({i - 1: Z, i: X, i + 1: Z}) for i in range(1, nq - 1)]          # cluster-type terms: pairwise commuting
Hc = sum(terms_c)
Hn = sum(op({i: X, i + 1: X}) + op({i: Y, i + 1: Y}) for i in range(nq - 1))                 # XY chain: neighbours do not commute
comm_ok = max(np.abs(a @ b - b @ a).max() for a in terms_c for b in terms_c) < 1e-9
A0 = op({1: X}); Bfar = op({8: Z})
def growth(H, t):
    U = expm(-1j * H * t); At = U.conj().T @ A0 @ U; return np.abs(At @ Bfar - Bfar @ At).max()
g_c = max(growth(Hc, t) for t in (1.0, 5.0, 20.0)); g_n = growth(Hn, 5.0)
# (ii) overlapping momentum-rule qubit moves do not commute
MOVE3D = [(('f', (-1, -2, 0), (0, 1)), 1), (('f', (-1, -2, 1), (0, 1)), -1), (('d', (-1, -1, 0), 1), -1), (('f', (-1, -1, 0), (1, 2)), -1),
          (('f', (-1, -1, 0), (0, 2)), 1), (('d', (-1, -1, 1), 1), 1), (('f', (-1, 0, 0), (0, 2)), -1), (('d', (0, -2, 0), 0), -1),
          (('f', (0, -2, 0), (1, 2)), 1), (('f', (0, -2, 0), (0, 2)), -1), (('d', (0, -2, 1), 0), 1), (('f', (0, -1, 0), (0, 1)), -1),
          (('f', (0, -1, 0), (1, 2)), 1), (('f', (0, -1, 0), (0, 2)), 1), (('f', (0, -1, 1), (0, 1)), 1), (('d', (0, 0, 0), 0), 1),
          (('d', (0, 0, 1), 0), -1), (('f', (1, -2, 0), (1, 2)), -1), (('d', (1, -1, 0), 1), 1), (('d', (1, -1, 1), 1), -1)]


def shifted(move, s):
    return {(t, tuple(np.array(x) + s), a): c for (t, x, a), c in move}


def apply_h(m, state):         # h = T_m + T_m^dag on a dict {config (frozenset of slots at -1/2): amplitude}; slots valued +-1/2
    out = {}
    for conf, amp in state.items():
        for sgn in (1, -1):    # T_m raises by m (sgn=1) or by -m (sgn=-1)
            ok = all(((s in conf) if sgn * c == 1 else (s not in conf)) for s, c in m.items())
            if ok:
                new = set(conf)
                for s, c in m.items():
                    if sgn * c == 1:
                        new.discard(s)
                    else:
                        new.add(s)
                key = frozenset(new); out[key] = out.get(key, 0) + amp
    return out


m0 = dict(((t, x, a), c) for (t, x, a), c in MOVE3D)
pairs_tested = noncommuting = 0; witness = None
for s in itertools.product(range(-2, 3), repeat=3):
    if s == (0, 0, 0):
        continue
    m1 = shifted(MOVE3D, np.array(s)); shared = set(m0) & set(m1)
    if not shared:
        continue
    pairs_tested += 1; found = False
    for s0, s1 in itertools.product((1, -1), repeat=2):
        # a configuration on which s0*m0 acts, and after which s1*m1 acts (shared slots permitting)
        conf = {sl for sl, cc in m0.items() if s0 * cc == 1}
        after = (conf - {sl for sl, cc in m0.items() if s0 * cc == 1}) | {sl for sl, cc in m0.items() if s0 * cc == -1}
        if any(((sl in after) != (s1 * cc == 1)) for sl, cc in m1.items() if sl in m0):
            continue
        conf |= {sl for sl, cc in m1.items() if sl not in m0 and s1 * cc == 1}
        conf = frozenset(conf)
        a = apply_h(m1, apply_h(m0, {conf: 1.0})); b = apply_h(m0, apply_h(m1, {conf: 1.0}))
        if any(abs(a.get(q, 0) - b.get(q, 0)) > 1e-12 for q in set(a) | set(b)):
            found = True; witness = witness or (s, len(shared)); break
    noncommuting += found
check("D: records as local events: exactly commuting local generators never spread a local operator (zero propagation), unlike a non-commuting chain; overlapping momentum-rule qubit moves (probe 10's 20-slot witness and its translates) fail to commute on explicit configurations, so the order of record events, and hence the local rates, matter",
      comm_ok and g_c < 1e-10 and g_n > 1e-3 and noncommuting > 0,
      f"commuting cluster chain: largest |[A(t), B_far]| over t = 1, 5, 20 is {g_c:.1e}; XY chain at t = 5: {g_n:.3f}; overlapping translates of the 3D move: {noncommuting} of {pairs_tested} fail to commute on sampled configurations (first witness: shift {witness[0]}, {witness[1]} shared slots)")

print("N5 resolution 1: a physical record-event rate (a local operator, or a positive-energy field) leaves an ordinary local Hamiltonian with a ground state; probe 11 applies and the Schur complement lowers, never raises, the scalar block.")
print("N5 resolution 2: an instantaneous auxiliary lapse with a wrong-sign gradient term removes the negative scalar only by adding a propagating helicity-0 graviton, through a non-analytic kernel; alpha -> 0 is GR's constraint.")
print("N5 resolution 3: the gauge reading is GR's Hamiltonian constraint; on the lattice its closing line is indefinite (landed block 112 and the 2026-09-25 clock-profile note).")
print("N5 resolution 4: exactly commuting record events carry nothing anywhere; overlapping momentum-rule moves do not commute, so event rates are physical unless the moves are first-class constraints.")
print("per_element: each lapse reading is tested on explicit tensor directions; each qubit move pair on explicit slot configurations.")
print("per_site: the qubit moves are the landed slot placement's 20-slot witness and its translates on the doubled lattice.")
print("per_mode: TT, transverse trace, spin-2 m=0, helicity 1 and longitudinal tensors about a generic direction.")
print("per_block: 2000 random physical lapse sectors; four auxiliary stiffnesses; a 10-qubit dense propagation check; all translates within radius 2.")
print("lattice_wide: checked and not executed - no native record-event dynamics, no constraint algebra for the qubit moves, no phase; Gaussian comparators only for A-C.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

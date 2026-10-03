"""A9 task 4: does a distant menu choice change local formation statistics?

Supplied toy (nothing adopted). Four qubits: x (forming site), y (x's unrecorded
neighbour), b (distant site whose record forms with menu M_b), c (distant
environment). A random joint pure state is drawn. The distant record at b forms
with one of three conditions: "no record yet", menu Z, menu X, or a random menu.
Q1's at-once update leaves (x,y) in branch state sigma_k with odds p_k. Local
statistics at x are averaged over the unread distant outcome k. No-signalling
requires the averaged local statistics to be the same for every distant condition.

Rules compared (F is a random local effect on (x,y), 0 <= F <= 1; U a random
two-site change between ticks; menu at x is Z):
  L-chance   : P(form) = tr(F s)                                   (linear)
  L-joint    : P(form, k) = tr(sqrt(F) (P_k x 1) sqrt(F) s)        (linear instrument)
  L-2tick    : [P(form@1), P(no@1, form@2)], no-record branch updated by sqrt(1-F)
  N-square   : P(form) = tr(F s)^2
  N-impurity : P(form) = 1 - tr(s_x^2)        ("forms where sharing is")
  N-product  : P(form, k) = tr(F s) * tr(P_k s_x)  (linear chance x raw site odds)
  N-2tick    : as L-2tick but the no-record branch leaves the possibilities untouched
  N-menu     : menu at x set by the neighbour's possibility (its Bloch axis);
               P(lock 'aligned') = <+n_y| s_x |+n_y>
Output: max over trials of the largest change in any averaged local statistic
between distant conditions; also a non-vacuity check (how different the branch
ensembles are).
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import sqrtm, expm

rng = np.random.default_rng(20261002)
I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1.0, -1.0]).astype(complex)


def haar_state(d):
    v = rng.normal(size=d) + 1j * rng.normal(size=d)
    return v / np.linalg.norm(v)


def haar_unitary(d):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def rand_effect(d):
    w = haar_unitary(d)
    lam = rng.uniform(0, 1, size=d)
    return (w * lam) @ w.conj().T


def psd_sqrt(a):
    lam, w = np.linalg.eigh((a + a.conj().T) / 2)
    lam = np.clip(lam, 0, None)
    return (w * np.sqrt(lam)) @ w.conj().T


def branches(psi, menu):
    """psi: 16-vector on (x,y,b,c). menu: None or 2x2 unitary (columns = menu vectors at b).
    Returns list of (p_k, sigma_xy_k)."""
    t = psi.reshape(2, 2, 2, 2)
    if menu is None:
        m = t.reshape(4, 4)  # (xy) x (bc)
        return [(1.0, m @ m.conj().T)]
    out = []
    for k in range(2):
        phi = np.einsum("xybc,b->xyc", t, menu[:, k].conj()).reshape(4, 2)
        p = float(np.vdot(phi, phi).real)
        if p < 1e-15:
            continue
        out.append((p, (phi @ phi.conj().T) / p))
    return out


def red_x(s):
    return np.einsum("ayby->ab", s.reshape(2, 2, 2, 2))


def red_y(s):
    return np.einsum("xaxb->ab", s.reshape(2, 2, 2, 2))


P = [np.kron(np.diag([1.0, 0.0]), I2), np.kron(np.diag([0.0, 1.0]), I2)]  # menu Z at x, on (x,y)
Px = [np.diag([1.0, 0.0]), np.diag([0.0, 1.0])]


def rules(F, U):
    sF = psd_sqrt(F)
    s1F = psd_sqrt(np.eye(4) - F)
    E = [sF @ Pk @ sF for Pk in P]
    F2 = U.conj().T @ F @ U  # Heisenberg-picture effect for tick 2

    def l_chance(s):
        return np.array([np.trace(F @ s).real])

    def l_joint(s):
        return np.array([np.trace(Ek @ s).real for Ek in E])

    def l_2tick(s):
        s_no = s1F @ s @ s1F  # unnormalised no-record branch (Lueders)
        return np.array([np.trace(F @ s).real, np.trace(F2 @ s_no).real])

    def n_square(s):
        return np.array([np.trace(F @ s).real ** 2])

    def n_impurity(s):
        sx = red_x(s)
        return np.array([1.0 - np.trace(sx @ sx).real])

    def n_product(s):
        f = np.trace(F @ s).real
        sx = red_x(s)
        return np.array([f * np.trace(Pk @ sx).real for Pk in Px])

    def n_2tick(s):
        f = np.trace(F @ s).real
        return np.array([f, (1.0 - f) * np.trace(F2 @ s).real])

    def n_menu(s):
        sy = red_y(s)
        r = np.array([np.trace(sy @ S).real for S in (SX, SY, SZ)])
        n = r / np.linalg.norm(r) if np.linalg.norm(r) > 1e-12 else np.array([0, 0, 1.0])
        proj = (I2 + n[0] * SX + n[1] * SY + n[2] * SZ) / 2
        return np.array([np.trace(proj @ red_x(s)).real])

    return {
        "L-chance": l_chance, "L-joint": l_joint, "L-2tick": l_2tick,
        "N-square": n_square, "N-impurity": n_impurity, "N-product": n_product,
        "N-2tick": n_2tick, "N-menu": n_menu,
    }


HAD = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
NTRIAL = 3000
names = None
worst = {}
mean = {}
nonvac = []
for trial in range(NTRIAL):
    psi = haar_state(16)
    F = rand_effect(4)
    U = haar_unitary(4)
    R = rules(F, U)
    if names is None:
        names = list(R)
        worst = {n: 0.0 for n in names}
        mean = {n: 0.0 for n in names}
    conds = [None, np.eye(2, dtype=complex), HAD, haar_unitary(2)]
    ens = [branches(psi, m) for m in conds]
    # non-vacuity: Z vs X menus give different branch states (trace distance of first branches)
    a, b = ens[1][0][1], ens[2][0][1]
    nonvac.append(0.5 * np.abs(np.linalg.eigvalsh(a - b)).sum())
    for n in names:
        stats = [sum(p * R[n](s) for p, s in e) for e in ens]
        d = max(np.max(np.abs(stats[i] - stats[j])) for i in range(4) for j in range(i + 1, 4))
        worst[n] = max(worst[n], d)
        mean[n] += d / NTRIAL

print(f"trials = {NTRIAL}; distant conditions = no record / menu Z / menu X / random menu")
print(f"non-vacuity: mean trace distance between Z-branch and X-branch states of (x,y) = {np.mean(nonvac):.3f}")
print(f"{'rule':12s} {'max change':>12s} {'mean change':>12s}")
for n in names:
    print(f"{n:12s} {worst[n]:12.3e} {mean[n]:12.3e}")

# Explicit A5-style Bell example for the product rule (x maximally linked with b; F = |1><1|_x).
bell = np.zeros(16, complex)
# |Phi> = (|0_x 0_b> + |1_x 1_b>)/sqrt2 with y = |0>, c = |0>
for v in (0, 1):
    idx = np.ravel_multi_index((v, 0, v, 0), (2, 2, 2, 2))
    bell[idx] = 1 / np.sqrt(2)
F1 = np.kron(np.diag([0.0, 1.0]), I2)
Rb = rules(F1, np.eye(4, dtype=complex))
for label, m in (("no record at b", None), ("menu Z at b", np.eye(2, dtype=complex)), ("menu X at b", HAD)):
    e = branches(bell, m)
    pj = sum(p * Rb["N-product"](s) for p, s in e)
    lj = sum(p * Rb["L-joint"](s) for p, s in e)
    print(f"Bell example, {label:15s}: product rule P(form,lock 0/1) = {np.round(pj, 4)}; "
          f"instrument rule = {np.round(lj, 4)}")

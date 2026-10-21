"""Shared helpers for block C4b (own code; does not import C4's c4lib).

Conventions follow C4 / the 2026-10-17 stabilizer note: O = 24 signed permutation matrices of
det +1 acting on Z^3 about the origin; soldering action Q: O -> SO(3) sends sigma_a at r to
sum_b Q(R)[b,a] sigma_b at R r.  Menu: trivial, sign diag(1,s,s), axis s|R|, full R, with
s = sign of the axis permutation |R|.
"""
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""), flush=True)
    return ok


def total():
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}", flush=True)


def build_O():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out


O = build_O()


def perm_sign(M):
    return int(round(np.linalg.det(np.abs(M))))


def menu_Q(M, action):
    if action == 'trivial':
        return np.eye(3, dtype=int)
    if action == 'sign':
        s = perm_sign(M)
        return np.diag([1, s, s])
    if action == 'axis':
        return perm_sign(M) * np.abs(M)
    if action == 'full':
        return np.array(M, int)
    raise ValueError(action)


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]
I2 = np.eye(2, dtype=complex)


def su2_lift(Q):
    """A unitary u with u sigma_a u^dag = sum_b Q[b,a] sigma_b (found by least squares on the
    4-dim space of 2x2 matrices; unique up to phase)."""
    # Solve u sigma_a = (sum_b Q[b,a] sigma_b) u  for u: linear in u.
    rows = []
    for a in range(3):
        rhs = sum(Q[b, a] * PAULI[b] for b in range(3))
        # vec(u s) - vec(rhs u) = (s^T kron I - I kron rhs) vec(u)  (column-major vec)
        rows.append(np.kron(PAULI[a].T, I2) - np.kron(I2, rhs))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A)
    v = vh[-1].conj()
    u = v.reshape(2, 2, order='F')
    u = u / np.sqrt(abs(np.linalg.det(u)))
    assert s[-1] < 1e-9, s
    return u

#!/usr/bin/env python3
"""T16 test 1: audit the June 2026-06-05 arrow toy (independent re-implementation; the
checkout is not imported or edited).  1 pointer qubit + 5 fragments, H_k = (pi/2) P1 (x) X_k."""
import numpy as np

rng = np.random.default_rng(16)
I2 = np.eye(2)
X = np.array([[0, 1], [1, 0]], float)
P1 = np.diag([0.0, 1.0])
nf = 5
ns = 1 + nf
dim = 2 ** ns


def kron(*ops):
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def Hk(k):
    ops = [P1] + [I2] * nf
    ops[1 + k] = X
    return (np.pi / 2) * kron(*ops)


def unitary(H):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w)) @ V.conj().T


U = [unitary(Hk(k)) for k in range(nf)]


def rdm(rho, keep):
    t = rho.reshape([2] * ns + [2] * ns)
    half = ns
    for s in sorted([s for s in range(ns) if s not in keep], reverse=True):
        t = np.trace(t, axis1=s, axis2=s + half)
        half -= 1
    d = 2 ** len(keep)
    return t.reshape(d, d)


def vn(r):
    r = (r + r.conj().T) / 2
    ev = np.linalg.eigvalsh(r)
    ev = ev[ev > 1e-12]
    return float(-np.sum(ev * np.log2(ev)))


def red(rho, th=0.9):
    Ss = vn(rdm(rho, [0]))
    n = 0
    for k in range(nf):
        if Ss + vn(rdm(rho, [1 + k])) - vn(rdm(rho, [0, 1 + k])) >= th:
            n += 1
    return n


def run(rho, order):
    seq = [red(rho)]
    for k in order:
        rho = U[k] @ rho @ U[k].conj().T
        seq.append(red(rho))
    return seq, rho


plus = np.array([1, 1]) / np.sqrt(2)
psi = plus.astype(complex)
for _ in range(nf):
    psi = np.kron(psi, np.array([1, 0], complex))
rho0 = np.outer(psi, psi.conj())

print("== 1a reproduce the reported sequences ==")
fwd, rhoM = run(rho0, range(nf))
print("forward low-record          R_red =", fwd)
rev, _ = run(np.conj(rhoM), range(nf))
print("time-reversed high-record   R_red =", rev)
g = np.zeros(dim, complex)
g[0] = g[-1] = 1 / np.sqrt(2)
ghz, _ = run(np.outer(g, g.conj()), range(nf))
print("GHZ built directly          R_red =", ghz)
idd, _ = run(np.eye(dim) / dim, range(nf))
print("I/d                         R_red =", idd)

print("\n== 1b second pass of the SAME generators from the fully recorded state ==")
two, _ = run(rho0, list(range(nf)) + list(range(nf)))
print("two passes k=0..4,0..4      R_red =", two)
three, _ = run(rho0, list(range(nf)) * 3)
print("three passes                R_red =", three)
erased = two[nf] == nf and two[2 * nf] == 0
print("records erased by the toy's own forward map on pass 2:", erased)

print("\n== 1c random product starts, one pass k=0..4 ==")
def haar_qubit():
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    return v / np.linalg.norm(v)

up = dn = flat = 0
Nst = 400
for _ in range(Nst):
    psi = np.array([1.0 + 0j])
    for _q in range(ns):
        psi = np.kron(psi, haar_qubit())
    s, _ = run(np.outer(psi, psi.conj()), range(nf))
    d = s[-1] - s[0]
    up += d > 0
    dn += d < 0
    flat += d == 0
print(f"random product starts (n={Nst}): raise {up}, lower {dn}, flat {flat}")

print("\nRESULT 1a reproduces:", fwd == [0, 1, 2, 3, 4, 5] and rev == [5, 4, 3, 2, 1, 0]
      and ghz == [5, 4, 3, 2, 1, 0] and set(idd) == {0})
print("RESULT 1b erased on pass 2:", erased)

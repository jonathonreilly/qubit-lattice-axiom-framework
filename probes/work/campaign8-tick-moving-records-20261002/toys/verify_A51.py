"""Coordinator check of A51's exact side result, from scratch.
Columnar dimer singlets along x are an exact eigenstate of the dual-frame Heisenberg rule
J(class) = j on (001),(011),(111); j/2 on (002),(012),(112); j/4 on (022),(122); j/8 on (222); 0 beyond.
(a) Pair condition J11 + J22 = J12 + J21 for every pair of dimers (infinite lattice, by class).
(b) Direct test on an open 4x2x2 cluster (16 qubits): H |VBS> = E |VBS>, and a control rule (plain NN only) fails."""
import itertools, signal
import numpy as np
signal.alarm(250)
TABLE = {(0,0,1): 1, (0,1,1): 1, (1,1,1): 1, (0,0,2): .5, (0,1,2): .5, (1,1,2): .5, (0,2,2): .25, (1,2,2): .25, (2,2,2): .125}
J = lambda d: TABLE.get(tuple(sorted(map(abs, d))), 0.0)
bad = 0; n = 0
for a, y, z in itertools.product(range(-4, 5), repeat=3):
    D = np.array((2 * a, y, z))
    if not D.any(): continue
    n += 1
    lhs = 2 * J(D); rhs = J(D + (1, 0, 0)) + J(D - (1, 0, 0))
    bad += abs(lhs - rhs) > 1e-12
print(f"(a) pair condition violated in {bad} of {n} dimer pairs {'OK' if bad == 0 else 'FAIL'}")

dims = (4, 2, 2); sites = list(itertools.product(*map(range, dims))); sid = {s: i for i, s in enumerate(sites)}; N = len(sites)
singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
psi = np.array([1.0])
order = []
for (y, z) in itertools.product(range(2), range(2)):
    for x0 in (0, 2):
        order += [sid[(x0, y, z)], sid[(x0 + 1, y, z)]]
for _ in range(N // 2): psi = np.kron(psi, singlet)
psi = np.transpose(psi.reshape([2] * N), np.argsort(order)).reshape(-1)    # qubit q of psi is site q
X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
def apply2(v, i, j, A):
    t = v.reshape([2] * N)
    t = np.moveaxis(np.tensordot(A, t, axes=([1], [i])), 0, i)
    t = np.moveaxis(np.tensordot(A, t, axes=([1], [j])), 0, j)
    return t.reshape(-1)
def Hpsi(v, Jf):
    out = np.zeros(v.shape, complex)
    for i, j in itertools.combinations(range(N), 2):
        c = Jf(np.array(sites[j]) - np.array(sites[i]))
        if c: out += c * sum(apply2(v, i, j, A) for A in (X, Y, Z))
    return out
for name, Jf in (("A51 closed-form rule", J), ("control: plain NN only", lambda d: 1.0 if sum(map(abs, d)) == 1 else 0.0)):
    h = Hpsi(psi.astype(complex), Jf)
    E = np.vdot(psi, h).real
    res = np.linalg.norm(h - E * psi)
    print(f"(b) {name}: E = {E:.6f}, |H psi - E psi| = {res:.2e} {'(eigenstate)' if res < 1e-10 else '(not an eigenstate)'}")

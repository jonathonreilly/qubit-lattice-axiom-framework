#!/usr/bin/env python3
"""J:attack-a:PR9373 -- WITNESS REALIZABILITY: the note's witnesses are the points f+- = (x, 1 - x, 1/2), e^{2 pi i x} = (2q +- i)^2/(1 + 4q^2), of the four-site Bloch cell of the composite-site network at J_x = J_y = 1, J_z = J(q), kappa = q.

Two realizability questions:
  (1) Are the points on the torus of the declared setting? |(2q + i)^2/(1 + 4q^2)| = 1 exactly, so x is real; f_3 = 1/2 is a Bloch momentum of the cell (translation (1, 1, 2)); f+ != f- for finite q.
  (2) Is the four-site Bloch matrix the Hamiltonian of a real-space periodic network? At q = 1/2 (J = 1, kappa = 1/2) the witness is f+ = (1/4, 3/4, 1/2), a point of the momentum grid of the periodic network with 4 x 4 x 2 cells (128 sites). This script builds the
      real-space antisymmetric matrix M of that network directly (cell index arithmetic mod (4, 4, 2), one 4 x 4 block per cell pair from the hopping list, reverse hops with the opposite sign), diagonalises H = i M (a 128 x 128 Hermitian matrix), and checks that
      the spectrum contains the double zero level of each of f+ and f-, with eigenvalues +-sqrt(48) at each (so the zero eigenvalue has multiplicity exactly 4 = 2 + 2 on this grid), and that the whole real-space spectrum equals the union of the 32 Bloch spectra.
The Bloch cell, the site rule and the flavour rule are rebuilt here, not taken from the PR's runner. The real-space matrix uses the same hopping list as the Bloch matrix, so (2) checks the Fourier reduction and the grid points, not the network definition itself (that is validated by the notes' own numbers, c = 48 and the README's nodes, in the falsifier of this PR). Floating point (numpy eigenvalues), labelled.
Prints SUMMARY:; HIT only if a witness is not realizable.
"""
import sys, time
import numpy as np
T0 = time.time()
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
def is_site(p):
    i, j, z = p; m = z % 4
    if m == 0: return j % 2 == 0
    if m == 1: return i % 2 == 1
    if m == 2: return j % 2 == 1
    return i % 2 == 0
def nbrs(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q): out.append(q)
    return out
def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0: return "z"
    lo = p if sum(d) > 0 else q; m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]
def reduce(p):
    n3 = p[2] // 2; x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2; rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)
def terms_of(Jx, Jy, Jz, kappa):
    J = {"x": Jx, "y": Jy, "z": Jz}; out = []
    for p in REPS:
        a, _ = reduce(p)
        if sum(p) % 2 == 0:
            for q in nbrs(p):
                b, n = reduce(q); out.append((a, b, n, 2 * J[flavour(p, q)]))
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in np.subtract(n2, n1)), 2 * kappa))
    return out
def Hfloat(F, T):
    F = np.atleast_2d(F); Mk = np.zeros((len(F), 4, 4), dtype=complex)
    for (a, b, n, amp) in T:
        ph = np.exp(2j * np.pi * (F @ np.array(n, dtype=float)))
        Mk[:, a, b] += float(amp) * ph; Mk[:, b, a] -= float(amp) * np.conj(ph)
    return 1j * Mk

# (1) the witnesses are points of the torus
for q in (0.03, 0.25, 0.5, 1.0, 3.0, 30.0):
    z = (2 * q + 1j) ** 2 / (1 + 4 * q * q)
    assert abs(abs(z) - 1) < 1e-13
xs = [(np.angle((2 * q + 1j) ** 2 / (1 + 4 * q * q)) / (2 * np.pi)) % 1.0 for q in (0.03, 0.25, 0.5, 1.0, 3.0, 30.0)]
check("for q = 0.03 ... 30, |(2q + i)^2/(1 + 4q^2)| = 1 to 1e-13 and x lies strictly between 0 and 1/2, so f+ = (x, 1 - x, 1/2) and f- = (1 - x, x, 1/2) are distinct points of the torus", all(0 < v < 0.5 for v in xs), f"x = {[round(v, 6) for v in xs]}")
# (2) real-space periodic network at q = 1/2
J = 1.0; kap = 0.5
T = terms_of(1.0, 1.0, J, kap)
m1, m2, m3 = 4, 4, 2
ncell = m1 * m2 * m3; N = 4 * ncell
idx = lambda a, c: 4 * (((c[0] % m1) * m2 + (c[1] % m2)) * m3 + (c[2] % m3)) + a
M = np.zeros((N, N))
for c0 in range(m1):
    for c1 in range(m2):
        for c2 in range(m3):
            c = (c0, c1, c2)
            for (a, b, n, amp) in T:
                i = idx(a, c); j = idx(b, (c[0] + n[0], c[1] + n[1], c[2] + n[2]))
                M[i, j] += amp; M[j, i] -= amp
H = 1j * M
check("the real-space matrix H = iM of the 4 x 4 x 2-cell network (128 sites) is Hermitian", np.allclose(H, H.conj().T))
ev = np.linalg.eigvalsh(H)
zero = int(np.sum(np.abs(ev) < 1e-9)); s48 = int(np.sum(np.abs(ev - np.sqrt(48)) < 1e-9)); sm48 = int(np.sum(np.abs(ev + np.sqrt(48)) < 1e-9))
# Bloch union over the 32 momenta
bl = []
for j1 in range(m1):
    for j2 in range(m2):
        for j3 in range(m3):
            f = np.array([j1 / m1, j2 / m2, j3 / m3]); bl.extend(np.linalg.eigvalsh(Hfloat(f, T))[0])
bl = np.sort(np.array(bl))
check("the real-space spectrum equals the union of the 32 Bloch spectra of the momenta j/(4, 4, 2) to 1e-10", np.allclose(np.sort(ev), bl, atol=1e-10), f"max difference {np.max(np.abs(np.sort(ev) - bl)):.1e}")
Hp = Hfloat(np.array([0.25, 0.75, 0.5]), T)[0]; Hm = Hfloat(np.array([0.75, 0.25, 0.5]), T)[0]
sp_ = np.linalg.eigvalsh(Hp); sm_ = np.linalg.eigvalsh(Hm)
check("f+ = (1/4, 3/4, 1/2) and f- = (3/4, 1/4, 1/2) are momenta of the 4 x 4 x 2 grid, and at each the Bloch spectrum is {-sqrt(48), 0, 0, +sqrt(48)}", np.allclose(sp_, [-np.sqrt(48), 0, 0, np.sqrt(48)], atol=1e-9) and np.allclose(sm_, [-np.sqrt(48), 0, 0, np.sqrt(48)], atol=1e-9), f"{np.round(sp_, 6)}, {np.round(sm_, 6)}")
check("in the real-space spectrum the eigenvalue 0 has multiplicity exactly 4 (the double zero levels of f+ and f-), and +-sqrt(48) each occur at least twice (once from each of f+ and f-)", zero == 4 and s48 >= 2 and sm48 >= 2, f"multiplicities: 0: {zero}, +sqrt(48): {s48}, -sqrt(48): {sm48}")
print(f"   total {time.time() - T0:.0f}s")
if not HITS:
    print(f"SUMMARY: no purchase: the witnesses f+- are points of the torus for every q tested, and at q = 1/2 they are momenta of the periodic 4 x 4 x 2-cell network, whose real-space spectrum (128 sites) contains the double zero levels of f+ and f- (zero multiplicity {zero}) with the Bloch spectra reproduced to 1e-10")
else:
    print("SUMMARY: a witness is not realizable: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)

#!/usr/bin/env python3
"""T27 test G (route R2): the qubit as a gauge singlet (parton / baryon site).

SU(2): Abrikosov fermions f_up, f_down per site, local SU(2) gauge generators
    G^+ = f_up^dag f_down^dag, G^- = f_down f_up, G^z = (n-1)/2      (Affleck-Zou-Hsu-Anderson 1988).
SU(3): three colour modes per site, generators G^A = f^dag (lambda^A/2) f (A = 1..8).
Pre-registered in PREREG.md (Test G).
"""
import itertools, json, sys
import numpy as np
import scipy.sparse as sp

OUT = {}
def log(*a): print(*a); sys.stdout.flush()
def check(name, cond, detail=""):
    OUT[name] = bool(cond); log(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))

I2 = sp.identity(2, format="csr", dtype=complex)
SZ = sp.csr_matrix(np.diag([1., -1.]).astype(complex))
SM = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=complex))
def kron_list(ms):
    out = sp.identity(1, format="csr", dtype=complex)
    for m in ms: out = sp.kron(out, m, format="csr")
    return out
def annihilators(nmode):
    return [kron_list([SZ if k < m else (SM if k == m else I2) for k in range(nmode)]) for m in range(nmode)]
def nnz0(M):
    M = sp.csr_matrix(M).copy(); M.eliminate_zeros(); return int(M.nnz)
def null_dim(Gs):
    A = sum((g.getH() @ g for g in Gs[1:]), Gs[0].getH() @ Gs[0])
    A = A.toarray(); A = (A + A.conj().T) / 2
    ev, U = np.linalg.eigh(A)
    return U[:, ev < 1e-9], A

# ----------------------------------------------------------------- SU(2) partons
L = 4
nm = 2 * L
f = annihilators(nm)            # site s has modes 2s (up), 2s+1 (down)
dim = 2 ** nm
GS = {}
for s in range(L):
    fu, fd = f[2 * s], f[2 * s + 1]
    nn = fu.getH() @ fu + fd.getH() @ fd
    Gp = fu.getH() @ fd.getH()
    Gm = fd @ fu
    Gz = (nn - sp.identity(dim, format="csr", dtype=complex)) * 0.5
    GS[s] = (Gp, Gm, Gz)
# algebra check
ok = True
for s in range(L):
    Gp, Gm, Gz = GS[s]
    ok = ok and nnz0(Gp @ Gm - Gm @ Gp - 2 * Gz) == 0 and nnz0(Gz @ Gp - Gp @ Gz - Gp) == 0
check("G1 SU(2) gauge generators close on su(2) at every site", ok)
gens = []
for s in range(L):
    Gp, Gm, Gz = GS[s]
    gens += [(Gp + Gm) * 0.5, (Gp - Gm) * (-0.5j), Gz]
Kn, A = null_dim(gens)
check("G2 Gauss kernel of the SU(2) parton model has dimension 2^L = %d (out of 4^L = %d)" % (2 ** L, 4 ** L), Kn.shape[1] == 2 ** L, "dim=%d" % Kn.shape[1])
# which computational basis states lie in the kernel?
diag = np.real(np.diag(A))
npat = int(np.sum(diag < 1e-12))
check("G3 number of computational-basis patterns that satisfy the SU(2) Gauss law: %d of %d (the wall's own model: 0 of 65536)" % (npat, dim), npat == 2 ** L)
# spin operators S^a_s = (1/2) f^dag sigma^a f are gauge invariant
def spin(s, a):
    fu, fd = f[2 * s], f[2 * s + 1]
    TAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    v = [fu, fd]
    acc = sp.csr_matrix((dim, dim), dtype=complex)
    for i in range(2):
        for j in range(2):
            c = TAU[a][i, j] / 2
            if c != 0: acc = acc + c * (v[i].getH() @ v[j])
    return acc.tocsr()
inv = True
for s in range(L):
    for a in range(3):
        Sa = spin(s, a)
        for t in range(L):
            for g in gens[3 * t:3 * t + 3]:
                inv = inv and nnz0(Sa @ g - g @ Sa) == 0
check("G4 all site spin operators S_s^a commute exactly with every gauge generator (they are gauge invariant)", inv)
# Heisenberg bond commutes with all gauge generators, and preserves the kernel
Hb = sum((spin(0, a) @ spin(1, a) for a in range(3)), sp.csr_matrix((dim, dim), dtype=complex))
inv2 = all(nnz0(Hb @ g - g @ Hb) == 0 for g in gens)
check("G5 the Heisenberg bond S_0.S_1 commutes with every gauge generator (kernel is invariant)", inv2)
# the same operators restricted to the kernel form a spin-1/2 chain: S_s^a restricted has spectrum +-1/2
S0z = Kn.conj().T @ spin(0, 2).toarray() @ Kn
ev = np.sort(np.linalg.eigvalsh((S0z + S0z.conj().T) / 2))
check("G6 on the kernel S_0^z has eigenvalues -1/2 (x8) and +1/2 (x8): the kernel is (C^2)^{tensor L}, one qubit per site", np.allclose(ev, [-.5] * 8 + [.5] * 8))
# gauge-VARIANT counterexample: plain hopping f^dag_i f_j is not gauge invariant
hop = sum((f[2 * 0 + a].getH() @ f[2 * 1 + a] + f[2 * 1 + a].getH() @ f[2 * 0 + a] for a in range(2)), sp.csr_matrix((dim, dim), dtype=complex))
var = any(nnz0(hop @ g - g @ hop) > 0 for g in gens)
check("G7 control: the bare parton hop f^dag_i f_j is NOT gauge invariant (it needs a link matrix); the gauge field is exactly this missing link", var)

# ----------------------------------------------------------------- SU(3) baryon site
L3 = 3
nm3 = 3 * L3
f3 = annihilators(nm3)
dim3 = 2 ** nm3
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
g3 = []
for s in range(L3):
    for A_ in range(8):
        acc = sp.csr_matrix((dim3, dim3), dtype=complex)
        for a in range(3):
            for b in range(3):
                c = lam[A_][a, b] / 2
                if abs(c) > 0: acc = acc + c * (f3[3 * s + a].getH() @ f3[3 * s + b])
        g3.append(acc.tocsr())
K3, A3 = null_dim(g3)
check("G8 SU(3) colour-singlet site: Gauss kernel dimension is 2^L3 = %d (each site carries {|000>, |111>}: a qubit)" % (2 ** L3), K3.shape[1] == 2 ** L3, "dim=%d" % K3.shape[1])
d3 = np.real(np.diag(A3))
npat3 = int(np.sum(d3 < 1e-12))
check("G9 number of computational-basis patterns satisfying the SU(3) Gauss law: %d of %d" % (npat3, dim3), npat3 == 2 ** L3)
# baryon hop b^dag_i b_j with b = f1 f2 f3 is gauge invariant and NN two-site
def baryon(s): return f3[3 * s + 0] @ f3[3 * s + 1] @ f3[3 * s + 2]
bh = baryon(0).getH() @ baryon(1)
bh = bh + bh.getH()
check("G10 the colour-singlet baryon hop b^dag_0 b_1 + h.c. commutes with every SU(3) generator (an ordinary two-site qubit term)", all(nnz0(bh @ g - g @ bh) == 0 for g in g3))
json.dump(OUT, open("t27_G_result.json", "w"), indent=1)

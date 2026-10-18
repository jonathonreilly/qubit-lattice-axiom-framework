"""COL-1 check 3: floating-token SU(3) structure, matter only, on rings of L qubits (FULL 2^L space).

Token at x (7 qubits): b_x b_{x+1} b_{x+2} | r1 r2 r3 | b_{x+6}  =  1 1 0 | one-hot | 0
Pi_x = [token pattern at x] (diagonal).  Colour i of the cell at x = excitation on qubit x+3+i.
G_x^a = Pi_x (T^a on the one-hot span of qubits x+3..x+5) Pi_x.  Gauge point at EVERY site x.
"""
import sys, numpy as np, scipy.sparse as sp
from su3common import T, F

TOK = 7
REG = (3, 4, 5)

def bits(states, L, k):
    return (states >> (k % L)) & 1

def build(L):
    N = 1 << L
    s = np.arange(N, dtype=np.int64)
    Pi = []
    regj = []
    for x in range(L):
        b = [bits(s, L, x + k) for k in range(TOK)]
        onehot = (b[3] + b[4] + b[5]) == 1
        P = (b[0] == 1) & (b[1] == 1) & (b[2] == 0) & onehot & (b[6] == 0)
        j = np.where(b[3] == 1, 0, np.where(b[4] == 1, 1, 2))
        Pi.append(P); regj.append(j)
    return s, Pi, regj

def G(L, s, Pi, regj, x, a):
    N = 1 << L
    act = np.nonzero(Pi[x])[0]
    j = regj[x][act]
    rows, cols, vals = [], [], []
    for i in range(3):
        amp = T[a][i, j]
        nz = np.abs(amp) > 0
        src = act[nz]
        jj = j[nz]
        tgt = src.copy()
        tgt &= ~(np.int64(1) << ((x + REG[0] + jj) % L))   # clear bit of colour j
        tgt |= (np.int64(1) << ((x + REG[0] + i) % L))     # set bit of colour i
        rows.append(tgt); cols.append(src); vals.append(amp[nz])
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))

def mx(m):
    m = m.tocoo()
    return float(np.abs(m.data).max()) if m.nnz else 0.0

def rot_perm(L, s):
    # translation T: qubit k -> qubit k+1
    return ((s << 1) | (s >> (L - 1))) & ((1 << L) - 1)

for L in [int(v) for v in sys.argv[1:]] or [14, 16, 18, 20]:
    s, Pi, regj = build(L)
    N = 1 << L
    G0 = [G(L, s, Pi, regj, 0, a) for a in range(8)]
    # (G1) relations and Casimir
    rel = 0.0
    for a in range(8):
        for b in range(a + 1, 8):
            lhs = G0[a] @ G0[b] - G0[b] @ G0[a]
            rhs = sp.csr_matrix((N, N), dtype=complex)
            for c in range(8):
                if abs(F[a, b, c]) > 0:
                    rhs = rhs + 1j * F[a, b, c] * G0[c]
            rel = max(rel, mx(lhs - rhs))
    cas = sum(g @ g for g in G0)
    Pdiag = sp.diags(Pi[0].astype(float))
    cas_err = mx(cas - (4.0 / 3.0) * Pdiag)
    # (G2) all cross commutators with G_0 (translation covariance gives the rest)
    worst = 0.0
    for y in range(1, L):
        Gy = [G(L, s, Pi, regj, y, a) for a in range(8)]
        for a in range(8):
            for b in range(8):
                worst = max(worst, mx(G0[a] @ Gy[b] - Gy[b] @ G0[a]))
    # (G3) translation covariance T G_x T^dag = G_{x+1}, all x
    perm = rot_perm(L, s)
    Tm = sp.csr_matrix((np.ones(N), (perm, s)), shape=(N, N))
    cov = 0.0
    for x in range(L):
        Gx = G(L, s, Pi, regj, x, 2)       # one diagonal and one off-diagonal generator suffice per x;
        Gx1 = G(L, s, Pi, regj, (x + 1) % L, 2)
        cov = max(cov, mx(Tm @ Gx @ Tm.T - Gx1))
        Gx = G(L, s, Pi, regj, x, 1); Gx1 = G(L, s, Pi, regj, (x + 1) % L, 1)
        cov = max(cov, mx(Tm @ Gx @ Tm.T - Gx1))
    # density of simultaneously active cells and floating placements
    nact = np.zeros(N, dtype=np.int16)
    for x in range(L):
        nact += Pi[x]
    maxact = int(nact.max())
    patterns = set()
    for st in np.nonzero(nact >= 2)[0][:200000]:
        xs = tuple(x for x in range(L) if Pi[x][st])
        gaps = tuple(sorted(((xs[(k + 1) % len(xs)] - xs[k]) % L) for k in range(len(xs))))
        patterns.add(gaps)
    nonuniform = sorted(p for p in patterns if len(set(p)) > 1)
    # P1 directly: active cells never overlap
    overlap = 0
    for d in range(1, TOK):
        overlap += int(np.count_nonzero(Pi[0] & Pi[d]))
    print("L=%2d dim=%7d | su(3) rel err %.1e | Casimir-4/3*Pi err %.1e | max|[G_0^a,G_y^b]| over y,a,b = %.1e | cov err %.1e"
          % (L, N, rel, cas_err, worst, cov))
    print("      active states at x=0: %d (=3*2^(L-7)) | overlapping-cell states: %d | max simultaneous cells %d (P-CAP bound %.2f)"
          % (int(Pi[0].sum()), overlap, maxact, L / np.log2(3)))
    print("      distinct gap patterns with >=2 cells: %d; non-uniform (floating) examples: %s"
          % (len(patterns), nonuniform[:4]))
    sys.stdout.flush()

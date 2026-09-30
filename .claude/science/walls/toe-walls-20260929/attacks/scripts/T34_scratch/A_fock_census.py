"""T34 Test A: weak-centre grading census.  Pre-registered in PREREGISTRATION.md.

Model (docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md): left-handed 8-state surface
  Q_L = (2,3)_{+1/3}, L_L = (2,1)_{-1}    (Q = T3 + Y/2)
plus the SUPPLIED right-handed sector  u_R (1,3)_{4/3}, d_R (1,3)_{-2/3}, e_R (1,1)_{-2}, nu_R (1,1)_0.
Exact linear algebra only (numpy).  No repo file is touched.
"""
import itertools, sys
import numpy as np

I2 = np.eye(2)
sp = np.array([[0, 1], [0, 0]], dtype=complex)   # sigma^- style lowering in occupation basis (|1> -> |0>)
Z = np.diag([1.0, -1.0]).astype(complex)

# ---------------------------------------------------------------- Fock space by Jordan-Wigner
def annihilators(n):
    ops = []
    for j in range(n):
        m = np.array([[1]], dtype=complex)
        for k in range(n):
            m = np.kron(m, Z if k < j else (sp if k == j else I2))
        ops.append(m)
    return ops

def second_quantize(g, a):
    n = len(a)
    G = np.zeros_like(a[0])
    for i in range(n):
        for j in range(n):
            if g[i, j] != 0:
                G = G + g[i, j] * a[i].conj().T @ a[j]
    return G

# ---------------------------------------------------------------- single-particle data
# L modes 0..7: q(a,c)=a*3+c (a=0 up,1 down; c colour), l(a)=6+a.  R modes 8..15: u(c),d(c),e,nu.
NL, NR = 8, 8
N = NL + NR
def q(a, c): return a * 3 + c
def l(a): return 6 + a
def u(c): return 8 + c
def d(c): return 11 + c
E, NU = 14, 15

def single_particle_generators(n_modes, with_R=True):
    # weak isospin
    Tp = np.zeros((n_modes, n_modes), dtype=complex)
    for c in range(3): Tp[q(0, c), q(1, c)] = 1      # raises down -> up
    Tp[l(0), l(1)] = 1
    Tm = Tp.conj().T
    T3 = np.zeros((n_modes, n_modes), dtype=complex)
    for c in range(3): T3[q(0, c), q(0, c)] = .5; T3[q(1, c), q(1, c)] = -.5
    T3[l(0), l(0)] = .5; T3[l(1), l(1)] = -.5
    Tx = (Tp + Tm) / 2; Ty = (Tp - Tm) / (2j)
    # colour lambda_a/2 acting on colour index of every triplet mode
    lam = np.zeros((8, 3, 3), dtype=complex)
    lam[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    lam[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
    lam[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    lam[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    lam[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
    lam[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    lam[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
    lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    col = []
    for k in range(8):
        g = np.zeros((n_modes, n_modes), dtype=complex)
        trip = [q(0, 0), q(1, 0)] + ([u(0), d(0)] if with_R else [])
        for base in trip:                     # base = index of colour 0 for this triplet
            step = 1 if base in (u(0), d(0)) else 3   # q(a,c)=a*3+c -> colour stride 1
            for c1 in range(3):
                for c2 in range(3):
                    g[base + c1, base + c2] += lam[k][c1, c2] / 2
        col.append(g)
    Y = np.zeros((n_modes, n_modes), dtype=complex)
    for a in range(2):
        for c in range(3): Y[q(a, c), q(a, c)] = 1 / 3
        Y[l(a), l(a)] = -1
    if with_R:
        for c in range(3): Y[u(c), u(c)] = 4 / 3; Y[d(c), d(c)] = -2 / 3
        Y[E, E] = -2; Y[NU, NU] = 0
    return dict(Tx=Tx, Ty=Ty, T3=T3, col=col, Y=Y)

# ---------------------------------------------------------------- A1 / A2: L-only Fock space (256 states)
def part_A_LonlyFock():
    n = NL
    a = annihilators(n)
    g = single_particle_generators(n, with_R=False)
    Gx, Gy, G3 = (second_quantize(g[k], a) for k in ("Tx", "Ty", "T3"))
    T2 = Gx @ Gx + Gy @ Gy + G3 @ G3
    F = sum(x.conj().T @ x for x in a)
    Fdiag = np.real(np.diag(F)).round().astype(int)
    # commutation sanity: [Tx,Ty]=iT3
    assert np.allclose(Gx @ Gy - Gy @ Gx, 1j * G3)
    # diagonalise T^2 within each F sector
    bad_bos = bad_ferm = 0
    table = {}
    for f in range(n + 1):
        idx = np.where(Fdiag == f)[0]
        sub = T2[np.ix_(idx, idx)]
        w = np.linalg.eigvalsh((sub + sub.conj().T) / 2)
        for x in w:
            T = (-1 + np.sqrt(1 + 4 * x.real)) / 2
            twoT = int(round(2 * T))
            assert abs(2 * T - twoT) < 1e-8
            table[(f % 2, twoT % 2)] = table.get((f % 2, twoT % 2), 0) + 1
            if f % 2 == 0 and twoT % 2 == 1: bad_bos += 1
            if f % 2 == 1 and twoT % 2 == 0: bad_ferm += 1
    # dictionary check: [G(g), O(M)] = O([g,M]) on the 8-mode Fock space
    ok = True
    for gname in ("Tx", "T3"):
        gmat = g[gname]
        Gop = second_quantize(gmat, a)
        for i in range(n):
            for j in range(n):
                Eij = np.zeros((n, n), dtype=complex); Eij[i, j] = 1
                lhs = Gop @ (a[i].conj().T @ a[j]) - (a[i].conj().T @ a[j]) @ Gop
                rhs = second_quantize(gmat @ Eij - Eij @ gmat, a)
                ok = ok and np.allclose(lhs, rhs)
    print("    Fock <-> one-body dictionary [G,O_M]=O_[g,M] verified:", ok)
    print("A1  L-only Fock space, dim", 2 ** n)
    print("    (F parity, 2T parity) -> number of states:", dict(sorted(table.items())))
    print("    bosonic (F even) states with half-integer T :", bad_bos)
    print("    fermionic (F odd) weak-singlet-parity states:", bad_ferm)
    A1 = (bad_bos == 0 and bad_ferm == 0)
    # weak singlets (T=0) in odd F: explicit
    n_odd_singlet = 0
    for f in range(1, n + 1, 2):
        idx = np.where(Fdiag == f)[0]
        w = np.linalg.eigvalsh(T2[np.ix_(idx, idx)])
        n_odd_singlet += int(np.sum(np.abs(w) < 1e-9))
    print("    odd-F weak singlets (candidate u_R/d_R/e_R built from the surface):", n_odd_singlet)
    return A1 and n_odd_singlet == 0

# ---------------------------------------------------------------- operator-space decomposition
def ad_action(gens, rows, cols, n):
    """Return list of linear maps (as matrices on vec of M restricted to rows x cols block) M -> [g,M]."""
    dimM = len(rows) * len(cols)
    def vec_index(i, j): return rows.index(i) * len(cols) + cols.index(j)
    maps = []
    for g in gens:
        mat = np.zeros((dimM, dimM), dtype=complex)
        for i in rows:
            for j in cols:
                col_index = vec_index(i, j)
                # M = E_ij ; [g,E_ij] = g E_ij - E_ij g
                # (g E_ij)_{kl} = g_{ki} delta_{jl};  (E_ij g)_{kl} = delta_{ki} g_{jl}
                for k in rows:
                    if g[k, i] != 0: mat[vec_index(k, j), col_index] += g[k, i]
                for m in cols:
                    if g[j, m] != 0: mat[vec_index(i, m), col_index] -= g[j, m]
        maps.append(mat)
    return maps

def decompose(gs, rows, cols, label, n):
    """Colour-singlet, then weak Casimir, then Y."""
    col_maps = ad_action(gs["col"], rows, cols, n)
    stacked = np.vstack(col_maps)
    u_, s_, vh = np.linalg.svd(stacked)
    null = vh[np.sum(s_ > 1e-9):].conj().T            # columns span colour singlets
    if null.shape[1] == 0:
        print(f"    {label}: colour singlets: 0"); return []
    Tx, Ty, T3 = ad_action([gs["Tx"], gs["Ty"], gs["T3"]], rows, cols, n)
    Y, = ad_action([gs["Y"]], rows, cols, n)
    C = Tx @ Tx + Ty @ Ty + T3 @ T3
    Cs = null.conj().T @ C @ null
    Ys = null.conj().T @ Y @ null
    # simultaneous diagonalisation of Cs (hermitian) and Ys
    w, v = np.linalg.eigh((Cs + Cs.conj().T) / 2 + 1e-3 * (Ys + Ys.conj().T) / 2)
    out = []
    for k in range(len(w)):
        vk = v[:, k]
        t2 = (vk.conj() @ Cs @ vk).real
        y = (vk.conj() @ Ys @ vk).real
        out.append((round(float((-1 + np.sqrt(1 + 4 * t2)) / 2), 6), round(float(y), 6)))
    tally = {}
    for t, y in out: tally[(t, y)] = tally.get((t, y), 0) + 1
    print(f"    {label}: colour singlets: {null.shape[1]};  (T, Y_op) -> multiplicity: {dict(sorted(tally.items()))}")
    return out

def part_A3():
    gs = single_particle_generators(N, with_R=True)
    Lm = list(range(NL)); Rm = list(range(NL, N))
    print("A2/A3  bosonic bilinear operators a^dag_i a_j (one-body operator space), colour singlets:")
    LL = decompose(gs, Lm, Lm, "L dag L   (L-only surface)", N)
    RL = decompose(gs, Rm, Lm, "R dag L   (needs the supplied weak-singlet sector)", N)
    RR = decompose(gs, Rm, Rm, "R dag R", N)
    a2 = all(abs(t - .5) > 1e-6 for t, y in LL)
    dbl = [(t, y) for t, y in RL if abs(t - .5) < 1e-6]
    # NOTE (bug fixed after first run, see A_output_run1.txt): the first run compared the number of
    # T3 COMPONENTS (8) with the pre-registered number of DOUBLETS (4).  Each doublet has 2 components.
    ndoublets = len(dbl) // 2
    a3 = (len(dbl) == 8 and ndoublets == 4 and sorted(round(y) for t, y in dbl[::1])[::2] == [-1, -1, 1, 1])
    print("    A2 (L-only has no colour-singlet doublet operator):", a2)
    print("    A3 (exactly four colour-singlet doublet bilinears = 8 components, Y_op = +1,+1,-1,-1):", a3,
          "; doublets:", ndoublets)
    return a2, a3

def part_A6_vectorlike():
    """R sector supplied as a COPY of the doublet surface (vector-like, as a taste symmetry acting on both chiralities would give)."""
    n = 2 * NL
    Lm = list(range(NL)); Rm = list(range(NL, n))
    g = single_particle_generators(NL, with_R=False)
    def dup(x):
        out = np.zeros((n, n), dtype=complex); out[:NL, :NL] = x; out[NL:, NL:] = x; return out
    gs = {k: (dup(v) if not isinstance(v, list) else [dup(x) for x in v]) for k, v in g.items()}
    print("A6  vector-like completion (R modes are weak doublets too):")
    RL = decompose(gs, Rm, Lm, "R dag L", n)
    return all(abs(t - .5) > 1e-6 for t, y in RL)

# ---------------------------------------------------------------- A4: M_2(C) record domain
def part_A4():
    s = [np.array([[0, 1], [1, 0]], dtype=complex) / 2,
         np.array([[0, -1j], [1j, 0]], dtype=complex) / 2,
         np.array([[1, 0], [0, -1]], dtype=complex) / 2]
    basis = []
    for i in range(2):
        for j in range(2):
            m = np.zeros((2, 2), dtype=complex); m[i, j] = 1; basis.append(m)
    def rep(act):
        mats = []
        for sk in s:
            M = np.zeros((4, 4), dtype=complex)
            for c, b in enumerate(basis):
                r = act(sk, b)
                for rr, bb in enumerate(basis):
                    M[rr, c] = np.trace(bb.conj().T @ r)
            mats.append(M)
        return mats
    def spins(mats):
        C = sum(m @ m for m in mats)
        w = np.linalg.eigvals(C).real
        return sorted(round(float((-1 + np.sqrt(1 + 4 * x)) / 2), 6) for x in w)
    conj = spins(rep(lambda g, X: g @ X - X @ g))
    left = spins(rep(lambda g, X: g @ X))
    right = spins(rep(lambda g, X: -X @ g))
    print("A4  M_2(C) (4 complex dims) spin content:")
    print("    under conjugation X -> [g,X] (the automorphism action):", conj)
    print("    under left multiplication X -> gX                     :", left)
    print("    under right multiplication                            :", right)
    return all(abs(x - .5) > 1e-6 for x in conj) and all(abs(x - .5) < 1e-6 for x in left)

if __name__ == "__main__":
    A1 = part_A_LonlyFock()
    A2, A3 = part_A3()
    A6 = part_A6_vectorlike()
    A4 = part_A4()
    print("\nSUMMARY  A1:", A1, " A2:", A2, " A3:", A3, " A4:", A4, " A6:", A6)
    print("ALL PASS" if all([A1, A2, A3, A4, A6]) else "SOME FAIL")

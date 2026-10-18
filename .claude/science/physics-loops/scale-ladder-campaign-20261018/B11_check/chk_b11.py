#!/usr/bin/env python3
"""B11 fresh-context check (same model family, fresh context).

Reference step: B18_check/chk_model.py (a copy of the scale-ladder runner Part 6 construction), used in its
k-space form Ws(k) = S(k) R_L(k) U_H U_L exactly as the runner defines it.  The circuit below is built here
independently of B11's circuit.py:
  * on-site factor V = U_H U_L: own Clements-type rectangular-mesh elimination (generic U(2) mode-pair gates);
  * R_L: plaquette blocks found from the connectivity of the real-space link matrix (not geometry), the two
    perfect matchings of each 4-cycle found by edge 2-colouring, R = A exp((pi/4) A B);
  * S: own D . S_B . S_A factorisation test.
The circuit's real-space unitary is Bloch-transformed and compared with the runner's Ws(k) at all 64 torus momenta.
Then: fermion->qubit angle bookkeeping by an explicit Jordan-Wigner check (2-3 modes), exact-ring/Galois tests
on U_H, U_L, W.  Supplied model only; no physical identification."""
import os, sys, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B18_check'))
from chk_model import *          # noqa  (runner copy: Sr, RLr, UH, UL, PH, PLm, Ws, Bloch, VERTS, CORN, ...)
t0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)

VID = C['VID']; TV = list(itertools.product(range(L), repeat=3))
site_modes = {v: [VID[(v, c)] for c in CORN] for v in TV}
V = UH @ UL

# ---------------- gate machinery: (modes, 2x2 or 1x1 unitary, tag)
gates = []
def apply(glist, n=nV):
    U = np.eye(n, dtype=complex)
    for modes, g, tag in glist:
        m = list(modes); U[m, :] = g @ U[m, :]
    return U

# ---------------- (1) on-site: Clements rectangular mesh, generic U(2) gates
def clements(U):
    """Return (pre_ops, D, post_ops) as lists of ((i, j), 2x2) such that, acting on column vectors,
    U = [post_ops applied after D] D [pre_ops]; implemented here as a single ordered gate list."""
    n = U.shape[0]; X = U.astype(complex).copy(); right = []; left = []
    def null_right(r, c):      # zero X[r, c] mixing columns c, c+1 (right-multiply by G on (c, c+1))
        a, b = X[r, c], X[r, c + 1]
        nr = np.hypot(abs(a), abs(b))
        if abs(a) < 1e-14: return
        # columns (c, c+1) -> (c, c+1) G with new X[r,c] = 0: G = [[b, conj(a)], [-a, conj(b)]]/nr  (unitary)
        G = np.array([[b, np.conj(a)], [-a, np.conj(b)]]) / nr
        X[:, [c, c + 1]] = X[:, [c, c + 1]] @ G; right.append(((c, c + 1), G))
    def null_left(r, c):       # zero X[r, c] mixing rows r-1, r (left-multiply by G on (r-1, r))
        a, b = X[r - 1, c], X[r, c]
        nr = np.hypot(abs(a), abs(b))
        if abs(b) < 1e-14: return
        G = np.array([[np.conj(a), np.conj(b)], [-b, a]]) / nr
        X[[r - 1, r], :] = G @ X[[r - 1, r], :]; left.append(((r - 1, r), G))
    for i in range(n - 1):
        if i % 2 == 0:
            for j in range(i + 1): null_right(n - 1 - j, i - j)
        else:
            for j in range(1, i + 2): null_left(n + j - i - 2, j - 1)
    D = np.diag(X).copy()
    assert np.allclose(X, np.diag(D), atol=1e-10), np.abs(X - np.diag(D)).max()
    # L_k..L_1 U R_1..R_m = D  =>  U = L_1^+..L_k^+ D R_m^+..R_1^+ = D (D^-1 L_1^+ D)..(D^-1 L_k^+ D) R_m^+..R_1^+
    # application order on vectors: R_1^+, ..., R_m^+, D^-1 L_k^+ D, ..., D^-1 L_1^+ D, then the phase layer D
    app = [(p, G.conj().T) for (p, G) in right]
    for (p, G) in left[::-1]:
        d = D[list(p)]; app.append((p, np.diag(1 / d) @ G.conj().T @ np.diag(d)))
    return app, D
loc, Dloc = clements(V)
Ut = np.eye(12, dtype=complex)
for p, g in loc: Ut[list(p), :] = g @ Ut[list(p), :]
Ut = np.diag(Dloc) @ Ut
check("own Clements-mesh decomposition reproduces the 12x12 on-site factor V = U_H U_L", np.allclose(Ut, V, atol=1e-10),
      f"{len(loc)} two-mode U(2) gates + 1 diagonal phase layer; max err {np.abs(Ut - V).max():.1e}")
for v in TV:
    idx = site_modes[v]
    for p, g in loc: gates.append(((idx[p[0]], idx[p[1]]), g, 'onsite'))
    for a in range(12): gates.append(((idx[a],), np.array([[Dloc[a]]]), 'onsite-ph'))
n_on = len(gates)

# ---------------- (2) R_L from connectivity
HL = np.sqrt(2) * RLr
adj = np.abs(HL) > 1e-12
comp = -np.ones(nV, int); blocks = []
for s in range(nV):
    if comp[s] >= 0: continue
    st = [s]; comp[s] = len(blocks); mem = [s]
    while st:
        x = st.pop()
        for y in np.nonzero(adj[x])[0]:
            if comp[y] < 0: comp[y] = len(blocks); st.append(y); mem.append(y)
    blocks.append(mem)
deg_ok = all(adj[np.ix_(b, b)].sum() == 8 and len(b) == 4 and all(adj[x].sum() == 2 for x in b) for b in blocks)
check("link matrix: connected components are 3 L^3 disjoint 4-cycles (every mode degree 2), entries +-1",
      len(blocks) == 3 * L ** 3 and deg_ok and np.allclose(np.abs(HL[adj]), 1))
ok_struct = True; ok_flux = True
for b in blocks:
    # order the cycle
    cyc = [b[0]]
    while len(cyc) < 4:
        nb = [y for y in np.nonzero(adj[cyc[-1]])[0] if y not in cyc]; cyc.append(nb[0])
    h = HL[np.ix_(cyc, cyc)].real
    ok_flux &= np.isclose(h[0, 1] * h[1, 2] * h[2, 3] * h[3, 0], -1)
    A = np.zeros((4, 4)); B = np.zeros((4, 4))
    for (i, j) in ((0, 1), (2, 3)): A[i, j] = A[j, i] = h[i, j]
    for (i, j) in ((1, 2), (3, 0)): B[i, j] = B[j, i] = h[i, j]
    AB = A @ B
    ok_struct &= np.allclose(A @ A, np.eye(4)) and np.allclose(B @ B, np.eye(4)) and np.allclose(A @ B, -B @ A)
    from scipy.linalg import expm
    E1 = expm(np.pi / 4 * AB)
    ok_struct &= np.allclose(A @ E1, h / np.sqrt(2))
    # exp(pi/4 AB) acts on the two diagonal pairs (0,2), (1,3)
    for (i, j) in ((0, 2), (1, 3)):
        ok_struct &= np.allclose(E1[np.ix_([i, j], [k for k in range(4) if k not in (i, j)])], 0)
        gates.append(((cyc[i], cyc[j]), E1[np.ix_([i, j], [i, j])].astype(complex), 'RL-diag'))
    for (i, j) in ((0, 1), (2, 3)):
        gates.append(((cyc[i], cyc[j]), A[np.ix_([i, j], [i, j])].astype(complex), 'RL-link'))
check("each block has flux pi, matchings A, B with A^2 = B^2 = 1, {A,B} = 0 and R_L = A exp((pi/4)AB), exp acting on the two diagonals",
      ok_flux and ok_struct)
n_RL = len(gates) - n_on
diag_pairs = [g[0] for g in gates[n_on:] if g[2] == 'RL-diag']

# ---------------- (3) S = D S_B S_A
PA = np.zeros((nV, nV)); PB = np.zeros((nV, nV))
for (i, j) in diag_pairs: PA[i, j] = PA[j, i] = 1
for v in TV:
    for c in CORN:
        d, e = tuple(c); PB[VID[(v, frozenset((neg(d), neg(e))))], VID[(v, c)]] = 1
Dg = Sr @ PA @ PB          # S = D PB PA, PA, PB involutions
okS = np.allclose(Dg, np.diag(np.diag(Dg))) and np.allclose(np.abs(np.diag(Dg)), 1)
check("S = D . S_B . S_A (S_A: plaquette-diagonal swaps found from R_L's blocks; S_B: on-site antipodes; D diagonal +-1)", okS,
      f"#(-1) in D: {int(np.sum(np.diag(Dg) < 0))} of {nV}")
for (i, j) in diag_pairs: gates.append(((i, j), np.array([[0, 1], [1, 0]], complex), 'S-diag'))
seen = set()
for v in TV:
    for c in CORN:
        d, e = tuple(c); a = VID[(v, c)]; b = VID[(v, frozenset((neg(d), neg(e))))]
        if a in seen: continue
        seen.update((a, b))
        gates.append(((a, b), np.array([[0, Dg[a, a]], [Dg[b, b], 0]], complex), 'S-onsite'))   # D folded in
n_S = len(gates) - n_on - n_RL

Uc = apply(gates)
ON = np.zeros((nV, nV), complex)
for v in TV: ON[np.ix_(site_modes[v], site_modes[v])] = V
Wreal = Sr @ RLr @ ON
check("circuit == real-space step S R_L (U_H U_L) entrywise (no global phase)", np.abs(Uc - Wreal).max() < 1e-10,
      f"max err {np.abs(Uc - Wreal).max():.1e}")
# Bloch comparison with the runner's k-space Ws(k): find the momentum convention
errs = {}
for sgn in (+1, -1):
    e = 0
    for t in itertools.product(range(L), repeat=3):
        k = np.array(t) * 2 * np.pi / L; Bk = Bloch(sgn * k)
        e = max(e, np.abs(Bk.conj().T @ Uc @ Bk - Ws(k)).max())
    errs[sgn] = e
check("Bloch transform of the circuit equals the runner's Ws(k) at all 64 torus momenta (one sign convention)",
      min(errs.values()) < 1e-10, f"max err by convention {errs}")
U_RL = apply(gates[n_on:n_on + n_RL]); U_S = apply(gates[n_on + n_RL:])
check("factor-wise: R_L sub-circuit == R_L, S sub-circuit == S", np.abs(U_RL - RLr).max() < 1e-12 and np.abs(U_S - Sr).max() < 1e-12)
pos = np.array([VERTS[i][0] for i in range(nV)])
span = max(max(abs(dmod(a - b)) for a, b in zip(pos[m[0]], pos[m[1]])) for m, g, t in gates if len(m) == 2)
check("every gate acts on <= 2 modes within sup-distance 1 (range-1 circuit)", span <= 1, f"max sup span {span}")

# ---------------- depth (ASAP over the gate order; one-mode gates optional)
def depth(gl, only2=True):
    t = {}; D_ = 0
    for m, g, tag in gl:
        if only2 and len(m) == 1: continue
        l = max(t.get(x, 0) for x in m) + 1
        for x in m: t[x] = l
        D_ = max(D_, l)
    return D_
d_on, d_RL, d_S = depth(gates[:n_on]), depth(gates[n_on:n_on + n_RL]), depth(gates[n_on + n_RL:])
print(f"two-mode depth: on-site (Clements) {d_on}, R_L {d_RL}, S {d_S}, total {depth(gates)}; with phase layer {depth(gates, False)}")
check("two-mode depth of this alternative circuit is <= 16 (12 on-site mesh + 2 + 2), below B11's 25 (B11's 25 is an upper bound, not minimal)",
      depth(gates) <= 16, f"total {depth(gates)}")

# ---------------- fermionic Clifford / Clifford+T classification of single-particle gates
def is_monomial_unit(M):     # signed/phased permutation with phases in {+-1, +-i}
    M = np.asarray(M)
    nz = np.abs(M) > 1e-12
    if not (nz.sum(0) == 1).all() or not (nz.sum(1) == 1).all(): return False
    z = M[nz]
    return np.allclose(np.min(np.abs(z[:, None] - np.array([1, -1, 1j, -1j])[None]), axis=1), 0)
def in_Zr2i(M, maxk=8):      # entries in Z[1/sqrt2, i]: sqrt2^k z has Gaussian-integer form a + b sqrt2 with a, b in Z[i]
    M = np.asarray(M).ravel()
    for k in range(maxk + 1):
        x = M * np.sqrt(2) ** k
        # write x = a + b sqrt2, a, b Gaussian integers: try b from small range
        ok = True
        for z in x:
            found = False
            for br in range(-20, 21):
                for bi in range(-20, 21):
                    a = z - (br + 1j * bi) * np.sqrt(2)
                    if abs(a.real - round(a.real)) < 1e-9 and abs(a.imag - round(a.imag)) < 1e-9: found = True; break
                if found: break
            if not found: ok = False; break
        if ok: return True
    return False
cls = {}
for m, g, tag in gates:
    key = tag.split('-')[0] if tag != 'onsite-ph' else 'onsite'
    c_ = 'cliff' if is_monomial_unit(g) else ('cliff+T' if in_Zr2i(g, 2) else 'other')
    cls.setdefault(tag, {}).setdefault(c_, 0); cls[tag][c_] += 1
print("single-particle gate classes per tag (cliff = phased permutation in {+-1,+-i}; cliff+T = entries in Z[1/sqrt2,i]):")
for k_, v_ in cls.items(): print("   ", k_, v_)
check("S: every gate a {+-1}-signed swap (fermionic Clifford); S itself a signed permutation matrix",
      set(cls['S-diag']) == {'cliff'} and set(cls['S-onsite']) == {'cliff'} and is_monomial_unit(Sr))
check("R_L: link gates Clifford, diagonal gates exp((pi/4)AB) have entries +-1/sqrt2 (not Clifford, in Z[1/sqrt2])",
      set(cls['RL-link']) == {'cliff'} and set(cls['RL-diag']) == {'cliff+T'} and in_Zr2i(RLr[np.ix_(blocks[0], blocks[0])], 2)
      and not is_monomial_unit(RLr))

# ---------------- Jordan-Wigner: 2-mode hopping gate -> two commuting Pauli rotations by theta/2
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Zp = np.diag([1, -1]); sm = np.array([[0, 1], [0, 0]])
def kr(*a):
    out = np.array([[1.0]])
    for x in a: out = np.kron(out, x)
    return out
c = [kr(sm, I2), kr(Zp, sm)]
from scipy.linalg import expm
def many_body(g2):
    """Gaussian unitary Gamma(g) for a 2x2 single-particle unitary g (Gamma c_j^dag Gamma^dag = sum_i g_ij c_i^dag)"""
    Hm = 1j * __import__('scipy.linalg', fromlist=['logm']).logm(g2)     # g = exp(-i Hm)
    Hm = (Hm + Hm.conj().T) / 2
    K = sum(Hm[i, j] * c[i].conj().T @ c[j] for i in range(2) for j in range(2))
    return expm(-1j * K)
paulis = [kr(a, b) for a in (I2, X, Y, Zp) for b in (I2, X, Y, Zp)]
def is_clifford(U):
    for P in paulis[1:]:
        Q = U @ P @ U.conj().T
        coef = [np.trace(Q @ R.conj().T) / 4 for R in paulis]
        if sum(abs(x) > 1e-9 for x in coef) != 1: return False
    return True
g_sw = np.array([[0, 1], [1, 0]], complex); g_rl = expm(np.pi / 4 * np.array([[0, 1], [-1, 0]]))
G1, G2 = many_body(g_sw), many_body(g_rl)
ok_map = np.allclose(G1 @ c[0].conj().T @ G1.conj().T, sum(g_sw[i, 0] * c[i].conj().T for i in range(2)))
ok_map &= np.allclose(G2 @ c[0].conj().T @ G2.conj().T, sum(g_rl[i, 0] * c[i].conj().T for i in range(2)))
# explicit Pauli form: theta (sy-type hop) -> exp(-i theta/2 (XY - YX)/... ) check: G2 == exp(-i pi/8 X Y) exp(+i pi/8 Y X) up to phase
cand = expm(-1j * np.pi / 8 * kr(X, Y)) @ expm(1j * np.pi / 8 * kr(Y, X))
def up_to_phase(A, B):
    i = np.unravel_index(np.argmax(np.abs(B)), B.shape); ph = A[i] / B[i]
    return abs(abs(ph) - 1) < 1e-9 and np.allclose(A, ph * B)
ok_pa = up_to_phase(G2, cand) or up_to_phase(G2, expm(1j * np.pi / 8 * kr(X, Y)) @ expm(-1j * np.pi / 8 * kr(Y, X)))
check("JW (2 modes): Gamma(signed swap) is a qubit Clifford; Gamma(exp((pi/4)AB) diagonal gate) = exp(-+i pi/8 XY) exp(+-i pi/8 YX), not Clifford, entries in Z[1/sqrt2,i]",
      ok_map and is_clifford(G1) and (not is_clifford(G2)) and ok_pa and in_Zr2i(G2, 2))

# ---------------- exact-ring / Galois tests
lamH = np.linalg.eigvalsh(Hon0)
lsH = sorted(set(np.round(lamH, 6)))
check("H_on eigenvalues -1-sqrt3, sqrt3-1, 2 (sorted), Lambda eigenvalues +-sqrt2, +-2sqrt2", np.allclose(lsH, [-1 - np.sqrt(3), np.sqrt(3) - 1, 2])
      and np.allclose(sorted(set(np.round(np.linalg.eigvalsh(Lam), 6))), [-2 * np.sqrt(2), -np.sqrt(2), np.sqrt(2), 2 * np.sqrt(2)]))
# sigma: sqrt3 -> -sqrt3 fixes Q(sqrt2, i) and swaps the H_on eigenvalues -1-sqrt3 <-> -1+sqrt3; H_on integer => sigma(P0) = P1
sUH = PH[1] - PH[0] - 1j * PH[2]
sW_on = sUH @ UL          # sigma fixes U_L (Lambda in Z[i], eigenvalues in Q(sqrt2)), S, R_L (entries in Z[1/sqrt2])
# is sigma(V) proportional to V?
ph = np.vdot(V.ravel(), sW_on.ravel()) / np.vdot(V.ravel(), V.ravel())
check("Galois test: sigma(U_H U_L) is NOT a phase times U_H U_L, so some product W_ia conj(W_jb) lies outside Q(zeta8) (=> no exact "
      "ancilla-clean, measurement-free Clifford+T circuit realises W on the code, by the trace argument of exact_field.py)",
      np.abs(sW_on - ph * V).max() > 0.1, f"min_c ||sigma(V) - cV||_max = {np.abs(sW_on - ph * V).max():.3f}")
# find an explicit product (a + b sqrt3)/36
Wk = Ws(np.zeros(3))
found = None
for (i, a, j, b) in itertools.product(range(12), repeat=4):
    if a == b: continue
    x = Wk[i, a] * np.conj(Wk[j, b]) * 36
    for bb in range(-6, 7):
        if bb == 0: continue
        r = x - bb * np.sqrt(3)
        if abs(r.imag) < 1e-9 and abs(r.real - round(r.real)) < 1e-9 and abs(x.imag) < 1e-9:
            found = ((i, a, j, b), round(r.real), bb); break
    if found: break
print("explicit product at k = 0 Bloch block: W_ia conj(W_jb) = (a + b sqrt3)/36 with", found)
check("an explicit W bilinear coefficient with a sqrt3 component exists (k = 0 block)", found is not None)
ULr = UL * 6
def dyadic(x, k=12): y = x * 2 ** k; return abs(y.real - round(y.real)) < 1e-6 and abs(y.imag - round(y.imag)) < 1e-6
nondy = [(i, a, j, b, UL[i, a] * np.conj(UL[j, b])) for i, a, j, b in itertools.product(range(12), repeat=4)
         if i != j and a != b and abs(UL[i, a] * UL[j, b]) > 1e-9 and not dyadic(UL[i, a] * np.conj(UL[j, b]))]
print("U_L distinct |entries|:", sorted(set(np.round(np.abs(UL[np.abs(UL) > 1e-9]), 6))), " e.g. non-dyadic product", nondy[0] if nondy else None)
check("U_L entries in (1/6) Z[i]; some product U_ia conj(U_jb) (i != j, a != b) is not dyadic (denominator 3)",
      np.allclose(ULr, np.round(ULr.real) + 1j * np.round(ULr.imag), atol=1e-9) and len(nondy) > 0)

# ---------------- flow index of S by counting (signed permutation)
fl = []
for ax in range(3):
    f = 0
    for i in range(nV):
        j = int(np.argmax(np.abs(Sr[:, i]))); dl = dmod(pos[j][ax] - pos[i][ax])
        if pos[i][ax] == 0 and dl == 1: f += 1
        if pos[i][ax] == 1 and dl == -1: f -= 1
        if pos[i][ax] == L - 1 and dl == 1: pass
    fl.append(f)
check("S: net number of modes crossing the plane x_ax = 1/2 is zero on every axis (index 0; consistent with the explicit 2-mode-gate circuit)",
      fl == [0, 0, 0], str(fl))
print(f"\nB11_check TOTAL: PASS={PASS} FAIL={FAIL}  [{time.time() - t0:.0f}s]")

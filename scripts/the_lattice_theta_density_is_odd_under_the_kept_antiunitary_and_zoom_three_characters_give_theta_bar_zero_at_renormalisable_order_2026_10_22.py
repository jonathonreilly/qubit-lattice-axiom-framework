AUDIT_INPUT_PATHS = ('docs/THE_LATTICE_THETA_DENSITY_IS_ODD_UNDER_THE_KEPT_ANTIUNITARY_AND_ZOOM_THREE_CHARACTERS_GIVE_THETA_BAR_ZERO_AT_RENORMALISABLE_ORDER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""strong-cp-revisit: theta on quantum rishon link registers and a Nelson-Barr
structure from zoom-3 translation characters.

A. Link-sector reality: rishon hop, det term, ring exchange are real in the
   occupation basis; the lattice theta density E.B is odd under complex
   conjugation K, under inversion and under PH*K; even under PH and proper turns.
   With K exact, spec H(c) = spec H(-c) and <E.B> = 0 at c = 0 (3D U(1) cube).
B. The det term's phase is removable: e^{i chi N_cluster} maps H(phi) to
   H(phi + 3 chi) (SU(3) rishon link with quarks, 12 modes).
C. 1+1D: half-integer S fixes theta = pi (two vacua, flux +-1/2), integer S
   gives theta = 0 (one vacuum).
D. One doublet: its vacuum phase is a hypercharge rotation: J = 0, arg det real
   (heavy vector-like copies included).
E. Two doublets with a relative phase: J != 0 and arg det of order one.
F. Zoom-3 translation characters (light = (j,j,j), heavy off-diagonal):
   doublet-filled light-heavy blocks vanish exactly; a character-carrying
   singlet vacuum fills only blocks that close no determinant loop, so
   arg det = 0 at renormalisable order with J != 0; the first leak is the
   dimension-five H sigma* term.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

T0 = time.time()
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

rng = np.random.default_rng(20261022)
def nrm(A):
    A = A.tocsr() if sp.issparse(A) else A
    return float(abs(A).max()) if (A.nnz if sp.issparse(A) else A.size) else 0.0

# ---------------- A. 3D U(1) spin-1/2 links on one cube ----------------
print("== A. link-sector reality and the lattice theta density (one cube, 12 spin-1/2 links)")
corners = list(itertools.product((0, 1), repeat=3))
links = [(c, i) for c in corners for i in range(3) if c[i] == 0]   # 12 links
lid = {l: k for k, l in enumerate(links)}
nL = len(links); D = 2 ** nL
I2 = sp.identity(2, format="csr")
Sp = sp.csr_matrix(np.array([[0., 1.], [0., 0.]]))   # raises E: |down>->|up>, basis (up, down)
Sz = sp.csr_matrix(np.diag([0.5, -0.5]))
def site_op(op, k):
    out = sp.identity(1, format="csr")
    for j in range(nL):
        out = sp.kron(out, op if j == k else I2, format="csr")
    return out
Uop = [site_op(Sp, k) for k in range(nL)]
Eop = [site_op(Sz, k) for k in range(nL)]
def add(c, i): return tuple(c[j] + (1 if j == i else 0) for j in range(3))
faces = []   # (normal k, x_k value, U_p)
for k in range(3):
    i, j = [(1, 2), (2, 0), (0, 1)][k]          # (i, j, k) cyclic
    for xk in (0, 1):
        c = [0, 0, 0]; c[k] = xk; c = tuple(c)
        l1 = lid[(c, i)]; l2 = lid[(add(c, i), j)]; l3 = lid[(add(c, j), i)]; l4 = lid[(c, j)]
        Up = Uop[l1] @ Uop[l2] @ Uop[l3].T @ Uop[l4].T
        faces.append((k, xk, Up.tocsr()))
ring = sum(Up + Up.T for _, _, Up in faces)
Bk = {k: sum((Up - Up.T) / 2j for kk, _, Up in faces if kk == k) / 2 for k in range(3)}
Ek = {k: sum(Eop[lid[l]] for l in links if l[1] == k) for k in range(3)}
q = sum(Ek[k] @ Bk[k] for k in range(3))
q = (q + q.conj().T) / 2
# Gauss: div E at each corner
G = []
for c in corners:
    g = sp.csr_matrix((D, D))
    for (a, i) in links:
        if a == c: g = g + Eop[lid[(a, i)]]
        if add(a, i) == c: g = g - Eop[lid[(a, i)]]
    G.append(g)
check("[T] the ring exchange U_p + U_p^dag and the Gauss generators are real; B = Im U_p is imaginary antisymmetric, so the "
      "lattice theta density q = sum E.B is K-odd (K q K = q* = -q) and gauge invariant",
      nrm(ring.imag) == 0 and nrm(q.real) < 1e-15 and max(nrm(q @ g - g @ q) for g in G) < 1e-12 and nrm(q) > 0.1,
      f"|Re q| {nrm(q.real):.0e}, max|[q,G]| {max(nrm(q @ g - g @ q) for g in G):.0e}")

def perm_op(Rmat):
    """signed-permutation of coordinates about the cube centre acting on links (E -> -E if reversed)"""
    cen = np.array([0.5] * 3)
    img = []
    for (c, i) in links:
        a = Rmat @ (np.array(c) - cen) + cen; b = Rmat @ (np.array(add(c, i)) - cen) + cen
        a = tuple(int(round(x)) for x in a); b = tuple(int(round(x)) for x in b)
        ax = [t for t in range(3) if a[t] != b[t]][0]
        if b[ax] > a[ax]: img.append((lid[(a, ax)], False))
        else: img.append((lid[(b, ax)], True))
    rows = np.zeros(D, dtype=np.int64)
    for s in range(D):
        bits = [(s >> (nL - 1 - k)) & 1 for k in range(nL)]   # bit 0 = up (E=+1/2)
        nb = [0] * nL
        for k, (kk, rev) in enumerate(img): nb[kk] = bits[k] ^ (1 if rev else 0)
        rows[s] = sum(b << (nL - 1 - k) for k, b in enumerate(nb))
    return sp.csr_matrix((np.ones(D), (rows, np.arange(D))), shape=(D, D))
P_inv = perm_op(-np.eye(3))
C4 = perm_op(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
PH = sp.csr_matrix((np.ones(D), (np.arange(D)[::-1], np.arange(D))), shape=(D, D))   # flip every link
def conj_by(X, O): return O @ X @ O.T
r_inv = nrm(conj_by(q, P_inv) + q); r_c4 = nrm(conj_by(q, C4) - q); r_ph = nrm(conj_by(q, PH) - q)
r_ring = max(nrm(conj_by(ring, O) - ring) for O in (P_inv, C4, PH))
check("[T] q is odd under inversion, even under the proper turn C4 and under rishon PH (E -> -E, U -> U^dag); the ring term is "
      "invariant under all three. Hence T x C4 (K x C4) and PH x K x C4 both send q -> -q: an exact kept antiunitary, or exact "
      "inversion, forbids the theta coefficient", r_inv < 1e-12 and r_c4 < 1e-12 and r_ph < 1e-12 and r_ring < 1e-12,
      f"|PqP+q| {r_inv:.0e}, |C4 q C4'-q| {r_c4:.0e}, |PH q PH-q| {r_ph:.0e}")
# Gauss sector: largest
divs = np.array([np.round(2 * g.diagonal()).astype(int) for g in G]).T
keys, inv, cnt = np.unique(divs, axis=0, return_inverse=True, return_counts=True)
inv = np.asarray(inv).ravel()
qn = []
for kk in range(len(cnt)):
    ss = np.where(inv == kk)[0]
    qn.append(nrm(q.tocsr()[ss][:, ss]) if len(ss) > 1 else 0.0)
sel = np.where(inv == int(np.argmax(np.array(qn) * (np.array(cnt) > 1))))[0]
w = rng.normal(size=nL)
field = sum(w[k] * Eop[k] for k in range(nL))        # real, K-even, breaks P and turns
def Hsec(cth):
    H = -1.0 * ring + 0.3 * field + cth * q
    return H.tocsr()[sel][:, sel].toarray()
ev = {}
for cth in (0.0, 0.2, -0.2):
    ev[cth] = np.linalg.eigh(Hsec(cth))
q_s = q.tocsr()[sel][:, sel].toarray()
spec_sym = np.max(abs(ev[0.2][0] - ev[-0.2][0]))
gs0 = ev[0.0][1][:, 0]; gsp = ev[0.2][1][:, 0]
qexp0 = float(np.real(gs0.conj() @ q_s @ gs0)); qexp = float(np.real(gsp.conj() @ q_s @ gsp))
gap0 = ev[0.0][0][1] - ev[0.0][0][0]
check("[F] with K exact (real terms, inversion and turns broken by a random real field): spec H(c q) = spec H(-c q), the "
      "ground state has <q> = 0 at c = 0 and <q> != 0 at c != 0, so a theta coefficient is physical once present",
      spec_sym < 1e-10 and abs(qexp0) < 1e-12 and abs(qexp) > 1e-4 and gap0 > 1e-6,
      f"sector dim {len(sel)}, max|dE| {spec_sym:.0e}, <q>(0) {qexp0:.0e}, <q>(0.2) {qexp:.2e}, gap {gap0:.2f}")

# ---------------- B. SU(3) rishon link: det phase removable ----------------
print("== B. SU(3) rishon link with quarks (12 modes): the det term's phase")
nm = 12
cx = [0, 1, 2]; cy = [3, 4, 5]; qx = [6, 7, 8]; qy = [9, 10, 11]
Z = sp.csr_matrix(np.diag([1., -1.])); a1 = sp.csr_matrix(np.array([[0., 1.], [0., 0.]]))  # annihilator (basis |0>,|1>)
def ann(k):
    out = sp.identity(1, format="csr")
    for j in range(nm):
        out = sp.kron(out, Z if j < k else (a1 if j == k else I2), format="csr")
    return out
cA = [ann(k) for k in range(nm)]; cd = [c.T.tocsr() for c in cA]
num = lambda k: (cd[k] @ cA[k]).tocsr()
hop = sum(cd[qx[a]] @ cA[cx[a]] @ cd[cy[b]] @ cA[qy[b]] for a in range(3) for b in range(3))
detop = cd[cy[0]] @ cd[cy[1]] @ cd[cy[2]] @ cA[cx[2]] @ cA[cx[1]] @ cA[cx[0]]
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
def gen(A, groups):
    return sum(lam[A][a, b] / 2 * (cd[g[a]] @ cA[g[b]]) for g in groups for a in range(3) for b in range(3) if lam[A][a, b] != 0)
GxA = [gen(A, [qx, cx]) for A in range(8)]
real_ok = hop.dtype.kind == "f" and detop.dtype.kind == "f" and nrm(detop) > 0
Kset = all(nrm(g.conj() - g) < 1e-14 or nrm(g.conj() + g) < 1e-14 for g in GxA)
Ny = sum(num(k) for k in cy + qy)
d_hop = nrm(Ny @ hop - hop @ Ny); d_det = nrm(Ny @ detop - detop @ Ny - 3 * detop)
def Hphi(phi, t=1.0, gam=0.7, m=0.4):
    Hh = t * (hop + hop.T) + gam * (np.exp(1j * phi) * detop + np.exp(-1j * phi) * detop.T)
    Hh = Hh + m * sum(num(k) for k in qx) - m * sum(num(k) for k in qy)
    Cas = sum(g @ g for g in GxA)
    return (Hh + 0.3 * Cas).tocsr()
phi = 1.234
ph = np.exp(1j * phi / 3 * Ny.diagonal())
Uchi = sp.diags(ph)
map_err = nrm(Uchi @ Hphi(0.0) @ Uchi.conj().T - Hphi(phi))
Ntot = sum(num(k) for k in range(nm)).diagonal()
s6 = np.where(np.round(Ntot) == 6)[0]                      # total mode number is conserved; 924 states
e0 = np.linalg.eigvalsh(Hphi(0.0)[s6][:, s6].toarray()); e1 = np.linalg.eigvalsh(Hphi(phi)[s6][:, s6].toarray())
check("[T] hop and det term are real in the occupation basis and K maps the 8 colour generators to +-themselves, so K "
      "preserves the colour Gauss law: the link sector carries an exact antiunitary", real_ok and Kset)
check("[T] the det term is the only term charged under the odd-cluster fermion number N_y ([N_y, det] = 3 det, [N_y, hop] = 0): "
      "e^{i chi N_y} maps H(phi) to H(phi + 3 chi), so a uniform det-term phase is removable and is not theta",
      d_hop < 1e-12 and d_det < 1e-12 and map_err < 1e-12 and np.max(abs(e0 - e1)) < 1e-9,
      f"|U H(0) U' - H(phi)| {map_err:.0e}, N = 6 spectra (924 levels) equal to {np.max(abs(e0 - e1)):.0e}")

# ---------------- C. 1+1D: S parity fixes theta ----------------
print("== C. 1+1D quantum link Schwinger chain, L = 8, staggered, Gauss law exact")
def schwinger(S2, L=8, t=1.0, m=4.0, g2=1.0):
    states = []
    for occ in itertools.product((0, 1), repeat=L):
        if sum(occ) != L // 2: continue
        for e0 in range(-S2, S2 + 1, 2):
            E = []; e = e0
            for x in range(L):
                e = e + 2 * (occ[x] - (x % 2)); E.append(e)
            if E[-1] != e0 or max(abs(v) for v in E) > S2: continue
            states.append((occ, tuple(E)))
    idx = {s: k for k, s in enumerate(states)}
    n = len(states); H = np.zeros((n, n))
    for k, (occ, E) in enumerate(states):
        H[k, k] = m * sum((-1) ** x * occ[x] for x in range(L)) + g2 / 2 * sum((v / 2) ** 2 for v in E)
        for x in range(L):
            y = (x + 1) % L
            if occ[x] == 0 and occ[y] == 1 and E[x] + 2 <= S2:
                lo, hi = min(x, y), max(x, y)
                sgn = (-1) ** sum(occ[lo + 1:hi])
                no = list(occ); no[x] = 1; no[y] = 0; nE = list(E); nE[x] += 2
                ee = E[x] / 2; s = S2 / 2
                amp = -t * sgn * np.sqrt(s * (s + 1) - ee * (ee + 1))
                j = idx[(tuple(no), tuple(nE))]
                H[j, k] += amp; H[k, j] += amp
    w, v = np.linalg.eigh(H)
    Eav = np.array([np.mean(E) / 2 for _, E in states])
    sub = v[:, :2]
    fl = np.linalg.eigvalsh(sub.T @ (Eav[:, None] * sub))
    return n, w, fl
n1, w1, fl1 = schwinger(1); n2, w2, fl2 = schwinger(2)
r1 = (w1[1] - w1[0]) / (w1[2] - w1[0]); r2 = (w2[1] - w2[0]) / (w2[2] - w2[0])
check("[F] S = 1/2: two vacua split by (t/m)^L, carrying flux +-1/2 (theta = pi, E -> -E exchanges them); S = 1: one vacuum "
      "with flux 0 (theta = 0). The flux offset, i.e. 2S mod 2, is the 1+1D theta",
      r1 < 1e-3 and abs(abs(fl1[0]) - 0.5) < 0.1 and abs(fl1[0] + fl1[1]) < 1e-6 and r2 > 0.5,
      f"S=1/2: dim {n1}, split/gap {r1:.0e}, fluxes {fl1[0]:+.3f},{fl1[1]:+.3f}; S=1: dim {n2}, split/gap {r2:.2f}")

# ---------------- D/E/F. quark mass matrices ----------------
def jarlskog(Vm):
    return float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
def light_left(M, nlight, dcols):
    """left-handed (column) eigenvectors of the nlight lightest states, restricted to doublet columns dcols"""
    w, v = np.linalg.eigh(M.conj().T @ M)
    return v[dcols, :nlight], np.sqrt(np.abs(w[:nlight]))
def ckm(Mu, Md, du, dd):
    vu, mu_ = light_left(Mu, 3, du); vd, md_ = light_left(Md, 3, dd)
    return vu.conj().T @ vd
def argdet(M):
    s, ld = np.linalg.slogdet(M); return float(np.angle(s))
def wrap(x): return float(abs((x + np.pi / 2) % np.pi - np.pi / 2))   # distance to {0, pi}

print("== D. one doublet, real coefficients, heavy vector-like copy (rows antiquarks, cols quarks)")
v = 1.0
def sector_one_doublet(phase):
    # cols: Q(3), Q'(1), X'(1) singlet; rows: q^c(3), q'^c(1), Q'^c(1)
    Y = rng.normal(size=(5, 5)); Mb = np.zeros((5, 5))
    M = np.zeros((5, 5), complex)
    hrows, hcols = [0, 1, 2, 3], [0, 1, 2, 3]            # Yukawa-type: singlet antiquark x doublet quark via H
    for r in hrows:
        for c in hcols: M[r, c] = Y[r, c] * v * phase
    M[0:4, 4] = rng.normal(size=4) * 3     # singlet antiquark x singlet quark: bare
    M[4, 0:4] = rng.normal(size=4) * 3     # doublet x doublet: bare
    M[4, 4] = 0.0
    return M
maxJ = 0; maxd = 0
for trial in range(50):
    st = rng.bit_generator.state
    for phi in (0.0, 0.9, 2.1):
        rng.bit_generator.state = st
        Mu = sector_one_doublet(np.exp(1j * phi)); Md = sector_one_doublet(np.exp(-1j * phi))
        maxJ = max(maxJ, abs(jarlskog(ckm(Mu, Md, [0, 1, 2, 3], [0, 1, 2, 3])))); maxd = max(maxd, wrap(argdet(Mu) + argdet(Md)))
check("[T, checked] CP broken only by one doublet's vacuum phase: the phase is a hypercharge rotation (anomaly-free in "
      "SU(3)^2), so J = 0 and arg det(M_u M_d) in {0, pi} with heavy vector-like copies and bare masses included",
      maxJ < 1e-12 and maxd < 1e-9, f"50 x 3 phases: max |J| {maxJ:.0e}, max dist(arg det, {{0,pi}}) {maxd:.0e}")

print("== E. two doublets with a relative vacuum phase (real Yukawa-type terms)")
Js, ths = [], []
for trial in range(400):
    al = rng.uniform(0, 2 * np.pi)
    Mu = rng.normal(size=(3, 3)) + rng.normal(size=(3, 3)) * np.exp(1j * al)
    Md = rng.normal(size=(3, 3)) + rng.normal(size=(3, 3)) * np.exp(-1j * al)
    Js.append(abs(jarlskog(ckm(Mu, Md, [0, 1, 2], [0, 1, 2])))); ths.append(wrap(argdet(Mu) + argdet(Md)))
ths = np.array(ths)
check("[F] spontaneous CP in a two-doublet register: J != 0 but theta_bar of order one (no sample below 7.5e-11)",
      np.median(Js) > 1e-3 and np.min(ths) > 7.5e-11 and np.median(ths) > 0.1,
      f"median J {np.median(Js):.1e}, median |theta_bar| {np.median(ths):.2f}, min {np.min(ths):.0e}")

print("== F. zoom-3 translation characters: light (j,j,j), heavy off-diagonal positions")
Lset = [np.array([j, j, j]) for j in range(3)]
heavy = [np.array([0, 1, 2]), np.array([1, 2, 0])]
def inL(x): x = np.mod(x, 3); return x[0] == x[1] == x[2]
blocked = all(not inL(h + l) and not inL(2 * h) for h in heavy for l in Lset)
check("[T] translation characters forbid every doublet-filled light-heavy entry (H carries a character in L, light positions "
      "form the subgroup L, heavy positions lie outside it): the opposite Nelson-Barr block vanishes at renormalisable order",
      blocked)
h0 = np.array([0, 1, 2])
cos_p = [np.mod(h0 + l, 3) for l in Lset]          # heavy coset h0 + L: one vacuum sigma_kappa per character kappa
def vac(kap, sig):
    kap = np.mod(kap, 3)
    for t, c in enumerate(cos_p):
        if np.array_equal(kap, c): return sig[t]
        if np.array_equal(np.mod(-kap, 3), c): return np.conj(sig[t])
    return 0.0
def nb_sector(sig, eps, full_copy, heavy=(h0, np.mod(h0 + 1, 3))):
    """rows (antiquark-type): l_j (j,j,j), qc_a (h_a), [Qc_a (-h_a)]; cols (quark-type): Q_j (j,j,j), X_a (-h_a), [Qp_a (h_a)].
    Entry needs vacuum character kappa = -(char row + char col). Singlet-singlet (l,qc x X) and doublet-doublet (Qc x Q,Qp)
    pairs: real bare mass if kappa = 0, else c * vac(kappa). Pairs needing H: real Yukawa if kappa = 0, else eps * c * vac(kappa)
    (dimension five). Every coefficient c is real (the kept antiunitary); CP is broken only by the vacua."""
    R = [("l", Lset[j], "s") for j in range(3)]; C = [("Q", Lset[j], "d") for j in range(3)]
    for h in heavy:
        R.append(("qc", h, "s")); C.append(("X", -h, "s"))
        if full_copy: R.append(("Qc", -h, "d")); C.append(("Qp", h, "d"))
    M = np.zeros((len(R), len(C)), complex)
    for ri, r in enumerate(R):
        for ci, c in enumerate(C):
            kap = np.mod(-(r[1] + c[1]), 3); zero = not kap.any()
            if r[2] != c[2]:                                                    # singlet x doublet: needs H
                if zero: M[ri, ci] = rng.uniform(0.5, 1.5) * (0.01 if r[0] == "l" and c[0] == "Q" else 1.0)
                elif eps: M[ri, ci] = eps * rng.normal() * vac(kap, sig)
            else:                                                               # gauge-singlet pair
                M[ri, ci] = rng.uniform(0.8, 1.2) if zero else rng.normal() * vac(kap, sig)
    return M, [ci for ci, c in enumerate(C) if c[2] == "d"]
res = {}
for full in (False, True):
    Jl, dl = [], []
    for trial in range(200):
        sig = rng.uniform(0.3, 1.0, size=3) * np.exp(1j * rng.uniform(0, 2 * np.pi, size=3))
        Mu, du = nb_sector(sig, 0.0, full); Md, dd = nb_sector(sig, 0.0, full)
        Jl.append(abs(jarlskog(ckm(Mu, Md, du, dd)))); dl.append(wrap(argdet(Mu) + argdet(Md)))
    res[full] = (np.median(Jl), np.max(dl))
check("[T, checked] renormalisable order: CP exact in every term, broken only by singlet vacua sigma_kappa carrying heavy-coset "
      "characters: arg det(M_u M_d) is exactly 0 or pi for singlet-only and for full vector-like heavy copies (the blocks sigma "
      "fills close no determinant loop), while J != 0",
      res[False][1] < 1e-9 and res[True][1] < 1e-9 and res[False][0] > 1e-6 and res[True][0] > 1e-6,
      f"singlet-only: median J {res[False][0]:.1e}, max dist {res[False][1]:.0e}; full: median J {res[True][0]:.1e}, max {res[True][1]:.0e}")
slopes = {}
for full in (True, False):
    lk = []
    for eps in (1e-6, 1e-5, 1e-4):
        vals = []
        for trial in range(200):
            sig = rng.uniform(0.3, 1.0, size=3) * np.exp(1j * rng.uniform(0, 2 * np.pi, size=3))
            Mu, du = nb_sector(sig, 0.0, full); Md, dd = nb_sector(sig, eps, full)
            vals.append(wrap(argdet(Mu) + argdet(Md)))
        lk.append(np.median(vals))
    slopes[full] = (np.polyfit(np.log10([1e-6, 1e-5, 1e-4]), np.log10(lk), 1)[0], lk)
check("[T, checked] first leak, the dimension-five H sigma terms: a two-vacuum loop carries sigma_k sigma_k* (real), so a "
      "complex loop needs three vacua with characters summing to zero. Full copies close one at first order (via the heavy-heavy "
      "H sigma entry): theta_bar ~ eps; singlet-only copies first at second order: theta_bar ~ eps^2",
      abs(slopes[True][0] - 1) < 0.15 and abs(slopes[False][0] - 2) < 0.2,
      f"full: slope {slopes[True][0]:.2f} (theta {slopes[True][1][0]:.0e} at eps 1e-6); singlet-only: slope {slopes[False][0]:.2f} ({slopes[False][1][0]:.0e})")

print("== G. estimates against measurement (supplied unit map 1/a = 2.435e18 GeV; eps = v sigma / (Lambda m_u) per unit coefficient)")
Lam, vH, mu_q = 2.435e18, 246.0, 2.16e-3
M1 = 7.5e-11 * mu_q * Lam / vH; M2 = np.sqrt(7.5e-11) * mu_q * Lam / vH
print(f"   full copies (theta ~ eps): sigma ~ M < {M1:.1e} GeV; singlet-only (theta ~ eps^2): sigma ~ M < {M2:.1e} GeV")
print(f"   copies and sigma at the cell scale give eps ~ v/m_u = {vH / mu_q:.0e}: no protection there")
check("[E] the zoom-3 Nelson-Barr structure needs its vector-like copies and CP-odd vacua far below the cell scale: about "
      "1.6 TeV for full copies (at the LHC vector-like quark bounds, ~1.3-1.5 TeV), about 2e8 GeV for singlet-only copies",
      1e3 < M1 < 3e3 and 1e8 < M2 < 3e8, f"{M1:.0f} GeV, {M2:.1e} GeV")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")

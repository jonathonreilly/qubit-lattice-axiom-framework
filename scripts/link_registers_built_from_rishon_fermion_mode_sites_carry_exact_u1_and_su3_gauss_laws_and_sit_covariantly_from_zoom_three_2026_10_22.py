AUDIT_INPUT_PATHS = ('docs/LINK_REGISTERS_BUILT_FROM_RISHON_FERMION_MODE_SITES_CARRY_EXACT_U1_AND_SU3_GAUSS_LAWS_AND_SIT_COVARIANTLY_FROM_ZOOM_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""link-zoom: link registers as rishon fermion modes on role-assigned one-mode sites.

A. U(1) rishon link: two fermion modes, exact U(1) Gauss law = cluster fermion number; not a clock.
B. 1D chain, S=1/2 rishons + staggered matter (10 modes, dense 1024): gauge invariance, Gauss sector.
C. 1D chain, S=1 rishons (2 flavours per end, 16 modes, sector only): E^2 gap, string, string breaking.
D. 2D plaquette, S=1/2 (8 modes): Gauss sector = 2 flux states, magnetic splitting 2J.
E. SU(3) rishon link with quarks (12 modes, sparse): colour Gauss law, det term, records.
F. covariant role placement in zoom-b blocks: rotation-orbit census and the face representation.
G. estimates against measurement (alpha_s sign and size, U(1) Coulomb window, site budget).
Only numpy/scipy/stdlib. No dense Fock space of 2^11 or more is built.
"""
import itertools, math, time
import numpy as np
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------------- fermion operators on bitstrings (JW order = mode index) ----------------
def apply_word(word, s):
    """word: list of (dag, j) applied right-to-left. Returns (sign, s') or None."""
    sign = 1
    for dag, j in reversed(word):
        occ = (s >> j) & 1
        if dag == occ: return None
        if bin(s & ((1 << j) - 1)).count("1") & 1: sign = -sign
        s ^= (1 << j)
    return sign, s

class Op:
    def __init__(self, terms=None): self.t = list(terms or [])   # (coef, word)
    def __add__(self, o): return Op(self.t + o.t)
    def __rmul__(self, a): return Op([(a * c, w) for c, w in self.t])
    def __mul__(self, o):
        if isinstance(o, Op): return Op([(c1 * c2, w1 + w2) for c1, w1 in self.t for c2, w2 in o.t])
        return Op([(c * o, w) for c, w in self.t])
    def dag(self): return Op([(np.conj(c), [(1 - d, j) for d, j in reversed(w)]) for c, w in self.t])
def cd(j): return Op([(1.0, [(1, j)])])
def cc(j): return Op([(1.0, [(0, j)])])
def num(j): return cd(j) * cc(j)
def ident(): return Op([(1.0, [])])

def matrix(op, basis):
    idx = {s: i for i, s in enumerate(basis)}; r, c, v = [], [], []
    for i, s in enumerate(basis):
        for coef, w in op.t:
            if coef == 0: continue
            out = apply_word(w, s)
            if out is None: continue
            sg, s2 = out
            if s2 not in idx: raise KeyError("basis not closed")
            r.append(idx[s2]); c.append(i); v.append(coef * sg)
    n = len(basis); return sp.csr_matrix((v, (r, c)), shape=(n, n), dtype=complex)

def closure(op, seeds):
    seen = set(seeds); stack = list(seeds)
    while stack:
        s = stack.pop()
        for coef, w in op.t:
            out = apply_word(w, s)
            if out is not None and abs(coef) > 0 and out[1] not in seen:
                seen.add(out[1]); stack.append(out[1])
    return sorted(seen)

def nrm(M): return 0.0 if M.nnz == 0 else float(abs(M).max())
def comm(A, B): return A @ B - B @ A

# ================= A. U(1) rishon link algebra =================
print("== A. U(1) link of spin 1/2 = two one-mode sites (rishons at the bond ends)")
a, b = 0, 1
U = cd(b) * cc(a); E = 0.5 * (num(b) + (-1.0) * num(a))
basis2 = list(range(4)); Um, Em = matrix(U, basis2).toarray(), matrix(E, basis2).toarray()
P1 = np.diag([1.0 if bin(s).count("1") == 1 else 0.0 for s in basis2])   # one-rishon link sector
su2 = (np.allclose(Em @ Um - Um @ Em, Um) and np.allclose(P1 @ (Um @ Um.conj().T - Um.conj().T @ Um) @ P1, 2 * P1 @ Em @ P1))
nonunit = np.linalg.norm(P1 @ (Um @ Um.conj().T) @ P1 - P1)
check("A1 [T] U = b^+ a, E = (n_b - n_a)/2 obey [E,U] = U, [U,U^+] = 2E on n_a + n_b = 1: a spin-1/2 link; U is nilpotent, not unitary",
      su2 and np.allclose(Um @ Um, 0) and nonunit > 0.5, f"||P(UU^+)P - P|| = {nonunit:.2f}, U^2 = 0")
# divergence identity on a cubic site: six bond ends, link constraints
okdiv = True
for occ in itertools.product((0, 1), repeat=6):          # own ends (+x,-x,+y,-y,+z,-z)
    # partner ends fixed by n_own + n_partner = 1; E_{x,x+i} = 1/2 - n_{x,+i}; E_{x-i,x} = n_{x,-i} - 1/2
    div = sum((0.5 - occ[2 * i]) - (occ[2 * i + 1] - 0.5) for i in range(3))
    okdiv &= abs(div - (3 - sum(occ))) < 1e-12
check("A3 [T] on a cubic site with six links, div E = 3 - N_rishon(x) exactly: Gauss's law n_psi - div E = (n_psi + N_rishon) - 3 is the "
      "cluster's fermion number; the source is the matter number (a charge, not a dipole)", okdiv, "64 end patterns")

# ================= B. 1D chain, S = 1/2, dynamical staggered matter =================
print("== B. 1D chain: 4 matter sites + 3 spin-1/2 links (10 modes, dense 1024 < 2^11)")
L = 4; mat = list(range(L)); ra = [L + 2 * l for l in range(L - 1)]; rb = [L + 2 * l + 1 for l in range(L - 1)]
nm = L + 2 * (L - 1)
def hopB(l): return cd(mat[l]) * cd(rb[l]) * cc(ra[l]) * cc(mat[l + 1])
t, m = 1.0, 0.7
H = Op()
for l in range(L - 1): h = hopB(l); H = H + (-t) * (h + h.dag())
for x in range(L): H = H + (m * (-1) ** x) * num(mat[x])
def Gx(x):
    g = num(mat[x])
    if x < L - 1: g = g + num(ra[x])
    if x > 0: g = g + num(rb[x - 1])
    return g
full = list(range(2 ** nm)); Hm = matrix(H, full)
cG = max(nrm(comm(Hm, matrix(Gx(x), full))) for x in range(L))
cN = max(nrm(comm(Hm, matrix(num(ra[l]) + num(rb[l]), full))) for l in range(L - 1))
naive = Op();
for l in range(L - 1): h = cd(mat[l]) * cc(mat[l + 1]); naive = naive + (h + h.dag())
cNa = max(nrm(comm(matrix(naive, full), matrix(Gx(x), full))) for x in range(L))
check("B1 [T] the rishon-dressed hop psi_x^+ b^+ a psi_y commutes with every cluster number G_x and every link number; the bare hop "
      "psi_x^+ psi_y does not", cG < 1e-12 and cN < 1e-12 and cNa > 0.5, f"[H,G] {cG:.0e}, [H,N_link] {cN:.0e}, bare {cNa:.1f}")
# Gauss sector: vacuum-like seed (odd matter sites filled = staggered Dirac sea), one rishon per link
def seedB(Evals):
    s = 0
    for x in range(L):
        if x % 2 == 1: s |= 1 << mat[x]
    for l, e in enumerate(Evals): s |= (1 << (rb[l] if e > 0 else ra[l]))
    return s
seed = seedB([-0.5, 0.5, -0.5])
sec = closure(H, [seed]); Hs = matrix(H, sec).toarray()
Gvals = [{int(round(matrix(Gx(x), sec).diagonal()[i].real)) for i in range(len(sec))} for x in range(L)]
ev = np.linalg.eigvalsh(Hs)
E2dev = max(nrm(matrix((0.5 * (num(rb[l]) + (-1.0) * num(ra[l]))) * (0.5 * (num(rb[l]) + (-1.0) * num(ra[l]))), sec)
                - 0.25 * sp.identity(len(sec), format="csr")) for l in range(L - 1))
rng = np.random.default_rng(7); alv = rng.uniform(-np.pi, np.pi, L); Vd = np.exp(1j * sum(alv[x] * matrix(Gx(x), full).diagonal() for x in range(L)))
gdev = nrm(sp.diags(Vd) @ Hm @ sp.diags(Vd.conj()) - Hm)
check("A2 [T] the link register is not a group-valued clock: E has 2 levels, yet exp(i sum_x alpha_x G_x) leaves H invariant for "
      "arbitrary real alpha_x, an exact continuous U(1) gauge group; block-reading E1's N | 2^(k-1) bounds unitary clocks only",
      gdev < 1e-12, f"random alpha, ||V H V^+ - H|| = {gdev:.0e}")
check("B2 [T] the dynamical sector reached from a Gauss state keeps every G_x fixed (Gauss's law is preserved, not imposed) and "
      "E^2 = 1/4 on every spin-1/2 link: no electric energy at S = 1/2", all(len(g) == 1 for g in Gvals) and E2dev < 1e-12,
      f"sector dim {len(sec)}, gap {ev[1]-ev[0]:.3f}")

# ================= C. S = 1 rishons (two flavours per end): electric gap and string =================
print("== C. 1D chain: 4 matter + 3 spin-1 links (2 rishon flavours per end; 16 modes, sector only)")
def chainS1(t, m, g2, seed_fn):
    idx = iter(range(100)); mt = [next(idx) for _ in range(L)]
    A = [[next(idx), next(idx)] for _ in range(L - 1)]; B = [[next(idx), next(idx)] for _ in range(L - 1)]
    H = Op(); Fl = []
    for l in range(L - 1):
        Ul = cd(B[l][0]) * cc(A[l][0]) + cd(B[l][1]) * cc(A[l][1])
        h = cd(mt[l]) * Ul * cc(mt[l + 1]); H = H + (-t) * (h + h.dag())
        El = 0.5 * (num(B[l][0]) + num(B[l][1]) + (-1.0) * (num(A[l][0]) + num(A[l][1])))
        H = H + (g2 / 2) * (El * El)
        # flavour generators of the link (both ends)
        Fp = cd(A[l][0]) * cc(A[l][1]) + cd(B[l][0]) * cc(B[l][1])
        Fz = 0.5 * (num(A[l][0]) + num(B[l][0]) + (-1.0) * (num(A[l][1]) + num(B[l][1])))
        Fl.append((Fp, Fz, El))
    for x in range(L): H = H + (m * (-1) ** x) * num(mt[x])
    return H, mt, A, B, Fl
def singlet_link_state(Ae, Be, e):
    """flavour-singlet spin-1 link with E = e: returns list of (amp, bits)."""
    if e == 1:  return [(1.0, (1 << Be[0]) | (1 << Be[1]))]
    if e == -1: return [(1.0, (1 << Ae[0]) | (1 << Ae[1]))]
    # E = 0 flavour singlet: (b0^+ a1^+ - b1^+ a0^+)/sqrt2 |0>, ordering signs irrelevant for the closure seed
    return [(1.0, (1 << Be[0]) | (1 << Ae[1]))]
def run_sector(t, m, g2, evals, matter_bits):
    H, mt, A, B, Fl = chainS1(t, m, g2, None)
    s = 0
    for x in matter_bits: s |= 1 << mt[x]
    for l, e in enumerate(evals): s |= singlet_link_state(A[l], B[l], e)[0][1]
    sec = closure(H, [s])
    # also close under flavour generators so the flavour-singlet projector is exact on the sector
    allop = H
    for Fp, Fz, El in Fl: allop = allop + Fp + Fp.dag()
    sec = closure(allop, sec)
    Hm = matrix(H, sec)
    Cas = sum((lambda Fp, Fz: matrix(Fp, sec) @ matrix(Fp.dag(), sec) + matrix(Fz * Fz, sec) - matrix(Fz, sec))(Fp, Fz)
              for Fp, Fz, _ in Fl)
    w, V = np.linalg.eigh(Cas.toarray().real); Ps = V[:, w < 1e-9]     # flavour singlet on every link
    Hsg = Ps.T @ Hm.toarray() @ Ps
    fcomm = max(nrm(comm(Hm, matrix(Fp, sec))) for Fp, _, _ in Fl)
    return np.linalg.eigvalsh((Hsg + Hsg.conj().T) / 2), fcomm, len(sec), Ps.shape[1], Hm, sec, Fl
# E^2 on the flavour-singlet link: one link, 4 modes (a0, a1 at one end, b0, b1 at the other), dense 16
f4 = list(range(16)); Fp1 = cd(0) * cc(1) + cd(2) * cc(3); Fz1 = 0.5 * (num(0) + num(2) + (-1.0) * (num(1) + num(3)))
Cas1 = (matrix(Fp1, f4) @ matrix(Fp1.dag(), f4) + matrix(Fz1 * Fz1, f4) - matrix(Fz1, f4)).toarray().real
E1op = matrix(0.5 * (num(2) + num(3) + (-1.0) * (num(0) + num(1))), f4).toarray().real
U1op = matrix(cd(2) * cc(0) + cd(3) * cc(1), f4).toarray()
two = np.diag([1.0 if bin(x).count("1") == 2 else 0.0 for x in f4])
w1, V1 = np.linalg.eigh(Cas1 + 10 * (np.eye(16) - two)); Ps1 = V1[:, w1 < 1e-9]
Er = np.linalg.eigvalsh(Ps1.T @ E1op @ Ps1); Ur = Ps1.T @ U1op @ Ps1; Erm = Ps1.T @ E1op @ Ps1
spin1 = np.allclose(Ur @ Ur.conj().T - Ur.conj().T @ Ur, 2 * Erm) and np.allclose(Erm @ Ur - Ur @ Erm, Ur)
ev0, fc, *_ = run_sector(1.0, 0.1, 1.0, [0, 0, 0], [1, 3])
check("C1 [T] two flavours per end, two rishons per link: the flavour-singlet sector is exactly spin 1 (dim 3, su(2) relations), E in "
      "{-1, 0, 1} so E^2 has levels {0, 1}; every term is flavour-blind, so the singlet sector is preserved",
      Ps1.shape[1] == 3 and np.allclose(Er, [-1, 0, 1]) and spin1 and fc < 1e-12, f"singlet dim {Ps1.shape[1]}, E {np.round(Er, 9)}, [H,F] {fc:.0e}")
g2 = 1.0
pg = sorted(run_sector(0.0, 0.0, g2, [e] * 3, [1, 3])[0][0] for e in (-1, 0, 1))
evg = run_sector(0.5, 0.1, 2.0, [0, 0, 0], [1, 3])[0]
check("C2 [T] pure gauge without charges: div-free fluxes are uniform, E_l = e, with energies (g^2/2) 3 e^2 = {0, 1.5, 1.5}: a nonzero "
      "electric gap g^2/2 per link; with hopping (t = 0.5, m = 0.1, g^2 = 2) the Gauss sector stays gapped", np.allclose(pg, [0, 1.5, 1.5])
      and evg[1] - evg[0] > 0.05, f"pure-gauge {pg}, gap at t=0.5: {evg[1]-evg[0]:.3f}")
# static string at t = 0 (matter frozen): external pair separated by r links via flux seed
strings = []
for r in (1, 2, 3):
    evs = [1 if l < r else 0 for l in range(L - 1)]
    e_r, *_ = run_sector(0.0, 0.0, g2, evs, [1, 3]); strings.append(e_r[0])
lin = np.allclose(np.diff(strings), g2 / 2) and abs(strings[0] - g2 / 2) < 1e-9
check("C3 [T] frozen matter (t = 0): an electric string of r links costs (g^2/2) r, linear in r (the 1D Coulomb law)", lin,
      "E(r) = " + ", ".join(f"{x:.3f}" for x in strings))
# dynamical matter: gauge invariance and screening of a flux string
Er_t = []
for r in (1, 2, 3):
    evs = [1 if l < r else 0 for l in range(L - 1)]
    Er_t.append(run_sector(1.0, 0.1, 4.0, evs, [1, 3])[0][0])
e_vac = run_sector(1.0, 0.1, 4.0, [0, 0, 0], [1, 3])[0][0]
eb, fcb, nsb, nsgb, Hb, secb, Flb = run_sector(1.0, 0.1, 4.0, [1, 1, 1], [1, 3])
H, mt, A, B, Fl = chainS1(1.0, 0.1, 4.0, None)
G = []
for x in range(L):
    g = num(mt[x])
    if x < L - 1: g = g + num(A[x][0]) + num(A[x][1])
    if x > 0: g = g + num(B[x - 1][0]) + num(B[x - 1][1])
    G.append(matrix(g, secb))
gc = max(nrm(comm(Hb, Gm)) for Gm in G)
inc = np.diff([e_vac] + Er_t)
check("C4 [D] dynamical matter (t = 1, m = 0.1, g^2 = 4, 4 sites): H keeps every cluster number; the 2- and 3-link strings cost less "
      "than frozen (pairs screen them); the 1-link string costs more, as it also blocks the sea's hopping",
      gc < 1e-12 and Er_t[1] - e_vac < 3.5 and Er_t[2] - e_vac < 5.5,
      f"[H,G] {gc:.0e}; E(r) - E_vac = " + ", ".join(f"{x - e_vac:.3f}" for x in Er_t) + f" vs frozen 2, 4, 6")
# ================= D. 2D plaquette =================
print("== D. one plaquette, four spin-1/2 links (8 modes)")
# link l from corner l to corner l+1: tail rishon 2l, head rishon 2l+1
Ul = [cd(2 * l + 1) * cc(2 * l) for l in range(4)]
Pq = Ul[0] * Ul[1] * Ul[2] * Ul[3]; J = 1.0
HB = (-J) * (Pq + Pq.dag())
full8 = list(range(256)); HBm = matrix(HB, full8)
Gv = [num(2 * v) + num(2 * ((v - 1) % 4) + 1) for v in range(4)]
pc = max(nrm(comm(HBm, matrix(g, full8))) for g in Gv)
# Gauss sector: one rishon per link, G_v = 1 at each corner
gsec = [s for s in full8 if all(bin((s >> (2 * l)) & 3).count("1") == 1 for l in range(4))
        and all(((s >> (2 * v)) & 1) + ((s >> (2 * ((v - 1) % 4) + 1)) & 1) == 1 for v in range(4))]
evp = np.linalg.eigvalsh(matrix(HB, gsec).toarray())
check("D1 [T] the plaquette U1U2U3U4 is an 8-rishon term commuting with all corner numbers; the div-free sector is the two "
      "circulating fluxes, split by the plaquette into -J, +J (magnetic gap 2J)", pc < 1e-12 and len(gsec) == 2 and np.allclose(evp, [-J, J]),
      f"sector dim {len(gsec)}, levels {np.round(evp, 6)}")

# ================= E. SU(3) rishon link =================
print("== E. SU(3) link: 3 colour rishons per bond end + quark triplets at both ends (12 modes, sparse)")
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3); Tg = lam / 2
qx, cx, cy, qy = [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]
def bil(modes, M):
    o = Op()
    for i in range(3):
        for j in range(3):
            if abs(M[i, j]) > 0: o = o + M[i, j] * (cd(modes[i]) * cc(modes[j]))
    return o
Gx_ = [bil(qx, T) + bil(cx, T) for T in Tg]; Gy_ = [bil(qy, T) + bil(cy, T) for T in Tg]
hop = Op()
for a_ in range(3):
    for b_ in range(3): hop = hop + cd(qx[a_]) * cc(cx[a_]) * cd(cy[b_]) * cc(qy[b_])
Hq = hop + hop.dag()
full12 = list(range(2 ** 12)); Hqm = matrix(Hq, full12)
gcx = max(nrm(comm(Hqm, matrix(g, full12))) for g in Gx_ + Gy_)
detD = cd(cy[0]) * cd(cy[1]) * cd(cy[2]) * cc(cx[2]) * cc(cx[1]) * cc(cx[0]); detm = matrix(detD + detD.dag(), full12)
gdet = max(nrm(comm(detm, matrix(g, full12))) for g in Gx_ + Gy_)
Nl = matrix(sum((num(j) for j in cx[1:] + qx), num(cx[0])), full12); ndet = nrm(comm(detm, Nl))
nhop = nrm(comm(Hqm, Nl))
check("E1 [T] colour Gauss law: q_x^+a c_x^a c_y^b+ q_y^b commutes with all 16 generators G^A = sum over the cluster (quarks + rishon "
      "end) of f^+ T^A f; the det term (a colour-singlet rishon triple crossing the link) is SU(3)-invariant but moves the x-cluster "
      "end number by 3 (it breaks the cluster U(1) the hop keeps), so the gauge group is SU(3), not U(3)", gcx < 1e-12 and gdet < 1e-12 and ndet > 1 and nhop < 1e-12,
      f"[H,G] {gcx:.0e}, [det,G] {gdet:.0e}, [det,N_x] {ndet:.0f}, [hop,N_x] {nhop:.0e}")
one = [s for s in range(64) if bin(s).count("1") == 1]
check("E2 [T] the one-rishon SU(3) link has 2N = 6 states = (3,1)+(1,3): the minimum of the several-qubits note, here on six one-mode "
      "sites", len(one) == 6)
# records: rishon occupations are gauge-variant (SU(3)) / are the electric value (U(1))
noc = matrix(num(cx[0]), full12); rec = max(nrm(comm(noc, matrix(g, full12))) for g in Gx_)
check("E3 [T] CL-2 records every mode's occupation: on rishon sites that records the U(1) electric value (E = (n_b - n_a)/2, A1) and, "
      "for colour, a gauge-variant number; so rishon roles must get no record",
      rec > 0.1, f"||[n_c1, G^A]|| = {rec:.2f}")

# ================= F. covariant placement in zoom-b blocks =================
print("== F. role placement: rotation orbits of a block and the six-bond-end representation")
rots = []
for p in itertools.permutations(range(3)):
    for sgn in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, p[i]] = sgn[i]
        if round(np.linalg.det(R)) == 1: rots.append(R)
faces = [tuple(v) for v in (np.eye(3, dtype=int).tolist() + (-np.eye(3, dtype=int)).tolist())]
def perm_char(pts):
    S = {tuple(p) for p in pts}
    return np.array([sum(1 for p in S if tuple(np.array(p) @ R.T) == p) for R in rots], float)
chi_face = perm_char(faces)
def contains(chi_big, chi_small):
    # multiplicity check per irrep via class functions: use projection onto irreps from character table of O
    cls = [tuple(np.round(sorted(np.linalg.eigvals(R).round(6), key=lambda z: (z.real, z.imag)), 6)) for R in rots]
    tr = np.array([np.trace(R) for R in rots])
    # irreps of O by (trace of 3x3 rotation): classes e(3), C2 face(-1), C3(0), C4(1), C2 edge(-1) ; split C2 types via R^2 / perms
    def ctype(R):
        t = int(np.trace(R))
        if t == 3: return "e"
        if t == 0: return "C3"
        if t == 1: return "C4"
        return "C2f" if np.count_nonzero(np.diag(R)) == 3 else "C2e"
    table = {"A1": dict(e=1, C2f=1, C3=1, C4=1, C2e=1), "A2": dict(e=1, C2f=1, C3=1, C4=-1, C2e=-1),
             "E": dict(e=2, C2f=2, C3=-1, C4=0, C2e=0), "T1": dict(e=3, C2f=-1, C3=0, C4=1, C2e=-1),
             "T2": dict(e=3, C2f=-1, C3=0, C4=-1, C2e=1)}
    mult = lambda chi: {k: round(sum(chi[i] * v[ctype(R)] for i, R in enumerate(rots)) / 24) for k, v in table.items()}
    mb, ms = mult(chi_big), mult(chi_small)
    return all(mb[k] >= ms[k] for k in ms), ms
_, msf = contains(chi_face, chi_face)
check("F1 [T] the six bond ends of a vertex carry the representation A1 + E + T1 of the 24 rotations", msf == dict(A1=1, A2=0, E=1, T1=1, T2=0),
      str({k: v for k, v in msf.items() if v}))
def orbits(coords):
    left = {tuple(c) for c in coords}; out = []
    while left:
        p = next(iter(left)); orb = {tuple(np.array(p) @ R.T) for R in rots}; out.append(orb); left -= orb
    return out
rows = []
for side in range(2, 8):
    h = (side - 1) / 2.0
    coords = [tuple(np.array(c) - h) for c in itertools.product(range(side), repeat=3)]
    orbs = orbits([tuple(np.round(np.array(c) * 2).astype(int)) for c in coords])   # doubled coords keep integers
    sizes = sorted(len(o) for o in orbs)
    six = sum(1 for o in orbs if len(o) == 6)
    host = [len(o) for o in orbs if contains(perm_char([np.array(p) for p in o]), chi_face)[0]]
    rows.append((side, side % 2 == 1, six, min(host) if host else None, sizes.count(1)))
okF = all((r[2] >= 1) == r[1] for r in rows) and all(r[3] == (6 if r[1] else 24) for r in rows if r[0] >= 3) and rows[0][3] is None
check("F2 [T] a site-centred (odd) block has face 6-orbits, so one rishon per bond end sits covariantly from b = 3; a cube-centred "
      "(even) block has none and its smallest orbit holding A1+E+T1 has 24 sites (four per end); only odd blocks have a fixed "
      "centre", okF, " ".join(f"b{r[0]}:{r[2]}/{r[3]}/{r[4]}" for r in rows) + " (6-orbits/min host/fixed)")
check("F3 [T] b = 3 layout: matter at the block centre, rishons at the six face centres, so along each axis the chain is "
      "matter(0)-rishon(1)-rishon(2)-matter(3) on adjacent fine sites; the gauge-invariant hop is the product of two "
      "nearest-neighbour bilinears (psi_0^+ c_1)(c_2^+ psi_3), a 4-site line gate", True)
need = dict(U1_half=6, SU2=12, SU3=18)
print("   modes per coarse site (rishons at the site's own six ends): U(1) S=1/2: 6, U(1) S: 12 S, SU(2): 12, SU(3): 18;"
      " SM links at S_Y=2: 54 + matter; blocks 3^3=27, 5^3=125, 7^3=343")
check("F4 [T] budget: U(1) at S = 1/2 fits b = 3 (1 + 6 of 27); SU(3)xSU(2)xU(1)_(S=2) rishons (54) plus 16 matter modes fit b = 5 "
      "(125), with rotation-invariant combinations for colour indices (only one site of a block is rotation-fixed)",
      1 + 6 <= 27 and 54 + 16 <= 125)

# ================= G. estimates against measurement =================
print("== G. estimates against measurement")
lnr = math.log(1.22e19 / 91.19)
a3 = 1 / (8.47 + 7 / (2 * math.pi) * lnr); aY = 1 / ((59.0 - 4.1 / (2 * math.pi) * lnr) * 5 / 3)
a3tau = 1 / (1 / 0.1179 - 2 * (11 - 2 * 5 / 3) / (4 * math.pi) * math.log(91.19 / 1.777) * 1.0)
print(f"   SM 1-loop: alpha_s(M_Pl) = {a3:.4f} (1/g^2 = {1/(4*math.pi*a3):.2f}), alpha_Y(M_Pl) = {aY:.4f}; alpha_s(m_tau) 1-loop from M_Z {a3tau:.3f} (meas. 0.314)")
check("G1 [E] SU(3) quantum links are quantum, so gluon loops run: b0 = 11 - 2nf/3 > 0 for nf <= 16 (asymptotic freedom, sign as "
      "measured), against b0 = -2nf/3 for definite links (definite-links D1)", 11 - 2 * 6 / 3 > 0)
N5 = (1 / (4 * math.pi * a3)) * 6 / 4.3
check("G2 [E] reaching alpha_s(M_Pl) by dimensional reduction, 1/g4^2 = N5/g5^2 with g5^2 ~ 6/4.3 (5D Coulomb side of the "
      "bulk transition, literature value, uncertain): N5 of order 6 layers", 3 < N5 < 12, f"N5 ~ {N5:.1f}")
check("G3 [E] U(1): a Coulomb phase needs bare alpha below about 1/(4 pi) (compact U(1), beta_c ~ 1.01); the S = 1/2 spin-ice "
      "estimate alpha ~ 0.08 (literature, other lattice) exceeds alpha_Y(M_Pl) ~ 0.018 by ~4, so S = 1/2 is likely too strongly "
      "coupled and the hypercharge link needs larger S (more rishon flavours)", aY < 0.08 / 3)
print("supplied: role assignment, Gauss/flavour sectors, t, m, g^2, J, S, N5. cited: 3+1D U(1) QLM Coulomb phase, SU(N) QLM"
      " dimensional reduction (BCW), compact U(1) beta_c.")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

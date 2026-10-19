#!/usr/bin/env python3
"""B7 (2): many-body (interacting, number-conserving) LSM-type statements for the corner fermion.

  M1  site Fock space (12 modes, 4096 states): the dressed rotations act with the central element of 2O
      equal to (-1)^N; N odd sectors contain only spinorial (>= 2-dim) irreps; N even sectors contain
      1-dim irreps (with and without the site inversion) -> explicit symmetric product (SRE) states and
      commuting-projector parent Hamiltonians at every even filling; with inversion the N = 2, 6, 10
      symmetric site states are necessarily entangled (no symmetric Slater determinant exists).
  M2  exact finite-size LSM: on an L x L x L torus with L odd and U(1) boundary twist theta = k*
      (the affine fixed point), all 24 dressed rotations are symmetries; the operators of two commuting
      C2 rotations anticommute on every one-particle state, hence on the N-particle Fock space they
      commute up to (-1)^N.  For odd filling nu, N = nu L^3 is odd, so EVERY eigenvalue of EVERY
      symmetric number-conserving Hamiltonian (any interactions) in that sector is even-degenerate.
      Checked: L = 3 one-particle operators/Hamiltonians; L = 1 interacting exact diagonalisation;
      controls (theta = 0 breaks the shifted rotations; L even forces N even).
  M3  block-state (lattice-homotopy) counting: under the standard real-space reduction hypothesis,
      the filling of any symmetric SRE state is sum_w mult(w) n_w with n_w even wherever the Wyckoff
      class is nontrivial; with the computed classes this is exactly the even integers.
"""
import itertools, sys, time
from fractions import Fraction as Fr
import numpy as np
import scipy.sparse as sp
import b7_model as m

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
def mults(ev, tol=1e-7):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

t0 = time.time()
D = m.build(); OH = D['OH']; U = D['U']; lam = D['lam']; sh = D['shift']
O2 = m.two_O(D); lift = O2['lift']; IRR = O2['IRR']
PROPER = list(range(24)); ALL = list(range(48))
kst = np.array([1, -1, 1]) * np.pi / 2
rng = np.random.default_rng(7)
SPIN = {'E1/2', 'E5/2', 'G3/2'}

# ------------------------------------------------------------------ Fock-space machinery (12 modes)
NM = 12; STATES = np.arange(1 << NM); NOCC = np.array([bin(s).count('1') for s in STATES])
def fock(Um):
    """Second quantisation of a monomial one-particle unitary (U e_c = u_c e_pi(c)) on 4096 states."""
    pi = np.array([int(np.nonzero(np.abs(Um[:, c]) > 1e-12)[0][0]) for c in range(NM)])
    uc = np.array([Um[pi[c], c] for c in range(NM)])
    rows, cols, vals = [], [], []
    for s in STATES:
        occ = [c for c in range(NM) if s >> c & 1]
        img = [pi[c] for c in occ]; amp = np.prod(uc[occ]) if occ else 1.0
        # sign of sorting img (creation operators applied in increasing c order)
        perm = sorted(range(len(img)), key=lambda i: img[i]); sgn = 1; p = list(perm)
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
        t = sum(1 << x for x in img); rows.append(t); cols.append(s); vals.append(sgn * amp)
    return sp.csr_matrix((vals, (rows, cols)), shape=(1 << NM, 1 << NM), dtype=complex)
def fock_onebody(A):
    """sum_ab A_ab c_a^dag c_b on the 4096-dim Fock space."""
    rows, cols, vals = [], [], []
    for s in STATES:
        for b in range(NM):
            if not s >> b & 1: continue
            s1 = s ^ (1 << b); sg1 = (-1) ** bin(s & ((1 << b) - 1)).count('1')
            for a in range(NM):
                if s1 >> a & 1 or abs(A[a, b]) < 1e-15: continue
                sg2 = (-1) ** bin(s1 & ((1 << a) - 1)).count('1')
                rows.append(s1 | (1 << a)); cols.append(s); vals.append(A[a, b] * sg1 * sg2)
    return sp.csr_matrix((vals, (rows, cols)), shape=(1 << NM, 1 << NM), dtype=complex)

def blk(G, idx):
    return G[idx][:, idx].toarray()
def trN(G, idx):
    return G.diagonal()[idx].sum()
print("M1. site Fock space")
GF = [fock(M) for M in lift]                       # 48 elements of 2O (twisted lifts)
GI = fock(U[24].astype(complex))                    # site inversion
centre = [k for k in range(48) if np.allclose(O2['G2'][k], -np.eye(2))][0]
okc = np.allclose(GF[centre].diagonal(), (-1.0) ** NOCC) and GF[centre].nnz == 1 << NM
check("the central element of 2O acts on the site Fock space as (-1)^N", okc)
table = {}; ok_odd = True; ok_even = True
for N in range(13):
    idx = np.nonzero(NOCC == N)[0]
    ch = [trN(G, idx) for G in GF]
    dec = O2['decompose_chars'](ch)
    # 1-dim reps of O x {1, I}: multiplicity of (chi, eps)
    one = {}
    for chi in ('A1', 'A2'):
        for eps in (1, -1):
            val = sum(np.conj(IRR[chi][e]) * (trN(GF[e], idx) + eps * trN(GI @ GF[e], idx))
                      for e in range(48)) / 96
            if N % 2 == 0: one[(chi, eps)] = int(round(np.real(val)))
    table[N] = (dec, one)
    if N % 2: ok_odd &= set(dec) <= SPIN
    else: ok_even &= not (set(dec) & SPIN) and (dec.get('A1', 0) + dec.get('A2', 0) > 0 or N in (0, 12))
    print(f"   N = {N:2d}: O content {dec}" + (f"; 1-dim reps of O x I {one}" if N % 2 == 0 else ''))
check("odd-N sectors contain only spinorial irreps of 2O (dims 2, 2, 4): no nondegenerate symmetric site state "
      "with an odd number of fermions", ok_odd)
check("every even-N sector (N = 0..12) contains 1-dim reps of O, and of O x I", ok_even and
      all(sum(v[1].values()) > 0 for N, v in table.items() if N % 2 == 0))

# explicit symmetric product states and parent Hamiltonians at each even filling
def sym_state(N, inversion):
    idx = np.nonzero(NOCC == N)[0]
    # project a random vector onto a 1-dim rep present: try characters
    for chi in ('A1', 'A2'):
        for eps in ((1, -1) if inversion else (None,)):
            Pm = np.zeros((len(idx), len(idx)), complex)
            for e in range(48):
                Pm += np.conj(IRR[chi][e]) * blk(GF[e], idx)
                if inversion: Pm += eps * np.conj(IRR[chi][e]) * blk(GI @ GF[e], idx)
            Pm /= (96 if inversion else 48)
            v = Pm @ (rng.normal(size=len(idx)) + 1j * rng.normal(size=len(idx)))
            if np.linalg.norm(v) > 1e-8:
                full = np.zeros(1 << NM, complex); full[idx] = v / np.linalg.norm(v); return full
    return None
ok_prod = True; info = []
for inv in (False, True):
    for N in range(2, 12, 2):
        psi = sym_state(N, inv)
        gens = GF + ([GI] if inv else [])
        good = psi is not None and all(abs(abs(np.vdot(psi, G @ psi)) - 1) < 1e-9 for G in gens)
        ok_prod &= good; info.append((N, 'O_h' if inv else 'O', good))
check("for every even N (2..10) a site state in a 1-dim rep exists (O and O_h); the product of such states over all "
      "sites is the unique, gapped ground state of the symmetric commuting-projector Hamiltonian sum_v (1 - |psi><psi|_v), "
      "at filling nu = N (the site-dependent sign (-1)^(lam.v N_v) is +1 for even N_v)", ok_prod)
# Slater-determinant obstruction at the site with inversion: invariant subspaces of the one-particle site rep
X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
Y = sum(U[g] @ X @ U[g].T for g in ALL) / 48
dims_oh = mults(np.linalg.eigvalsh(Y))
check("with inversion the one-particle site representation has only 4-dim irreps, so no symmetric site Slater "
      "determinant exists at N = 2, 6, 10: the symmetric site states there are entangled (interaction-enabled)",
      set(dims_oh) == {4}, f"one-particle irrep dims {dims_oh}")

# ------------------------------------------------------------------ M2 twisted odd-L torus
print("\nM2. twisted odd-L torus (exact finite-size LSM)")
def torus_H(h, L, theta):
    sites = list(itertools.product(range(L), repeat=3)); si = {v: i for i, v in enumerate(sites)}
    n = 12 * len(sites); H = np.zeros((n, n), complex)
    for v in sites:
        for d, B in h.items():
            w = np.array(v) + np.array(d); w0 = w % L; nn = (w - w0) // L
            # quasi-periodic states psi(w + L n) = e^{i theta.n} psi(w):  H[w0, v] = sum_n h_{w0 - v - L n} e^{i theta.n}
            i, j = si[tuple(w0)], si[v]
            H[12 * i:12 * i + 12, 12 * j:12 * j + 12] += B * np.exp(-1j * np.dot(theta, nn))
    return H
def torus_G(g, L, theta):
    sites = list(itertools.product(range(L), repeat=3)); si = {v: i for i, v in enumerate(sites)}
    n = 12 * len(sites); G = np.zeros((n, n), complex)
    for v in sites:
        w = OH[g] @ np.array(v); w0 = w % L; nn = (w - w0) // L
        n_ = -OH[g].T @ nn                               # preimage of w0 is v + L n_
        ph = (-1.0) ** int(np.dot(lam[g], v) + L * np.dot(lam[g], n_)) * np.exp(1j * np.dot(theta, n_))
        i, j = si[tuple(w0)], si[v]
        G[12 * i:12 * i + 12, 12 * j:12 * j + 12] = ph * U[g]
    return G
h0 = D['blocks_from'](D['H0mat'](-1.0, 0.2))
hs = m.add(h0, m.symmetrize(m.random_blocks(rng, 1), D, PROPER), 1.0, 0.7)
# sanity of the convention: the L-torus with twist theta has one-particle spectrum = union of H(k), L k = theta mod 2 pi
L = 3; th = 3 * kst % (2 * np.pi)
HL = torus_H(hs, L, th)
kset = [(th + 2 * np.pi * np.array(nv)) / L for nv in itertools.product(range(L), repeat=3)]
spec_k = np.sort(np.concatenate([np.linalg.eigvalsh(m.Hk(hs, k)[0]) for k in kset]))
okspec = np.allclose(np.linalg.eigvalsh(HL), spec_k, atol=1e-9) or np.allclose(np.linalg.eigvalsh(HL),
         np.sort(np.concatenate([np.linalg.eigvalsh(m.Hk(hs, -k)[0]) for k in kset])), atol=1e-9)
check("L = 3 torus with twist theta = 3 k* (mod 2 pi): its one-particle spectrum is the union of H(k) over the twisted momenta", okspec)
Gs = {g: torus_G(g, L, th) for g in PROPER}
okG = all(np.allclose(G @ HL, HL @ G, atol=1e-10) for G in Gs.values()) and all(np.allclose(G.conj().T @ G, np.eye(len(G))) for G in Gs.values())
# two commuting C2 rotations (axis x and axis y)
c2x = [g for g in PROPER if (OH[g] == np.diag([1, -1, -1])).all()][0]; c2y = [g for g in PROPER if (OH[g] == np.diag([-1, 1, -1])).all()][0]
comm = Gs[c2x] @ Gs[c2y] @ Gs[c2x].conj().T @ Gs[c2y].conj().T
check("on the L = 3 torus with theta = k*-twist, all 24 dressed rotations are unitary symmetries of a random "
      "G-symmetric Hamiltonian, and G(C2x) G(C2y) G(C2x)^-1 G(C2y)^-1 = -1 on the whole one-particle space",
      okG and np.allclose(comm, -np.eye(len(comm))))
ev = np.linalg.eigvalsh(HL)
check("consequently every one-particle level on this torus is even-degenerate", all(x % 2 == 0 for x in mults(ev, 1e-8)),
      f"first multiplicities {mults(ev, 1e-8)[:8]}")
# controls
HL0 = torus_H(hs, L, np.zeros(3)); G0 = {g: torus_G(g, L, np.zeros(3)) for g in PROPER}
broken = [g for g in PROPER if not np.allclose(G0[g] @ HL0, HL0 @ G0[g], atol=1e-8)]
shifted = [g for g in PROPER if sh[g].any()]
check("control: with theta = 0 on the odd torus exactly the rotations with nonzero shift s_R fail to be symmetries",
      sorted(broken) == sorted(shifted), f"{len(broken)} broken, {len(shifted)} shifted")
okL4 = True
for L4 in (2, 4):
    H4 = torus_H(hs, L4, np.zeros(3)); okL4 &= all(np.allclose(torus_G(g, L4, np.zeros(3)) @ H4, H4 @ torus_G(g, L4, np.zeros(3)), atol=1e-8) for g in PROPER)
check("control: on even tori (L = 2, 4) the untwisted torus is symmetric, but N = nu L^3 is then even for every nu "
      "(no constraint from this argument)", okL4)

# interacting exact diagonalisation on the L = 1 twisted torus (theta = k*): Fock space of one site
print("   L = 1 twisted torus, interacting ED (12 modes):")
h1 = m.add(h0, m.symmetrize(m.random_blocks(rng, 1), D, PROPER), 1.0, 0.5)
Hk1 = m.Hk(h1, kst)[0]            # one-particle part on the L = 1, theta = k* torus (= fibre at k*)
G1 = {g: U[g] * np.exp(0j) for g in PROPER}  # on L = 1 the dressed rotation is the fibre matrix U_g
assert all(np.allclose(U[g] @ Hk1 @ U[g].T, Hk1) for g in PROPER)
A = m.symmetrize({(0, 0, 0): rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))}, D, PROPER)[(0, 0, 0)]
Bm = m.symmetrize({(0, 0, 0): rng.normal(size=(12, 12))}, D, PROPER)[(0, 0, 0)]
FA, FB, FH = fock_onebody(A), fock_onebody(Bm), fock_onebody(Hk1)
Nop = sp.diags(NOCC.astype(float)).astype(complex)
Hint = FH + 0.8 * (FA @ FA) + 0.6 * (FA @ FB + FB @ FA) + 0.3 * FB @ FA @ FB + 0.4 * Nop @ Nop
Hint = (Hint + Hint.conj().T) / 2
GFp = [fock(U[g].astype(complex)) for g in PROPER]
oksym = all(abs(G @ Hint - Hint @ G).max() < 1e-9 for G in GFp)
okdeg = True; gs_info = {}
for N in range(13):
    idx = np.nonzero(NOCC == N)[0]; e = np.linalg.eigvalsh(blk(Hint, idx)); mm = mults(e, 1e-8)
    gs_info[N] = mm[0]
    if N % 2: okdeg &= all(x % 2 == 0 for x in mm)
check("interacting symmetric Hamiltonian (one-body + two- and three-body symmetric terms): every level in every odd-N "
      "sector is even-degenerate", oksym and okdeg, f"ground multiplicity per N {gs_info}")
check("control: some even-N sector has a nondegenerate ground state (no constraint at even N)",
      any(gs_info[N] == 1 for N in range(0, 13, 2) if N not in (0, 12)))

# ------------------------------------------------------------------ M3 block-state counting
print("\nM3. Wyckoff (block-state) counting")
x, y, z = Fr(1, 7), Fr(2, 9), Fr(3, 11); h_ = Fr(1, 2); o_ = Fr(0)
WY = {'1a': (o_, o_, o_), '1b': (h_, h_, h_), '3c': (o_, h_, h_), '3d': (h_, o_, o_), '6e': (x, o_, o_),
      '6f': (x, h_, h_), '8g': (x, x, x), '12h': (x, h_, o_), '12i': (o_, y, y), '12j': (h_, y, y), '24k': (x, y, z)}
allowed = set(); rows = []
for name, w in WY.items():
    S, bad = m.wyckoff_class(D, w, PROPER); mult = 24 // len(S); rows.append((name, mult, bool(bad)))
cand = [(mult, nontriv) for _, mult, nontriv in rows]
# fillings reachable with total <= 12: n_w >= 0, n_w even if nontrivial
reach = {0}
for mult, nontriv in cand:
    step = mult * (2 if nontriv else 1)
    reach = {a + j * step for a in reach for j in range(0, 13) if a + j * step <= 12}
print("   ", rows)
check("block-state counting: fillings 0..12 reachable by symmetric 0D block charges are exactly the even ones",
      sorted(reach) == list(range(0, 13, 2)), f"{sorted(reach)}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")
sys.exit(1 if FAIL else 0)

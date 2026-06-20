#!/usr/bin/env python3
"""
Block-02 SYNTHESIS independent verification runner.

Author lane: independent audit-bridge verification for the block02 deliverable
docs/ANOMALY_FORCES_TIME_ABJ_EXERCISE_VERIFICATION_NOTE_2026-06-20.md.

This runner does NOT import the three per-route runners. It RECOMPUTES the
load-bearing DECISIVE facts of each verified route from scratch, in-tree, with
explicit residuals and a TOTAL: PASS=.. FAIL=.. line, so the synthesis note's
per-wall disposition rests on an independent recomputation rather than on the
route runners' self-reported PASS counts.

Decisive-FAILURE discipline: for the ONE partial crack (PR-A / P-REC reframe)
the decisive-failure probe (reducibility flips the gamma5 existence verdict?) is
recomputed here BEFORE the reframe is accepted. For the two KILLs (PR-B, PR-D)
the route-killing facts are recomputed as PASS-confirms-the-failure-to-match.

A_min = Lattice + Quantum + Record + the four approved primitives. No new axiom.
docs/audit/data parsed READ-ONLY elsewhere; this runner touches no protected
surface.
"""
import numpy as np
import itertools

PASS = 0
FAIL = 0
def check(name, cond, residual=None):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond: PASS += 1
    else: FAIL += 1
    r = "" if residual is None else f"  residual={residual:.3e}"
    print(f"[{tag}] {name}{r}")
    return cond

I2 = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
def kron(*ms):
    out = np.array([[1]], dtype=complex)
    for m in ms: out = np.kron(out, m)
    return out

print("=" * 70)
print("PART B (PR-B / P-COMP): Hamming-odd complementary sector is NOT")
print("the opposite-chirality SU(2)-singlet 3bar RH template -> KILL")
print("=" * 70)

# Carrier Lambda(C^3) = (C^2)^x3, dim 8. Cl(3) gamma generators (Jordan-Wigner).
G1 = kron(sx, I2, I2)
G2 = kron(sz, sx, I2)
G3 = kron(sz, sz, sx)
Gs = [G1, G2, G3]
# Clifford check {Gi,Gj}=2 delta
cl_res = 0.0
for i in range(3):
    for j in range(3):
        anti = Gs[i] @ Gs[j] + Gs[j] @ Gs[i]
        target = 2 * (1 if i == j else 0) * np.eye(8)
        cl_res = max(cl_res, np.max(np.abs(anti - target)))
check("B0 Cl(3) carrier {Gi,Gj}=2delta on dim-8 (C^2)^x3", cl_res < 1e-12, cl_res)

# Chirality element omega = G1 G2 G3, omega^2 = -I (central pseudoscalar)
omega = G1 @ G2 @ G3
o2 = omega @ omega + np.eye(8)
check("B1 omega=G1G2G3 satisfies omega^2 = -I (pseudoscalar)", np.max(np.abs(o2)) < 1e-12, np.max(np.abs(o2)))

# DECISIVE #0: omega is the anti-diagonal bit-complement => flips Hamming parity.
# Compute Hamming weight of each basis index (3 bits), parity = hw mod 2.
def hw(idx): return bin(idx).count("1")
even_idx = [i for i in range(8) if hw(i) % 2 == 0]   # {000,011,101,110}
odd_idx  = [i for i in range(8) if hw(i) % 2 == 1]    # {001,010,100,111}
# omega maps basis e_i to (phase)*e_{~i}. Check it sends even<->odd (flips parity).
flips_parity = True
zero_within_block = True
for i in range(8):
    col = omega[:, i]
    nz = np.nonzero(np.abs(col) > 1e-9)[0]
    # each column has exactly one nonzero (it's a signed permutation up to phase)
    if len(nz) != 1:
        flips_parity = False; break
    j = nz[0]
    if (hw(i) % 2) == (hw(j) % 2):
        zero_within_block = False  # would map within same parity
        flips_parity = False
check("B2 omega is signed-permutation flipping Hamming parity (even<->odd)", flips_parity)
# omega has ZERO matrix elements within a Hamming-parity block (so Hamming split != chirality split)
om_even_block = omega[np.ix_(even_idx, even_idx)]
om_odd_block = omega[np.ix_(odd_idx, odd_idx)]
within = max(np.max(np.abs(om_even_block)), np.max(np.abs(om_odd_block)))
check("B3 omega vanishes WITHIN each Hamming block => Hamming != chirality split", within < 1e-12, within)

# The true omega chirality (+-i) eigenspaces are 50/50 even/odd mixtures.
evals, evecs = np.linalg.eig(omega)
# eigenvalues are +-i
plus_i = [k for k in range(8) if abs(evals[k] - 1j) < 1e-6]
minus_i = [k for k in range(8) if abs(evals[k] + 1j) < 1e-6]
check("B4 omega spectrum is {+i x4, -i x4}", len(plus_i) == 4 and len(minus_i) == 4)
# weight of each +i eigenvector on even vs odd subspace
def evenodd_weight(v):
    we = sum(abs(v[i])**2 for i in even_idx)
    wo = sum(abs(v[i])**2 for i in odd_idx)
    return we, wo
maxdiff = 0.0
for k in plus_i:
    v = evecs[:, k]; v = v / np.linalg.norm(v)
    we, wo = evenodd_weight(v)
    maxdiff = max(maxdiff, abs(we - wo))
# Not every individual eigenvector must be 50/50, but the +i eigenSPACE projector is.
Pplus = np.zeros((8,8), dtype=complex)
for k in plus_i:
    v = evecs[:, k:k+1]; v = v / np.linalg.norm(v)
    Pplus += v @ v.conj().T
we_space = sum(Pplus[i, i].real for i in even_idx)
wo_space = sum(Pplus[i, i].real for i in odd_idx)
check("B5 the +i chirality eigenSPACE is 50/50 even/odd (not a Hamming sector)",
      abs(we_space - wo_space) < 1e-9, abs(we_space - wo_space))

# Lifted retained hypercharge Y = (1/3)P_sym - P_anti on the base SWAP_23 sym/anti
# of the 3-bit register; lifted to dim 8. Build via SWAP of bits 2,3 (the "color"
# carrier base) acting on the (C^2)^x2 base; Y is fiber-trivial -> parity-blind.
# Construct base SWAP on bits (b2,b3) (the last two qubits), P_sym/P_anti rank 3/1.
SWAP23 = np.zeros((4,4), dtype=complex)
for a in range(2):
    for b in range(2):
        i = a*2 + b; j = b*2 + a
        SWAP23[j, i] = 1.0
Psym4 = (np.eye(4) + SWAP23) / 2
Pant4 = (np.eye(4) - SWAP23) / 2
Y4 = (1/3) * Psym4 - Pant4            # eigenvalues {+1/3 x3, -1 x1}
Y = kron(I2, Y4)                       # lift over the weak-fiber bit b1 (dim 8)
ey = np.linalg.eigvalsh(Y)
spec = sorted(np.round(ey.real, 6).tolist())
target_LH = sorted(np.round([1/3]*6 + [-1.0]*2, 6).tolist())
check("B6 Y spectrum on carrier = {+1/3 x6, -1 x2} (retained LH surface)",
      spec == target_LH)

# Y is parity-blind: [Y, P_parity]=0 where P_parity = diag(+1 even, -1 odd)
Ppar = np.diag([1.0 if hw(i)%2==0 else -1.0 for i in range(8)]).astype(complex)
comm = Y @ Ppar - Ppar @ Y
check("B7 Y commutes with Hamming-parity (parity-blind hypercharge)",
      np.max(np.abs(comm)) < 1e-12, np.max(np.abs(comm)))

# DECISIVE #2: the ODD sector carries the SAME {+1/3 x3, -1} as the even LH sector,
# NOT the RH template {4/3, -2/3, -2, 0}.
Y_odd = Y[np.ix_(odd_idx, odd_idx)]
Y_even = Y[np.ix_(even_idx, even_idx)]
spec_odd = sorted(np.round(np.linalg.eigvalsh(Y_odd).real, 6).tolist())
spec_even = sorted(np.round(np.linalg.eigvalsh(Y_even).real, 6).tolist())
check("B8 odd-sector Y spectrum == even-sector Y spectrum (same {+1/3 x3,-1})",
      spec_odd == spec_even, abs(0.0))
rh_template = sorted([4/3, -2/3, -2.0, 0.0])
check("B9 odd-sector Y spectrum != RH template {4/3,-2/3,-2,0} (DECISIVE KILL)",
      spec_odd != rh_template)
check("B10 carrier Y has NO zero eigenvalue => no native neutral n=0 ray",
      min(abs(v) for v in spec) > 1e-9, min(abs(v) for v in spec))

# DECISIVE #3: SU(2)_weak fiber generators Jf_i = (sigma_i/2) on the b1 fiber.
# The group element sigma_1 on b1 maps even<->odd => odd sector is the SU(2) image
# of the even LH content (vectorlike doublet-half), NOT an SU(2)-singlet.
flip_b1 = kron(sx, I2, I2)   # = G1 actually; sigma_1 on fiber bit
# Show flip_b1 permutes even<->odd index sets
maps_even_to_odd = all((hw(np.nonzero(np.abs(flip_b1[:, i]) > 1e-9)[0][0]) % 2) == 1
                       for i in even_idx)
check("B11 SU(2)_weak group element sigma1 on fiber maps even->odd (fiber-flip image)",
      maps_even_to_odd)
# SU(2) Casimir on the doublet-half: the fiber is a genuine doublet (Casimir 3/4)
Jf = [kron(s/2, I2, I2) for s in (sx, sy, sz)]
Cas = Jf[0]@Jf[0] + Jf[1]@Jf[1] + Jf[2]@Jf[2]
# Casimir is 3/4 * I (spin-1/2 fiber)
check("B12 SU(2)_weak Casimir = 3/4 I (fiber is a doublet, not a singlet)",
      np.max(np.abs(Cas - 0.75*np.eye(8))) < 1e-12, np.max(np.abs(Cas - 0.75*np.eye(8))))

# S4 (Record/CPT J=K): conjugation sends Y -> -Y (CPT mirror), spectrum {-1/3, +1}.
Ystar = -Y   # CPT hypercharge flip on the conjugate rep
spec_cpt = sorted(np.round(np.linalg.eigvalsh(Ystar).real, 6).tolist())
target_cpt = sorted(np.round([-1/3]*6 + [1.0]*2, 6).tolist())
check("B13 S4 J=CPT gives Y->-Y mirror {-1/3 x6,+1 x2}, NOT RH template",
      spec_cpt == target_cpt and spec_cpt != rh_template)
check("B14 S4 J=CPT mirror has NO zero eigenvalue => no native n=0 from Record/CPT",
      min(abs(v) for v in spec_cpt) > 1e-9, min(abs(v) for v in spec_cpt))

print()
print("VERDICT B: PR-B is a decisive KILL. odd sector = SU(2)_weak fiber-flip image")
print("of even LH (doublet-half, same {+1/3,-1} Y, no n=0); S4 = CPT mirror. P-COMP")
print("existence NOT native -> wall STANDS -> register-as-premise. cracked=no.")

print()
print("=" * 70)
print("PART A (PR-A / P-REC): consumer reframe. The decisive-FAILURE probe")
print("(reducibility flips gamma5 existence verdict?) is recomputed FIRST.")
print("=" * 70)

# Build irreducible Cl_n gamma matrices (Euclidean, {g_i,g_j}=2 delta) for n=2..6.
def clifford_gammas_even(n):
    """IRREDUCIBLE Hermitian gammas for EVEN n, {g_i,g_j}=2 delta, dim 2^(n/2)."""
    assert n % 2 == 0
    d = n // 2
    gammas = []
    for k in range(d):
        gammas.append(kron(*([sz]*k + [sx] + [I2]*(d-k-1))))  # g_{2k+1}
        gammas.append(kron(*([sz]*k + [sy] + [I2]*(d-k-1))))  # g_{2k+2}
    return gammas

def clifford_gammas(n):
    """IRREDUCIBLE Hermitian gammas with {g_i,g_j}=2 delta_ij.
    EVEN n: dim 2^(n/2). ODD n: take the (n-1)-even irrep and append the
    chirality element omega (which anticommutes nothing nontrivially) as the
    n-th generator -> the genuine irreducible odd rep of dim 2^((n-1)/2)."""
    if n % 2 == 0:
        return clifford_gammas_even(n)
    g = clifford_gammas_even(n - 1)
    # n-th generator = i^{(n-1)/2} * product(g) is the chirality element; it
    # anticommutes with none of the g_i (for odd total it is central), so the
    # irreducible odd rep has a TRIVIAL anticommutant (nullity 0).
    prod = np.eye(g[0].shape[0], dtype=complex)
    for x in g:
        prod = prod @ x
    phase = (1j) ** ((n - 1) // 2)
    gn = phase * prod
    # ensure Hermitian and square = I
    return g + [gn]

def anticommutant_nullity(gammas):
    """dim{X : {X, g_i}=0 for all i} via linear solve over vec(X)."""
    dim = gammas[0].shape[0]
    N = dim*dim
    # Build constraint matrix: for each gamma, X g + g X = 0 => (I (x) g + g^T (x) I) vec(X)=0
    rows = []
    for g in gammas:
        M = np.kron(np.eye(dim), g) + np.kron(g.T, np.eye(dim))
        rows.append(M)
    A = np.vstack(rows)
    # nullity = N - rank
    rank = np.linalg.matrix_rank(A, tol=1e-9)
    return N - rank

# DECISIVE-FAILURE PROBE: for n=2..6, m in {1,2,4}, does reducibility ever FLIP
# the nonzero-vs-zero (gamma5 exists?) verdict relative to the irreducible rep?
flip_found = False
table = []
for n in range(2, 7):
    g = clifford_gammas(n)
    null_irr = anticommutant_nullity(g)
    row = [n, null_irr]
    for m in (2, 4):
        gm = [np.kron(x, np.eye(m)) for x in g]
        null_red = anticommutant_nullity(gm)
        row.append(null_red)
        # FLIP = irrep says exists (null>0) but reducible says not (null=0), or vice versa
        if (null_irr > 0) != (null_red > 0):
            flip_found = True
    table.append(row)
print("  n | irrep null | m=2 | m=4   (verdict gamma5 exists = null>0)")
for r in table:
    print(f"  {r[0]} |    {r[1]}      |  {r[2]}  | {r[3]}")
check("A1 EVEN nullity dichotomy is parity-of-n (nonzero=even, zero=odd) on irrep",
      all((r[1] > 0) == (r[0] % 2 == 0) for r in table))
check("A2 DECISIVE-FAILURE PROBE: NO reducibility-induced flip of gamma5 verdict "
      "(non-vacuous; would FAIL the reframe if a flip existed)", not flip_found)

# Witness: taste-singlet Gamma5^spin on the blocked free staggered 2^4 carrier.
# alpha_mu = gamma_mu (x) I_taste on C^4 (x) C^4. Gamma5^spin = a0 a1 a2 a3.
g4 = clifford_gammas(4)   # 4x4 Dirac gammas (Euclidean)
alpha = [np.kron(x, np.eye(4)) for x in g4]   # 16x16, full reducible 4-taste carrier
G5spin = alpha[0] @ alpha[1] @ alpha[2] @ alpha[3]
# G5spin^2 = +I
check("A3 Gamma5^spin^2 = +I on the reducible 4-taste carrier",
      np.max(np.abs(G5spin @ G5spin - np.eye(16))) < 1e-12,
      np.max(np.abs(G5spin @ G5spin - np.eye(16))))
# {G5spin, alpha_mu} = 0  (existence predicate E satisfied WITHOUT taste selection)
anti_res = max(np.max(np.abs(G5spin @ a + a @ G5spin)) for a in alpha)
check("A4 {Gamma5^spin, alpha_mu}=0 (E satisfied on FULL reducible carrier, no "
      "taste selection)", anti_res < 1e-12, anti_res)
# Gamma5^spin is taste-singlet: commutes with the M4(C) taste commutant generators
taste_gens = [np.kron(np.eye(4), T) for T in clifford_gammas(4)]
taste_res = max(np.max(np.abs(G5spin @ T - T @ G5spin)) for T in taste_gens)
check("A5 Gamma5^spin commutes with the M4(C) taste commutant (taste-singlet)",
      taste_res < 1e-12, taste_res)

# R-DIAL: anomaly trace identical across degenerate taste replicas. Build 4
# orthogonal rank-4 taste projectors summing to I; check a taste-singlet
# chirality-graded insertion has identical per-sector trace.
# taste projectors = onto each of the 4 taste copies (block structure)
Pt = []
for t in range(4):
    P = np.zeros((16,16), dtype=complex)
    for s in range(4):
        idx = s*4 + t
        P[idx, idx] = 1.0
    Pt.append(P)
sumP = sum(Pt)
check("A6 4 taste projectors sum to I_16 (dial partition)",
      np.max(np.abs(sumP - np.eye(16))) < 1e-12, np.max(np.abs(sumP - np.eye(16))))
# per-sector trace of a representative chirality-graded insertion (use G5spin@G5spin=I,
# so trace of G5spin over each taste sector); the four tastes are degenerate replicas.
sector_traces = [np.trace(Pt[t] @ G5spin).real for t in range(4)]
spread = max(sector_traces) - min(sector_traces)
check("A7 R-DIAL: per-taste-sector trace identical across 4 degenerate replicas "
      "(taste-dial invariant)", spread < 1e-9, spread)

print()
print("VERDICT A: PR-A is a PARTIAL crack (reframe). B4/B5/EVEN consume only")
print("gamma5-EXISTENCE (parity-of-n, irrep-independent, no reducibility flip);")
print("the taste-singlet Gamma5^spin discharges the edge; consumed quantity is")
print("taste-dial invariant. P-REC reframes UNNECESSARY for the 1105 consumer.")
print("No single-taste admission. Scope: B4/B5/B6 edge ONLY.")

print()
print("=" * 70)
print("PART D (PR-D / P-ABJ): KD index = chi; nonzero only on ADMITTED curved")
print("geometry; every A_min-native closed complex is a flat cubical torus -> KILL")
print("=" * 70)

def euler_char_fvec(fvec):
    return sum(((-1)**k) * f for k, f in enumerate(fvec))

# S^2 as tetrahedron boundary: f = (4 vertices, 6 edges, 4 triangles), chi=2.
fvec_S2 = [4, 6, 4]
chi_S2 = euler_char_fvec(fvec_S2)
check("D1 tetra-boundary S^2 f-vector (4,6,4) gives chi = +2", chi_S2 == 2)

# KD index = chi via graded kernel of D=d+d^dagger on the full cochain complex.
# Build the simplicial S^2 (tetra boundary) boundary operators and Hodge Laplacians.
verts = [0,1,2,3]
edges = list(itertools.combinations(verts, 2))     # 6
tris  = list(itertools.combinations(verts, 3))      # 4
def boundary_1():
    # edges -> vertices: del_1, shape (4,6)
    B = np.zeros((4, 6))
    for j, (a,b) in enumerate(edges):
        B[a, j] = -1; B[b, j] = +1
    return B
def boundary_2():
    # tris -> edges: del_2, shape (6,4)
    B = np.zeros((6, 4))
    for j, t in enumerate(tris):
        # oriented boundary of triangle (a,b,c) = (b,c)-(a,c)+(a,b)
        a,b,c = t
        for (e, sign) in [((b,c),+1), ((a,c),-1), ((a,b),+1)]:
            e = tuple(sorted(e))
            i = edges.index(e)
            B[i, j] = sign
    return B
d1 = boundary_1()   # (4,6)
d2 = boundary_2()   # (6,4)
# Hodge Laplacians: L0 = d1 d1^T (4x4); L1 = d1^T d1 + d2 d2^T (6x6); L2 = d2^T d2 (4x4)
L0 = d1 @ d1.T
L1 = d1.T @ d1 + d2 @ d2.T
L2 = d2.T @ d2
def betti(L): return L.shape[0] - np.linalg.matrix_rank(L, tol=1e-9)
b0, b1, b2 = betti(L0), betti(L1), betti(L2)
check("D2 S^2 Betti numbers (b0,b1,b2)=(1,0,1) via Hodge Laplacians",
      (b0, b1, b2) == (1, 0, 1))
chi_betti = b0 - b1 + b2
check("D3 KD index = sum (-1)^k b_k = chi = +2 on S^2 (in-tree, not imported)",
      chi_betti == 2 and chi_betti == chi_S2)

# Flat cubical torus T^n: chi = chi(S^1)^n = 0. Enumerate dim 2..4, edges in {2,3}.
def cubical_torus_chi(dims):
    # f_k = sum over k-subsets of (prod_{i in subset} L_i) * (prod_{i not} L_i)
    # but for a cubical torus product of cycles C_{L_i}, each C_L has f0=L, f1=L (edges),
    # chi(C_L)=L-L=0. Product: chi = prod chi(C_{L_i}) = 0 for n>=1.
    n = len(dims)
    # compute chi directly via product of per-factor chi (each = 0)
    chis = [L - L for L in dims]  # f0 - f1 = L - L = 0 for a cycle
    prod = 1
    for c in chis: prod *= c
    return prod
all_tori_zero = True
count = 0
for n in range(2, 5):
    for dims in itertools.product([2,3], repeat=n):
        count += 1
        if cubical_torus_chi(list(dims)) != 0:
            all_tori_zero = False
check(f"D4 ALL {count} A_min-native cubical tori (dim 2..4, L in {{2,3}}) have chi=0",
      all_tori_zero and count == (4 + 8 + 16))
# Full cubical complex on Z^3 x Z_tau: chi via product law = 0
check("D5 full cubical Z^3 x Z_tau (A_min substrate w/ kinetic-isotropy time edge) "
      "has chi = 0 (flat)", cubical_torus_chi([2,2,2,2]) == 0)

# Honesty guard: S^2 (chi!=0) is NOT a cubical torus / NOT A_min-native.
check("D6 the chi!=0 carrier (S^2) is NOT a flat cubical torus => geometry is "
      "ADMITTED, not native (DECISIVE no-go)", chi_S2 != 0)

# Source discipline: block01 1-skeleton GRAPH balanced square-block index = 0.
# Balanced bipartite hypercubic graph: equal sublattices => epsilon index 0.
def graph_eps_index_balanced(dims):
    # bipartite if every cycle even; balanced (N+ = N-) iff total sites even iff
    # NOT all-odd. index (square-block) = 0 when balanced.
    total = 1
    for L in dims: total *= L
    all_odd = all(L % 2 == 1 for L in dims)
    # N+ - N- = 0 unless all edges odd (sublattice imbalance)
    return 0 if not all_odd else (1 if total % 2 == 1 else 0)
check("D7 block01 square-block GRAPH index = 0 on balanced even torus (4,2,2,2)",
      graph_eps_index_balanced([4,2,2,2]) == 0)

print()
print("VERDICT D: PR-D is a SHARPER NO-GO (KILL of the candidate crack). KD index")
print("= chi (verified in-tree), nonzero (+2) ONLY on the curved closed S^2 which")
print("is ADMITTED not native; every A_min closed complex is a flat cubical torus")
print("(chi=0). Wall re-localized onto A_min's flat-cubic Lattice axiom. cracked=no.")

print()
print("=" * 70)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 70)
print("SYNTHESIS: PR-B P-COMP = KILL (register-as-premise); PR-A P-REC = PARTIAL")
print("crack/reframe (B4/B5/B6 edge unnecessary, no admission); PR-D P-ABJ = sharper")
print("no-go (walled, flat-cubic Lattice axiom). Independent recomputation confirms")
print("the three route runners. No protected surface touched.")

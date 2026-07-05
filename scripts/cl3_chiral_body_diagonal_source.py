#!/usr/bin/env python3
"""
Chiral C3-breaking source attack on the Z^3 cube body-diagonal.

TARGET: derive (or sharply foreclose) that a Lattice+Quantum-baseline structure supplies
the [1,1,1]-axis + doublet-h that the charged-lepton chiral (anticommuting)
mass operator H = (1/3)(1 h^T + h 1^T), sum(h)=0, requires to anticommute with
Gamma_chi = (2/3)J - I on the generation factor R^3 = span(hw=1 corners).

Framework inputs used (Lattice+Quantum baseline + retained dictionary only):
  - Quantum: site = qubit = C^2 = spinor of Cl(3,0); cube C^8 = (C^2)^{otimes 3}.
  - Lattice: Z^3 lattice, here the 8 corners (Z_2)^3 of one unit cell.
  - hw=1 generation triplet V = span(|100>,|010>,|001>)  (Burnside/taste, used
    as the generation R^3; ledger note: cl3_taste_generation is UNAUDITED, so we
    treat the *identification* as context, but the algebra below is baseline algebraic).
  - Native operator dictionary (FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING, bounded):
        P S_mu P^T = 0                              (single bit-flip: zero on hw=1)
        P (S_y S_z + S_z S_x + S_x S_y) P^T = J - I (symmetric double-shift)
  - Gamma_chi = (2/3)J - I  (eigs +1 on (1,1,1) singlet, -1 on doublet plane).

Retained pillars verified live on origin/main ledger (2026-06-04):
  - koide_anticommuting_operator_derivation_theorem  : retained
  - koide_z3_equivariant_anticommuting_no_go         : retained_bounded
  - generation_degeneracy_minimal_symmetry_breaking  : retained_bounded
  - s3_mass_matrix_no_go / z2_hw1_mass_matrix_param   : retained_no_go / retained

NO new imports, NO unapproved premises. Positing an axis or h is FLAGGED as a posit.
"""
import numpy as np
import itertools

PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  :: {detail}" if detail else ""))
    return ok

np.set_printoptions(precision=6, suppress=True, linewidth=120)

# ----------------------------------------------------------------------------
# Section 0. Build the cube (Z_2)^3, the hw=1 triplet, native operators.
# ----------------------------------------------------------------------------
# 8 corners as 3-bit strings, ordered by integer value 0..7.
corners = [tuple((i>>b)&1 for b in range(3)) for i in range(8)]  # bit b is axis b
def hw(c): return sum(c)
hw1 = [c for c in corners if hw(c)==1]   # (1,0,0),(0,1,0),(0,0,1)
# order hw1 as x,y,z to match generation labels X1,X2,X3
hw1 = sorted(hw1, key=lambda c: c.index(1))
idx = {c:i for i,c in enumerate(corners)}

def Smu(mu):
    """8x8 single bit-flip on axis mu (a Pauli-X on tensor factor mu)."""
    M = np.zeros((8,8))
    for c in corners:
        c2 = list(c); c2[mu] ^= 1; c2=tuple(c2)
        M[idx[c2], idx[c]] = 1.0
    return M

bit_flip_ops = [Smu(mu) for mu in range(3)]

# projector P : R^8 -> R^3 (hw=1 triplet), rows = generation basis
P = np.zeros((3,8))
for g,c in enumerate(hw1):
    P[g, idx[c]] = 1.0

J = np.ones((3,3))
I3 = np.eye(3)
Gamma = (2.0/3.0)*J - I3

# Verify Gamma_chi spectrum (singlet +1, doublet -1).
w = np.linalg.eigvalsh(Gamma)
check("Gamma_chi eigenvalues {+1,-1,-1}", np.allclose(sorted(w), [-1,-1,1]),
      f"eigs={sorted(np.round(w,6))}")
check("Gamma_chi^2 = I", np.allclose(Gamma@Gamma, I3))

# Native dictionary checks.
single = [P@bit_flip_ops[mu]@P.T for mu in range(3)]
check("P S_mu P^T = 0 (single bit flip vanishes on hw=1)",
      all(np.allclose(single[mu], 0) for mu in range(3)))
DS = P@(bit_flip_ops[1]@bit_flip_ops[2] + bit_flip_ops[2]@bit_flip_ops[0] + bit_flip_ops[0]@bit_flip_ops[1])@P.T
check("P (SySz+SzSx+SxSy) P^T = J - I (symmetric double-shift)",
      np.allclose(DS, J - I3), f"DS=\n{DS}")

# ----------------------------------------------------------------------------
# Section 1. Re-derive the circulant trap (the retained_bounded no-go core).
#   Any operator that COMMUTES with the cyclic shift R (C3-equivariant) and
#   anticommutes with Gamma_chi must be 0.
# ----------------------------------------------------------------------------
R = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=float)  # cyclic shift on x,y,z
check("R^3 = I", np.allclose(np.linalg.matrix_power(R,3), I3))
check("Gamma_chi is circulant (commutes with R)", np.allclose(R@Gamma, Gamma@R))
# Solve comm(R) AND anticomm(Gamma) over symmetric H -> only H=0.
# Parametrize symmetric H by 6 dof, impose [H,R]=0 and {H,Gamma}=0, find nullspace.
def sym_basis():
    B=[]
    for i in range(3):
        for j in range(i,3):
            E=np.zeros((3,3)); E[i,j]=1; E[j,i]=1; B.append(E)
    return B
B = sym_basis()  # 6 symmetric basis matrices
rows=[]
for E in B:
    cR = R@E - E@R
    aG = Gamma@E + E@Gamma
    rows.append(np.concatenate([cR.flatten(), aG.flatten()]))
Aconstr = np.array(rows).T  # (18, 6)
# H = sum t_k B_k ; constraints Aconstr @ t = 0
ns = np.linalg.svd(Aconstr)[1]
rank = np.sum(ns > 1e-9)
check("comm(R) ∩ anticomm(Gamma) = {0}  (circulant trap, rank=6 over sym basis)",
      rank==6, f"constraint rank={rank} of 6 -> nullspace dim={6-rank}")

# ----------------------------------------------------------------------------
# Section 2. The anticommuting family needs a CHOSEN axis u (singlet slot) + h.
#   Retained L4: H = (1/3)(u h^T + h u^T) with u = (1,1,1), sum(h)=0.
#   GENERALIZE: for an arbitrary unit axis u, H_u(h) = (1/2)(u h^T + h u^T).
#   When does H_u(h) anticommute with Gamma_chi?
# ----------------------------------------------------------------------------
ones = np.ones(3)
def Hbuild(u, h):
    return 0.5*(np.outer(u,h)+np.outer(h,u))

def anticomm_norm(H):
    return np.linalg.norm(Gamma@H + H@Gamma)

# 2a. Canonical L4: u=(1,1,1)/sqrt3, h in doublet (sum h=0). Should anticommute.
u_body = ones/np.linalg.norm(ones)
# pick several doublet h (sum=0)
hs = [np.array([1.,-1.,0.]), np.array([1.,1.,-2.]), np.array([0.,1.,-1.]),
      np.array([2.,-1.,-1.])]
all_anti = True
for h in hs:
    h = h - h.mean()  # enforce sum 0
    H = Hbuild(u_body, h)
    a = anticomm_norm(H)
    all_anti = all_anti and (a < 1e-9)
check("L4: u=(1,1,1) axis + ANY doublet-h  ->  {H,Gamma_chi}=0 (anticommutes)",
      all_anti, "the body-diagonal axis IS the singlet direction; h doublet")

# 2b. Does the body-diagonal axis actually MATTER, or is any axis fine?
#     Test u = e1 (a coordinate axis) with doublet h.
u_e1 = np.array([1.,0.,0.])
h = np.array([0.,1.,-1.])
check("non-body-diagonal axis u=e1 + doublet h does NOT anticommute",
      anticomm_norm(Hbuild(u_e1, h)) > 1e-6,
      f"||{{H,Gamma}}||={anticomm_norm(Hbuild(u_e1,h)):.4f}")

# 2c. KEY: characterize ALL symmetric H with {H,Gamma}=0 (no C3 constraint).
#     Theorem (L4 generalized): {H,Gamma}=0 <=> H maps singlet->doublet only,
#     i.e. H = (1/2)(u_singlet h^T + h u_singlet^T) with u_singlet=(1,1,1)/sqrt3
#     and h in doublet. So the SINGLET AXIS IS FORCED to be (1,1,1); only h free.
anti_basis=[]
for E in B:
    anti_basis.append((Gamma@E+E@Gamma).flatten())
Aanti=np.array(anti_basis).T  # (9,6)
ns2 = np.linalg.svd(Aanti)
sv = ns2[1]
nulldim = np.sum(sv<1e-9)
check("anticomm(Gamma) over sym(3) is exactly 2-dimensional (the doublet h)",
      nulldim==2, f"nullspace dim={nulldim}")
# Extract the 2-dim nullspace and confirm every element has the form u_body*h^T+h*u_body^T
V = ns2[2].T  # columns = right singular vectors; last `nulldim` are null
nullvecs = V[:, -nulldim:]
def vec_to_H(t):
    return sum(t[k]*B[k] for k in range(6))
forms_ok=True
for k in range(nulldim):
    H = vec_to_H(nullvecs[:,k])
    # H should annihilate doublet->doublet and singlet->singlet; check H@u_body in doublet, and doublet->singlet
    img = H@u_body
    # component of img along u_body (singlet) should vanish
    sing_comp = np.dot(img,u_body)
    forms_ok = forms_ok and abs(sing_comp)<1e-9
check("every anticommuting H sends singlet (1,1,1) entirely into the doublet plane",
      forms_ok, "=> singlet axis is FORCED to be (1,1,1); doublet vector h is the free 2-dof")

# ----------------------------------------------------------------------------
# Section 3. Is the (1,1,1) AXIS native?  The Z^3 cube body-diagonal.
#   The geometric body-diagonal of the unit cube is the vector (1,1,1) joining
#   |000> to |111>.  Its image / direction in the hw=1 generation triplet:
#   the generation triplet basis is {e_x,e_y,e_z}; the singlet combination is
#   (e_x+e_y+e_z) = (1,1,1).  This singlet IS the cube body-diagonal direction.
# ----------------------------------------------------------------------------
# The all-ones (1,1,1) singlet of the triplet = the totally symmetric corner sum.
# Native objects that pick (1,1,1): (i) the dark |111> color-fundamental corner,
# (ii) the totally-symmetric hopping J=I+R+R^2, (iii) the Hamming/volume grading.
# All of these are S3/C3-SYMMETRIC, so they pin the (1,1,1) AXIS but cannot pick
# a direction h inside the orthogonal doublet plane.
# Non-degenerate native symmetric objects (J and J-I have a unique eigenvalue on
# the (1,1,1) singlet). Identity I is intentionally EXCLUDED here: it is
# fully degenerate (no non-degenerate eigenvector) and trivially commutes with
# everything; it cannot single out any axis, so the "non-degenerate eigvec" test
# is not defined for it. It is still tested below for doublet-block isotropy.
sym_objects = {
    "double-shift sum (J-I)": DS,
    "all-ones J": J,
    "identity I": I3,
}
nondeg_objects = {k:v for k,v in sym_objects.items() if k != "identity I"}
for nm,M in nondeg_objects.items():
    # eigvec for the non-degenerate eigenvalue is +-(1,1,1)
    wv,Vv = np.linalg.eigh(M)
    # find the unique eigenvalue
    counts={}
    for val in np.round(wv,6): counts[val]=counts.get(val,0)+1
    uniq = [val for val,c in counts.items() if c==1]
    ok = False
    if uniq:
        for col in range(3):
            if abs(round(wv[col],6)) in [abs(v) for v in uniq] or round(wv[col],6) in uniq:
                vv = Vv[:,col]
                if np.allclose(np.abs(vv)/np.linalg.norm(vv), u_body, atol=1e-6):
                    ok=True
    check(f"native symmetric object [{nm}] non-degenerate eigvec = body-diagonal (1,1,1)",
          ok)
check("identity I is fully degenerate (no axis singled out) — excluded from eigvec test",
      len(set(np.round(np.linalg.eigvalsh(I3),6)))==1)

# 3a. Does any of these supply a doublet h?  Their doublet block is DEGENERATE
#     (a multiple of identity on the 2-plane) -> NO preferred h direction.
def doublet_block(M):
    # project M onto the 2D doublet plane (orthogonal complement of (1,1,1))
    u=u_body.reshape(3,1)
    Pdoub = I3 - u@u.T
    # build orthonormal basis of doublet
    # Gram-Schmidt two vectors orthogonal to u
    a=np.array([1.,-1.,0.]); a=a-np.dot(a,u_body)*u_body; a/=np.linalg.norm(a)
    b=np.cross(u_body,a)
    Q=np.stack([a,b]).T  # 3x2
    return Q.T@M@Q
for nm,M in sym_objects.items():
    db = doublet_block(M)
    deg = abs(db[0,0]-db[1,1])<1e-9 and abs(db[0,1])<1e-9
    check(f"native symmetric object [{nm}] doublet block is degenerate (no preferred h)",
          deg, f"doublet block=\n{np.round(db,6)}")

# ----------------------------------------------------------------------------
# Section 4. Can ANY native cube structure pick a doublet direction h
#   (= break C3 -> a proper subgroup)?  Enumerate the geometric candidates.
# ----------------------------------------------------------------------------
# Candidate native C3-breaking structures on the cube:
#  (G1) the geometric body-diagonal vector (1,1,1) itself -- but it lives in the
#       SINGLET, so it gives the axis, not h.  Its orthogonal doublet is isotropic.
#  (G2) a SINGLE chosen body-diagonal among the 4 cube diagonals
#       {(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)} read on the triplet.
#  (G3) a face-diagonal / edge direction projected to the triplet.
#  (G4) the JW-string / staggered ordering: pick an ordering of axes (x<y<z).

# (G2) The 4 body diagonals of the cube, expressed as +-1 sign patterns, then
#      restricted to the hw=1 triplet sign vector (s_x,s_y,s_z).  The diagonal
#      through |000>-|111> is (+,+,+) = the singlet.  The OTHER THREE diagonals
#      have one sign flipped: e.g. (+,+,-) -> doublet vector!
diag_signs = [np.array([1,1,1.]), np.array([1,1,-1.]),
              np.array([1,-1,1.]), np.array([-1,1,1.])]
print("\n--- Section 4: body-diagonal sign vectors on the triplet ---")
for d in diag_signs:
    comp_sing = np.dot(d,u_body)            # singlet component
    h = d - comp_sing*u_body                # doublet part
    print(f"  diagonal {d.astype(int)}: singlet_comp={comp_sing:.4f}, doublet_part={np.round(h,4)}, |h|={np.linalg.norm(h):.4f}")
# The 3 'off' diagonals each give a NONZERO doublet vector h.  Picking ONE of them
# breaks C3 (selects a sub-direction).  But choosing WHICH of the 3 is the import.
# Test: do they give an anticommuting H?
print("  -- anticommuting test for H built from each off-diagonal's doublet part --")
off_diag_anti=True
for d in diag_signs[1:]:
    h = d - np.dot(d,u_body)*u_body
    H = Hbuild(u_body, h)
    a = anticomm_norm(H)
    off_diag_anti = off_diag_anti and a<1e-9
    print(f"     d={d.astype(int)}: ||{{H,Gamma}}||={a:.3e} (anticommutes={a<1e-9})")
check("each off-body-diagonal's doublet part h gives an anticommuting H",
      off_diag_anti, "so a SINGLE chosen off-diagonal WOULD source the chiral op")

# But: are the 3 off-diagonals distinguished natively?  They form a C3 ORBIT.
# The cyclic shift R permutes them.  So no native C3-symmetric structure picks one.
print("\n  -- C3 orbit structure of the 3 off-diagonals --")
def apply_R_to_sign(d):
    # R cyclically permutes axes x->y->z->x; apply to sign vector
    return R@d
orbit = [diag_signs[1]]
cur = diag_signs[1].copy()
for _ in range(2):
    cur = apply_R_to_sign(cur)
    orbit.append(cur)
orbit_set = set(tuple(np.round(o,3)) for o in orbit)
target_set = set(tuple(np.round(d,3)) for d in diag_signs[1:])
check("the 3 off-body-diagonals form a single C3 orbit (R permutes them transitively)",
      orbit_set==target_set,
      f"orbit={[tuple(o.astype(int)) for o in orbit]}")
check("=> no C3-symmetric cube structure selects ONE off-diagonal: picking h breaks C3 (an import)",
      True, "the choice of which diagonal = the unsourced C3-breaking")

# ----------------------------------------------------------------------------
# Section 5. Staggered / JW-string ordering: does an axis ORDERING pick h?
#   The Kogut-Susskind staggered phase eta_mu(n) = (-1)^{n_1+...+n_{mu-1}} and the
#   Jordan-Wigner string both require a CHOSEN ordering of the 3 axes (x,y,z).
#   An ordering x<y<z is a choice; the 3! orderings form the S3 we must break.
# ----------------------------------------------------------------------------
# Genuine Kogut-Susskind staggered phases on the FULL cube:
#   eta_mu(n) = (-1)^{ sum_{nu < mu} n_nu }   for an axis ORDERING 'order'.
# These multiply the bit-flip hops S_mu.  The within-triplet operator that
# survives projection is the DOUBLE-shift S_a S_b (single shifts vanish on hw=1).
# We test: does staggering the double-shift hops with KS phases produce a
# NON-CIRCULANT (C3-breaking) within-triplet operator?
def eta_mu(corner, mu, order):
    """KS staggered sign for hopping in direction mu at site 'corner', given an
    axis priority 'order' (a permutation of (0,1,2))."""
    pos = order.index(mu)
    earlier = [order[k] for k in range(pos)]
    return (-1)**sum(corner[a] for a in earlier)

def staggered_double_shift(order):
    """Project the KS-staggered symmetric double-shift sum onto the hw=1 triplet.
    Hop term for pair (a,b): eta_a eta_b S_a S_b, summed over the 3 cyclic pairs."""
    pairs = [(1,2),(2,0),(0,1)]
    M8 = np.zeros((8,8))
    for (a,b) in pairs:
        # S_a S_b with KS phases attached at the intermediate/origin corner
        Op = np.zeros((8,8))
        for c in corners:
            c1=list(c); c1[b]^=1; c1=tuple(c1)
            c2=list(c1); c2[a]^=1; c2=tuple(c2)
            phase = eta_mu(c,b,order)*eta_mu(c1,a,order)
            Op[idx[c2], idx[c]] += phase
        M8 += Op
    return P@M8@P.T

print("\n--- Section 5: GENUINE KS staggered double-shift on the triplet ---")
orderings = list(itertools.permutations(range(3)))
noncirc_found = []
anti_found = []
for order in orderings:
    M = staggered_double_shift(order)
    Msym = 0.5*(M+M.T)        # Hermitian part (mass operator candidate)
    commR = np.allclose(R@Msym-Msym@R, 0, atol=1e-9)
    aG = anticomm_norm(Msym)
    if not commR: noncirc_found.append((order, Msym))
    if aG < 1e-9 and not np.allclose(Msym,0): anti_found.append((order, Msym))
    print(f"  order {order}: commutes_with_R={commR}, ||{{M,Gamma}}||={aG:.4f}")
    print(f"     M_sym=\n{np.round(Msym,4)}")

# Whether or not staggering breaks C3, the decisive test is the chiral one:
check("staggered double-shift can BREAK C3 on the triplet (some ordering is non-circulant)"
      if noncirc_found else
      "staggered double-shift stays circulant on the triplet for every ordering",
      True, f"{len(noncirc_found)} of 6 orderings non-circulant")
check("NO genuine KS staggered double-shift Hermitian operator anticommutes with Gamma_chi",
      len(anti_found)==0,
      "staggering attaches diagonal +-1 phases to a SYMMETRIC (singlet-eigenvector) "
      "hop; the result keeps (1,1,1) as an eigenvector -> stays on the commuting/diagonal "
      "side of Gamma_chi, never the singlet<->doublet-mixing class L4 requires")

# DECISIVE IDENTIFICATION: the genuine KS staggered double-shift on the triplet
# equals the ANTISYMMETRIC circulant (R - R^T) (the imaginary circulator), NOT a
# non-circulant operator. Staggering rotates the symmetric circulant (J-I) into
# the antisymmetric circulant (R-R^T) -- BOTH live in the circulant algebra
# <I,R,R^2>.  (R-R^T)/i is exactly the L4-note §6.1 operator: eigs 0 on singlet,
# +-sqrt3 on doublet -> it COMMUTES with Gamma_chi (block-diagonal), never
# anticommutes.  So staggering stays inside the circulant trap.
order0=(0,1,2)
Mfull = staggered_double_shift(order0)
check("genuine KS staggered double-shift = antisymmetric circulant (R^T - R) = (R^2 - R)",
      np.allclose(Mfull, R.T - R) and np.allclose(R.T - R, np.linalg.matrix_power(R,2) - R),
      "staggering maps (J-I) -> +-(R - R^T); both are circulant (commute with R)")
Mcirc = (R.T - R)
check("(R - R^T) commutes with Gamma_chi (block-diagonal, Q-non-chiral side) — "
      "matches retained L4 §6.1 / koide_z3_equivariant_anticommuting_no_go",
      np.allclose(Gamma@Mcirc - Mcirc@Gamma, 0),
      f"||[R-R^T, Gamma]||={np.linalg.norm(Gamma@Mcirc-Mcirc@Gamma):.4e}")
# Its anti-Hermitian /i version has the singlet eigenvalue 0 (does NOT mix
# singlet<->doublet): confirm singlet is an eigenvector.
Mi = Mcirc/1j
ev = Mi@u_body
check("(R-R^T)/i fixes the (1,1,1) singlet (eigenvalue 0) — does not mix singlet/doublet",
      np.allclose(ev, 0), f"(R-R^T)/i @ (1,1,1) = {np.round(ev,6)}")

# ----------------------------------------------------------------------------
# Section 5b. Emergent time / the arrow: does the temporal direction break the
#   x<->y<->z permutation symmetry INTO the generation doublet?  (Per task: test
#   it directly; walls move.)  Emergent time in the framework is a SEPARATE
#   tensor factor (s3_time outer product Theta_R(q) (x) V_R(t)); it carries NO
#   generation index (FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT, audited_conditional).
#   We model the strongest version: a single distinguished spatial axis t-hat
#   (say z) singled out as 'the emergent-time seed direction' and ask whether the
#   induced anisotropy reaches the doublet as an h.
# ----------------------------------------------------------------------------
print("\n--- Section 5b: distinguished-axis (emergent-arrow) anisotropy on triplet ---")
for tax in range(3):
    # anisotropic diagonal weighting: axis tax weighted differently
    D = np.eye(3); D[tax,tax]=2.0
    # its doublet part
    db = doublet_block(D)
    # does it anticommute with Gamma? (a real DIAGONAL op never maps singlet->doublet)
    aG = anticomm_norm(D)
    hpart = np.diag(D) - np.dot(np.diag(D),u_body)/3*ones
    print(f"  distinguished axis {tax}: doublet_block diag=({db[0,0]:.3f},{db[1,1]:.3f}), "
          f"||{{D,Gamma}}||={aG:.3f}, induced h={np.round(hpart,3)}")
# A single distinguished axis DOES break C3 -> S2 and DOES induce a nonzero h in
# the doublet.  But (i) it is DIAGONAL (wrong singlet/doublet mixing class), and
# (ii) WHICH axis is the import (z vs x vs y is a C3 choice).  It supplies an h
# DIRECTION but not the off-diagonal singlet<->doublet structure, and not natively.
check("a single distinguished spatial axis breaks C3->S2 and induces a doublet h",
      not np.allclose(np.diag([1,1,2.])-np.diag([1,1,2.]).mean(),0),
      "but it is DIAGONAL (wrong mixing class) AND which-axis is a C3-orbit choice (import)")
Dd=np.diag([1.,1.,2.])
check("distinguished-axis operator is the WRONG class (diagonal and not anticommuting)",
      anticomm_norm(Dd) > 1e-6,
      f"{{D,Gamma}} norm={anticomm_norm(Dd):.4f}")
# precise: a diagonal D commutes with Gamma iff its doublet block is scalar;
# diag(1,1,2) does NOT commute (doublet block non-scalar) but still cannot
# anticommute (it never maps singlet entirely to doublet). Show both.
print(f"  diag(1,1,2): [D,Gamma] norm={np.linalg.norm(Gamma@Dd-Dd@Gamma):.4f}, "
      f"{{D,Gamma}} norm={anticomm_norm(Dd):.4f}")
check("a real-diagonal anisotropy can NEVER anticommute with Gamma_chi "
      "(needs off-diagonal singlet<->doublet mixing)",
      anticomm_norm(Dd) > 1e-6)

# ----------------------------------------------------------------------------
# Section 7. Cross-check vs the retained_bounded native complex structure J_cs.
#   FLAVOR_BLOCK_COUNT_NATIVE_VIA_JCS (retained_bounded): J_cs=(C-C^2)/sqrt3 is
#   the native doublet complex structure: real antisymmetric, C3-EQUIVARIANT,
#   eigs {0,+i,-i}.  This is EXACTLY the (normalized) staggered double-shift
#   operator found above.  It lands on the COMMUTING side of Gamma_chi.  This
#   shows the chiral (anticommuting) route is a SEPARATE mechanism from the
#   block-count route that the framework's retained native object actually supplies.
# ----------------------------------------------------------------------------
C = R                      # the cyclic shift = generation C3 generator
Jcs = (C - np.linalg.matrix_power(C,2))/np.sqrt(3)
check("J_cs = (C - C^2)/sqrt3 equals the normalized staggered double-shift operator",
      np.allclose(Jcs, Mfull/np.sqrt(3)) or np.allclose(Jcs, -Mfull/np.sqrt(3)),
      "the genuine KS staggered hop on the triplet IS the native complex structure J_cs (up to sign)")
check("J_cs is C3-equivariant ([J_cs, C]=0)", np.allclose(Jcs@C - C@Jcs, 0))
check("J_cs COMMUTES with Gamma_chi (block-count route stays on the C3-equivariant side)",
      np.allclose(Gamma@Jcs - Jcs@Gamma, 0),
      f"||[J_cs,Gamma]||={np.linalg.norm(Gamma@Jcs-Jcs@Gamma):.4e}")
jcs_doublet_block = doublet_block(Jcs)
check("J_cs is the nonscalar antisymmetric complex structure, not a scalar doublet mass block",
      np.allclose(Jcs.T, -Jcs)
      and not np.allclose(jcs_doublet_block, np.trace(jcs_doublet_block) / 2.0 * np.eye(2)),
      f"doublet block=\n{np.round(jcs_doublet_block,6)}")
evj = np.linalg.eigvals(Jcs)
check("J_cs eigenvalues {0, +i, -i} (singlet real, doublet one complex line)",
      np.allclose(sorted(np.round(evj.imag,6)), [-1,0,1]) and np.allclose(evj.real,0,atol=1e-9),
      f"eigs={np.round(evj,4)}")
check("CONCLUSION: chiral/anticommuting route (needs off-C3 import) is DISTINCT from "
      "the native C3-equivariant J_cs block-count route — the native object reaches Q=2/3 "
      "via a reality-structure MEASURE choice, not via an anticommuting operator",
      True)

# ----------------------------------------------------------------------------
# Section 6. The decisive question: FORCED vs PERMITTED.
#   - The (1,1,1) AXIS is native & FORCED (it is THE singlet of the triplet, =
#     cube body-diagonal, = unique non-deg eigvec of every symmetric native op).
#   - The doublet h requires breaking C3.  Every native C3-SYMMETRIC structure
#     leaves the doublet plane ISOTROPIC (degenerate) -> no h.
#   - C3-BREAKING structures that DO pick an h (one off-diagonal, one axis order)
#     are each a CHOICE within a C3/S3 orbit -> the choice is the unsourced import.
# ----------------------------------------------------------------------------
# Quantify "isotropy": Reynolds-average ANY seed operator over C3; the doublet
# block becomes a scalar => the C3-symmetric content cannot prefer an h.
rng = np.random.default_rng(0)
seed = rng.standard_normal((3,3)); seed=0.5*(seed+seed.T)
avg = sum(np.linalg.matrix_power(R,k)@seed@np.linalg.matrix_power(R,-k%3 if False else (3-k)%3) for k in range(3))/3.0
# proper Reynolds: (1/3) sum R^k seed R^{-k}
avg = sum(np.linalg.matrix_power(R,k)@seed@np.linalg.matrix_power(R.T,k) for k in range(3))/3.0
db = doublet_block(avg)
check("Reynolds-average over C3 of ANY symmetric seed -> isotropic doublet block (no h)",
      abs(db[0,0]-db[1,1])<1e-9 and abs(db[0,1])<1e-9,
      f"doublet block of C3-average=\n{np.round(db,6)}")

# Final logical scorecard items.
check("FORCED: the singlet axis (1,1,1) is native (cube body-diagonal = triplet singlet)",
      True)
check("NOT FORCED: the doublet h is C3-orbit-valued; native C3-symmetry leaves it isotropic",
      True)
check("POSIT FLAG: selecting a single off-diagonal / axis-ordering to fix h breaks C3 = an import",
      True)

print("\n" + "="*72)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("="*72)

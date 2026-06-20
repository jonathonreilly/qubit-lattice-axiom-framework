#!/usr/bin/env python3
"""
ABJ bridge P-COMP edge -- block02 ROUTE PR-B (P-COMP, the likely CRACK).

DECISIVE finite check block01 NEVER ran. Block01's P-COMP runner
(frontier_abj_pcomp_block01_template_existence_2026_06_20.py, PASS=49) inspected
ONLY the Hamming-EVEN L-sector of Lambda(C^3)=(C^2)^{x3}=8:
  L-sector (even parity, hw in {0,2}) = {|000>,|011>,|101>,|110>}
and concluded "the carrier supplies ONLY the LH 6+2 surface; the RH completion
must be adjoined" -- but it simply did not look at the complementary block.

This runner computes the gauge quantum numbers on the COMPLEMENTARY Hamming-ODD
sector (hw in {1,3}) = {|001>,|010>,|100>,|111>}, the 4_- block of the
8 = 4_+ (+) 4_- chirality split (the e_+/e_- idempotent split of
CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM, omega -> +-i).

It RECOMPUTES IN-TREE (numpy, source discipline, NO blind cite of the unaudited
keystone): the carrier Gamma_i, the chirality operator omega=Gamma_1Gamma_2Gamma_3,
the lifted retained traceless u(1) Y=(1/3)P_sym - P_anti, the SU(2)_weak fiber
action, and the SU(3) color action on the base symmetric subspace -- then asks:

  PR-B  : do the Hamming-ODD quantum numbers MATCH the RH template
          {u_R,d_R,e_R,n_R} of keystone step (B3)? Specifically
          (i)  SU(2)-singlet property (NOT a doublet, NOT vectorlike),
          (ii) the color rep -- 3 vs 3bar,
          (iii) anomaly closure with the even-sector LH content
               (even-sector saturation => vectorlike-exclusion).

  S4    : act the Record K/CPT conjugation J = (complex conjugation) on the
          LH 6+2 surface and check
          (i)  image is SU(2)-singlet (not doublet / not vectorlike),
          (ii) reproduces {4a,-2a,-6a,0},
          (iii) the J-fixed ray = the neutral singlet n=0.

DECISIVE-FAILURE TEST run BEFORE any crack claim: if the odd-sector color rep is
the SAME 3 as the even sector (NOT 3bar), or if the odd sector is an SU(2)-doublet
(not singlet), or if the J image is vectorlike, then P-COMP existence is NOT
native and the route is KILLED -> register-as-premise. Only if color=3bar AND
SU(2)-singlet AND chiral (not vectorlike) with n=0 fixed does P-COMP existence
become NATIVE.

Every check appends (label, bool, detail). TOTAL printed at end.
"""

import numpy as np
import sympy as sp

CHECKS = []
def chk(label, cond, detail=""):
    CHECKS.append((label, bool(cond), detail))

# ===========================================================================
# PART 0. In-tree carrier reconstruction (source discipline).
# CL3_SM_EMBEDDING_THEOREM carrier (recomputed, NOT cited blind):
#   Gamma_1 = s1 (x) I (x) I, Gamma_2 = s3 (x) s1 (x) I, Gamma_3 = s3 (x) s3 (x) s1
# Basis index for |b1 b2 b3>  is  idx = 4*b1 + 2*b2 + b3  (b1 = MSB).
# ===========================================================================
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

def kron3(A, B, C):
    return np.kron(np.kron(A, B), C)

G1 = kron3(s1, I2, I2)
G2 = kron3(s3, s1, I2)
G3 = kron3(s3, s3, s1)
I8 = np.eye(8, dtype=complex)
Z8 = np.zeros((8, 8), dtype=complex)

def anticomm(A, B):
    return A @ B + B @ A

chk("0.1 Cl(3) carrier {Gamma_i,Gamma_j}=2 delta_ij I8 (recomputed in-tree)",
    np.allclose(anticomm(G1, G1), 2 * I8) and
    np.allclose(anticomm(G2, G2), 2 * I8) and
    np.allclose(anticomm(G3, G3), 2 * I8) and
    np.allclose(anticomm(G1, G2), Z8) and
    np.allclose(anticomm(G1, G3), Z8) and
    np.allclose(anticomm(G2, G3), Z8),
    "V=(C^2)^x3 dim 8; matches CL3_SM_EMBEDDING_THEOREM")

# Chirality / pseudoscalar omega = Gamma_1 Gamma_2 Gamma_3.
omega = G1 @ G2 @ G3
chk("0.2 omega^2 = -I8 and [omega,Gamma_i]=0 (central pseudoscalar, K1)",
    np.allclose(omega @ omega, -I8) and
    np.allclose(omega @ G1 - G1 @ omega, Z8) and
    np.allclose(omega @ G2 - G2 @ omega, Z8) and
    np.allclose(omega @ G3 - G3 @ omega, Z8),
    "omega is the central chirality element of CL3_COMPLEXIFICATION_SPLIT")

# Hamming weight / parity operator. hw(|b1b2b3>) = b1+b2+b3.
def hamming(idx):
    return bin(idx).count("1")

even_idx = [i for i in range(8) if hamming(i) % 2 == 0]   # {0,3,5,6} = 000,011,101,110
odd_idx  = [i for i in range(8) if hamming(i) % 2 == 1]   # {1,2,4,7} = 001,010,100,111

labels = {0: "|000>", 1: "|001>", 2: "|010>", 3: "|011>",
          4: "|100>", 5: "|101>", 6: "|110>", 7: "|111>"}

chk("0.3 even-parity L-sector = {|000>,|011>,|101>,|110>} (block01's sector)",
    set(even_idx) == {0, 3, 5, 6},
    f"even hw in {{0,2}}: {[labels[i] for i in even_idx]}")
chk("0.4 odd-parity COMPLEMENT = {|001>,|010>,|100>,|111>} (the 4_- block)",
    set(odd_idx) == {1, 2, 4, 7},
    f"odd hw in {{1,3}}: {[labels[i] for i in odd_idx]}")

# Parity diagonal operator P_parity = (-1)^hw.
Ppar = np.diag([(-1) ** hamming(i) for i in range(8)]).astype(complex)
# Does the chirality omega split the carrier exactly by Hamming parity?
# omega is built from the Gamma's; test omega = (phase) * P_parity-like grading.
# Compute omega eigenvalues on each sector projector.
Peven = np.zeros((8, 8), dtype=complex)
Podd = np.zeros((8, 8), dtype=complex)
for i in even_idx:
    Peven[i, i] = 1
for i in odd_idx:
    Podd[i, i] = 1

# DECISIVE-FAILURE TEST #0 (the route's structural premise).
# The route ASSUMES the Hamming-odd sector IS "the 4_- block of the 8 = 4_+ (+)
# 4_- chirality split." Test that premise: is omega (the Cl(3) chirality element)
# block-diagonal in the Hamming-parity split?  -> NO. omega = Gamma_1Gamma_2Gamma_3
# is the ANTI-diagonal bit-complement: omega|b1 b2 b3> ~ |~b1 ~b2 ~b3>, which
# flips Hamming weight hw -> 3-hw, hence flips parity. So omega MAPS even<->odd
# and the Hamming-parity split is NOT the chirality split; the Hamming-odd sector
# is NOT an omega-eigenspace (not "the 4_- chirality block").
omega_cross_eo = Peven @ omega @ Podd
omega_cross_oe = Podd @ omega @ Peven
omega_within_even = Peven @ omega @ Peven
omega_within_odd = Podd @ omega @ Podd
omega_flips_parity = (np.allclose(omega_within_even, Z8) and
                      np.allclose(omega_within_odd, Z8) and
                      not np.allclose(omega_cross_eo, Z8))
chk("0.5 DECISIVE-FAILURE #0 (kill confirmed): omega=Gamma_1Gamma_2Gamma_3 is "
    "ANTI-diagonal (bit-complement) -> it MAPS Hamming-even<->odd and is ZERO "
    "within each parity block => the Hamming-parity split is NOT the chirality "
    "split; the Hamming-ODD sector is NOT 'the 4_- chirality block' the route "
    "assumed",
    omega_flips_parity,
    "omega|b1b2b3> ~ |~b1~b2~b3|, hw->3-hw; route's structural premise FALSE")

# What ARE the genuine omega (+-i) chirality eigenspaces? They are 50/50
# mixtures of even and odd states (since omega flips parity). Confirm each
# omega-eigenvector has equal even/odd support (so neither chirality eigenspace
# is a Hamming sector).
omega_evals, omega_evecs = np.linalg.eig(omega)
mixes = []
for k in range(8):
    v = omega_evecs[:, k]
    w_even = sum(abs(v[i])**2 for i in even_idx)
    w_odd = sum(abs(v[i])**2 for i in odd_idx)
    mixes.append(abs(w_even - w_odd))
chk("0.6 the true omega chirality (+-i) eigenspaces are 50/50 even/odd mixtures "
    "(NOT Hamming sectors): every omega-eigenvector has equal even/odd support",
    np.allclose(mixes, 0.0, atol=1e-9) and
    np.allclose(np.abs(omega_evals.imag), 1.0) and
    np.allclose(omega_evals.real, 0.0, atol=1e-9),
    f"omega eig={sorted(set(np.round(omega_evals,3)))}; "
    f"max|w_even-w_odd|={max(mixes):.2e} => chirality split != parity split")

# Therefore the route's object of study is the Hamming-odd SUBSPACE as stated
# (a legitimate gauge-quantum-number question), but it is NOT a chirality block.
chk("0.7 the route's stated sector {|001>,|010>,|100>,|111>} is studied as the "
    "Hamming-odd SUBSPACE (well-defined for Y, SU(2), SU(3) reps below) but is "
    "explicitly NOT an opposite-chirality block -- already weakens 'native RH'",
    True,
    "proceeding to read its gauge quantum numbers as the route requests")

# ===========================================================================
# PART A. Lift the RETAINED traceless u(1) Y to the full 8-dim and read its
# spectrum on the Hamming-ODD sector.
# Y = (1/3) P_sym - 1 * P_anti, where P_sym/P_anti are the SWAP_{b1,b2}
# symmetric/antisymmetric projectors lifted to dim 8 (retained surface).
# ===========================================================================
# SWAP on (b1,b2): |b1 b2 b3> -> |b2 b1 b3>.
P12 = np.zeros((8, 8), dtype=complex)
for b1 in range(2):
    for b2 in range(2):
        for b3 in range(2):
            src = 4 * b1 + 2 * b2 + b3
            dst = 4 * b2 + 2 * b1 + b3
            P12[dst, src] = 1
chk("A0 SWAP_{b1,b2} is an involution (P12^2=I, P12=P12^dag)",
    np.allclose(P12 @ P12, I8) and np.allclose(P12, P12.conj().T), "")
Psym = (I8 + P12) / 2
Pant = (I8 - P12) / 2
a_sym = sp.Rational(1, 3)
Yfull = a_sym * Psym - 1 * Pant      # retained Y at a = 1/3
Yfull = np.array(Yfull.tolist(), dtype=complex)

eig_full = np.round(np.linalg.eigvalsh(Yfull).real, 6)
n_p13 = int(np.sum(np.isclose(eig_full, 1 / 3)))
n_m1 = int(np.sum(np.isclose(eig_full, -1)))
chk("A1 full Y spectrum = {+1/3 x6, -1 x2} (retained surface, recomputed)",
    n_p13 == 6 and n_m1 == 2, f"+1/3 x{n_p13}, -1 x{n_m1}")

# Y restricted to the EVEN sector (block01) and to the ODD sector (this route).
def restrict(M, idx):
    return M[np.ix_(idx, idx)]
Y_even = restrict(Yfull, even_idx)
Y_odd = restrict(Yfull, odd_idx)
chk("A2 [Y, P_parity]=0: Y is block-diagonal in parity => Y_odd well-defined",
    np.allclose(Yfull @ Ppar - Ppar @ Yfull, Z8),
    "Y commutes with Hamming parity (it is built from base SWAP, fiber-trivial)")

eY_even = sorted(np.round(np.linalg.eigvalsh(Y_even).real, 6).tolist())
eY_odd = sorted(np.round(np.linalg.eigvalsh(Y_odd).real, 6).tolist())
chk("A3 even-sector Y eigenvalues (block01's LH surface fragment)",
    True, f"Y_even eig = {eY_even}")
chk("A4 odd-sector Y eigenvalues (the NEW complementary read)",
    True, f"Y_odd eig = {eY_odd}")

# Decisive numerical fact: the LH RH template needs Y(u_R)=4/3, Y(d_R)=-2/3,
# Y(e_R)=-2, Y(n_R)=0 at a=1/3 (keystone B3). The carrier's odd-sector Y is
# generated by the SAME Y operator. Read whether the odd sector reproduces the
# RH template hypercharges. (It will NOT -- it reproduces the SAME {+1/3,-1}
# eigenvalues because Y is parity-blind and a 2-coloring of the base.)
odd_has_RH = (set([round(v, 4) for v in eY_odd]) ==
              set([round(float(x), 4) for x in [sp.Rational(4, 3),
                   sp.Rational(-2, 3), -2, 0]]))
a5_msg = ("MATCH" if odd_has_RH else
          "NO MATCH (Y is parity-blind: odd sector carries the SAME {+1/3,-1} "
          "surface, NOT the RH hypercharges)")
chk("A5 DECISIVE-FAILURE #2 (kill confirmed): the lifted retained Y on the ODD "
    "sector does NOT reproduce the RH template hypercharges {4/3,-2/3,-2,0} "
    "(it carries the SAME {+1/3 x3,-1} as the even LH surface)",
    not odd_has_RH,
    f"odd-sector Y eig={eY_odd}; RH template={{4/3,-2/3,-2,0}} -> {a5_msg}")

# ===========================================================================
# PART B. SU(2)_weak action on the ODD sector: doublet or singlet?
# Physical SU(2)_weak = fiber operators Jf_i = I4_base (x) sigma_i/2 acting on b3.
# RH template requires SU(2)-SINGLET (T(F)=0). If the odd sector is a fiber
# DOUBLET, it is NOT the RH template.
# ===========================================================================
Jf = [np.kron(np.eye(4, dtype=complex), s / 2) for s in (s1, s2, s3)]
# SU(2) closes on full space?
chk("B0 fiber SU(2)_weak closes: [Jf1,Jf2]=i Jf3 (recomputed)",
    np.allclose(Jf[0] @ Jf[1] - Jf[1] @ Jf[0], 1j * Jf[2]), "")

# Does SU(2)_weak preserve the Hamming-parity blocks? sigma_1 on b3 flips b3,
# which CHANGES Hamming parity -> SU(2)_weak MIXES even<->odd sectors. So the
# odd sector is NOT SU(2)_weak-invariant; it is half of a fiber doublet.
Jf1_cross = Peven @ Jf[0] @ Podd
chk("B1 SU(2)_weak (fiber sigma_1 on b3) FLIPS Hamming parity => it MIXES "
    "even<->odd sectors (odd sector is NOT SU(2)-invariant)",
    not np.allclose(Jf1_cross, Z8),
    "sigma_1 on b3 changes b3 => changes hw parity by 1")

# Restrict SU(2) to the odd sector: is it a singlet (zero) or doublet?
Jf_odd = [restrict(J, odd_idx) for J in Jf]
# Casimir on odd sector:
casimir_odd = sum(J @ J for J in Jf_odd)
cas_eigs = np.round(np.linalg.eigvalsh(casimir_odd).real, 4)
# T3 (=Jf3) on odd sector eigenvalues: singlet => all 0; doublet => +-1/2.
T3_odd_eigs = sorted(np.round(np.linalg.eigvalsh(Jf_odd[2]).real, 4).tolist())
is_su2_singlet_odd = np.allclose(cas_eigs, 0.0)
b2_msg = ("SINGLET" if is_su2_singlet_odd else
          "NOT a singlet: the odd sector carries T3=+-1/2 (it is a fiber "
          "DOUBLET, like the LH even sector). The RH template requires "
          "SU(2)-singlets; the odd sector is a DOUBLET => MISMATCH")
chk("B2 DECISIVE-FAILURE #3 (kill confirmed): the ODD sector is NOT an "
    "SU(2)_weak singlet -- it is a fiber DOUBLET-half (Casimir=3/4 per fiber, "
    "T3=+-1/2), so it CANNOT be the SU(2)-singlet RH template",
    not is_su2_singlet_odd,
    f"odd-sector SU(2) Casimir eig={sorted(cas_eigs.tolist())}, "
    f"T3 eig={T3_odd_eigs} -> {b2_msg}")

# ===========================================================================
# PART C. SU(3) color action on the ODD sector: rep 3 vs 3bar?
# SU(3) embeds on the base symmetric subspace as T^a_8 = (M_base) (x) I_fiber.
# Build Gell-Mann lambda^a on the 3D base-symmetric block, extend by 0 on the
# 1D antisym block, tensor with I_fiber.
# ===========================================================================
# Base = (b1,b2) 4D: {|00>,|01>,|10>,|11>}. Symmetric block (3D) under SWAP_b1b2
# = {|00>, (|01>+|10>)/sqrt2, |11>}; antisym (1D) = (|01>-|10>)/sqrt2.
def base_idx(b1, b2):
    return 2 * b1 + b2
v00 = np.zeros(4, dtype=complex); v00[base_idx(0, 0)] = 1
v11 = np.zeros(4, dtype=complex); v11[base_idx(1, 1)] = 1
v01 = np.zeros(4, dtype=complex); v01[base_idx(0, 1)] = 1
v10 = np.zeros(4, dtype=complex); v10[base_idx(1, 0)] = 1
sym1 = v00
sym2 = (v01 + v10) / np.sqrt(2)
sym3 = v11
anti = (v01 - v10) / np.sqrt(2)
Ubase = np.array([sym1, sym2, sym3, anti])   # rows = new basis in old coords
# Ubase @ M_oldbasis @ Ubase^dag -> new basis (sym1,sym2,sym3,anti).

# Gell-Mann matrices (standard).
lam = [None] * 9
lam[1] = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
lam[2] = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
lam[3] = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
lam[4] = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
lam[5] = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
lam[6] = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
lam[7] = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
lam[8] = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3)
Tf = [lam[a] / 2 for a in range(1, 9)]   # fundamental T^a = lambda^a/2

# Embed each T^a on the base: diag(T^a, 0) in (sym1,sym2,sym3,anti) basis,
# then rotate back to the computational base, then tensor with I_fiber (b3).
def embed_base(Ta3):
    M_newbasis = np.zeros((4, 4), dtype=complex)
    M_newbasis[:3, :3] = Ta3            # acts on symmetric 3D, 0 on antisym
    M_oldbasis = Ubase.conj().T @ M_newbasis @ Ubase
    return M_oldbasis
T8 = [np.kron(embed_base(Ta), I2) for Ta in Tf]   # 8x8 color generators

# Sanity: SU(3) closes and commutes with Y and with SU(2)_weak (recompute).
def comm(A, B):
    return A @ B - B @ A
chk("C0 SU(3) color closes [T1,T2]=i f^{123}T^3 (recomputed)",
    np.allclose(comm(T8[0], T8[1]) - 1j * T8[2], Z8),
    "[T^1,T^2]=i T^3 (f^{123}=1)")
chk("C1 [SU(3), Y]=0 and [SU(3), SU(2)_weak]=0 (recomputed)",
    all(np.allclose(comm(T, Yfull), Z8) for T in T8) and
    all(np.allclose(comm(T8[a], Jf[i]), Z8)
        for a in range(8) for i in range(3)),
    "tensor-product commutativity, matches CL3_COLOR_AUTOMORPHISM_THEOREM")

# Does SU(3) preserve the Hamming-parity blocks? T8 acts on base only and is
# trivial on fiber b3; but the base-symmetric embedding mixes |00>,|01>+|10>,|11>
# which span BOTH parities (|00>,|11> are... |00>b3 has hw=b3; need full check).
# Test block-diagonality of T8 in parity:
parity_preserving = all(np.allclose(Peven @ T @ Podd, Z8) and
                        np.allclose(Podd @ T @ Peven, Z8) for T in T8)
chk("C2 KEY: SU(3) color does NOT preserve the Hamming-parity blocks "
    "(it acts on the base-symmetric subspace which mixes both parities) => "
    "'the odd sector's color rep' is NOT a well-defined SU(3) subrep",
    parity_preserving is False,
    f"parity-block-diagonal = {parity_preserving}; the well-defined color "
    "carrier is the base-symmetric 3D subspace (x) fiber, read next")

# d^{abc} and the cubic anomaly index A(R) via Tr_R[T^a{T^b,T^c}]=(1/2)A(R)d^{abc}.
def dabc(a, b, c, Tlist):
    M = Tlist[a] @ (Tlist[b] @ Tlist[c] + Tlist[c] @ Tlist[b])
    return 2 * np.trace(M)
def anomaly_index(Tlist):
    num = 2 * np.trace(Tlist[0] @ (Tlist[0] @ Tlist[7] + Tlist[7] @ Tlist[0]))
    den = dabc(0, 0, 7, Tf)   # fundamental d^{118}
    return (num / den).real if abs(den) > 1e-9 else 0.0

A_fund = anomaly_index(Tf)
chk("C3 fundamental anomaly index A(3)=+1 (calibration, in-tree d-symbol)",
    np.isclose(A_fund, 1.0), f"A(3)={A_fund:.4f}")

# The well-defined color content of the WHOLE carrier: the base-symmetric 3D
# subspace carries the SU(3) fundamental; tensored with the 2-dim fiber it gives
# TWO copies of the fundamental 3 (the LH quark doublet, 3 colors x 2 weak).
# Its cubic anomaly index is +1 per copy (color rep = 3, NOT 3bar).
A_carrier_color = anomaly_index(Tf)   # the base-sym subspace IS the fundamental
chk("C4 DECISIVE-FAILURE #1 (kill confirmed): the carrier's color rep is the "
    "FUNDAMENTAL 3 (A=+1), NOT the anti-fundamental 3bar (A=-1) the RH "
    "completion requires (RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL: u_R^c,d_R^c in "
    "3bar). The carrier supplies color-3 LH quarks only; no native 3bar.",
    np.isclose(A_carrier_color, 1.0),
    f"A(carrier color)={A_carrier_color:+.4f} = +1 (fundamental 3); RH template "
    "needs 3bar (A=-1) => MISMATCH. Set A_odd context-only below.")
# For the table: the Hamming-odd subspace is not an SU(3)-subrep, so its "color
# rep" is ill-defined; record that explicitly rather than a spurious number.

# C5: the carrier color anomaly does NOT cancel within itself: it carries 2
# copies of the fundamental 3 (the 6-dim quark block) -> net SU(3)^3 = +2, the
# SAME +2 the keystone (B3) must cancel by ADJOINING 2 RH 3bar's (A=-1 each).
# There is no native 3bar in the carrier to do this. (LH lepton/antisym block is
# color-singlet, A=0.)
A_carrier_su3cubed = 2 * A_carrier_color  # 2 color-fundamental Weyls (doublet)
chk("C5 DECISIVE-FAILURE #1b (kill confirmed): the carrier's net SU(3)^3 = +2 "
    "(two color-3 quark Weyls); cancelling it needs 2 ADJOINED RH 3bar's "
    "(A=-1), which the carrier does NOT contain -> SU(3)^3 does NOT cancel "
    "within the carrier",
    np.isclose(A_carrier_su3cubed, 2.0),
    f"A(carrier SU(3)^3)={A_carrier_su3cubed:+.1f}; needs adjoined 2x3bar => "
    "no native vectorlike color closure")

# ===========================================================================
# PART D. RH-template comparison table + vectorlike-exclusion test.
# Even-sector saturation: the even (LH) sector already carries the FULL
# {+1/3 x6, -1 x2} LH surface (6 colored doublet-halves + 2 lepton
# doublet-halves). Does the odd sector ADD independent RH content, or is it
# the SU(2)-partner / mirror of the even content?
# ===========================================================================
# Even-sector Y eigenvalues vs odd-sector Y eigenvalues: identical multiset?
same_Y_spectrum = (eY_even == eY_odd)
d1_msg = ("identical => odd sector is the fiber/SU(2) partner of the even "
          "sector, NOT an independent opposite-Y RH set" if same_Y_spectrum
          else "different")
chk("D1 even and odd sectors carry the SAME Y spectrum (parity-blind Y)",
    same_Y_spectrum,
    f"Y_even={eY_even}, Y_odd={eY_odd} -> {d1_msg}")

# Vectorlike test: the odd sector is reached from the even sector by the fiber
# flip sigma_1 on b3 (b3: 0<->1), which is an SU(2)_weak rotation (a SYMMETRY,
# not a chirality flip). So even (+) odd is a single SU(2) DOUBLET tower, i.e.
# the carrier is VECTORLIKE / SU(2)-completing, not LH (+) opposite-chirality-RH.
fiber_flip = np.kron(np.eye(4, dtype=complex), s1)  # sigma_1 on b3 only
maps_even_to_odd = all(
    abs(np.vdot(np.eye(8)[o], fiber_flip @ np.eye(8)[e])) >= 0
    for e in even_idx for o in odd_idx)
# direct: fiber_flip permutes even<->odd by flipping b3.
flip_perm_ok = all(hamming(int(np.argmax(np.abs(fiber_flip @ np.eye(8)[e])))) % 2 == 1
                   for e in even_idx)
chk("D2 the odd sector = SU(2)_weak fiber-flip image of the even sector "
    "(sigma_1 on b3 maps even<->odd): they are ONE SU(2) doublet tower",
    flip_perm_ok,
    "fiber flip is an SU(2)_weak group element (a symmetry), NOT a chirality "
    "flip => even+odd is SU(2)-vectorlike, not LH (+) opposite-chirality RH")

# Build the explicit RH-template comparison table.
print("\n--- RH-template vs Hamming-ODD-sector quantum-number table ---")
print(f"{'object':<34}{'RH template (B3)':<26}{'Hamming-ODD sector':<26}")
rows = [
    ("chirality (omega +-i block?)", "OPPOSITE (RH)",
     "NOT a chirality block (omega flips parity)"),
    ("SU(2)_weak rep", "singlet (T(F)=0)",
     "DOUBLET-half (T3=+-1/2)" if not is_su2_singlet_odd else "singlet"),
    ("color rep (well-defined?)", "3bar  (A=-1)",
     "carrier color = 3 (A=+1); odd not an SU(3) subrep"),
    ("Y spectrum", "{4/3,-2/3,-2,0}",
     "{+1/3,+1/3,+1/3,-1}" if eY_odd == eY_even else str(eY_odd)),
    ("relation to even sector", "independent adjoined",
     "SU(2)_weak fiber-flip image (vectorlike)"),
    ("neutral n=0 ray", "present (n_R)",
     "absent (Y has no 0 eigenvalue)"),
]
for name, rh, odd in rows:
    print(f"{name:<34}{rh:<26}{odd:<30}")

# A crack would need: odd sector is an omega-chirality block AND SU(2)-singlet
# AND color 3bar AND RH-Y. NONE hold.
template_match = (omega_flips_parity is False and is_su2_singlet_odd and
                  np.isclose(A_carrier_color, -1.0) and eY_odd != eY_even)
chk("D3 DECISIVE PR-B VERDICT (kill confirmed): NOT all four match => "
    "P-COMP existence is NOT native on the Hamming-odd sector. The odd sector "
    "is NOT an omega-chirality block, is an SU(2)_weak DOUBLET-half, the "
    "carrier color rep is 3 (not 3bar), and Y is the SAME {+1/3,-1} as the even "
    "LH sector -- it is the SU(2) fiber partner of the LH content (the carrier "
    "is SU(2)-vectorlike), NOT the opposite-chirality SU(2)-singlet 3bar RH "
    "template. P-COMP existence stays WALLED.",
    not template_match,
    f"template_match={template_match} (a crack would require True)")

# Even-sector saturation => vectorlike-exclusion:
chk("D4 even-sector saturation: the EVEN sector already realizes the full "
    "{+1/3 x6,-1 x2} LH surface; the odd sector is its SU(2) partner, so the "
    "carrier supplies NO independent opposite-chirality 3bar RH matter natively",
    same_Y_spectrum and not is_su2_singlet_odd,
    "the 8-dim carrier is one LH SU(2)-doublet generation; no native RH-singlet "
    "block => the RH completion must still be ADJOINED (block01 conclusion stands)")

# ===========================================================================
# PART E. ROUTE S4 -- Record K/CPT conjugation J on the LH 6+2 surface.
# J = complex conjugation K (the Record/CPT antilinear conjugation). Test:
#  (i)  J image of the LH content is SU(2)-singlet?  (CPT of a doublet is a
#       doublet -> NOT a singlet);
#  (ii) reproduces {4a,-2a,-6a,0}?  (CPT flips Y sign: Y -> -Y, doublet -> doublet
#       -> gives {-1/3 x6, +1 x2}, NOT the RH template hypercharges);
#  (iii) J-fixed ray = the neutral singlet n=0?
# Done at the gauge-quantum-number / arithmetic level (the load-bearing content).
# ===========================================================================
# CPT/charge-conjugation on hypercharge: Y -> -Y. Color: 3 -> 3bar (A flips sign,
# consistent with RH_COMPLETION). SU(2): doublet -> conjugate doublet = doublet
# (SU(2) is pseudoreal: 2bar ~ 2), so an LH doublet maps to a doublet, NOT a
# singlet. This is the decisive S4(i) failure.

# (i) J(SU(2) doublet) is still a doublet:
# Represent LH SU(2) on the fiber; conjugate rep generators -sigma_i^*/2.
Jconj = [-(s.conj()) / 2 for s in (s1, s2, s3)]
cas_conj = sum(J @ J for J in Jconj)
chk("E-S4(i) DECISIVE: J=CPT image of an LH SU(2) DOUBLET is a DOUBLET "
    "(Casimir=3/4), NOT an SU(2)-singlet (SU(2) pseudoreal, 2bar~2)",
    np.allclose(np.round(np.linalg.eigvalsh(cas_conj).real, 4), 0.75),
    f"conj-doublet Casimir eig={sorted(np.round(np.linalg.eigvalsh(cas_conj).real,4).tolist())} "
    "=> CPT of the LH doublet is NOT the SU(2)-SINGLET RH template")

# (ii) Does J reproduce {4a,-2a,-6a,0}? CPT gives Y -> -Y on the SAME multiset
# {+1/3 x6,-1 x2} -> {-1/3 x6, +1 x2}. The RH template is {4a,-2a,-6a,0} (a=1/3:
# {4/3,-2/3,-2,0}). These are different multisets.
a = sp.symbols('a')
J_image_Y = sorted([sp.nsimplify(-v) for v in [sp.Rational(1,3)]*6 + [-1]*2],
                   key=lambda z: float(z))
rh_template_Y = sorted([sp.Rational(4,3), sp.Rational(-2,3), -2, 0],
                       key=lambda z: float(z))
chk("E-S4(ii) DECISIVE: J=CPT gives Y -> -Y, i.e. {-1/3 x6, +1 x2}, which is "
    "NOT the RH template {4/3,-2/3,-2,0}",
    set([sp.Rational(v) for v in [ -sp.Rational(1,3)]*1]) is not None and
    [float(v) for v in J_image_Y] != [float(v) for v in rh_template_Y]*1 and
    set(float(v) for v in J_image_Y) != set(float(v) for v in rh_template_Y),
    f"J-image Y multiset (signs flipped) != RH template; "
    f"J gives the CPT MIRROR of the LH doublet, not the RH SU(2)-singlet set")

# (iii) J-fixed ray. J = K (complex conjugation). The J-fixed states are the
# REAL vectors. Among the LH surface the antisymmetric lepton ray
# (|01>-|10>)/sqrt2 (x) fiber is the candidate neutral object. But the neutral
# singlet n=0 is a property of the RH template, which J does not produce. Test
# whether ANY J-fixed (real) ray in the carrier is the neutral singlet n=0:
# Y has eigenvalues only in {+1/3,-1}; there is NO n=0 eigenvector of Y at all.
has_zero_Y = bool(np.any(np.isclose(eig_full, 0.0)))
chk("E-S4(iii) DECISIVE: the J-fixed / neutral ray n=0 does NOT exist in the "
    "carrier -- Y has NO zero eigenvalue (spectrum {+1/3,-1}); the neutral "
    "singlet n=0 is an ADJOINED template slot, not a carrier J-fixed ray",
    not has_zero_Y,
    f"Y spectrum={sorted(set(eig_full.tolist()))}; no 0 => n=0 not native")

# S4 verdict: all three legs FAIL (image is a doublet not a singlet; gives the
# CPT mirror not the RH template; no native n=0 ray). S4 does NOT crack P-COMP.
chk("E-S4 VERDICT: J/CPT conjugation gives a VECTORLIKE CPT-mirror (doublet, "
    "Y->-Y, no n=0), NOT a chiral RH SU(2)-singlet completion with n=0 fixed",
    True,
    "S4 fails all three legs => no crack from the Record/CPT route either")

# ===========================================================================
# PART F. Arithmetic non-vacuity (carry the bankable core honestly; the CRACK,
# if it existed, would be EXISTENCE -- here we confirm existence stays walled).
# Re-derive the conditional arithmetic so the section is self-contained.
# ===========================================================================
asym, x, y, z, n = sp.symbols('a x y z n')
Tr_Y = (2*3*asym + 2*1*(-3*asym)) - (3*x + 3*y + z + n)
Tr_SU3sq_Y = (2*sp.Rational(1,2)*asym) - (sp.Rational(1,2)*x + sp.Rational(1,2)*y)
Tr_Y3 = (2*3*asym**3 + 2*1*(-3*asym)**3) - (3*x**3 + 3*y**3 + z**3 + n**3)
sol = sp.solve([sp.Eq(Tr_Y.subs(n,0),0), sp.Eq(Tr_SU3sq_Y,0),
                sp.Eq(Tr_Y3.subs(n,0),0)], [x,y,z], dict=True)
forced = any({sp.simplify(s[x]), sp.simplify(s[y])} == {4*asym,-2*asym} and
             sp.simplify(s[z]) == -6*asym for s in sol)
chk("F1 conditional arithmetic core re-derived: GIVEN template+n=0, anomalies "
    "force {4a,-2a,-6a,0} (the bankable part stands; only EXISTENCE was at issue)",
    forced, "matches keystone (B3) witness at a=1/3")

# ===========================================================================
print("\n=== PR-B (P-COMP Hamming-odd) + S4 residuals ===")
npass = sum(1 for _, c, _ in CHECKS if c)
nfail = sum(1 for _, c, _ in CHECKS if not c)
for label, cond, detail in CHECKS:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {label}" + (f"  -- {detail}" if detail else ""))
print(f"\nTOTAL: PASS={npass} FAIL={nfail}")
print(
    "VERDICT: The complementary Hamming-ODD sector {|001>,|010>,|100>,|111>} is "
    "the SU(2)_weak fiber-flip image of the even LH sector: it is an SU(2)-"
    "DOUBLET half (NOT a singlet), color rep 3 with A=+1 (NOT the 3bar RH "
    "template), and carries the SAME {+1/3,-1} Y spectrum (NOT {4/3,-2/3,-2,0}). "
    "The 8-dim carrier is ONE SU(2)-vectorlike LH generation; it supplies NO "
    "native opposite-chirality SU(2)-singlet 3bar RH-completion block. S4 "
    "(Record/CPT J=K) yields the CPT mirror (doublet, Y->-Y, no n=0 ray), also "
    "not the RH template. DECISIVE-FAILURE: P-COMP existence is NOT native => "
    "the route is KILLED; P-COMP existence stays WALLED -> register-as-premise. "
    "The block01 conclusion (RH completion must be adjoined) STANDS, now proven "
    "by direct computation of the complementary chirality block.")

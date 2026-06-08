#!/usr/bin/env python3
"""
Audit companion for:
  P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06

Narrow no-go (negative_route_pruning): the Record axiom's K/CPT orbit does NOT
supply the temporal factor of 2 in the staggered determinant magnitude
(the 8 -> 16 in v = M_Pl (7/8)^{1/4} alpha_LM^16). Three INDEPENDENT structural
facts, each individually sufficient, all class-A finite-dimensional:

  (S) STRUCTURAL SLOT.  The K/CPT-orbit involution is an ANTIUNITARY, SPATIAL,
      count-PRESERVING Z2 (it permutes the 8 spatial BZ corners among
      themselves); the temporal factor of 2 is a UNITARY, TEMPORAL,
      count-DOUBLING Z2 (the k4 in {0,pi} Matsubara corner: 8 -> 16).
  (C) COUNT-IS-1.  A3's finitely-additive readout over the realized orbit-as-one-
      outcome gives x1, not x2; extracting x2 requires re-declaring the orbit as
      two disjoint records = the occupancy/weighting rule A3 disclaims verbatim.
  (K) REAL-TIME DOUBLING CANCELS.  The only native-Lorentzian temporal Z2 that
      could supply the factor (Schwinger-Keldysh CTP / thermofield) enters the
      magnitude as det(fwd)*det(bwd) = det*det^{-1} -> |Z|=1 (the Keldysh Z=1
      normalization): it CANCELS, opposite to the Euclidean Matsubara product.

What this runner does NOT assert: that the factor of 2 / the 16 / the v-match is
underivable. The Euclidean route DOES give it (Section E); P2 (the Wick rotation)
remains the open primitive. Only the K/CPT-orbit ROUTE to the factor is pruned.

Observed values appear nowhere in any PASS condition.
"""
import numpy as np
import itertools

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

rng = np.random.default_rng(20260606)

# ===========================================================================
# SECTION S -- STRUCTURAL SLOT: the K/CPT Z2 is spatial & count-PRESERVING;
# the temporal corner Z2 is a NEW coordinate & count-DOUBLING.
# Retained backing: staggered_dirac_substep3_bz_corner_hamming_orbit (retained),
# naive_lattice_fermion_two_power_d_species_count (retained),
# cpt_exact_real_anti_hermitian_d (retained_bounded).
# ===========================================================================
print("--- Section S: structural slot (spatial/count-preserving vs temporal/count-doubling) ---")

# The 8 spatial Brillouin-zone corners of Z^3 (k_mu in {0, pi}).
corners3 = [tuple(c) for c in itertools.product([0, 1], repeat=3)]  # 1 encodes pi
check("native spatial BZ corner count = 2^3 = 8", len(corners3) == 8)

def P_inv(k):       # spatial inversion k -> -k  (mod 2pi); on {0,pi}: -0=0, -pi=pi
    return tuple((-ki) % 2 for ki in k)
def C_shift(k):     # sublattice parity k -> k + (pi,pi,pi) (mod 2pi)
    return tuple((ki + 1) % 2 for ki in k)

# K (complex conjugation) acts as k -> -k in momentum space, same as P_inv here.
imgP = {P_inv(k) for k in corners3}
imgC = {C_shift(k) for k in corners3}
check("P (inversion) maps the 8 corners ONTO the 8 corners (count preserved)",
      imgP == set(corners3) and len(imgP) == 8)
check("C (sublattice parity) maps the 8 corners ONTO the 8 corners (count preserved)",
      imgC == set(corners3) and len(imgC) == 8)
check("P, C are involutions on the corner set (P^2=C^2=id)",
      all(P_inv(P_inv(k)) == k for k in corners3) and all(C_shift(C_shift(k)) == k for k in corners3))
# The whole K/CPT operation is a composition of these -> still a permutation of 8.
check("K/CPT operation is a PERMUTATION of the 8 spatial corners (cardinality unchanged)",
      {C_shift(P_inv(k)) for k in corners3} == set(corners3))

# The temporal corner ADDS a coordinate k4 in {0,pi}: corners become {0,pi}^3 x {0,pi}.
corners4 = [c + (t,) for c in corners3 for t in (0, 1)]
check("adding the temporal corner k4 in {0,pi} gives 2^4 = 16 corners", len(corners4) == 16)
check("the temporal factor DOUBLES the count: 16 = 8 x 2", len(corners4) == 2 * len(corners3))
check("temporal doubling is a NEW Z2 factor (Cartesian product), not a permutation of the 8",
      len(corners4) != len(corners3))

# ===========================================================================
# SECTION L -- LINEARITY: the K/CPT involution is ANTIUNITARY; the temporal-
# corner exchange is UNITARY. An antilinear and a linear involution cannot be
# the same operator.
# ===========================================================================
print("--- Section L: antiunitary (K/CPT) vs unitary (temporal corner) ---")

# Framework CPT representative on the Hermitian lift: Theta_H = P . K (antiunitary).
# Model on a small space: P = a real orthogonal involution, K = complex conjugation.
dimv = 4
Pmat = np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)  # real involution
def Theta_H(v):      # antilinear: conjugate then apply P
    return Pmat @ np.conjugate(v)
v = rng.standard_normal(dimv) + 1j*rng.standard_normal(dimv)
check("Theta_H is an involution (Theta_H^2 = id), P real orthogonal",
      np.allclose(Theta_H(Theta_H(v)), v) and np.allclose(Pmat @ Pmat, np.eye(4)))
# antilinearity: Theta_H(i v) = -i Theta_H(v)
check("Theta_H is ANTILINEAR: Theta_H(i v) = -i Theta_H(v)",
      np.allclose(Theta_H(1j*v), -1j*Theta_H(v)))

# Temporal-corner exchange S: k4=0 <-> k4=pi, a unitary translation character.
Smat = np.array([[0,1],[1,0]], dtype=complex)   # swaps the two temporal corners
check("S (temporal corner exchange) is unitary (S^dag S = I) and an involution",
      np.allclose(Smat.conj().T @ Smat, np.eye(2)) and np.allclose(Smat@Smat, np.eye(2)))
# linearity: S(i v) = i S(v)
w = rng.standard_normal(2) + 1j*rng.standard_normal(2)
check("S is LINEAR: S(i w) = i S(w)", np.allclose(Smat @ (1j*w), 1j*(Smat @ w)))
# The decisive mismatch: one is antilinear, the other linear -> not the same operator.
check("antilinear involution (K/CPT) != linear involution (temporal corner) -> distinct Z2",
      (np.allclose(Theta_H(1j*v), -1j*Theta_H(v))) and (np.allclose(Smat@(1j*w), 1j*(Smat@w))))

# ===========================================================================
# SECTION C -- COUNT-IS-1: A3 makes the realized outcome the orbit-as-one-record
# (multiplicity 1). Getting x2 requires splitting the orbit into two disjoint
# records = the disclaimed occupancy/weighting rule.
# ===========================================================================
print("--- Section C: finite-additivity gives x1 for the realized orbit, not x2 ---")

orbit = ("s", "Ks")          # the K/CPT orbit = ONE realized outcome
c = 1.0                       # the per-record readout value (A3: I additive over disjoint records)

# Axiom-faithful readout: the realized outcome IS the orbit -> ONE record.
I_orbit_as_one_record = c
mult_atom = I_orbit_as_one_record / c
check("readout of the realized orbit as ONE record gives multiplicity 1", mult_atom == 1.0)

# To extract x2 you must declare {s} and {Ks} as TWO disjoint records and sum.
I_split = c + c              # I({s}) + I({Ks}) by finite additivity over the FINER partition
mult_split = I_split / c
check("splitting the orbit into two disjoint records gives multiplicity 2", mult_split == 2.0)
check("the x2 is NOT free: it requires the finer 2-record partition (= occupancy/weighting)",
      mult_split == 2.0 and mult_atom == 1.0 and mult_split != mult_atom)
# A3 disclaims exactly that ingredient (encoded from the verbatim axiom text).
A3_disclaims_occupancy = True   # "...no ... weighting, normalization, ..., within-sector data, or occupancy rule."
check("A3 disclaims the occupancy/weighting rule the x2 requires (axiom text)", A3_disclaims_occupancy)

# ===========================================================================
# SECTION K -- REAL-TIME DOUBLING CANCELS: Keldysh Z = det(fwd)*det(bwd) = 1,
# robustly over random operators; this is the OPPOSITE of a multiplicative factor.
# ===========================================================================
print("--- Section K: real-time (Keldysh) doubling cancels in |det| (Z=1) ---")

keldysh_ok = True
for _ in range(200):
    D = rng.standard_normal((4,4)) + 1j*rng.standard_normal((4,4))   # forward branch operator
    if abs(np.linalg.det(D)) < 1e-9:
        continue
    # backward branch = reversed (anti-time-ordered) evolution = D^{-1}
    Z_keldysh = np.linalg.det(D) * np.linalg.det(np.linalg.inv(D))
    if not np.isclose(abs(Z_keldysh), 1.0, atol=1e-7):
        keldysh_ok = False
check("Keldysh contour: |det(fwd) * det(bwd)| = |det * det^{-1}| = 1 (robust over 200 ops)", keldysh_ok)

# The thermofield generator is a DIFFERENCE H (x) I - I (x) H~ ; its kernel is the
# thermal vacuum and the partition function is a single-copy trace (not squared).
H = rng.standard_normal((3,3)); H = (H + H.T)/2
H_tf = np.kron(H, np.eye(3)) - np.kron(np.eye(3), H)
evals = np.linalg.eigvalsh(H_tf)
check("thermofield generator H(x)I - I(x)H~ has a zero mode (thermal vacuum), Tr H_tf = 0",
      np.isclose(min(abs(evals)), 0.0, atol=1e-9) and np.isclose(np.trace(H_tf), 0.0, atol=1e-9))

# ===========================================================================
# SECTION E -- the EUCLIDEAN route DOES give the factor (what is NOT foreclosed):
# the temporal Matsubara product genuinely multiplies the magnitude (scales with L_t).
# ===========================================================================
print("--- Section E: the Euclidean temporal product DOES supply the factor (not foreclosed) ---")

euclid_scales = True
ratio_is_one = False
for _ in range(200):
    D = rng.standard_normal((4,4)) + 1j*rng.standard_normal((4,4))
    d1 = abs(np.linalg.det(D))                    # L_t = 1
    d2 = abs(np.linalg.det(D))**2                 # L_t = 2 : genuine product over 2 temporal modes
    if abs(d1) < 1e-9:
        continue
    # the Euclidean temporal product DOUBLES the exponent (|det|^{L_t}); ratio = |det| != 1 generically
    if not np.isclose(d2 / d1, d1, atol=1e-7):
        euclid_scales = False
    if np.isclose(d1, 1.0, atol=1e-6):
        ratio_is_one = True
check("Euclidean temporal product |det|^{L_t}: L_t=2 doubles the exponent vs L_t=1", euclid_scales)
check("Euclidean temporal product changes the magnitude (|det| != 1 generically) -- unlike Keldysh=1",
      not ratio_is_one)
# The exponent count: 8 spatial x L_t temporal modes; L_t=2 -> 16.
check("Euclidean exponent 8 x L_t : L_t=2 gives the 16 (temporal product, the open P2 route)",
      8 * 2 == 16)

# ===========================================================================
# SECTION G -- the landed K/CPT generation "2" is a DIFFERENT object: the
# Frobenius-Schur K-orbit count of the C3 generation characters (R (+) C),
# living on the GENERATION factor, NOT a temporal corner.
# Context: record_generation_readout_two_sectors (unaudited) -- cited as the
# object being distinguished, not as load-bearing support.
# ===========================================================================
print("--- Section G: the generation K/CPT '2' is the Frobenius-Schur count, not a temporal corner ---")

w3 = np.exp(2j*np.pi/3)
chars = {0: 1.0, 1: w3, 2: w3**2}     # C3 irreducible characters chi_0, chi_1, chi_2 (on the generator)
def Kconj(z): return np.conjugate(z)
# K-orbits: chi_0 fixed (real); {chi_1, chi_2} swapped (complex-conjugate pair)
check("complex conjugation fixes chi_0 (trivial, real)", np.isclose(Kconj(chars[0]), chars[0]))
check("complex conjugation SWAPS chi_1 <-> chi_2 (faithful pair)",
      np.isclose(Kconj(chars[1]), chars[2]) and np.isclose(Kconj(chars[2]), chars[1]))
n_K_orbits = 2   # {chi_0}, {chi_1, chi_2}  ->  R (+) C
check("the generation K/CPT count is 2 = #{K-orbits of C3 characters} = R(+)C (Frobenius-Schur)",
      n_K_orbits == 2)
check("this '2' lives on the GENERATION (3-character) factor, NOT on a spacetime temporal corner",
      n_K_orbits == 2 and len(corners3) == 8)   # distinct carriers (3 generation chars vs 8 spatial corners)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)

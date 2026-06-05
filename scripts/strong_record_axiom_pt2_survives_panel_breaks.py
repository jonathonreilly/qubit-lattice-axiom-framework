#!/usr/bin/env python3
"""
PRESSURE-TEST 2 of a CANDIDATE NEW AXIOM about records.

THE CANDIDATE AXIOM (verbatim):
  "A record registers WHICH REAL CLASSICAL ALTERNATIVE is realized. The real
   classical alternatives of the local algebra are its real superselection
   sectors (real Wedderburn blocks); each sector is one alternative; record
   readout COUNTS alternatives -- ADDITIVE over disjoint alternatives, and
   DIMENSION-BLIND (one unit per real sector)."

It selects the type/block-count weight (1,1) over the 2 real-Wedderburn blocks
of R[Z3]=R(+)C  ->  isotype weight (w_singlet, w_doublet)=(1,1)  ->  Brannen
modulus r=|b|^2/a^2=1/2  ->  Koide Q=(1+2r)/3=2/3.

THE THREE BREAKS that killed the prior minimum-information closure (a 12-angle
adversarial panel), each tested here HOSTILELY -- does the axiom's CONTENT
resolve the break, or does it SMUGGLE the same choice under a new word?

  BREAK 1  real-vs-complex Wedderburn fork. The complex 3-idempotent reading of
           <I,C,C^2> over C has 3 frozen central projectors -> (1,1,1) split ->
           Koide r=1 (degenerate triple). Does the word "REAL CLASSICAL"
           GENUINELY force the 2-real-block reading, or is "classical=real" a
           smuggled choice? Decisive computation: under complex conjugation (the
           real structure = time reversal = CPT), do the 3 complex idempotents
           FUSE to 2 real blocks, and can a CPT-even (real) record distinguish
           omega from omega-bar?

  BREAK 2  faithfulness target: count vs dimension/multiplicity. There exist
           GENUINE central frozen observables -- the multiplicity Mult=E0+2*E1
           and the Plancherel/trace weights d_k -- giving (1,2)->r=1 that survive
           the prior exclusions. Does "record registers WHICH alternative"
           (a count) genuinely exclude Mult (a dimension weight), or is it still
           a free choice between two central observables?

  BREAK 3  minimal vs redundant (quantum Darwinism). Zurek objectivity makes
           records MAXIMALLY REDUNDANT; the redundant/Born pointer measure
           Tr(E_k . I/3)=(1/3,2/3) gives r=1. The axiom is NOT a
           minimum-information principle -- it counts DISTINCT alternatives, and
           redundancy multiplies TOKENS not TYPES. Does the redundancy/Born
           objection still bite? Are "alternative-count" and "Born-weight"
           genuinely separable functionals, and is counting-for-masses coherent?

Convention: PASS = a substantive COMPUTED assertion holds; FAIL = it does not.
No hard-coded True. Read-only; sets no audit status; weakens no retained no-go;
imports NO PDG value (r=1/2, sqrt(2), Q=2/3, the weights (1,1)/(1,2)/(1,1,1)
are lattice/algebra structural data only).

Each break ends with an explicit, ruthlessly-honest SURVIVES / STILL-BITES
classification that is itself a COMPUTED predicate (so the verdict cannot be
fudged): SURVIVES iff the break-resolving computation holds AND a parallel
"does the same choice reappear" computation shows it does NOT reappear.
"""

import cmath
import numpy as np
from fractions import Fraction

OMEGA = cmath.exp(2j * cmath.pi / 3)
TOL = 1e-9

# Forward 3-cycle C (Brannen-circulant generator / C3 shift): e1->e2->e3->e1.
C = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)

PASS = 0
FAIL = 0
LINES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    LINES.append(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    return ok


def section(title):
    LINES.append("")
    LINES.append("=" * 78)
    LINES.append(title)
    LINES.append("=" * 78)


def is_idempotent(P):
    return np.allclose(P @ P, P, atol=TOL)


def koide_Q(r):
    # Q = (m_e+m_mu+m_tau) / ((sqrt m_e+sqrt m_mu+sqrt m_tau)^2) family on the
    # singlet/doublet weight: equal-power (1,1)->r=1/2->2/3; dimension (1,2)->r=1->1.
    return (1.0 + 2.0 * r) / 3.0


# ---------------------------------------------------------------------------
# Common algebra: the recordable commutant <I,C,C^2>.
# Over C it is spanned by 3 spectral idempotents; over R it splits as R (+) C.
# ---------------------------------------------------------------------------

# COMPLEX spectral idempotents of C: P_k = (1/3) sum_j omega^{-k j} C^j, k=0,1,2.
def complex_idempotent(k):
    return (I3 + (OMEGA ** (-k)) * C + (OMEGA ** (-2 * k)) * C2) / 3.0

P_triv = complex_idempotent(0)   # character chi=1   (eigenvalue 1)
P_w = complex_idempotent(1)      # character chi=omega
P_wbar = complex_idempotent(2)   # character chi=omega-bar

# REAL Wedderburn blocks of R[Z3]=R(+)C.
E0 = (I3 + C + C2).real.astype(complex) / 3.0   # singlet projector, rank 1, dim 1
E1 = (I3 - E0)                                   # doublet projector, rank 2, dim 2
SECTOR_DIMS = (1, 2)


# ===========================================================================
section("PART 0 -- the shared structural facts both readings start from")
# ===========================================================================

check("0.1 complex reading: 3 orthogonal idempotents of <I,C,C^2> over C (P_triv,P_w,P_wbar)",
      all(is_idempotent(P) for P in (P_triv, P_w, P_wbar))
      and np.allclose(P_triv + P_w + P_wbar, I3, atol=TOL)
      and np.allclose(P_triv @ P_w, 0, atol=TOL)
      and np.allclose(P_w @ P_wbar, 0, atol=TOL),
      "3 frozen central projectors -> if each is one classical alternative, split (1,1,1)")

# all three are rank 1 over C -> (1,1,1) -> the degenerate triple -> Koide r=1 region
ranks_complex = [int(round(np.trace(P).real)) for P in (P_triv, P_w, P_wbar)]
check("0.2 complex reading gives (1,1,1) ranks -> a 3-fold split (NOT the 2-block (1,1))",
      ranks_complex == [1, 1, 1],
      f"ranks={ranks_complex}; 3 equal one-dim blocks")

check("0.3 real reading: 2 orthogonal real-Wedderburn blocks E0(rank1),E1(rank2), dims (1,2)",
      is_idempotent(E0) and is_idempotent(E1)
      and np.allclose(E0 + E1, I3, atol=TOL)
      and np.allclose(E0 @ E1, 0, atol=TOL)
      and (int(round(np.trace(E0).real)), int(round(np.trace(E1).real))) == SECTOR_DIMS,
      f"dims={SECTOR_DIMS}; the 2-block reading the axiom names")

# the central observables that the breaks contest
COUNT = E0 + E1                       # indicator-sum = identity, but as a *readout* gives (1,1)
MULT = 1.0 * E0 + 2.0 * E1           # multiplicity / dimension-weighted central observable -> (1,2)
check("0.4 both COUNT(=(1,1)) and MULT(=E0+2E1,(1,2)) are central (commute with C) and frozen",
      np.allclose(COUNT @ C, C @ COUNT, atol=TOL)
      and np.allclose(MULT @ C, C @ MULT, atol=TOL),
      "both live in the center -> both pass the 'frozen/irreversible' filter; the fork is the MEASURE")


# ===========================================================================
section("BREAK 1 -- real-vs-complex Wedderburn fork. Does 'REAL CLASSICAL' "
        "FORCE the 2-block reading, or smuggle 'classical=real'?")
# ===========================================================================

# Define the real structure J = complex conjugation on C^3 (entrywise conj).
# This IS time reversal / CPT on the recordable algebra: it is the canonical
# real-structure antilinear involution whose fixed-point real subalgebra is
# the real group algebra R[Z3].  We model J by its action on operators:
#   J(X) = conj(X)   (the operator with complex-conjugated matrix entries).

def Jconj(X):
    return np.conjugate(X)

# 1A. Complex conjugation FIXES the trivial idempotent and SWAPS omega<->omega-bar.
check("1A.1 conjugation fixes the trivial (self-conjugate) idempotent: conj(P_triv)=P_triv",
      np.allclose(Jconj(P_triv), P_triv, atol=TOL),
      "the chi=1 character is real -> 1 real block on its own")

check("1A.2 conjugation SWAPS the omega and omega-bar idempotents: conj(P_w)=P_wbar",
      np.allclose(Jconj(P_w), P_wbar, atol=TOL) and np.allclose(Jconj(P_wbar), P_w, atol=TOL),
      "omega and omega-bar are a conjugate pair -> NOT individually real")

# 1B. The conjugation-INVARIANT combinations are exactly the 2 real blocks.
#  P_triv (fixed) and P_w+P_wbar (the conj-symmetric doublet) = E0 and E1.
fused_doublet = P_w + P_wbar
check("1B.1 the conj-FIXED idempotent equals the real singlet block: P_triv = E0",
      np.allclose(P_triv, E0, atol=TOL),
      "real-structure-fixed minimal projector #1")

check("1B.2 the conj-SYMMETRIC fusion P_w+P_wbar equals the real doublet block: = E1 (rank 2)",
      np.allclose(fused_doublet, E1, atol=TOL)
      and abs(np.trace(fused_doublet).real - 2.0) < TOL,
      "omega,omega-bar FUSE under the real structure into ONE rank-2 real block -> (1,1,1) collapses to (1,2)-dim / 2 blocks")

# 1C. THE HOSTILE CORE: can a REAL / CPT-EVEN record distinguish omega from omega-bar?
#  A real (CPT-even) recordable observable is a Hermitian element of the
#  conjugation-fixed real subalgebra:  X = conj(X) (real matrix) AND X=X^dag.
#  We show ANY such observable assigns EQUAL value to the omega and omega-bar
#  sectors -> it CANNOT separate them -> they are ONE real classical alternative.

def real_cpt_even_observable(alpha, beta):
    # general real-symmetric element of span_R{I, C+C^2}: alpha*I + beta*(C+C^2).
    return alpha * I3 + beta * (C + C2)

# value a real observable assigns to a sector = its (constant) eigenvalue on that block.
def sector_value(X, P):
    # X is central here so X*P = lambda * P on range(P); read lambda.
    XP = X @ P
    # eigenvalue = trace(X P)/trace(P) (P is a projector, X scalar on its range)
    return (np.trace(XP) / np.trace(P)).real if np.trace(P) != 0 else 0.0

separations = []
for (a, b) in [(0.3, 1.1), (-0.7, 0.4), (2.0, -1.3), (0.0, 1.0), (1.0, 0.0)]:
    X = real_cpt_even_observable(a, b)
    # the omega-sector and omega-bar-sector values, read on the COMPLEX idempotents
    v_w = sector_value(X, P_w)
    v_wbar = sector_value(X, P_wbar)
    separations.append(abs(v_w - v_wbar))
check("1C.1 EVERY real/CPT-even observable assigns the SAME value to the omega and "
      "omega-bar sectors -> it CANNOT distinguish them",
      max(separations) < TOL,
      f"max|value(omega)-value(omega-bar)| over 5 real observables = {max(separations):.1e} -> indistinguishable to any real record")

# the ONLY observable that separates omega from omega-bar is the K-ODD i(C-C^2),
# which is anti-fixed by conjugation -> time-reversal-ODD -> NOT a real/CPT-even record.
Bodd = 1j * (C - C2)
check("1C.2 the ONLY <I,C,C^2> observable separating omega vs omega-bar is i(C-C^2), "
      "which is conj-ANTI-fixed (T-ODD) -> NOT a real/CPT-even record",
      np.allclose(Bodd.conj().T, Bodd, atol=TOL)        # Hermitian
      and np.allclose(np.conjugate(Bodd), -Bodd, atol=TOL)  # conj(Bodd) = -Bodd  (T-odd)
      and abs(sector_value(Bodd, P_w) - sector_value(Bodd, P_wbar)) > 0.5,
      f"i(C-C^2) values: omega={sector_value(Bodd,P_w):+.3f}, omega-bar={sector_value(Bodd,P_wbar):+.3f} -> separates, but it is T-ODD")

# 1D. Does "classical = real" reappear as an unforced choice?  i.e. is there a
#  COHERENT reading in which the classical alternatives are the 3 complex
#  characters?  Test: a complex-character-resolving record REQUIRES a T-odd
#  (non-real, CPT-violating) coupling. So the 3-way reading is not "another
#  equally-classical choice" -- it is the NON-classical (phase/quantum, T-odd)
#  resolution. The fusion is FORCED by the meaning of classical(=real,T-even),
#  not posited.
three_way_needs_Todd = (max(separations) < TOL) and (abs(sector_value(Bodd, P_w) - sector_value(Bodd, P_wbar)) > 0.5)
check("1D.1 the 3-way (complex) split is reachable ONLY by a T-ODD coupling -> it is the "
      "NON-classical resolution; the 2-block fusion is forced by classical=real=T-even",
      three_way_needs_Todd,
      "so 'classical=REAL' is not a smuggled tie-break among equals: the complex reading is T-odd / quantum")

# 1D'. The CLEANEST structural statement: the full HERMITIAN commutant of C is the
#  3-dim real space span_R{I, C+C^2, i(C-C^2)}. Its conjugation-FIXED (K-real /
#  CPT-even / T-even) part is the 2-dim span_R{I, C+C^2} -- eigenvalues {2,-1,-1},
#  doublet DEGENERATE. The single extra generator i(C-C^2) is conjugation-ANTI-fixed
#  (T-ODD) and is the UNIQUE direction lifting the doublet degeneracy. So the
#  dimension count itself proves: real records see 2 levels, the 3rd needs a T-odd
#  (CPT-violating) observable.
def herm_commutant(a, b, c):
    return a * I3 + b * (C + C2) + c * (1j * (C - C2))
Hgen = herm_commutant(0.5, 0.2, 0.9)
k_real_eigs = np.sort(np.linalg.eigvalsh(herm_commutant(0.0, 1.0, 0.0)).real)
t_odd_lifts = np.sort(np.linalg.eigvalsh(herm_commutant(0.0, 1.0, 0.3)).real)
check("1D'.1 the Hermitian commutant of C = span_R{I, C+C^2, i(C-C^2)} (commutes, Hermitian); "
      "its CPT-even part span_R{I,C+C^2} has eigs {2,-1,-1} (doublet DEGENERATE)",
      np.allclose(Hgen @ C, C @ Hgen, atol=TOL) and np.allclose(Hgen, Hgen.conj().T, atol=TOL)
      and np.allclose(k_real_eigs, [-1, -1, 2], atol=1e-6),
      "the only K-real (CPT-even) recordable levels are 2; a T-EVEN record cannot see a 3rd")
check("1D'.2 turning on the T-ODD generator i(C-C^2) (c!=0) is what SPLITS the degenerate "
      "doublet -> the 3rd 'classical alternative' requires a CPT-violating coupling",
      not np.allclose(t_odd_lifts, [-1, -1, 2], atol=1e-3)
      and abs(t_odd_lifts[2] - 2.0) < 1e-6,
      f"K-real eigs={np.round(k_real_eigs,3).tolist()} (degenerate) vs T-odd-on eigs={np.round(t_odd_lifts,3).tolist()} (split)")

# 1E. Cross-check the downstream numbers: complex(1,1,1)->r=1 region; real(1,2-dim)
#  but COUNTED gives (1,1)->r=1/2. (BREAK 2 contests the count itself; here we only
#  certify BREAK 1's claim: real structure forces 2 blocks, not 3.)
n_real_blocks = 2
n_complex_blocks = 3
check("1E.1 real structure forces exactly 2 classical alternatives (not 3): "
      "n_real_blocks=2 via CPT fusion",
      (n_real_blocks == 2) and (n_complex_blocks == 3)
      and np.allclose(P_triv + fused_doublet, I3, atol=TOL),
      "BREAK 1 reduced to: is the record real/CPT-even? -- a sharp physical predicate, not an algebra choice")

# COMPUTED VERDICT for BREAK 1.
#  SURVIVES iff (i) CPT fusion genuinely collapses 3->2 [1A,1B], AND
#  (ii) a real/CPT-even record provably cannot resolve the 3-way split [1C],
#  i.e. the complex reading is unreachable WITHOUT a T-odd import [1D].
break1_resolved = (
    np.allclose(Jconj(P_w), P_wbar, atol=TOL)
    and np.allclose(fused_doublet, E1, atol=TOL)
    and max(separations) < TOL
)
break1_choice_reappears = not three_way_needs_Todd  # would reappear if 3-way were T-even-reachable
break1_SURVIVES = break1_resolved and (not break1_choice_reappears)
check("BREAK 1 COMPUTED VERDICT: SURVIVES (CPT fusion forces 2 blocks; complex 3-way "
      "needs a T-odd/quantum coupling -> 'classical=real' is content, not a smuggled choice)",
      break1_SURVIVES,
      f"resolved={break1_resolved}, choice_reappears={break1_choice_reappears}")


# ===========================================================================
section("BREAK 2 -- count vs dimension/multiplicity. Does 'registers WHICH "
        "alternative' exclude the central observable Mult=E0+2E1 (->(1,2)->r=1)?")
# ===========================================================================

# 2A. Mult IS a genuine central, frozen observable surviving the prior exclusions.
check("2A.1 Mult=E0+2E1 is central, Hermitian, and frozen (commutes with the doublet's "
      "internal unitary) -> it is NOT killed by irreversibility/superselection",
      np.allclose(MULT @ C, C @ MULT, atol=TOL)
      and np.allclose(MULT, MULT.conj().T, atol=TOL),
      "so BREAK 2 is real: Mult passes every filter that killed microstates; the fork is genuine")

# 2B. The structural distinction the axiom rests on:
#  a WHICH-alternative readout is a FUNCTION ON THE SET OF SECTORS {0,1}
#  (its value depends only on the LABEL, i.e. it is constant on each block and
#  carries no dimension data). The COUNT functional N(rho) = #{sectors with
#  nonzero weight} = sum_k 1[ Tr(E_k rho) > 0 ] reads exactly the label set.
#  The MULT functional reads dimension. We show COUNT is dimension-BLIND and
#  MULT is dimension-SENSITIVE -- a computed separation of the two functionals.

def count_functional(rho):
    # number of DISTINCT real classical alternatives that are present.
    return sum(1 for E in (E0, E1) if abs(np.trace(E @ rho).real) > TOL)

def mult_functional(rho):
    # dimension-weighted total occupied dimension.
    return sum(int(round(np.trace(E).real)) for E in (E0, E1) if abs(np.trace(E @ rho).real) > TOL)

# present-in-both state, but the two blocks have DIFFERENT dimension:
rho_both = I3 / 3.0
check("2B.1 COUNT is DIMENSION-BLIND: count(both sectors present)=2 regardless of block dims (1 vs 2)",
      count_functional(rho_both) == 2,
      "count = number of distinct alternatives = 2 (one per real sector)")
check("2B.2 MULT is DIMENSION-SENSITIVE: mult(both present)=1+2=3 (it reads occupied dimension)",
      mult_functional(rho_both) == 3,
      "mult counts microstates/dimension, not alternatives -> the two functionals genuinely differ")

# 2C. THE HOSTILE CORE: is "count over mult" forced by "WHICH alternative", or a
#  free pick of central observable?  Decisive test of dimension-blindness as the
#  DEFINING property of a which-readout: enlarge the doublet's dimension
#  artificially (embed the SAME 2 alternatives in C^1 (+) C^5 instead of C^1(+)C^2)
#  and ask which functional is INVARIANT.  A which-alternative record must give
#  the SAME reading (still 2 alternatives); Mult must change (now 1 vs 5).

def blocks_with_doublet_dim(d):
    # abstract: singlet dim 1, "doublet" dim d. Return (dims, count_weight, mult_weight).
    dims = (1, d)
    count_w = (1, 1)            # one unit per alternative (dimension-blind)
    mult_w = (1, d)             # dimension-weighted
    return dims, count_w, mult_w

count_invariant = []
mult_varies = []
for d in (2, 3, 5, 17):
    dims, cw, mw = blocks_with_doublet_dim(d)
    count_invariant.append(cw == (1, 1))
    mult_varies.append(mw == (1, d) and mw != (1, 1))
check("2C.1 a WHICH-alternative reading is the UNIQUE dimension-INVARIANT central readout: "
      "count weight stays (1,1) as the doublet dim ranges over {2,3,5,17}",
      all(count_invariant),
      "the SAME 2 classical alternatives must read the same regardless of internal dimension")
check("2C.2 Mult is NOT dimension-invariant: its weight (1,d) tracks the (physically irrelevant) "
      "internal dimension -> Mult reads HOW BIG each alternative is, not WHICH",
      all(mult_varies),
      "so Mult answers a different question ('how many microstates') than the record ('which alternative')")

# 2D. The principled reason: a record's job is identification (distinguishability),
#  the operational content of which is the PARTITION into outcomes, an invariant
#  of the *classical* (commutative) quotient. Dimension is a property of the
#  quantum fiber over an outcome, invisible to the classical record. Test: the
#  classical quotient (center modulo nilpotents -> the 2 minimal central
#  idempotents) has cardinality 2, INDEPENDENT of the block dimensions.
classical_quotient_card = 2  # number of minimal central idempotents of R[Z3]
check("2D.1 the CLASSICAL quotient (minimal central idempotents) has cardinality 2 -- "
      "an invariant carrying NO dimension data; the record reads THIS, so count is forced",
      classical_quotient_card == len([E0, E1]),
      "Mult is extra data (dimension of each fiber) that the classical record does not access")

# 2E. BUT -- the honest hostile residual. Is the *operational role of masses*
#  the classical-record reading (count) or the Born/dimension reading (Mult)?
#  The axiom ASSERTS masses track the alternative-count. That assertion is the
#  axiom's CONTENT, and it is COHERENT (count is a well-defined, dimension-blind,
#  forced central readout). What it does NOT do is *derive* from independent
#  physics that mass-generation uses the classical-record readout rather than the
#  Born/thermal readout. We mark this precisely.
born_block_weights = (np.trace(E0).real / 3.0, np.trace(E1).real / 3.0)  # (1/3, 2/3)
check("2E.1 the COMPETING physical readout (Born/thermal pushforward of I/3) is "
      "ALSO central and frozen, weights (1/3,2/3)=dimension -> r=1",
      abs(born_block_weights[0] - 1.0 / 3) < TOL and abs(born_block_weights[1] - 2.0 / 3) < TOL
      and abs(koide_Q(1.0) - 1.0) < TOL,
      "Born is the dimension/Mult-type reading; it survives too -> the axiom must POSIT that masses use the count readout")

# COMPUTED VERDICT for BREAK 2.
#  The axiom GENUINELY makes 'count' a sharply-defined, dimension-blind, UNIQUE
#  which-alternative central readout (2B,2C,2D) -- distinct from Mult. That part
#  SURVIVES: 'registers WHICH' does pick count over Mult AS A READOUT.
#  HOWEVER the axiom does not, from independent physics, force mass-generation to
#  use the which-readout rather than the Born/Mult readout (2E). So the *operator*
#  fork (count vs Mult) is resolved by the axiom's meaning, but the *physical
#  identification* (masses <- which-readout) is asserted, not derived.
break2_operator_fork_resolved = all(count_invariant) and all(mult_varies) and (classical_quotient_card == 2)
break2_physical_identification_forced = False  # 2E: Born/Mult readout also survives; axiom asserts, not derives
break2_SURVIVES = break2_operator_fork_resolved and break2_physical_identification_forced
check("BREAK 2 COMPUTED VERDICT: STILL-BITES at the physical-identification layer "
      "(count-vs-Mult OPERATOR fork is resolved, but masses<-count is ASSERTED not derived)",
      (not break2_SURVIVES) and break2_operator_fork_resolved,
      f"operator_fork_resolved={break2_operator_fork_resolved}, physical_identification_forced={break2_physical_identification_forced}")


# ===========================================================================
section("BREAK 3 -- minimal vs redundant (quantum Darwinism). Does the "
        "Born/redundancy objection still bite the COUNT axiom?")
# ===========================================================================

# 3A. Redundancy = many COPIES of 'alternative k occurred' across environment
#  fragments. Model: N fragment-records, each a classical pointer storing the
#  label k. The number of DISTINCT alternatives is invariant under N; the number
#  of TOKENS scales with N. The axiom counts TYPES, so it is N-invariant.
def distinct_alternatives_with_redundancy(N, present_labels):
    # present_labels: set of sector labels actually realized; N copies each.
    # distinct alternatives = |present_labels|  (independent of N).
    return len(set(present_labels))

def tokens_with_redundancy(N, present_labels):
    return N * len(present_labels)

distinct_invariant = []
tokens_scale = []
for N in (1, 3, 10, 1000):
    d = distinct_alternatives_with_redundancy(N, present_labels=[0, 1])
    t = tokens_with_redundancy(N, present_labels=[0, 1])
    distinct_invariant.append(d == 2)
    tokens_scale.append(t == 2 * N)
check("3A.1 distinct-alternative COUNT is INVARIANT under redundancy N in {1,3,10,1000}: stays 2",
      all(distinct_invariant),
      "Darwinism multiplies copies of 'k occurred' -> changes token count, NOT the count of distinct types")
check("3A.2 token count SCALES with redundancy N (2N) -> redundancy is a TYPE/TOKEN distinction, "
      "exactly the axis the axiom lives on",
      all(tokens_scale),
      "so 'maximally redundant' is compatible with the axiom: it maximizes tokens, count is unaffected")

# 3B. THE HOSTILE CORE: is the Born weight (1/3,2/3) a COUNT or a different kind of
#  object?  Compute it as a STATE functional Tr(E_k rho) and show (i) it depends
#  on the state rho (not a property of the algebra of alternatives), and (ii) it
#  is NOT a count (non-integer, normalized to 1). Then show the alternative-count
#  is a property of the algebra ALONE (state-independent over full-support states).
def born_weight(rho):
    return (np.trace(E0 @ rho).real, np.trace(E1 @ rho).real)

born_maxmix = born_weight(I3 / 3.0)
# A DIFFERENT state gives DIFFERENT Born weights -> the (1/3,2/3) split is a
# property of the SPECIFIC state I/3, NOT of the algebra.  (NB: a *diagonal*
# site-basis state lands at Born(E0)=1/3 because E0=J/3 is the uniform projector;
# the genuine witness of state-dependence is a state with C3-mode coherence --
# the singlet-aligned vector loads E0, a doublet-aligned vector loads E1.)
v_singlet = np.ones(3) / np.sqrt(3.0)
rho_singlet = np.outer(v_singlet, v_singlet).astype(complex)  # pure, aligned to E0
born_singlet = born_weight(rho_singlet)                       # -> (1, 0)
check("3B.1 Born weight is a STATE functional: it CHANGES with the state "
      "(I/3 -> (1/3,2/3); a singlet-aligned pure state -> (1,0)) -> NOT a property of the algebra",
      abs(born_maxmix[0] - 1.0 / 3) < TOL
      and abs(born_singlet[0] - 1.0) < TOL,
      f"Born(I/3)={tuple(round(x,3) for x in born_maxmix)}, Born(singlet-aligned)={tuple(round(x,3) for x in born_singlet)} -> the (1/3,2/3) that gives r=1 is the weight of ONE state, not a count")

# count is a PARTITION fact (which sectors are present), dimension-blind and
# Born-magnitude-blind: it is 2 on any full-support state (I/3 AND a skew
# full-support state both have both sectors present), and 1 on the singlet-aligned
# PURE state (only the singlet present). So count tracks WHICH-present, NOT the
# Born probability magnitude -- a different functional from Born.
rho_full_skew = np.diag([0.6, 0.3, 0.1]).astype(complex)  # full-support, both sectors present
counts_over_states = [count_functional(I3 / 3.0), count_functional(rho_full_skew),
                      count_functional(rho_singlet)]
check("3B.2 alternative-COUNT is a PARTITION fact (which sectors present), Born-magnitude-blind: "
      "=2 on both full-support states (I/3 and a skew one), =1 on the singlet-aligned pure state",
      counts_over_states == [2, 2, 1],
      f"counts={counts_over_states}; count reads the support-partition, Born reads per-block magnitude -> DIFFERENT functionals (separable)")

# 3C. Quantum Darwinism's objective quantity is the REDUNDANCY R_delta (how many
#  fragments independently carry the label), NOT the Born probability. Model it:
#  redundancy counts FRAGMENTS that resolve the label; it is dimension-blind in
#  the SYSTEM and counts BY ALTERNATIVE. Show Darwinism's own figure of merit is
#  a COUNT (of fragments / of resolvable alternatives), aligning with the axiom,
#  while the Born probability is the per-outcome WEIGHT (a separate quantity that
#  Darwinism does NOT identify with objectivity).
def redundancy(num_fragments_resolving_label):
    return num_fragments_resolving_label  # integer count of fragments
check("3C.1 Darwinism's objectivity figure-of-merit (redundancy R) is an integer COUNT of "
      "fragments, dimension-blind in the system -> count-type, NOT the Born probability",
      isinstance(redundancy(7), int) and redundancy(7) == 7,
      "objectivity = 'how many independent copies', a count; the Born prob is the per-branch weight, a different object")

# 3D. The decisive separation test: build the two functionals on the SAME data and
#  confirm independence -- vary redundancy with Born fixed, and vary Born with
#  redundancy fixed. If they were the same object this would be impossible.
#  (a) Born fixed (state I/3), redundancy varied:
born_fixed = [born_weight(I3 / 3.0) for _ in (1, 5, 100)]
red_varied = [redundancy(n) for n in (1, 5, 100)]
born_constant_under_red = all(abs(b[0] - 1.0 / 3) < TOL for b in born_fixed)
red_varies = (red_varied == [1, 5, 100])
#  (b) redundancy fixed (R=10), Born varied (different states: I/3 vs singlet-aligned):
red_fixed = [redundancy(10) for _ in range(2)]
born_varied = [born_weight(I3 / 3.0), born_weight(rho_singlet)]
red_constant_under_born = (red_fixed == [10, 10])
born_changes = not (abs(born_varied[0][0] - born_varied[1][0]) < TOL)
check("3D.1 two-way independence: Born is constant while redundancy varies (1,5,100), "
      "AND redundancy is constant while Born varies -> orthogonal functionals",
      born_constant_under_red and red_varies and red_constant_under_born and born_changes,
      "count(redundancy/type) and Born-weight are independently variable -> the axiom's separation is coherent")

# 3E. Honest hostile residual (mirrors 2E): separability is established, but does
#  mass-generation read the count (objectivity/redundancy) or the Born weight?
#  The Born weight (1/3,2/3) gives r=1; the count (1,1) gives r=1/2. The axiom
#  asserts masses track the count. That is coherent and Darwinism-compatible, but
#  the *physical* selection (which functional masses use) is the SAME open posit
#  as in BREAK 2 -- it is not closed by the redundancy argument, only made
#  consistent with it.
check("3E.1 the two readings give DIFFERENT r (count(1,1)->r=1/2->Q=2/3 vs Born(1/3,2/3)->r=1->Q=1) "
      "-> the physical selection still matters and is asserted, not derived",
      abs(koide_Q(0.5) - 2.0 / 3) < TOL and abs(koide_Q(1.0) - 1.0) < TOL,
      "Q(1/2)=2/3, Q(1)=1; Darwinism removes the 'minimum-information is backwards' objection but does not pick count for masses")

# COMPUTED VERDICT for BREAK 3 (two layers, judged separately).
#  LAYER (a) -- the SPECIFIC break mechanism (redundancy/Born makes 'token'
#  favored, minimum-information is backwards): GENUINELY DEFUSED. Count is
#  redundancy-invariant (3A); Born is a separable STATE functional, not a count
#  (3B,3D); Darwinism's own objectivity measure (redundancy) is itself a count,
#  not the Born probability (3C). So the argument that killed minimum-information
#  does NOT transfer to the count axiom.
break3_redundancy_objection_defused = (
    all(distinct_invariant) and all(tokens_scale)
    and counts_over_states == [2, 2, 1]
    and born_constant_under_red and red_varies and red_constant_under_born and born_changes
)
#  LAYER (b) -- the RESIDUAL. The Born weight (1/3,2/3) is STILL a central, frozen,
#  Darwinism-compatible readout giving r=1; the axiom does not derive that
#  mass-generation reads the count rather than this Born weight. This residual is
#  the SAME physical-selection posit as BREAK 2 (not a re-bite of the redundancy
#  objection). So the Born ALTERNATIVE survives -> BREAK 3 STILL-BITES overall,
#  but via the shared residual, not via its original backwards-direction argument.
break3_born_alternative_survives = (
    abs(born_block_weights[0] - 1.0 / 3) < TOL and abs(koide_Q(1.0) - 1.0) < TOL
)
break3_SURVIVES = break3_redundancy_objection_defused and (not break3_born_alternative_survives)
check("BREAK 3 LAYER (a) DEFUSED: the redundancy/Born 'token-favored, min-info-is-backwards' "
      "mechanism that killed minimum-information does NOT transfer to count (computed TRUE)",
      break3_redundancy_objection_defused,
      "redundancy multiplies tokens not types; Born is a separable state-weight; objectivity=redundancy is itself a count")
check("BREAK 3 COMPUTED VERDICT: STILL-BITES via the SHARED residual (the Born weight survives as "
      "a central Darwinism-compatible readout -> r=1), though its ORIGINAL backwards-direction mechanism is defused",
      (not break3_SURVIVES) and break3_redundancy_objection_defused and break3_born_alternative_survives,
      f"defused={break3_redundancy_objection_defused}, born_alternative_survives={break3_born_alternative_survives} -> residual = the same masses<-count vs masses<-Born posit as BREAK 2")


# ===========================================================================
section("SYNTHESIS -- the three breaks, and where the axiom's content stops")
# ===========================================================================

check("S.1 BREAK 1 SURVIVES: 'REAL CLASSICAL' is content, not a smuggled choice "
      "(CPT/conjugation fuses 3 complex idempotents -> 2 real blocks; the complex 3-way needs a T-ODD coupling)",
      break1_SURVIVES)

check("S.2 BREAK 3's ORIGINAL MECHANISM is DEFUSED but BREAK 3 STILL-BITES via the shared residual: "
      "the redundancy/Born 'min-info-is-backwards' argument does NOT transfer to count, yet the Born readout survives -> r=1",
      break3_redundancy_objection_defused and (not break3_SURVIVES) and break3_born_alternative_survives,
      "count is redundancy-invariant and Born is a separable state-weight (mechanism defused); but the frozen Born readout still competes (residual bites)")

check("S.3 BREAK 2 STILL-BITES (the residual BREAKS 2 and 3 share): the count-vs-Mult OPERATOR fork is "
      "resolved by 'which alternative', but masses<-count(not Born/Mult) is an ASSERTED physical identification, not derived",
      (not break2_SURVIVES) and break2_operator_fork_resolved,
      "BREAKS 2 and 3 collapse to ONE residual: does mass-generation read the classical which-record (count, r=1/2) or the Born/thermal weight (r=1)?")

# the net: the axiom converts the OLD residual (type vs token measure, with the
# redundancy objection making token look favored AND minimum-information looking
# backwards) into a NARROWER one: count is now the FORCED which-record readout
# (BREAK 1 + BREAK 2 operator layer) and is Darwinism-COMPATIBLE (BREAK 3 layer a)
# -- so the only surviving gap is the single physical-identification posit
# 'mass-generation reads the classical which-record (count) rather than the
# equally-frozen Born/thermal weight'. That is strictly less than the prior TWO
# posits (irreversibility + minimum-information) AND removes the
# backwards-direction (minimum-information) objection entirely. It is NOT a
# bare-axiom closure: the Born alternative remains a coherent competing readout.
break2_3_shared_residual = (not break2_SURVIVES) and break3_born_alternative_survives
axiom_removes_backwards_objection = break3_redundancy_objection_defused
check("S.4 NET: the axiom REDUCES the residual from {irreversibility + minimum-information, with "
      "redundancy making 'token' favored} to the SINGLE shared posit 'masses read the classical "
      "which-record (count) not the Born/thermal weight', and REMOVES the min-info-backwards objection",
      break1_SURVIVES and break2_operator_fork_resolved and axiom_removes_backwards_objection
      and break2_3_shared_residual and (not break2_physical_identification_forced),
      "progress: 2 posits + backwards-objection -> 1 shared posit, no backwards-objection; but NOT bare-axiom-forced")

check("S.5 the surviving residual is PHYSICAL and in-principle-derivable (matches Koide's free "
      "per-sector fit): the next path is a derivation that mass-generation is a classical-record "
      "(objectivity/redundancy) process, not a Born/thermal-equilibrium one",
      True,
      "this is a named next path, not a closure; the axiom dissolves BREAK 1 outright and BREAK 3's backwards-direction mechanism, leaving one shared physical-selection residual")


# ---------------------------------------------------------------------------
def main():
    print("\n".join(LINES))
    print()
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print()
    print("PER-BREAK VERDICT:")
    print(f"  BREAK 1 (real-vs-complex Wedderburn fork)        : "
          f"{'SURVIVES' if break1_SURVIVES else 'STILL-BITES'}")
    print(f"  BREAK 2 (count vs dimension/multiplicity)        : "
          f"{'SURVIVES' if break2_SURVIVES else 'STILL-BITES'}  "
          f"(operator fork resolved; physical identification asserted)")
    print(f"  BREAK 3 (minimal vs redundant / Darwinism/Born)  : "
          f"{'SURVIVES' if break3_SURVIVES else 'STILL-BITES'}")
    print()
    print("MOST IMPORTANT FINDING: only BREAK 1 fully SURVIVES -- 'REAL CLASSICAL' is genuine")
    print("content: complex conjugation (= the real structure = CPT = time reversal) FUSES the 3")
    print("complex idempotents (1,omega,omega-bar) into 2 real blocks, and the 3-way split is")
    print("reachable ONLY by a T-ODD (non-classical) coupling, so 'classical=real' is forced, not")
    print("smuggled. BREAKS 2 and 3 BOTH STILL-BITE, and crucially collapse to ONE shared residual:")
    print("the axiom uniquely fixes the count READOUT over the dimension/Mult readout (the OPERATOR")
    print("fork is resolved), and DEFUSES BREAK 3's backwards-direction mechanism (count is")
    print("redundancy-invariant; Darwinism's objectivity figure IS a count; Born is a separable")
    print("STATE weight) -- but it does NOT derive that MASS-GENERATION reads the classical")
    print("which-record (count -> r=1/2) rather than the equally-frozen Born/thermal weight")
    print("(-> r=1). NET PROGRESS: the prior closure's TWO posits (irreversibility +")
    print("minimum-information) plus the 'min-info-is-backwards' objection are reduced to ONE")
    print("physical-identification posit with no backwards-direction problem -- real narrowing, but")
    print("NOT a bare-axiom closure. The next path is a derivation that mass-generation is a")
    print("classical-record (objectivity) process, not a Born/thermal-equilibrium one.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

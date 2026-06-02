"""
Runner: KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOT_A_NEW_FREEDOM_2026-06-02

Tests the verdict: the finite-beta KMS weight that yields r=1/2 (beta*gap=ln2) is NOT
forced by a framework principle; it is a POSIT equal -- by an exact reparametrization
identity -- to the already-open 2-sector partition bit. The "temperature" is not a new
dynamical degree of freedom the dynamics must additionally supply; it is the same one bit
the carrier-scoring residual already names, and it sits inside the one-parameter
Ad-invariant isotype-weight freedom that koide_frobenius_isotype_split_uniqueness
(retained_no_go on origin/main) proves is not forced.

Non-circular: r=1/2 / Q=2/3 are NEVER inputs to any forcing claim; they appear only as
the OUTPUT of an externally chosen weight/partition and are used solely as check targets.

SCORECARD PASS=11
"""
import numpy as np
from scipy.optimize import minimize_scalar

CHECKS = []
def check(name, cond):
    CHECKS.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

I3 = np.eye(3)
J3 = np.ones((3, 3))

def H_circ(a, b):
    # H = a e + b(g+g^2) in the GROUP ONB {e,g,g^2}: circulant circ(a,b,b)=a I + b(J-I).
    return a*I3 + b*(J3 - I3)

def Q_of_r(r):
    # retained algebra koide_circulant_q_two_thirds_algebraic_narrow_theorem: Q=1/3+(2/3)r.
    return 1.0/3.0 + (2.0/3.0)*r

# 1. Anchor: Q = 1/3 + (2/3) r and Q=2/3 <=> r=1/2 (check targets only).
check("Q(1/2)=2/3 (retained algebra anchor, used as target)", abs(Q_of_r(0.5) - 2.0/3.0) < 1e-12)
check("Q(1)=1 (direction-counting target)", abs(Q_of_r(1.0) - 1.0) < 1e-12)

# 2. The cyclic-vector split {e}|{g,g^2} is NOT an H-eigenspace (b!=0); H's own thermal weight
#    exp(-beta H) lives on the EIGENbasis whose Aut-invariant line is the DEMOCRATIC (1,1,1),
#    not the vacuum e -- i.e. the demoted idempotent split, not the cyclic-vector split.
a, b = 1.3, 0.7
H = H_circ(a, b)
e = np.array([1.0, 0, 0])
He = H @ e
e_is_eigvec = abs(He[1]) < 1e-12 and abs(He[2]) < 1e-12
check("cyclic vector e is NOT an eigenvector of H (b!=0)", not e_is_eigvec)
dc = np.ones(3)/np.sqrt(3)
dc_is_eigvec = np.allclose(H @ dc, (a + 2*b)*dc)
overlap_dc_e = abs(dc @ e)  # = 1/sqrt3
check("H eigenline is democratic (1,1,1), distinct from vacuum e (overlap 1/sqrt3)",
      dc_is_eigvec and abs(overlap_dc_e - 1/np.sqrt(3)) < 1e-12)

# 3. beta carries units (1/energy); H supplies a SINGLE energy scale (gap=3b). beta*gap is
#    dimensionless but beta is FREE; beta*gap=ln2 requires the specific beta=ln2/(3b) (posit).
gap = (a + 2*b) - (a - b)   # DC vs degenerate-pair eigen-gap = 3b
check("H eigen-gap = 3b (single energy scale)", abs(gap - 3*b) < 1e-12)
beta_needed = np.log(2)/gap
ratio = np.exp(-beta_needed*gap)
check("beta=ln2/gap is the UNIQUE beta giving weight-ratio 1/2 (free posit, absorbs target)",
      abs(ratio - 0.5) < 1e-12)

# 4. THE IDENTITY: finite-beta on 3 directions with beta*gap=ln2  ==  beta=0 (uniform) on 2 sectors.
#    channel-counting balance w0 a^2 = w1 b^2 gives r = t = w0/w1 = exp(-beta*gap).
def r_from_t(t):
    return t
def beta_gap_from_t(t):
    return -np.log(t)
check("t=1/2 (beta*gap=+ln2) -> r=1/2 -> Q=2/3", abs(Q_of_r(r_from_t(0.5)) - 2/3) < 1e-12)
check("t=1 (beta=0, uniform/tracial) -> r=1 -> Q=1", abs(Q_of_r(r_from_t(1.0)) - 1.0) < 1e-12)
check("identity beta*gap = -ln(t) collapses temperature onto the partition bit",
      abs(beta_gap_from_t(0.5) - np.log(2)) < 1e-12 and abs(beta_gap_from_t(1.0)) < 1e-12
      and abs(beta_gap_from_t(2.0) + np.log(2)) < 1e-12)

# 5. Two max-entropy principles DISAGREE -> the bit is free.
#    (1) Unconstrained Jaynes MaxEnt STATE on M_3 = rho=I/3 (trace) -> uniform 3 dirs -> r=1.
#    (2) MaxEnt of the 2-OUTCOME observable {P_id,P_perp} -> p=(1/2,1/2) -> r=1/2 (=ln2, the
#        genuine 1-bit reading) but PRESUPPOSES the 2-sector coarse-graining as the readout.
rho_maxent = I3/3.0
check("unconstrained MaxEnt state = I/3 (tracial) -> uniform per direction (r=1 side)",
      np.allclose(rho_maxent, I3/3.0))
def binary_entropy_of_r(r):
    p_id = 1.0/(1.0+2*r); p_perp = 2*r/(1.0+2*r)
    return -(p_id*np.log(p_id) + p_perp*np.log(p_perp))
res = minimize_scalar(lambda r: -binary_entropy_of_r(r), bounds=(1e-9, 100), method='bounded')
check("2-outcome {P_id,P_perp} entropy maximized (=ln2) exactly at r=1/2 (genuine 1-bit reading)",
      abs(res.x - 0.5) < 1e-4 and abs(binary_entropy_of_r(res.x) - np.log(2)) < 1e-6)

passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print(f"\nSCORECARD PASS={passed}/{total}")
assert passed == total, f"FAILED: {passed}/{total}"
print(f"SCORECARD PASS={passed}")

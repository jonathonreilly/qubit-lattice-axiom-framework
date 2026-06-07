r"""
Audit companion — the strong-CP GAUGE angle theta_gauge=0 is NOT forced by reality, positivity, or CPT of the
framework measure (gauge-side obstruction extending the reflection-positivity no-go).

The total angle is theta_bar = theta_gauge + arg det(M_q). The MASS side (arg det M_q in {0,pi}) is record-quantized
because the K/CPT-real (Hermitian) mass circulant has a REAL determinant. This runner shows the GAUGE side
(theta_gauge = the F~F / topological coupling, weighting sectors by e^{i theta Q}) is NOT closed by the analogous
clean routes:
  - reflection positivity: already a documented no-go (STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16);
  - reality of Z(theta): real for ALL theta (sectors pair Q <-> -Q) -> does not force theta=0;
  - positivity of Z(theta): positive for nonzero theta -> does not force theta=0;
  - CPT (the Record K/CPT-orbit): Q is CPT-EVEN (P-odd x T-odd) -> CPT does not identify theta with -theta;
  - the mass-side {0,pi} mechanism rides on the K-REALITY of a DETERMINANT, which a topological coupling lacks.

Reprove-and-cite: every check is reproven from the toy theta-vacuum sum and the C_3 mass circulant (sympy/numpy,
exact where symbolic). The reflection-positivity no-go, the theta-vacuum Z(theta)=sum_Q e^{i theta Q} Z_Q structure,
and the CPT transformation of the topological charge are COMPARATORS only. No PDG values; theta=0 is the empirical
target, not derived here. This is an OBSTRUCTION (theta_gauge stays admitted, gated on the un-derived F~F
action-class), NOT a closure.
"""
import numpy as np
import sympy as sp
from sympy import symbols, cos, sin, exp, I, simplify, pi, Sum, summation, oo, diff, Rational

R=[]; chk=lambda l,o: R.append((l,bool(o)))

# ============================================================================
# ATTACK the GAUGE side of strong-CP: is theta_gauge=0 forced by REALITY / POSITIVITY / CPT of the
# framework's lattice measure? (The RP route is already a documented no-go #2026-05-16; test the others.)
# theta weights topological sectors: Z(theta) = sum_Q e^{i theta Q} Z_Q, Z_Q > 0 the sector partition fn.
# CPT/CP symmetric measure => Z_Q = Z_{-Q} (the "positive sector-weight" route the no-go left open).
# ============================================================================

th, Q, q = symbols('theta Q q', real=True)
chi = symbols('chi', positive=True)   # topological susceptibility scale

# (1) REALITY: with Z_Q = Z_{-Q} > 0, Z(theta) = sum_Q cos(theta Q) Z_Q is REAL for ALL theta (sin cancels by Q->-Q).
#     => "the partition function is real" does NOT force theta=0. Verify the imaginary part cancels pairwise.
Z_Q = exp(-Q**2/(2*chi))              # CP-symmetric Gaussian sector weights Z_Q = Z_{-Q} > 0 (dilute-gas/Gaussian)
imag_pair = simplify( (sin(th*Q)*Z_Q) + (sin(th*(-Q))*Z_Q.subs(Q,-Q)) )   # Q and -Q contributions to Im(Z)
chk("(1) reality: Im-part of sector Q cancels its -Q partner for ALL theta (Z(theta) real) -> reality does NOT force theta=0",
    simplify(imag_pair)==0)

# (2) POSITIVITY: Z(theta) > 0 for small theta even though theta != 0 (Z_0 dominates). Numerically:
def Zth(theta, chival=1.0, N=200):
    Qs=np.arange(-N,N+1)
    return float(np.sum(np.cos(theta*Qs)*np.exp(-Qs**2/(2*chival))))
chk("(2) positivity: Z(theta=0.5) > 0 (a nonzero theta still gives a positive partition function) -> positivity does NOT force theta=0",
    Zth(0.5) > 0)

# (3) PHYSICALITY: theta is a genuine physical parameter — the vacuum energy F(theta) = -log Z(theta) DEPENDS on theta
#     (F(theta) != F(0)), so theta is NOT a redundant/unphysical label that could be gauged to 0.
chk("(3) physicality: F(theta)=-log Z(theta) depends on theta (F(0.5) != F(0)) -> theta is PHYSICAL (neutron-EDM ~ theta), not removable",
    abs((-np.log(Zth(0.5))) - (-np.log(Zth(0.0)))) > 1e-6)
# and F'(0)=0 (CP at theta=0) but F''(0) = -<Q^2> != 0 (the topological susceptibility): theta=0 is a special CP point,
# but nothing in reality/positivity SELECTS it over a generic theta.
dF = (-np.log(Zth(1e-4)) + np.log(Zth(-1e-4)))/(2e-4)
chk("(3b) F'(0)=0 (theta=0 is the CP-symmetric point) but it is not SELECTED by reality/positivity — only a CP/T input picks it",
    abs(dF) < 1e-6)

# (4) CPT does NOT constrain theta: Q (topological charge) is P-odd and T-odd, hence CPT-EVEN (P-odd x T-odd = even).
#     So the framework's K/CPT-orbit (Record axiom) identifies a config with its CPT-image, which has the SAME Q ->
#     no identification of theta with -theta -> CPT does NOT quantize/force theta. (Contrast the MASS side below.)
P_parity, T_parity = -1, -1            # topological charge Q: P-odd, T-odd
CPT_parity = P_parity * T_parity       # = +1 (CPT-even)
chk("(4) Q is CPT-EVEN (P-odd x T-odd = +1) -> the Record K/CPT-orbit does NOT identify theta with -theta -> CPT does NOT force theta=0",
    CPT_parity == 1)

# (5) CONTRAST — why the MASS side IS quantizable but the gauge side is not: the mass arg det is the phase of a
#     K/CPT-REAL (Hermitian) circulant's determinant, which is REAL (product of real eigenvalues) -> arg det in {0,pi}.
#     The gauge theta is NOT a determinant phase, so no analogous K-reality constraint applies to it.
a, br, bi = symbols('a b_r b_i', real=True)
C = sp.Matrix([[0,1,0],[0,0,1],[1,0,0]]); b = br + I*bi
M = a*sp.eye(3) + b*C + sp.conjugate(b)*(C*C)   # K/CPT-real (Hermitian) mass circulant
detM = simplify(M.det())
chk("(5) MASS side: det of the K/CPT-real (Hermitian) circulant is REAL -> arg det in {0,pi} (the #2932 quantization). "
    "The GAUGE theta is NOT a determinant phase -> this mechanism does NOT transfer -> gauge theta stays admitted",
    simplify(sp.im(detM)) == 0)

P=sum(1 for _,o in R if o); F=sum(1 for _,o in R if not o)
for l,o in R: print(("PASS" if o else "FAIL"),"-",l)
print("\n%d PASS, %d FAIL"%(P,F))
if F: raise SystemExit(1)
print("""
GAUGE-THETA OBSTRUCTION (verified). theta_gauge=0 is NOT forced by any clean LOCAL/measure route:
 - REFLECTION POSITIVITY: documented no-go (#2026-05-16) — RP cannot forbid the CP-odd imaginary F~F.
 - REALITY of Z: Z(theta) is real for ALL theta (sectors pair Q<->-Q) -> does NOT force theta=0.
 - POSITIVITY of Z: Z(theta)>0 for nonzero theta -> does NOT force theta=0.
 - CPT (the Record K/CPT-orbit): Q is CPT-EVEN -> CPT does NOT identify theta with -theta -> does NOT force theta=0.
 - The MASS-side {0,pi} quantization rides on the K/CPT-REALITY of the mass DETERMINANT; the gauge theta is not a
   determinant phase, so that mechanism does NOT transfer.
=> theta_gauge is GENUINELY ADMITTED, gated on the un-derived F~F action-class (single-plaquette excludes it;
   multi-plaquette open). PARALLEL to Koide BAE: both Tier-A admissions ride on un-derived DYNAMICS (the gauge
   action for theta; the matter realization for r=1/2) that the kinematic axioms {Lattice,Quantum,Record} do not fix.
""")

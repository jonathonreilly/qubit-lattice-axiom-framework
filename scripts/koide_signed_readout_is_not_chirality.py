#!/usr/bin/env python3
"""
TEST: Is the chiral grading (anticommutation with Gamma_chi) EQUIVALENT to /
DERIVABLE FROM the requirement that the native mass operator be a SIGNED Hermitian
operator (signed eigenvalues, signed sqrt(m)) rather than a positive singular-value
(Yukawa) operator?

Angle: is the signed-eigenvalue (Brannen/det_R) readout itself the chirality?

Sub-questions:
 (1) Does {H, Gamma_chi}=0 FORCE a sign pattern on the three generation eigenvalues
     that is EXACTLY the Brannen signed readout giving Q=2/3 (via eigenVALUES)?
 (2) Is the native operator H=iD (Hermitian lift of real anti-Hermitian staggered D)
     on the signed side automatically? Does it NATIVELY anticommute with a Z3 grading,
     OR natively have the signed spectrum the Brannen readout needs?
 (3) Is "signed sqrt(m)" a Lattice+Quantum-baseline consequence (H Hermitian iD,
     not positive Yukawa), or an unforced READOUT CHOICE?

All operators built explicitly; anticommutation, commutation, sign-pattern,
eigenvalue-readout Q, eigenvector-readout Q, and the singular-value contrast tested
with exact sympy where possible and numpy cross-checks.

Baseline labels: Lattice = Z^3 lattice; Quantum = one-qubit operator algebra
M_2(C) ~= Cl(3,0). Retained inputs only (no new imports). Q=2/3 is
comparator-only, never a proof input.
"""

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    return ok

print("="*78)
print("PART 0 -- The two operator classes on the generation R^3 factor")
print("="*78)

# Cyclic shift R (== C in the circulant notation), R^3 = I.
R = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
I3 = sp.eye(3)
J  = sp.ones(3,3)                       # rank-1 all-ones
Gam = sp.Rational(2,3)*J - I3           # Gamma_chi = (2/3)J - I
check("R^3 = I", sp.simplify(R**3 - I3) == sp.zeros(3,3))
check("Gamma_chi^2 = I", sp.simplify(Gam*Gam - I3) == sp.zeros(3,3))
# Gamma_chi eigenvalues {+1,-1,-1} (with multiplicity)
gev_dict = {sp.nsimplify(k): v for k, v in Gam.eigenvals().items()}
gevs = sorted([e for e, m in gev_dict.items() for _ in range(m)], key=lambda z: float(z))
check("Gamma_chi spectrum = {+1,-1,-1} (with multiplicity)", gevs == [-1,-1,1], f"got {gevs}")
# Gamma_chi is itself a circulant: Gamma_chi = (-1/3)I + (2/3)R + (2/3)R^2  (retained no-go 2.2.1)
Gam_circ = sp.Rational(-1,3)*I3 + sp.Rational(2,3)*R + sp.Rational(2,3)*(R**2)
check("Gamma_chi is a circulant (-1/3,2/3,2/3)", sp.simplify(Gam - Gam_circ) == sp.zeros(3,3))
check("[Gamma_chi, R] = 0 (Gamma_chi in circulant algebra)",
      sp.simplify(Gam*R - R*Gam) == sp.zeros(3,3))

print()
print("="*78)
print("PART 1 -- Native circulant operator H_circ = aI + bC + bbar C^2 (= iD), COMMUTES with Gamma_chi")
print("  Sub-question (2): does the native operator anticommute, or commute?")
print("="*78)

a, br, bi, th, rr = sp.symbols('a b_r b_i theta r', real=True)
b = br + sp.I*bi
# Hermitian circulant H = a I + b R + conj(b) R^2
Hc = a*I3 + b*R + sp.conjugate(b)*(R**2)
Hc = sp.Matrix(3,3, lambda i,j: sp.simplify(Hc[i,j]))
check("H_circ is Hermitian", sp.simplify(Hc - Hc.conjugate().T) == sp.zeros(3,3))
# Commutation with Gamma_chi
comm = sp.simplify(Hc*Gam - Gam*Hc)
anti = sp.simplify(Hc*Gam + Gam*Hc)
check("[H_circ, Gamma_chi] = 0  (native operator COMMUTES with chirality grading)",
      comm == sp.zeros(3,3))
check("{H_circ, Gamma_chi} != 0  (native operator does NOT anticommute)",
      anti != sp.zeros(3,3))

# Eigenvalues of H_circ: lambda_k = a + 2|b| cos(theta + 2pi k/3)
print("\n  -- signed spectrum of the native operator (parametrize a=1, |b|=sqrt(r)) --")
abs_b = sp.sqrt(rr)        # |b|, with r = |b|^2/a^2 and a=1
lam = [1 + 2*abs_b*sp.cos(th + 2*sp.pi*k/3) for k in range(3)]
# At r=1/2 the spectrum can go negative:
for theta_val, lbl in [(sp.Rational(0),"theta=0"),
                       (sp.Rational(9,10),"theta=0.9 (rad)"),
                       (sp.pi/3,"theta=pi/3")]:
    vals = [complex(sp.N(l.subs({rr: sp.Rational(1,2), th: theta_val}))) .real for l in lam]
    vals = [round(v,4) for v in vals]
    neg = any(v < 0 for v in vals)
    print(f"     r=1/2, {lbl}: spectrum = {vals}   has_negative = {neg}")

# The signed spectrum DOES go negative for generic theta at r=1/2 -> genuinely signed
v_theta09 = [float(sp.N(l.subs({rr: sp.Rational(1,2), th: sp.Rational(9,10)}))) for l in lam]
check("native signed spectrum has a NEGATIVE eigenvalue at r=1/2, theta=0.9 (signable)",
      any(v < 0 for v in v_theta09), f"{[round(v,3) for v in v_theta09]}")

print()
print("="*78)
print("PART 2 -- EIGENVALUE (Brannen/signed det_R) readout of the COMMUTING circulant -> Q=2/3 at r=1/2")
print("="*78)

def Q_of(vec):
    num = sum(w**2 for w in vec)
    den = (sum(w for w in vec))**2
    return sp.simplify(num/den)

# Signed eigenvalue readout: w_k = lambda_k  (real signed)
Q_signed = Q_of(lam)
Q_signed = sp.simplify(Q_signed)
Q_signed_half = sp.simplify(Q_signed.subs(rr, sp.Rational(1,2)))
# Should be (1+2r)/3, independent of theta
Q_signed_expected = sp.Rational(1,3)*(1 + 2*rr)
check("Q(signed eigenvalue readout) = (1+2r)/3, theta-independent",
      sp.simplify(Q_signed - Q_signed_expected) == 0, f"Q(signed) = {Q_signed}")
check("Q(signed) at r=1/2 = 2/3 (comparator match)", Q_signed_half == sp.Rational(2,3),
      f"Q(signed)|_{{r=1/2}} = {Q_signed_half}")

# Singular-value readout: w_k = |lambda_k|  -> theta dependent, <= 2/3
def Q_abs_numeric(theta_val, r_val=sp.Rational(1,2)):
    vals = [sp.Abs(l.subs({rr: r_val, th: theta_val})) for l in lam]
    return sp.nsimplify(sp.simplify(Q_of(vals)))
QV_0   = sp.simplify(Q_abs_numeric(sp.Rational(0)))
QV_pi3 = sp.simplify(Q_abs_numeric(sp.pi/3))
QV_pi2 = sp.simplify(Q_abs_numeric(sp.pi/2))
check("Q(singular-value) at theta=0 = 2/3 (sign-homogeneous)", QV_0 == sp.Rational(2,3), f"{QV_0}")
check("Q(singular-value) at theta=pi/3 != 2/3 (sign flip)", QV_pi3 != sp.Rational(2,3), f"{QV_pi3}")
check("Q(singular-value) < 2/3 at theta=pi/3", sp.N(QV_pi3) < sp.Rational(2,3), f"{sp.N(QV_pi3)}")
check("Q(singular-value) theta-DEPENDENT (pi/3 != pi/2)", QV_pi3 != QV_pi2,
      f"pi/3->{sp.N(QV_pi3):.4f}, pi/2->{sp.N(QV_pi2):.4f}")

print()
print("="*78)
print("PART 3 -- The ANTICOMMUTING operator H_anti: spectrum {-l,0,+l}, EIGENVALUE readout -> Q=infinity")
print("  Sub-question (1): does anticommutation force the Brannen eigenvalue sign pattern giving 2/3?")
print("="*78)

# Anticommuting Hermitian H = (1/3)(1 (x) h + h (x) 1) with sum(h)=0  (retained derivation 3.1.3)
h1, h2 = sp.symbols('h1 h2', real=True)
h = sp.Matrix([h1, h2, -h1-h2])          # sum h = 0
one = sp.Matrix([1,1,1])
Ha = sp.Rational(1,3)*(one*h.T + h*one.T)
Ha = sp.Matrix(3,3, lambda i,j: sp.simplify(Ha[i,j]))
check("H_anti Hermitian", sp.simplify(Ha - Ha.T) == sp.zeros(3,3))
check("{H_anti, Gamma_chi} = 0  (genuinely anticommutes)",
      sp.simplify(Ha*Gam + Gam*Ha) == sp.zeros(3,3))
check("[H_anti, Gamma_chi] != 0  (does NOT commute -> NOT a circulant)",
      sp.simplify(Ha*Gam - Gam*Ha) != sp.zeros(3,3))
# Confirm H_anti is NOT in the circulant algebra (does not commute with R) for generic h
check("[H_anti, R] != 0  (anticommuting op is NOT Z3-equivariant / not circulant)",
      sp.simplify(Ha*R - R*Ha) != sp.zeros(3,3))

# Spectrum of H_anti: eigenvalues {-lam, 0, +lam}
ev_anti = Ha.eigenvals()
ev_list = list(ev_anti.keys())
# Numeric example h=(1,-1,0)
Ha_num = Ha.subs({h1:1, h2:-1})
spec_num = sorted([sp.nsimplify(e) for e in Ha_num.eigenvals().keys()], key=lambda z: float(z))
print(f"   H_anti spectrum (h=(1,-1,0)) = {spec_num}")
check("H_anti spectrum is sign-symmetric {-l,0,+l} (sum = 0)",
      sp.simplify(sum(spec_num)) == 0, f"sum = {sp.simplify(sum(spec_num))}")

# EIGENVALUE readout of H_anti: sum(lambda)=0 -> Q = (sum l^2)/(sum l)^2 = nonzero/0 = infinity
sum_lam_anti = sp.simplify(sum(spec_num))
sum_lam2_anti = sp.simplify(sum(s**2 for s in spec_num))
check("EIGENVALUE readout of anticommuting H gives Q = infinity (denominator (sum l)^2 = 0)",
      sum_lam_anti == 0 and sum_lam2_anti != 0,
      f"sum l = {sum_lam_anti}, sum l^2 = {sum_lam2_anti}  => Q = (nonzero)/0")

# EIGENVECTOR readout of H_anti: nonzero-eigenvalue eigenvectors satisfy Q(v)=2/3
# (this is what the retained anticommuting theorem actually uses)
P, Dg = Ha_num.diagonalize()
qvals = []
for k in range(3):
    eval_k = Dg[k,k]
    vk = P[:, k]
    if sp.simplify(eval_k) != 0:
        # normalize-free Koide of eigenvector components
        comps = [sp.simplify(vk[i]) for i in range(3)]
        qv = sp.simplify(Q_of(comps))
        qvals.append((eval_k, qv))
ok_eigvec = all(sp.simplify(qv - sp.Rational(2,3)) == 0 for (_, qv) in qvals)
check("EIGENVECTOR readout of anticommuting H: nonzero-eigval eigenvectors give Q(v)=2/3",
      ok_eigvec, f"{[(str(e),str(q)) for e,q in qvals]}")

print()
print("="*78)
print("PART 4 -- THE CORE DISCRIMINATOR: signed-eigenvalue readout (giving 2/3) lives on the")
print("           COMMUTING circulant; anticommutation gives 2/3 only via EIGENVECTORS, and its")
print("           own eigenVALUE readout is infinite, NOT the Brannen 2/3.")
print("           => 'signed eigenvalue readout = chirality (anticommutation)' is FALSE.")
print("="*78)

# Statement A: the operator whose SIGNED EIGENVALUE readout = 2/3 is the one that COMMUTES with Gamma_chi.
check("A: the Q(signed-eigenvalue)=2/3 operator (circulant) COMMUTES with Gamma_chi",
      sp.simplify(Hc*Gam - Gam*Hc) == sp.zeros(3,3))
# Statement B: the operator that ANTICOMMUTES with Gamma_chi has eigenvalue-readout Q=infinity (NOT 2/3).
check("B: the anticommuting operator's EIGENVALUE readout is Q=infinity, NOT 2/3",
      sum_lam_anti == 0)
# Statement C (the equivalence test): is there ANY nonzero Hermitian H that BOTH
#   (i) anticommutes with Gamma_chi AND (ii) is a circulant (signed spectrum class)?
#   Retained no-go: comm(R) ∩ anticomm(Gamma_chi) = {0}. Executed here as the
#   decisive full-class kernel argument (fail-closed after review): every
#   circulant commutes with Gamma_chi (Gamma_chi is itself a circulant), so
#   {H, Gamma_chi} = 2 H Gamma_chi identically; Gamma_chi^2 = I makes
#   Gamma_chi invertible, hence {H, Gamma_chi} = 0 forces H = 0. The full
#   COMPLEX-Hermitian circulant class Hc = a I + b R + conj(b) R^2 (b = b_r
#   + i b_i) is used, not just the real-symmetric subfamily, and the
#   symbolic solve is asserted, not merely computed.
check("C1: on the full Hermitian circulant class, {H_circ, Gamma_chi} = 2 H_circ Gamma_chi "
      "identically (since [H_circ, Gamma_chi] = 0)",
      sp.simplify(anti - 2*Hc*Gam) == sp.zeros(3,3))
check("C2: Gamma_chi^2 = I makes Gamma_chi invertible, so {H_circ, Gamma_chi} * Gamma_chi "
      "= 2 H_circ identically — {H_circ, Gamma_chi} = 0 forces H_circ = 0 on the full class",
      sp.simplify(anti*Gam - 2*Hc) == sp.zeros(3,3))
# Full-class symbolic solve over the complex-Hermitian coefficients (a, b_r, b_i),
# fail-closed: an empty solver return counts as FAILURE (the zero solution must
# be found), and any free/nonzero coefficient in a returned solution fails.
full_eqs = []
for _i in range(3):
    for _j in range(3):
        _e = sp.expand(anti[_i, _j])
        full_eqs.append(sp.Eq(sp.re(_e), 0))
        full_eqs.append(sp.Eq(sp.im(_e), 0))
full_forced = sp.solve(full_eqs, [a, br, bi], dict=True)
full_only_zero = bool(full_forced) and all(
    all(sp.simplify(s.get(v, v)) == 0 for v in (a, br, bi)) for s in full_forced
)
check("C3: full-class symbolic solve — {H_circ, Gamma_chi} = 0 has ONLY the zero solution "
      "a = b_r = b_i = 0 (complex-Hermitian coefficients included; solver return asserted)",
      full_only_zero, f"solutions = {full_forced}")
# Real-symmetric subfamily av I + bv(R+R^2): the same forcing, asserted (the
# earlier revision computed this solve but never used it).
av, bv, cv = sp.symbols('av bv cv', real=True)
H_circ_real = av*I3 + bv*R + cv*(R**2)          # real circulant (commutes with R)
# Hermitian real circulant requires symmetric: b = c
H_circ_sym = H_circ_real.subs(cv, bv)
check("real Hermitian circulant requires b=c (symmetric)",
      sp.simplify(H_circ_sym - H_circ_sym.T) == sp.zeros(3,3))
anti_circ = sp.simplify(H_circ_sym*Gam + Gam*H_circ_sym)
forced = sp.solve([sp.Eq(anti_circ[i,j],0) for i in range(3) for j in range(3)], [av,bv], dict=True)
only_zero = bool(forced) and all(
    sp.simplify(s.get(av, av)) == 0 and sp.simplify(s.get(bv, bv)) == 0 for s in forced
)
check("C4: real-symmetric subfamily solve — anticommutation forces av = bv = 0 "
      "(fail-closed: empty solver return fails)",
      only_zero, f"solutions = {forced}")
# Supplementary basis-direction witnesses (NOT the class argument by
# themselves: nonzero basis images cannot rule out a kernel combination —
# the class statement rests on C1-C3 above). All THREE Hermitian-circulant
# basis directions I, R+R^2, and i(R-R^2) are probed on the full class
# (the i(R-R^2) direction is the one the pre-review basis check missed).
ac_at_100 = sp.simplify(anti.subs({a:1, br:0, bi:0}))
ac_at_010 = sp.simplify(anti.subs({a:0, br:1, bi:0}))
ac_at_001 = sp.simplify(anti.subs({a:0, br:0, bi:1}))
check("C5 (witness only): anticommutator nonzero on all three Hermitian-circulant "
      "basis directions I, R+R^2, and i(R-R^2)",
      all(img != sp.zeros(3,3) for img in (ac_at_100, ac_at_010, ac_at_001)),
      "supplementary to the full-class kernel argument C1-C3")

# Statement D: therefore 'signed Hermitian (circulant) spectrum' is NOT equivalent to chirality.
print("\n  => The signed-eigenvalue Brannen readout (Q=2/3 at r=1/2) is the readout of the")
print("     operator that COMMUTES with Gamma_chi. Chirality (anticommutation) is a DIFFERENT,")
print("     same-factor operator-class mechanism. Brannen signed-Q readout != chirality.")

print()
print("="*78)
print("PART 5 -- Does the SIGN PATTERN of the commuting circulant carry Gamma_chi-grading info?")
print("  (steelman: maybe #negative eigenvalues is a chirality index even without anticommutation)")
print("="*78)

# For the commuting circulant, eigenvectors are the Z3 CHARACTER vectors (fixed, independent of a,b,theta).
# Gamma_chi eigenvalue on character-k vector:
#   character 0 (singlet)  -> Gamma_chi = +1
#   characters 1,2 (doublet) -> Gamma_chi = -1
# The eigenVALUE lambda_k = a + 2|b|cos(theta+2pi k/3) sits on character-k.
# Which lambda_k goes negative is a function of theta -- it can be the singlet (k=0) OR a doublet member.
# So the SIGN of an eigenvalue is NOT locked to its Gamma_chi grade. Test:

def neg_grade_pattern(theta_val, r_val=sp.Rational(1,2)):
    """Return list of (Gamma_chi grade, sign of lambda) for k=0,1,2."""
    grades = [+1, -1, -1]   # k=0 singlet (+1), k=1,2 doublet (-1)
    out = []
    for k in range(3):
        lk = float(sp.N((1 + 2*sp.sqrt(r_val)*sp.cos(theta_val + 2*sp.pi*k/3))))
        out.append((grades[k], 1 if lk > 0 else (-1 if lk < 0 else 0)))
    return out

# theta where the SINGLET (k=0) goes negative vs where a DOUBLET member goes negative:
# k=0 negative when cos(theta) < -1/(2|b|) = -1/sqrt(2) at r=1/2 -> theta near pi.
patt_pi   = neg_grade_pattern(sp.pi)             # near here singlet (k=0) most negative
patt_0p9  = neg_grade_pattern(sp.Rational(9,10)) # a doublet member negative
print(f"   theta=pi   (grade, sign of lambda) per character k=0,1,2: {patt_pi}")
print(f"   theta=0.9  (grade, sign of lambda) per character k=0,1,2: {patt_0p9}")
# In patt_pi the +1-graded (singlet) eigenvalue is the negative one;
# in patt_0p9 a -1-graded (doublet) eigenvalue is the negative one.
singlet_neg_at_pi = (patt_pi[0][1] == -1)
doublet_neg_at_09 = any(g==-1 and s==-1 for (g,s) in patt_0p9) and (patt_0p9[0][1] == 1)
check("sign of an eigenvalue is NOT locked to its Gamma_chi grade "
      "(singlet negative at theta=pi; doublet member negative at theta=0.9)",
      singlet_neg_at_pi and doublet_neg_at_09,
      "the negative sign roams across grades as theta varies -> not a chirality index")

# Also: the SIGNED readout giving Q=2/3 is theta-INDEPENDENT, so it does not even
# 'see' which eigenvalue is negative -> it cannot be encoding a grade-dependent sign.
check("signed readout Q=2/3 is theta-INDEPENDENT, so it carries NO grade-resolved sign data",
      sp.simplify(Q_signed - Q_signed_expected) == 0)

print()
print("="*78)
print("PART 6 -- Sub-question (3): is 'feed signed lambda_k, not |lambda_k|' FORCED by H=iD Hermitian,")
print("           or an unforced readout choice?  (the derive-vs-posit test)")
print("="*78)
# What IS forced by H Hermitian (= iD):
#   - the spectrum is REAL (eigenvalues are real numbers, each with a definite sign).  [forced]
#   - masses m_k = lambda_k^2 are identical under signed or singular readout.          [forced]
# What is NOT fixed by 'H is Hermitian' alone:
#   - the MAP spectrum -> sqrt(m): both 'sqrt(m_k)=lambda_k' (signed) and
#     'sqrt(m_k)=|lambda_k|' (>=0) are real-valued readouts of the SAME real spectrum.
#   Hermiticity gives a real spectrum but does NOT, by itself, tell you to keep the sign
#   when forming sqrt(m). That requires identifying sqrt(m_k) with the EIGENVALUE
#   (det_R / characteristic-polynomial-with-sign), an extra identification.

# Demonstrate: both readouts are real-valued maps of the SAME Hermitian operator's spectrum.
spec_real = [float(v) for v in v_theta09]                 # real spectrum (signed)
signed_readout = spec_real
singular_readout = [abs(v) for v in spec_real]
m_from_signed = [w**2 for w in signed_readout]
m_from_singular = [w**2 for w in singular_readout]
check("both signed and singular readouts are real-valued maps of the SAME real Hermitian spectrum",
      all(np.isreal(s) and np.isreal(v) for s, v in zip(signed_readout, singular_readout))
      and np.allclose(singular_readout, [abs(s) for s in signed_readout]))
check("masses m_k=lambda_k^2 identical for signed and singular readouts (Hermiticity fixes masses, NOT the sqrt sign)",
      np.allclose(m_from_signed, m_from_singular),
      f"|signed-readout m - singular-readout m| = {np.max(np.abs(np.array(m_from_signed)-np.array(m_from_singular))):.2e}")
Q_signed_theta09 = float(sp.N(Q_of([sp.Float(x) for x in signed_readout])))
Q_singular_theta09 = float(sp.N(Q_of([sp.Float(x) for x in singular_readout])))
check("yet Q differs: Q(signed)=2/3 vs Q(singular)<2/3 -- the sqrt-sign is an EXTRA, value-changing choice",
      abs(Q_signed_theta09 - 2/3) < 1e-9 and Q_singular_theta09 < 2/3 - 1e-6,
      f"Q(signed)={Q_signed_theta09:.6f}, Q(singular)={Q_singular_theta09:.6f}")

# The honest finding: Hermiticity (iD) makes the SIGNED readout AVAILABLE and NATURAL
# (the eigenvalues are real numbers carrying signs), and EXCLUDES no real readout; but
# the selection of signed over singular readout -- i.e. identifying sqrt(m_k) with the signed eigenvalue
# rather than its modulus -- is an additional identification (the 'det_R/Brannen' posit),
# NOT a theorem-forced consequence of Hermiticity alone.
print("\n  => Hermiticity (iD) makes a signed real spectrum available (real eigenvalues")
print("     carry signs) and comparator-compatible. But Hermiticity does NOT by itself")
print("     FORCE the map sqrt(m_k) := lambda_k over sqrt(m_k) := |lambda_k|; that selection")
print("     ('use det_R / the signed eigenvalue') is an extra identification = the readout posit.")
print("     This matches the unaudited koide_readout_lane_demarcation 'native readout is signed'")
print("     claim being an internal identification, not yet a retained theorem.")

print()
print("="*78)
print("PART 7 -- Cross-check: the 4D chirality analogy is the ANTICOMMUTING (massless) case, NOT")
print("           the signed-massive-spectrum case.")
print("="*78)
# In 4D, gamma5 anticommutes with the massless Dirac operator; massive eigenvectors have
# zero chirality expectation. The finite analog is H_anti (spectrum {-l,0,+l}) -- which is
# exactly the case whose EIGENVALUE Koide is infinite. The native MASSIVE circulant operator,
# whose signed spectrum gives Q=2/3, is the gamma5-COMMUTING (non-chiral) case.
# So the 'signedness' that yields Q=2/3 is the NON-chiral (commuting) structure;
# genuine chirality (anticommutation) yields the {-l,0,+l} massless pattern, not 2/3.
check("4D-analog chirality (anticommuting) = {-l,0,+l} pattern = the Q=infinity eigenvalue case, "
      "NOT the signed Q=2/3 case",
      sum_lam_anti == 0)
check("circulant Q=2/3 operator is the Gamma_chi-COMMUTING (non-chiral on this factor)",
      sp.simplify(Hc*Gam - Gam*Hc) == sp.zeros(3,3))

print()
print("="*78)
print("PART 8 -- N5 execution certificate: what this runner resolves, per class")
print("="*78)
print(
    "per_element: checked — the operator identities are resolved entry by entry on "
    "3x3 matrices: Gamma_chi = (2/3)J - I matches the circulant (-1/3, 2/3, 2/3) in "
    "all nine entries, [Gamma_chi, R] and [H_circ, Gamma_chi] vanish in all nine, and "
    "the circulant/Gamma_chi anticommutator is nonzero on all three Hermitian-"
    "circulant basis directions I, R+R^2, and i(R-R^2)."
)
print(
    "per_site: checked and not executed — every operator here lives on the internal "
    "three-generation R^3 factor; the Z^3 lattice baseline named in the header is "
    "never instantiated, so no spatial site carries any of these operators and no "
    "site-resolved statement about the readout is produced."
)
print(
    "per_mode: checked — the three Z3 character modes are resolved individually with "
    f"Gamma_chi grades (+1, -1, -1): at theta=pi the grade/sign pairs are {patt_pi} so "
    f"the +1 singlet mode is the negative one, while at theta=0.9 they are {patt_0p9} "
    "so a -1 doublet mode is negative — the sign roams across grades."
)
print(
    "per_block: checked — the Gamma_chi grading splits the generation factor into a "
    "1-dimensional +1 block and a 2-dimensional -1 block, and the two operator classes "
    "over those blocks are disjoint: no nonzero Hermitian circulant anticommutes with "
    "Gamma_chi, executed as the full-class kernel argument (every circulant commutes "
    "with Gamma_chi, so {H, Gamma_chi} = 2 H Gamma_chi, and Gamma_chi^2 = I forces "
    "H = 0) plus the asserted symbolic solve over the complex-Hermitian coefficients, "
    f"the anticommuting representative having spectrum {spec_num} summing to 0."
)
print(
    "lattice_wide: checked and not executed — the Lattice = Z^3 and Qubit = M_2(C) "
    "baselines are cited as provenance only and nothing is evaluated beyond the single "
    "three-generation factor, so the readout contrast Q(signed) = "
    f"{Q_signed_theta09:.6f} vs Q(singular) = {Q_singular_theta09:.6f} is certified at "
    f"that scope alone, with PASS={PASS}, FAIL={FAIL}."
)

print()
print("="*78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("="*78)

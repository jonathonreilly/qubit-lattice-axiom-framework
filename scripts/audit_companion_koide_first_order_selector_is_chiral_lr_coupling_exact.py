import sympy as sp
from sympy import I, simplify, symbols, Matrix, eye, exp, pi, Rational, conjugate, sqrt, zeros

R=[]; chk=lambda l,o: R.append((l,bool(o)))
w=exp(2*I*pi/3)
C=Matrix([[0,1,0],[0,0,1],[1,0,0]])           # cyclic shift, C^3=I
a,bre,bim,d=symbols('a bre bim delta',real=True)

# (1) U(1)_b RED HERRING: Q=(1+2r)/3 is delta-INDEPENDENT. masses sqrt(m_k)=lambda_k=a+2|b|cos(delta+2pi k/3).
bmod=symbols('bmod',positive=True)
lam=[a+2*bmod*sp.cos(d+2*pi*k/3) for k in range(3)]
Slam=simplify(sum(lam)); Slam2=simplify(sum(l**2 for l in lam))
Q=simplify(Slam2/Slam**2)
chk("(1a) Sum lambda = 3a, Sum lambda^2 = 3a^2+6|b|^2 (both delta-INDEPENDENT) -> U(1)_b is a red herring",
    simplify(Slam-3*a)==0 and simplify(Slam2-(3*a**2+6*bmod**2))==0)
r=symbols('r',positive=True)
chk("(1b) Q=(1+2r)/3 with r=|b|^2/a^2 -> Q=2/3 iff r=1/2; Q has NO delta dependence (count is a functional choice, not a symmetry quotient)",
    simplify(Q.subs(bmod, sqrt(r)*a) - (1+2*r)/3)==0)

# (2) DISCRETE Z3 clock grading rho(M)=Omega^-1 M Omega, Omega=diag(1,w,w^2): rho(C^k)=w^k C^k -> nontrivial Z3.
Om=Matrix([[1,0,0],[0,w,0],[0,0,w**2]])
chk("(2a) clock grading: Omega^-1 C Omega = w * C (genuine nontrivial Z3 action, character k on C^k line)",
    simplify(Om.inv()*C*Om - w*C)==zeros(3,3))
# character/index multiplicity: regular rep = triv (+) w (+) wbar,
# each multiplicity 1 -> conditional (singlet,doublet)=(1,1) block balance.
chi_reg=[3,0,0]; inner=lambda A,B: simplify(sum(x*conjugate(y) for x,y in zip(A,B))/3)
mult=(inner(chi_reg,[1,1,1]), inner(chi_reg,[1,w,w**2]), inner(chi_reg,[1,w**2,w**4]))
chk("(2b) discrete Z3 character index -> multiplicity (1,1,1), so the conditional (singlet,doublet)=(1,1) block-balance algebra respects C^3=I",
    mult==(1,1,1))

# (3) WITHIN-R^3 NO-GO: Gamma_chi=(2/3)J-I (J=I+C+C^2) is CIRCULANT -> every C3-equivariant (circulant) H COMMUTES
#     with Gamma_chi -> comm(C) cap anticomm(Gamma_chi) = {0}; physical r-weighting still needs a readout rule.
#     The converse is false in the full matrix algebra: preserving the singlet/doublet split is weaker than C3-equivariance.
J=eye(3)+C+C*C; Gam=Rational(2,3)*J-eye(3)
chk("(3a) Gamma_chi=(2/3)(I+C+C^2)-I is circulant with eigenvalues {+1,-1,-1} (generation chirality grading)",
    simplify(Gam*C-C*Gam)==zeros(3,3) and sorted(Gam.eigenvals().keys(),key=lambda z:sp.re(z))==[-1,1])
p,q=symbols('p q')
H=a*eye(3)+p*C+q*C*C                                # general C3-equivariant (circulant) generation operator
anti=H*Gam+Gam*H                                    # require anticommute -> {H,Gam}=0
sol=sp.solve([anti[i,j] for i in range(3) for j in range(3)],[a,p,q],dict=True)
chk("(3b) comm(C) cap anticomm(Gamma_chi) = {0}: the ONLY C3-equivariant Gamma_chi-anticommuting operator is 0 -> within R^3, first-order is forbidden",
    sol==[{a:0,p:0,q:0}] or all(s[a]==0 and s[p]==0 and s[q]==0 for s in sol))
Pe=eye(3)-Rational(1,3)*J
K=Pe*Matrix([[1,0,0],[0,0,0],[0,0,-1]])*Pe
chk("(3c) converse guard: an operator can commute with Gamma_chi while failing C3-equivariance, so the source may claim only the forward/native-circulant implication",
    simplify(K*Gam-Gam*K)==zeros(3,3) and simplify(K*C-C*K)!=zeros(3,3))

# (4) THE ESCAPE (factor-crossing): on R^3 (x) C^2, I3(x)sx is C3-equivariant AND Gamma_chi-anticommuting;
#     the L-R coupling M(b)(x)sigma_+ wires the chirality factor to the b-dependent mass.
sx=Matrix([[0,1],[1,0]]); sz=Matrix([[1,0],[0,-1]]);
def kron(A,B):
    return Matrix(sp.BlockMatrix([[A[i,j]*B for j in range(A.cols)] for i in range(A.rows)]).as_explicit())
Cx=kron(C,eye(2)); Gx=kron(eye(3),sz); O=kron(eye(3),sx)
chk("(4) on R^3(x)C^2: O=I3(x)sx COMMUTES with C(x)I (C3-equivariant) AND ANTICOMMUTES with I3(x)sz (chirality) -> the escape EXISTS across factors",
    simplify(O*Cx-Cx*O)==zeros(6,6) and simplify(O*Gx+Gx*O)==zeros(6,6) and O!=zeros(6,6))

# (5) NATIVE default: M(b) eigenvectors are the b-INDEPENDENT C3-Fourier vectors -> Berry-flat / commuting side.
b=bre+I*bim; M=a*eye(3)+b*C+conjugate(b)*(C*C)
fk=lambda k: Matrix([1,w**k,w**(2*k)])
chk("(5) M(b) f_k = (a+b w^k + bbar w^2k) f_k for b-INDEPENDENT Fourier f_k -> eigenvectors b-independent -> Berry-flat commuting side; no physical r weighting is selected here",
    all(simplify(M*fk(k) - (a+b*w**k+conjugate(b)*w**(2*k))*fk(k))==zeros(3,1) for k in range(3)))

# (6) source-note boundary tokens (honest scope: localization + correction, NOT a derivation)
from pathlib import Path
NOTE=Path(__file__).resolve().parent.parent/"docs"/"KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md"
if NOTE.exists():
    tt=NOTE.read_text()
    toks=[
        "**Type:** bounded_theorem",
        "**Claim type:** bounded_theorem",
        "red herring",
        "not a derivation of `r = 1/2`",
        "L-R coupling",
        "grading",
        "The converse is **not** claimed",
        "no retained bridge supplied here",
        "2026-06-13 bridge-scope firewall",
        "not a retained bridge from",
        "not a physical `r`-weighting derivation",
        "not a proof that the framework supplies the first-order chiral coupling",
        "commutes with Gamma_chi  does not imply  C3-equivariant",
        "must not cite this packet as a retained derivation of",
        "physical `M(b)⊗σ₊` tensor coupling",
        "not as a retained positive theorem deriving the physical",
        "2026-06-18 bounded-localization source packet",
        "Load-bearing theorem surface:",
        "Non-load-bearing open gates:",
        "bounded algebraic localization and route-pruning theorem",
        "KOIDE_FIRST_ORDER_SELECTOR_BOUNDED_LOCALIZATION_CERTIFICATE_2026-06-18.md",
        "independent audit lane only",
        # 2026-06-20 bounded-localization source-boundary repair:
        # the row keeps the source-boundary SECOND branch (bounded localization only),
        # explicitly leaving the physical M(b)(x)sigma_+ bridge + r-weighting OPEN.
        "**Status authority:** independent audit lane only",
        "2026-06-20 bounded-localization source-boundary repair",
        "This repair confirms the **second** branch",
        "No physical `M(b)⊗σ₊` bridge and no",
        "the `AC_phi_lambda` /",
        "physical first-order/readout `r`-weighting rule",
        "`r=1/2` is a **stable dial",
        "names the **algebraic shape inside",
    ]
    banned=[
        "**The selector is exactly that L-R coupling.**",
        "which makes the generation eigenvectors b-dependent → nonzero Berry curvature → first-order → `r=1/2`",
    ]
    chk("(6) source note keeps the bounded localization/no-derivation boundary and removes old positive-selector wording",
        all(k in tt for k in toks) and not any(k in tt for k in banned))
else:
    chk("(6) source note present", False)

P=sum(1 for _,o in R if o); F=sum(1 for _,o in R if not o)
for l,o in R: print(("PASS:" if o else "FAIL:"),l)
print("\nTOTAL: PASS=%d FAIL=%d"%(P,F))
print("SUMMARY: PASS=%d FAIL=%d"%(P,F))
if F: raise SystemExit(1)
print("\nBOUNDED-LOCALIZATION SYNTHESIS verified: (1) U(1)_b is a RED HERRING (Q delta-independent; count=functional choice).\n"
      "(2) the DISCRETE Z3-character index gives the conditional (1,1) block-balance algebra while respecting C^3=I,\n"
      "so an index can encode that balance without a continuous symmetry. (3) WITHIN R^3, C3-equivariant/native\n"
      "circulant mass has comm(C) cap anticomm(Gamma_chi)={0}; the converse commutes-with-Gamma_chi=>C3-equivariant\n"
      "is false and is not claimed. (4) the factor-crossing L-R coupling shape M(b)(x)sigma_+ exists in the algebra.\n"
      "(5) the native mass is Berry-flat/commuting. NET: this is bounded algebraic localization only; the framework\n"
      "supplies the grading eps but NOT the physical coupling or r-weighting rule -> gated on the AC_phi_lambda corner\n"
      "realization. NOT a derivation of r=1/2 and NOT a retained positive selector theorem.")

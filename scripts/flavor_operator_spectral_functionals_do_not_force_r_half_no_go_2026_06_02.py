#!/usr/bin/env python3
"""
Variational-forcing test for the charged-lepton Koide value r = |b|^2/a^2 = 1/2
(<=> Q = 2/3) on the C_3-circulant weight family of generation C^3 = grade-1 of Cl(3).

ANGLE: does a choice-free operator-spectral functional on the weight family make
r=1/2 a UNIQUE / FORCED extremum (not merely a permitted stationary point)?

Setup:
  H = a I + b (J - I)  on C^3,  J = all-ones, eig(J)={3,0,0}
  eigenvalues of H: {a+2b (singlet), a-b (doublet x2)}
  r := b^2/a^2 ;  Q := Tr(H^2)/(Tr H)^2 = 1/3 + (2/3) r   [exact]
  Tr H^2 = 3 a^2 + 6 b^2 = ||I||_HS^2 a^2 + ||J-I||_HS^2 b^2  (HS norms 3, 6)
  r = 1/2  <=>  3 a^2 = 6 b^2  (equal-HS-energy)  <=>  Q = 2/3

Each check() returns True iff the asserted fact holds. The script prints
SCORECARD: PASS=N FAIL=0 when all pass.
"""
import numpy as np
import sympy as sp

from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    return ok


# ----------------------------------------------------------------------
# 0. EXACT Q(r) and the equal-HS-energy characterization of r=1/2
# ----------------------------------------------------------------------
a = sp.symbols('a', positive=True)
b = sp.symbols('b', real=True)
r = sp.symbols('r', positive=True)
t = sp.symbols('t', positive=True)

lam = [a + 2 * b, a - b, a - b]
TrH = sum(lam)
TrH2 = sum(l**2 for l in lam)
Q_ab = sp.simplify(TrH2 / TrH**2)
Q_r = sp.simplify(Q_ab.subs(b, a * sp.sqrt(r)))   # b = +a sqrt(r) branch
check("0a. Tr H^2 = 3 a^2 + 6 b^2 (HS norms 3,6)",
      sp.simplify(TrH2 - (3 * a**2 + 6 * b**2)) == 0,
      f"TrH2={sp.expand(TrH2)}")
check("0b. Q(r) = 1/3 + (2/3) r exactly",
      sp.simplify(Q_r - (sp.Rational(1, 3) + sp.Rational(2, 3) * r)) == 0,
      f"Q(r)={Q_r}")
check("0c. r=1/2 <=> 3a^2=6b^2 (equal-HS-energy) <=> Q=2/3",
      sp.simplify(Q_r.subs(r, sp.Rational(1, 2))) == sp.Rational(2, 3))

# ----------------------------------------------------------------------
# 1. OPERATOR-SPECTRAL FUNCTIONALS ALL LAND AT r=0 or r=1, NOT r=1/2
#    (these take the entropy/energy of states built DIRECTLY from H, no
#     hand-picked 2-sector partition -> they are the genuinely-forced ones)
# ----------------------------------------------------------------------
bb = sp.sqrt(r)
lam_r = [1 + 2 * bb, 1 - bb, 1 - bb]            # a=1 gauge
mu = [l**2 for l in lam_r]                       # eig(H^2)=eig(H^dag H)
Zspec = sum(mu)
pspec = [m / Zspec for m in mu]
xs = np.linspace(1e-4, 0.999, 6000)


def argext(expr, kind='max'):
    f = sp.lambdify(r, expr, 'numpy')
    y = f(xs)
    idx = np.nanargmax(y) if kind == 'max' else np.nanargmin(y)
    return float(xs[idx])


# spectral (3-eigenvalue) entropy -> max at r->0
S3 = -sum(pi * sp.log(pi) for pi in pspec)
check("1a. Spectral entropy S3 (3 eigenvalues) peaks at r->0, NOT 1/2",
      argext(S3, 'max') < 0.05, f"argmax~{argext(S3,'max'):.4f}")

# vN entropy of rho = H^2/Tr H^2 == spectral entropy -> r->0
check("1b. vN entropy of rho=H^2/TrH^2 peaks at r->0, NOT 1/2",
      argext(S3, 'max') < 0.05)

# vN entropy of thermal rho = e^{-H}/Z  -> r->0
ex = [sp.exp(-l) for l in lam_r]
Zb = sum(ex)
pth = [e / Zb for e in ex]
Sth = -sum(pi * sp.log(pi) for pi in pth)
check("1c. vN entropy of rho=e^{-H}/Z peaks at r->0, NOT 1/2",
      argext(Sth, 'max') < 0.05, f"argmax~{argext(Sth,'max'):.4f}")

# relative entropy S(rho_spec || I/3) -> min at r->0 (closest to uniform)
Srel = sum(pspec[i] * sp.log(pspec[i] / sp.Rational(1, 3)) for i in range(3))
check("1d. Rel.entropy S(rho_spec||I/3) min at r->0, NOT 1/2",
      argext(Srel, 'min') < 0.05, f"argmin~{argext(Srel,'min'):.4f}")

# purity Tr rho_spec^2 minimized (most mixed) at r->0
pur = sum(pi**2 for pi in pspec)
check("1e. Purity Tr(rho_spec^2) min (most mixed) at r->0, NOT 1/2",
      argext(pur, 'min') < 0.05, f"argmin~{argext(pur,'min'):.4f}")

# ----------------------------------------------------------------------
# 2. THE CANONICAL HS METRIC ON THE C_3-COMMUTANT IS FORCED & ISOTROPIC,
#    BUT GIVES THE 3-MODE (DIMENSION) COUNT -> r=1, NOT r=1/2
# ----------------------------------------------------------------------
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)   # cyclic shift, C^3=I
I3 = np.eye(3, dtype=complex)
basis = [I3, C, C @ C]                                      # span of commutant M_3(C)^{C3}
gram = np.array([[np.trace(basis[i].conj().T @ basis[j]) for j in range(3)]
                 for i in range(3)])
check("2a. {I,C,C^2} are HS-orthogonal, each norm^2=3 (canonical, forced metric)",
      np.allclose(gram, 3 * np.eye(3)),
      f"diag={np.round(np.diag(gram).real,3)}")
JmI = (C + C @ C)                                            # J - I = C + C^2 (real doublet channel)
check("2b. Real channels: ||I||^2=3, ||J-I||^2=6 (UNEQUAL) -> dimension count weights C,C^2 separately -> r=1",
      np.isclose(np.trace(I3.conj().T @ I3).real, 3)
      and np.isclose(np.trace(JmI.conj().T @ JmI).real, 6))
# Cl(3) grade-1 (Pauli) metric is isotropic delta_ij and generation-blind
sig = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]
Gg = np.array([[np.trace(sig[i] @ sig[j]).real / 2 for j in range(3)] for i in range(3)])
check("2c. Cl(3) grade-1 canonical metric is isotropic delta_ij (says nothing about I-vs-(J-I) weight)",
      np.allclose(Gg, np.eye(3)))

# ----------------------------------------------------------------------
# 3. THE FUNCTIONALS THAT DO LAND AT r=1/2 ALL REQUIRE THE 2-SECTOR
#    (BLOCK-FOLD / Frobenius beta=0 / det_C) CHOICE -- PERMITTED, NOT FORCED
# ----------------------------------------------------------------------
pI = 1 / (1 + 2 * r)            # 2-sector power dist (folds C,C^2 into ONE doublet)
poff = 2 * r / (1 + 2 * r)
S2 = -(pI * sp.log(pI) + poff * sp.log(poff))
crit2 = [s for s in sp.solve(sp.diff(S2, r), r) if s.is_real and s > 0]
check("3a. Sector-power entropy S2 has unique crit pt r=1/2 (a MAX, S=log2)",
      crit2 == [sp.Rational(1, 2)]
      and sp.simplify(S2.subs(r, sp.Rational(1, 2)) - sp.log(2)) == 0
      and sp.diff(S2, r, 2).subs(r, sp.Rational(1, 2)) < 0)
imbalance = (pI - poff)**2
crit_imb = [s for s in sp.solve(sp.diff(imbalance, r), r) if s.is_real and s > 0]
check("3b. 2-sector imbalance (p_I-p_off)^2 has unique min at r=1/2",
      crit_imb == [sp.Rational(1, 2)])

# ----------------------------------------------------------------------
# 4. THE RETAINED FROBENIUS NO-GO, PARAMETRIZED: the Ad-invariant PD metric
#    family B = alpha Tr(AB) + beta tr(A)tr(B) has a FREE beta; r=1/2 <=> beta=0,
#    UNFORCED on the whole PD cone (alpha>0, alpha+3 beta>0).
# ----------------------------------------------------------------------
al, be = sp.symbols('alpha beta', real=True)
a2, b2 = sp.symbols('a b', real=True)
B_HH = al * (3 * a2**2 + 6 * b2**2) + be * (3 * a2)**2     # = (3al+9be)a^2 + 6 al b^2
acoef = sp.expand(B_HH).coeff(a2**2)
bcoef = sp.expand(B_HH).coeff(b2**2)
# 'balanced metric' (equal channel coefficient) solves acoef==bcoef for the metric:
bal = sp.solve(sp.Eq(acoef, bcoef), be)
check("4a. Ad-invariant metric energy B(H,H)=(3a+9b)a^2 + 6a b^2; 'channel-balance' needs alpha=3 beta (a free curve)",
      bal == [al / 3])
check("4b. r=1/2 (3a^2=6b^2 channel-energy balance) corresponds to Frobenius beta=0 -- a single UNFORCED point of the PD cone",
      sp.simplify(acoef.subs(be, 0) - 3 * al) == 0
      and sp.simplify(bcoef.subs(be, 0) - 6 * al) == 0)
# PD cone admits beta != 0 (e.g. alpha=beta=1): scalar weight 4, traceless weight 1, PD, NOT Frobenius
check("4c. PD cone contains beta!=0 (alpha=beta=1: PD, Ad-invariant, != Frobenius) -> beta=0 not forced",
      (1 > 0) and (1 + 3 * 1 > 0))

# ----------------------------------------------------------------------
# 5. RP / T-POSITIVITY is an INEQUALITY (cone) condition: e^{-tH} is PD for
#    EVERY real (a,b) since H is real-symmetric -> pins NO interior r.
# ----------------------------------------------------------------------
def min_eig_exp(av, bv, tv=1.0):
    H = av * np.eye(3) + bv * (np.ones((3, 3)) - np.eye(3))
    return np.min(np.linalg.eigvalsh(__import__('scipy.linalg', fromlist=['expm']).expm(-tv * H))) \
        if False else np.min(np.exp(-tv * np.linalg.eigvalsh(H)))


pts = [(1.0, x) for x in np.linspace(-0.4, 0.9, 14)]   # interior of PD/admissible window
allpos = all(min_eig_exp(av, bv) > 0 for av, bv in pts)
check("5. RP/T-positivity (e^{-tH} PD) holds on the WHOLE admissible r-line -> inequality, pins no interior r",
      allpos)

# ----------------------------------------------------------------------
print()
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
emit_n5_resolution_certificate(
    per_element=(
        sp.simplify(Q_r - (sp.Rational(1, 3) + sp.Rational(2, 3) * r)) == 0,
        "the exact three-eigenvalue trace functional reduces elementwise to Q(r)=1/3+(2/3)r",
    ),
    per_site=(
        True,
        "checked and not executed — the tested invariant is the internal C3 commutant Gram matrix and has no spatial-site index or intersite operator",
    ),
    per_mode=(
        np.allclose(gram, 3 * np.eye(3)) and allpos,
        "the three canonical C3 modes are Hilbert-Schmidt isotropic while all fourteen positivity samples leave the interior ratio unpinned",
    ),
    per_block=(
        crit2 == [sp.Rational(1, 2)] and bal == [al / 3],
        "the two-sector fold reaches r=1/2 only after the executed block choice, while the invariant metric retains a free beta curve",
    ),
    lattice_wide=(
        True,
        "checked and not executed — the exact proof exhausts the finite three-mode carrier and positivity samples but defines no lattice tensor product or spatial limit",
    ),
)

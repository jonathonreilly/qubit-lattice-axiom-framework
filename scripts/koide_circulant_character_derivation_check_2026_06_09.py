#!/usr/bin/env python3
"""
Runner for KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md
(claim_id: koide_circulant_character_derivation_note_2026-04-18).

WHAT THIS RUNNER PROVES (load-bearing, exact sympy, classes C/A)
----------------------------------------------------------------
The note is a BOUNDED theorem. Its unconditional content is:

  Circulant commutant: on the retained hw=1 triplet, every Hermitian
      operator commuting with the C_3[111] cyclic conjugation action is a
      circulant H = a*I + b*C + conj(b)*C^2, with a real and b complex.
      Proven here by solving C H = H C on a generic 9-real-parameter
      Hermitian, and cross-checked against the Ad-character isotypic
      multiplicities (3,3,3) of C_3 on M_3(C).
  Cosine spectrum: eig(H) = {a + 2|b| cos(arg b + 2*pi*k/3): k=0,1,2}.
  Character-weight bridge: the C_3 character coefficients of the eigenvalue
      triple are a_0 = sqrt(3)*a, z = sqrt(3)*b, hence the
      Frobenius-equipartition condition (3a^2 = 6|b|^2) is equivalent to
      the equal-character-weight condition a_0^2 = 2|z|^2.
  Conditional Koide implication: if Frobenius equipartition
      (2|b| = sqrt(2)*a, a>0) and square-root readout
      (lambda_k = sqrt(m_k) >= 0) hold, then Q = 2/3 exactly, for every
      symbolic phase delta (delta-independence is exact, not numeric).
  Positivity boundary: under Frobenius equipartition the eigenvalue ratio is
      capped at 1 + sqrt(2); positivity of all lambda_k restricts delta to a
      window whose edge (massless eigenvalue) sits exactly at delta = pi/12.

WHAT THIS RUNNER DOES NOT PROVE (the declared open boundary)
------------------------------------------------------------
No selection principle for Frobenius equipartition, no derivation of square-root readout, no derivation of
delta = 2/9 or of the scale v_0 is claimed or checked as a theorem.
The PDG comparisons in PART D below are EXTERNAL COMPARATOR checks
(class D) at the FITTED phase delta = 2/9 and FITTED scale v_0; they are
decoration for the bounded claim, never load-bearing.  A runner PASS in
PART D must not be read as a first-principles mass derivation.

Check classes are labelled per check: [C] first-principles compute from
the framework C_3[111] structure, [A] exact algebraic identity,
[D] external comparator (PDG inputs, fitted scale/phase).
No check in this file is class (B), (E), (F) or (G)-as-derivation:
every PART D check is explicitly declared a comparator.

Runtime: a few seconds.  Exact sympy everywhere in parts C/A;
mpmath (50 dps) in part D.
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 50

PASS = 0
FAIL = 0
LOG = []


def check(name, cond, detail=""):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        LOG.append(f"  [PASS] {name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"  [FAIL] {name}" + (f" :: {detail}" if detail else ""))


# exact primitive cube root of unity (Cartesian form, no exp() surprises)
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2

# cyclic shift X_i -> X_{i+1 mod 3} on the hw=1 triplet basis
C = sp.Matrix([[0, 0, 1],
               [1, 0, 0],
               [0, 1, 0]])

# ==========================================================================
# PART C/A-1: group + isotypic structure of Ad(C_3) on M_3(C)   [class C]
# ==========================================================================

check("C1 [C] C^3 = I and C != I, C^2 != I (C generates Z_3 exactly)",
      sp.simplify(C**3) == sp.eye(3) and C != sp.eye(3) and C**2 != sp.eye(3))

# Ad character: chi_Ad(g) = |tr U(g)|^2 ; multiplicities by exact character
# orthogonality  m_j = (1/3) * sum_g chi_Ad(g) * conj(chi_j(g))
tr = [sp.trace(C**p) for p in range(3)]           # 3, 0, 0
chi_ad = [sp.Abs(t)**2 for t in tr]               # 9, 0, 0
mults = []
for j in range(3):
    m_j = sp.Rational(1, 3) * sum(
        chi_ad[g] * sp.conjugate(omega**(j * g)) for g in range(3))
    mults.append(sp.simplify(m_j))
check("C2 [C] Ad(C_3) isotypic multiplicities on M_3(C) are (3,3,3)",
      mults == [3, 3, 3],
      f"m_triv,m_omega,m_omegabar = {mults}")

# ==========================================================================
# PART C/A-2: commutant theorem circulant-commutant theorem (circulant-commutant theorem of the note)             [class C]
# ==========================================================================

xs = sp.symbols('x0:9', real=True)
H_gen = sp.Matrix([
    [xs[0],                 xs[3] + sp.I * xs[4], xs[5] + sp.I * xs[6]],
    [xs[3] - sp.I * xs[4],  xs[1],                xs[7] + sp.I * xs[8]],
    [xs[5] - sp.I * xs[6],  xs[7] - sp.I * xs[8], xs[2]]])

check("C3 [A] H_gen is the generic Hermitian (H_gen.H == H_gen, 9 real params)",
      sp.simplify(H_gen.H - H_gen) == sp.zeros(3, 3))

sols = sp.solve(list(C * H_gen - H_gen * C), list(xs), dict=True)
check("C4 [C] commutant solve C H = H C has a unique solution branch",
      len(sols) == 1)
sol = sols[0]
H_comm = sp.simplify(H_gen.subs(sol))
free = sorted(H_comm.free_symbols, key=lambda s: s.name)
check("C5 [C] commutant of Ad(C_3) in Herm(3) is a 3-real-parameter family",
      len(free) == 3, f"free real parameters: {free}")

# exhibit it as a*I + b*C + conj(b)*C^2 exactly
a_s = sp.symbols('a', real=True)
br, bi = sp.symbols('b_r b_i', real=True)
b_s = br + sp.I * bi
H_circ = a_s * sp.eye(3) + b_s * C + sp.conjugate(b_s) * C**2
# The commutant solve left exactly three free real parameters
# (x2 = common diagonal, x7 + i*x8 = common upper off-diagonal = conj(b)).
# The identification a = x2, b = x7 - i*x8 is an explicit linear bijection
# between the solved family and the circulant family.
x2_, x7_, x8_ = free
H_circ_mapped = H_circ.subs({a_s: x2_, br: x7_, bi: -x8_})
check("C6 [C] commutant family is EXACTLY {a*I + b*C + conj(b)*C^2}"
      " under the bijection a = x2, b = x7 - i*x8",
      sp.simplify(sp.expand_complex(H_comm - H_circ_mapped)) == sp.zeros(3, 3),
      "circulant form forced, not assumed")

check("C7 [A] a*I + b*C + conj(b)*C^2 is Hermitian for all real a, complex b",
      sp.simplify(H_circ.H - H_circ) == sp.zeros(3, 3))

# circulants lie in the trivial isotypic component (Ad-invariance)
check("C8 [A] circulant family is Ad(C)-invariant (trivial isotypic component)",
      sp.simplify(C * H_circ * C**-1 - H_circ) == sp.zeros(3, 3))

# ==========================================================================
# PART A-3: spectrum theorem cosine-spectrum theorem (cosine-spectrum theorem of the note)                [class A]
# ==========================================================================

r, delta = sp.symbols('r delta', real=True, positive=True), \
    sp.symbols('delta_ph', real=True)
r = sp.symbols('r', positive=True)
b_polar = r * sp.exp(sp.I * delta)
H_pol = a_s * sp.eye(3) + b_polar * C + sp.conjugate(b_polar) * C**2

lam_claim = [sp.simplify(a_s + 2 * r * sp.cos(delta + 2 * sp.pi * k / 3))
             for k in range(3)]

# eigenvalues via the Fourier eigenvectors of C: C v = mu v, mu^3 = 1
ok_spec = True
mus = [omega**k for k in range(3)]
for k, mu in enumerate(mus):
    v = sp.Matrix([1, mu**2, mu])          # C v = mu v for this convention
    if sp.simplify(C * v - mu * v) != sp.zeros(3, 1):
        v = sp.Matrix([1, mu, mu**2])
    ok_spec &= (sp.simplify(C * v - mu * v) == sp.zeros(3, 1))
    lam_k = a_s + b_polar * mu + sp.conjugate(b_polar) * sp.conjugate(mu)
    ok_spec &= (sp.simplify(H_pol * v - lam_k * v) == sp.zeros(3, 1))
    diff = sp.simplify(sp.expand_complex(
        lam_k - (a_s + 2 * r * sp.cos(delta + 2 * sp.pi * k / 3))))
    ok_spec &= (sp.simplify(sp.trigsimp(diff)) == 0)
check("A9 [A] eig(H) = { a + 2|b| cos(arg b + 2 pi k/3) }, exact, symbolic delta",
      ok_spec)

# ==========================================================================
# PART A-4: Frobenius norm + character bridge character-weight bridge                [class A]
# ==========================================================================

frob = sp.simplify(sp.trace(H_pol.H * H_pol))
check("A10 [A] ||H||_F^2 = 3 a^2 + 6 |b|^2 exactly",
      sp.simplify(sp.expand_complex(frob - (3 * a_s**2 + 6 * r**2))) == 0)

lam = lam_claim
a0 = sp.trigsimp((lam[0] + lam[1] + lam[2]) / sp.sqrt(3))
z = sp.simplify(sp.expand_complex(
    (lam[0] + sp.conjugate(omega) * lam[1] + omega * lam[2]) / sp.sqrt(3)))
check("A11 [A] a_0 = sqrt(3) * a (character coefficient of eigenvalue triple)",
      sp.simplify(a0 - sp.sqrt(3) * a_s) == 0)
check("A12 [A] z = sqrt(3) * b (character coefficient of eigenvalue triple)",
      sp.simplify(sp.expand_complex(z - sp.sqrt(3) * b_polar)) == 0)
check("A13 [A] a_0^2 - 2|z|^2 = 3a^2 - 6|b|^2 (Frobenius equipartition <=> equal character weight)",
      sp.simplify(sp.expand_complex(
          a0**2 - 2 * sp.Abs(z)**2 - (3 * a_s**2 - 6 * r**2))) == 0,
      "Frobenius equipartition is the operator-space lift, not a new independent premise")

# ==========================================================================
# PART A-5: cosine identities + conditional Koide implication   [class A]
# ==========================================================================

cos_sum = sp.trigsimp(sum(sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)))
cos2_sum = sp.trigsimp(sum(sp.cos(delta + 2 * sp.pi * k / 3)**2
                           for k in range(3)))
check("A14 [A] sum_k cos(delta + 2 pi k/3) = 0, symbolic delta", cos_sum == 0)
check("A15 [A] sum_k cos^2(delta + 2 pi k/3) = 3/2, symbolic delta",
      sp.simplify(cos2_sum - sp.Rational(3, 2)) == 0)

# Frobenius-equipartition condition: 3a^2 = 6|b|^2  <=>  2|b| = sqrt(2) a (for a, |b| > 0)
rho = sp.symbols('rho', positive=True)
check("A16 [A] 3a^2 = 6|b|^2 <=> 2|b|/a = sqrt(2) for a,|b| > 0",
      sp.simplify(sp.solve(3 * a_s**2 - 6 * (rho * a_s / 2)**2, rho)[0]
                  - sp.sqrt(2)) == 0)

lam_a1 = [a_s * (1 + sp.sqrt(2) * sp.cos(delta + 2 * sp.pi * k / 3))
          for k in range(3)]
S1 = sp.trigsimp(sum(lam_a1))
S2 = sp.trigsimp(sp.expand(sum(x**2 for x in lam_a1)))
check("A17 [A] under Frobenius-equipartition condition: sum_k lambda_k = 3a exactly",
      sp.simplify(S1 - 3 * a_s) == 0)
check("A18 [A] under Frobenius-equipartition condition: sum_k lambda_k^2 = 6a^2 exactly",
      sp.simplify(S2 - 6 * a_s**2) == 0)
Q = sp.simplify(S2 / S1**2)
check("A19 [A] conditional Koide: Q = (sum m)/(sum sqrt m)^2 = 2/3 EXACTLY,"
      " delta-independent (square-root readout identification: lambda_k = sqrt(m_k))",
      sp.simplify(Q - sp.Rational(2, 3)) == 0 and delta not in Q.free_symbols,
      f"Q = {Q} for symbolic delta")

# the alternative identification lambda_k = m_k does NOT give Q = 2/3
lam29 = [x.subs({a_s: 1, delta: sp.Rational(2, 9)}) for x in lam_a1]
Q_alt = sum(lam29) / (sum(sp.sqrt(x) for x in lam29))**2
Q_alt_n = sp.N(Q_alt, 30)
check("A20 [A] alternative reading lambda_k = m_k FAILS Koide"
      " (|Q_alt - 2/3| > 0.05 at delta = 2/9)",
      sp.Abs(Q_alt_n - sp.Rational(2, 3)) > sp.Rational(5, 100),
      f"Q_alt = {sp.N(Q_alt, 8)}")

# ==========================================================================
# PART A-6: boundary structure positivity-boundary theorem (ceiling + positivity window) [class A]
# ==========================================================================

max_over_delta = [sp.maximum(1 + sp.sqrt(2) * sp.cos(delta + 2*sp.pi*k/3),
                             delta, sp.S.Reals) for k in range(3)]
check("A21 [A] under Frobenius-equipartition condition, a>0: sup_delta lambda_k / a = 1 + sqrt(2) exactly"
      " (symbolic maximum over the whole real delta line)",
      all(sp.simplify(m - (1 + sp.sqrt(2))) == 0 for m in max_over_delta),
      f"sup over delta = {max_over_delta[0]} for each k")

lam_pi12 = [sp.simplify(x.subs({a_s: 1, delta: sp.pi / 12}))
            for x in lam_a1]
check("A22 [A] delta = pi/12 gives EXACTLY one massless eigenvalue"
      " (1 + sqrt(2) cos(3 pi/4) = 0 exactly)",
      sorted([sp.simplify(x) == 0 for x in lam_pi12]) == [False, False, True],
      f"eigs/a at pi/12: {[sp.nsimplify(x) for x in lam_pi12]}")

lam_29 = [sp.N(x.subs({a_s: 1, delta: sp.Rational(2, 9)}), 30)
          for x in lam_a1]
check("A23 [A] delta = 2/9 lies strictly inside the positivity window"
      " (all lambda_k > 0); 2/9 < pi/12 with gap 0.0396 rad",
      all(x > 0 for x in lam_29)
      and sp.N(sp.pi / 12 - sp.Rational(2, 9), 10) > 0,
      f"pi/12 - 2/9 = {sp.N(sp.pi/12 - sp.Rational(2,9), 4)} rad")

lam_03 = [sp.N(x.subs({a_s: 1, delta: sp.Rational(3, 10)}), 30)
          for x in lam_a1]
check("A24 [A] positivity window is REAL: delta = 0.3 > pi/12 gives a"
      " negative eigenvalue (square-root readout identification needs the window hypothesis)",
      min(lam_03) < 0, f"min eig/a at delta=0.3: {sp.N(min(lam_03), 5)}")

# delta-candidate arithmetic from Appendix A.2 (pure arithmetic, class A)
d29 = mp.mpf(2) / 9
cand = {
    "2*atan(1/9)": (2 * mp.atan(mp.mpf(1) / 9), 0.41),
    "pi/14": (mp.pi / 14, 0.98),
    "2*pi/27": (2 * mp.pi / 27, 4.72),
}
ok_cand = True
det = []
for nm, (val, pct) in cand.items():
    off = abs(float((val - d29) / d29 * 100))
    ok_cand &= abs(off - pct) < 0.02
    det.append(f"{nm}: {off:.2f}% off")
check("A25 [A] Appendix A.2 candidate-delta residuals: 0.41%, 0.98%, 4.72%",
      ok_cand, "; ".join(det))
check("A26 [A] 2/9 = 2/dim_R Herm(3) = 2/|C_3|^2 (exact arithmetic identity;"
      " the radian unit bridge stays OPEN)",
      sp.Rational(2, 9) == sp.Rational(2, 3**2))

# ==========================================================================
# PART D: EXTERNAL COMPARATOR (PDG inputs, FITTED delta and v_0) [class D]
# NOT load-bearing for the bounded theorem.  Decoration only.
# ==========================================================================

m_e = mp.mpf('0.5109989')      # MeV, PDG
m_mu = mp.mpf('105.6583745')   # MeV, PDG
m_tau = mp.mpf('1776.86')      # MeV, PDG
s_e, s_mu, s_tau = (mp.sqrt(x) for x in (m_e, m_mu, m_tau))
v0 = (s_e + s_mu + s_tau) / 3

check("D27 [D] sqrt-mass data: sqrt(m_e,mu,tau) = (0.71484, 10.27903,"
      " 42.15282) sqrt(MeV); v_0 = 17.71556 (FITTED scale)",
      abs(s_e - mp.mpf('0.71484')) < 1e-5
      and abs(s_mu - mp.mpf('10.27903')) < 1e-5
      and abs(s_tau - mp.mpf('42.15282')) < 1e-5
      and abs(v0 - mp.mpf('17.71556')) < 1e-5,
      f"v_0 = {mp.nstr(v0, 7)} sqrt(MeV)")

Q_pdg = (m_e + m_mu + m_tau) / (s_e + s_mu + s_tau)**2
check("D28 [D] empirical Koide ratio Q_PDG = 0.6666605;"
      " |Q_PDG - 2/3| = 6.2e-6 (comparator, not a derivation)",
      abs(Q_pdg - mp.mpf('0.6666605')) < 1e-7
      and abs(Q_pdg - mp.mpf(2) / 3) < mp.mpf('7e-6'),
      f"Q_PDG - 2/3 = {mp.nstr(Q_pdg - mp.mpf(2)/3, 3)}")

# exact character projection of the PDG triple (assignment tau,e,mu -> k=0,1,2)
om_n = mp.exp(2j * mp.pi / 3)
lam_pdg = [s_tau, s_e, s_mu]
b_fit = sum(lam_pdg[k] * om_n**(-k) for k in range(3)) / 3
a_fit = sum(lam_pdg) / 3
delta_fit = mp.arg(b_fit)
rho_fit = 2 * abs(b_fit) / a_fit
check("D29 [D] exact character projection of PDG triple: delta_fit = 0.2222296"
      " (|delta_fit - 2/9| = 7.4e-6 rad; FITTED phase)",
      abs(delta_fit - mp.mpf('0.2222296')) < 1e-7
      and abs(delta_fit - d29) < mp.mpf('8e-6'),
      f"delta_fit = {mp.nstr(delta_fit, 8)}")
check("D30 [D] rho_fit = 2|b|/a = 1.4142005; |rho_fit - sqrt(2)| = 1.3e-5"
      " (Frobenius equipartition holds to 1e-5 empirically; selection NOT derived)",
      abs(rho_fit - mp.mpf('1.4142005')) < 1e-7
      and abs(rho_fit - mp.sqrt(2)) < mp.mpf('2e-5'),
      f"rho_fit = {mp.nstr(rho_fit, 8)}")

# prediction table at delta = 2/9 exactly (note's corrected table)
assign = {0: ('tau', s_tau), 1: ('e', s_e), 2: ('mu', s_mu)}
table_expect = {  # (cos, 1+sqrt2 cos, v0*(.), residual_pct) note values
    0: ('0.97541', '2.37944', '42.1531', 0.00063),
    1: ('-0.67858', '0.04035', '0.71482', -0.0029),
    2: ('-0.29684', '0.58021', '10.2788', -0.0024),
}
ok_tab = True
det = []
for k in range(3):
    th = d29 + 2 * mp.pi * k / 3
    c = mp.cos(th)
    f = 1 + mp.sqrt(2) * c
    pred = v0 * f
    nm, obs = assign[k]
    resid_pct = (pred - obs) / obs * 100
    ec, ef, ep, er = table_expect[k]
    ok_tab &= abs(c - mp.mpf(ec)) < 1e-5
    ok_tab &= abs(f - mp.mpf(ef)) < 1e-5
    ok_tab &= abs(pred - mp.mpf(ep)) < 2e-4
    ok_tab &= abs(resid_pct - er) < 5e-4
    det.append(f"{nm}: pred {mp.nstr(pred, 6)} vs {mp.nstr(obs, 6)}"
               f" ({mp.nstr(resid_pct, 2)}%)")
check("D31 [D] corrected prediction table at delta = 2/9: residuals"
      " tau +0.0006%, e -0.0029%, mu -0.0024% (all < 0.01%)",
      ok_tab and all(abs((v0 * (1 + mp.sqrt(2) * mp.cos(d29 + 2*mp.pi*k/3))
                          - assign[k][1]) / assign[k][1]) < mp.mpf('1e-4')
                     for k in range(3)),
      "; ".join(det))

# sector non-universality (Appendix A.3): PDG quark masses (GeV)
m_u, m_c, m_t = mp.mpf('0.00216'), mp.mpf('1.273'), mp.mpf('172.57')
m_d, m_s, m_b = mp.mpf('0.00470'), mp.mpf('0.0935'), mp.mpf('4.183')
v0_up = sum(mp.sqrt(x) for x in (m_u, m_c, m_t)) / 3
v0_dn = sum(mp.sqrt(x) for x in (m_d, m_s, m_b)) / 3
rat_t = mp.sqrt(m_t) / v0_up
rat_b = mp.sqrt(m_b) / v0_dn
rat_tau = s_tau / v0
ceil = 1 + mp.sqrt(2)
check("D32 [D] top overshoots the Frobenius-equipartition condition ceiling: ratio 2.754 -> required"
      " cos = 1.240 > 1 (impossible); bottom 2.536 -> 1.086 > 1",
      abs(rat_t - mp.mpf('2.754')) < 2e-3
      and (rat_t - 1) / mp.sqrt(2) > 1
      and abs(rat_b - mp.mpf('2.536')) < 2e-3
      and (rat_b - 1) / mp.sqrt(2) > 1,
      f"required cos: up {mp.nstr((rat_t-1)/mp.sqrt(2), 4)},"
      f" down {mp.nstr((rat_b-1)/mp.sqrt(2), 4)}")
check("D33 [D] tau sits at 98.6% of the 1+sqrt(2) ceiling (ratio 2.37942)",
      abs(rat_tau - mp.mpf('2.37942')) < 1e-4
      and abs(rat_tau / ceil - mp.mpf('0.9856')) < 1e-3,
      f"tau ratio/ceiling = {mp.nstr(rat_tau/ceil, 5)}")

# Appendix A.1 heuristic cascade arithmetic (NOT retained; double-count
# warning preserved in the note).  Checked as arithmetic only.
v_ew = mp.mpf('246.283')   # GeV (retained EW scale, used here as input)
a_lm = mp.mpf('0.0907')    # alpha_LM (framework constant, used as input)
x1 = v_ew * a_lm**2
x2 = x1 * mp.mpf(7) / 8
x3 = x1 * mp.sqrt(mp.mpf(7) / 8)
v0_h = mp.sqrt(x2 * 1000) / (1 + mp.sqrt(2) * mp.cos(d29))
sum_ml = (m_e + m_mu + m_tau) / 1000
check("D34 [D] A.1 heuristic arithmetic: v*a_LM^2 = 2.0260 GeV;"
      " *(7/8) = 1.7728 (-0.23% vs m_tau); *sqrt(7/8) = 1.8952 (+0.65%);"
      " v_0 route 17.695 (-0.12%) -- heuristic, NOT retained",
      abs(x1 - mp.mpf('2.0260')) < 1e-4
      and abs(x2 - mp.mpf('1.7728')) < 1e-4
      and abs((x2 - m_tau/1000) / (m_tau/1000) * 100 + 0.23) < 0.01
      and abs(x3 - mp.mpf('1.8952')) < 1e-4
      and abs((x3 - sum_ml) / sum_ml * 100 - 0.65) < 0.01
      and abs(v0_h - mp.mpf('17.695')) < 1e-3
      and abs((v0_h - v0) / v0 * 100 + 0.12) < 0.01,
      f"x1={mp.nstr(x1,5)} x2={mp.nstr(x2,5)} x3={mp.nstr(x3,5)}"
      f" v0_h={mp.nstr(v0_h,6)}")

# ==========================================================================
# Summary
# ==========================================================================

print("=" * 74)
print("KOIDE CIRCULANT / CHARACTER DERIVATION -- BOUNDED-THEOREM COMPANION")
print("=" * 74)
for line in LOG:
    print(line)
print()
n_C = sum(1 for l in LOG if "[C]" in l and "[PASS]" in l)
n_A = sum(1 for l in LOG if "[A]" in l and "[PASS]" in l)
n_D = sum(1 for l in LOG if "[D]" in l and "[PASS]" in l)
print(f"Check classes: C={n_C} A={n_A} D={n_D} (B=0, E=0, F=0, G=0)")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print()
if FAIL == 0:
    print("Verdict (bounded):")
    print("  - UNCONDITIONAL: commutant => circulant form, cosine")
    print("    spectrum, Frobenius equipartition <=> equal-character-weight bridge,")
    print("    and the exact delta-independent implication")
    print("    circulant commutant + cosine spectrum + Frobenius equipartition")
    print("    + square-root readout => Q = 2/3, plus the 1+sqrt(2) ceiling")
    print("    and pi/12 positivity boundary. All exact in sympy.")
    print("  - OPEN BOUNDARY (not claimed, not checked as theorem):")
    print("    selection principle for Frobenius equipartition, derivation of square-root readout,")
    print("    the phase delta = 2/9, and the scale v_0.")
    print("  - PART D is PDG comparator decoration at fitted delta, v_0.")
    print()
    print("  KOIDE_CIRCULANT_CHARACTER_DERIVATION_BOUNDED=TRUE")
else:
    print(f"  {FAIL} checks failed; bounded claim NOT certified.")
    print("  KOIDE_CIRCULANT_CHARACTER_DERIVATION_BOUNDED=FALSE")

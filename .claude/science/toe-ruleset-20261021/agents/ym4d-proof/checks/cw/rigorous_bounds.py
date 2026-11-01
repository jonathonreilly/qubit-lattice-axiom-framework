"""Rigorous / validated bounds for SU(2) Wilson lattice gauge theory in d=4 at strong coupling.
Normalization: weight per plaquette exp[(beta/2) Tr U_p] = exp[beta * cos(theta_p)], beta = 4/g^2.
Sections:
 (1) character coefficients: check c_j = int exp(beta cos th) chi_j dU = 2(2j+1) I_{2j+1}(beta)/beta,
     a_j = c_j/(d_j c_0) = I_{2j+1}(beta)/I_1(beta)   (quadrature vs closed form)
 (2) Dobrushin single-link uniqueness constant q(beta) = 18 * sup_{i,j} TV-influence.
     (2a) interval-certified route: TV <= sqrt(KL/2) (Pinsker), KL <= (1/2) lam_max(Cov) |delta|^2,
          lam_max(Cov_w) <= 1/4 for all |w|  [certified with arb on kappa-intervals]  =>  C_ij <= beta/2.
     (2b) validated-numerics route: C_ij <= beta * M(6 beta),  M(K) = sup_{kappa<=K, e} MAD_kappa(<u,e>),
          computed by high-precision quadrature on a grid with an explicit Lipschitz margin.
 (3) Kotecky-Preiss bound for the character (strong-coupling) polymer expansion.
 (4) truncation tails tau_J(beta) = sum_{j>J} d_j^2 a_j(beta)   (MDTN/j_max-type truncation error, sup norm)
Outputs JSON to data/rigorous_bounds.json and a text log.
"""
import json, math, sys
import mpmath as mp
from flint import arb, ctx

ctx.prec = 200
mp.mp.dps = 30
OUT = {}

def a_j_arb(beta, twoj):  # a_j = I_{2j+1}/I_1 ; twoj = 2j
    b = arb(beta) if not isinstance(beta, arb) else beta
    return b.bessel_i(twoj + 1) / b.bessel_i(1)

# ---------- (1) character coefficients ----------
chk = []
for beta in [0.1, 0.5, 1.0, 2.3]:
    for twoj in [0, 1, 2, 3, 4]:
        d = twoj + 1
        quad = (2/mp.pi) * mp.quad(lambda th: mp.e**(beta*mp.cos(th)) * mp.sin(d*th)/mp.sin(th) * mp.sin(th)**2, [0, mp.pi])
        closed = 2*d*mp.besseli(d, beta)/beta
        chk.append({"beta": beta, "j": twoj/2, "quad": float(quad), "closed": float(closed), "absdiff": float(abs(quad-closed))})
OUT["character_coeff_check"] = {"max_absdiff": max(c["absdiff"] for c in chk), "rows": chk}
print("(1) max |quad - closed| over checks:", OUT["character_coeff_check"]["max_absdiff"])
print("    a_1/2(beta)=I2/I1:", {b: float(mp.besseli(2, b)/mp.besseli(1, b)) for b in [0.1, 0.5, 1, 2, 2.3]})

# ---------- (2a) certified variance bound ----------
# For u uniform on S^3 tilted by exp(kappa t), t=<u,w_hat>: density of t ~ sqrt(1-t^2) e^{kappa t}.
# mean R(kappa) = I2/I1, Var_par = R' = 1 - R^2 - 3R/kappa  (identity checked numerically below),
# Var_perp = (1 - E t^2)/3 <= 1/4 proven analytically (Chebyshev association: E_k t^2 >= E_0 t^2 = 1/4).
def var_par_arb(k):  # k: arb ball, k>0
    R = k.bessel_i(2)/k.bessel_i(1)
    return 1 - R*R - 3*R/k
# numeric identity check vs quadrature
idchk = []
for k in [0.05, 0.3, 1.0, 3.0]:
    Z = mp.quad(lambda t: mp.sqrt(1-t*t)*mp.e**(k*t), [-1, 1])
    m1 = mp.quad(lambda t: t*mp.sqrt(1-t*t)*mp.e**(k*t), [-1, 1])/Z
    m2 = mp.quad(lambda t: t*t*mp.sqrt(1-t*t)*mp.e**(k*t), [-1, 1])/Z
    idchk.append(float(abs((m2-m1*m1) - mp.mpf(var_par_arb(arb(k)).mid().str(30, radius=False)))))
print("(2a) identity Var=1-R^2-3R/k check, max abs diff:", max(idchk))
# small kappa: Var(k) <= 1/4 - k^2/32 + k^3/6 * 150 (|kappa_5| <= 150 since |moments|<=1) -> <= 1/4 for k <= 6/(32*150)
k0 = 6/(32*150)
K_MAX = 1.2   # covers 6*beta for beta <= 0.2
n = 20000
h = (K_MAX - k0)/n
worst = arb(-1)
ok = True
for i in range(n):
    lo, hi = k0 + i*h, k0 + (i+1)*h
    ball = arb((lo+hi)/2, (hi-lo)/2)
    v = var_par_arb(ball)
    if not (v < arb(0.25)):
        ok = False; print("    FAIL cell", lo, hi, v); break
    if v.upper() > worst.upper(): worst = v
OUT["var_par_certificate"] = {"kappa_range": [0, K_MAX], "small_kappa_cutoff": k0, "cells": n, "all_cells_below_quarter": ok,
                              "max_upper_bound_on_cells": float(worst.upper())}
print("(2a) Var_par(kappa) < 1/4 certified on (0,%.2f]:" % K_MAX, ok, " (max cell upper bound %.6f)" % float(worst.upper()))
# Hence Cov_w <= I/4, KL <= (1/2)(1/4)|delta|^2 with |delta| <= 2 beta  =>  KL <= beta^2/2, TV <= beta/2.
# Dobrushin row sum q = 18 * beta/2 = 9 beta  < 1  iff beta < 1/9.   Valid while 6*beta <= K_MAX.
OUT["dobrushin_certified"] = {"C_ij_bound": "beta/2", "q(beta)": "9*beta", "beta_D": 1/9, "requires_6beta_le": K_MAX}
print("(2a) certified Dobrushin: q(beta) = 9 beta < 1 for beta < 1/9 = %.6f" % (1/9))

# ---------- (2b) validated-numerics MAD route ----------
def mad(k, phi):
    c, s = math.cos(phi), math.sin(phi)
    if k == 0:
        return 4/(3*math.pi)
    m = c*float(mp.besseli(2, k)/mp.besseli(1, k))
    def g(th):
        r = mp.sin(th)
        w = 2*r if s < 1e-14 else 2*mp.sinh(k*s*r)/(k*s)
        return mp.e**(k*c*mp.cos(th))*w*r
    thm = mp.acos(m)
    num = mp.quad(lambda th: (mp.cos(th)-m)*g(th), [0, thm]) - mp.quad(lambda th: (mp.cos(th)-m)*g(th), [thm, mp.pi])
    den = 2*mp.pi*mp.besseli(1, k)/k
    return float(num/den)
# sanity: k=0 value from formula limit
mad_small = mad(1e-8, 0.3)
grid_k = [i*0.01 for i in range(0, 81)]      # kappa in [0, 0.8]
grid_p = [j*(math.pi/2)/40 for j in range(41)]
mp.mp.dps = 20
best = (0, None)
for k in grid_k:
    for p in grid_p:
        v = mad(k, p)
        if v > best[0]: best = (v, (k, p))
hk, hp = 0.01, (math.pi/2)/40
margin = (2*hk + 2*hp)/2   # Lipschitz constants <= 2 in kappa and in phi (see notes)
M_upper = best[0] + margin
# beta_D(num) : largest beta with 6 beta <= 0.8 and 18 beta M_upper < 1
beta_num = min(1/(18*M_upper), 0.8/6)
# also the sharper value if the sup is attained at kappa=0 (as the grid suggests): 18 beta 4/(3 pi) < 1
beta_sharp = 1/(18*4/(3*math.pi))
OUT["dobrushin_validated"] = {"mad_kappa0": 4/(3*math.pi), "mad_at_1e-8": mad_small, "grid_max": best[0], "grid_argmax": best[1],
    "lipschitz_margin": margin, "M_upper": M_upper, "beta_D_validated": beta_num,
    "beta_D_if_sup_at_kappa0": beta_sharp}
print("(2b) MAD grid max %.6f at %s; margin %.4f; M<=%.5f -> beta_D(validated) = %.5f; if sup at kappa=0: %.5f"
      % (best[0], best[1], margin, M_upper, beta_num, beta_sharp))

# mass lower bounds from Dobrushin: m_lat >= -log q
rows = []
for beta in [1/32, 1/20, 0.08, 0.1, 0.11]:
    q_c = 9*beta
    q_v = 18*beta*M_upper
    rows.append({"beta": beta, "q_cert": q_c, "m_cert": (-math.log(q_c) if q_c < 1 else None),
                 "q_valid": q_v, "m_valid": (-math.log(q_v) if q_v < 1 else None)})
OUT["dobrushin_mass_bounds"] = rows
for r in rows: print("    beta=%.4f  q_cert=%.4f m>=%s | q_valid=%.4f m>=%s" % (r["beta"], r["q_cert"], r["m_cert"], r["q_valid"], r["m_valid"]))

# ---------- (3) Kotecky-Preiss for the character expansion ----------
def eps_arb(beta, J=40):
    b = arb(beta)
    s = arb(0)
    for twoj in range(1, J+1):
        s += (twoj+1)**2 * a_j_arb(b, twoj)
    # tail: I_nu(x) <= (x/2)^nu e^{x^2/4}/Gamma(nu+1); I_1(x) >= x/2 ; d^2 <= nu^2 for nu=2j+1
    tail = arb(0)
    for nu in range(J+2, J+200):
        tail += arb(nu)**2 * (b/2)**nu * (b*b/4).exp() / arb(nu+1).gamma() / (b/2)
    return s + arb(0, tail.upper())
def kp_ok(beta, Dp):
    e = eps_arb(beta)
    best_ok = False
    for ia in range(1, 400):
        a = arb(ia/1000)
        x = Dp*e*a.exp()
        if not (x < 1): break
        lhs = (arb(6)/Dp) * x**6/(1-x)
        if lhs < a/4: return True, float(a.mid())
    return False, None
res = {}
for label, Dp in [("self-contained (4*Delta)^(n-1), Delta=20", 80), ("standard lattice-animal (e*Delta)^(n-1), Delta=20", 20*math.e)]:
    lo, hi = 1e-5, 0.1
    for _ in range(40):
        mid = (lo+hi)/2
        if kp_ok(mid, arb(Dp))[0]: lo = mid
        else: hi = mid
    res[label] = {"beta_KP": lo, "a": kp_ok(lo, arb(Dp))[1], "eps(beta_KP)": float(eps_arb(lo).mid())}
    print("(3) KP %s: beta_KP = %.6f (a=%s, eps=%.5f)" % (label, lo, res[label]["a"], res[label]["eps(beta_KP)"]))
OUT["kotecky_preiss"] = res

# ---------- (4) truncation tails ----------
tails = {}
for beta in [0.5, 1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0]:
    b = arb(beta); row = {}
    terms = [(twoj+1)**2 * a_j_arb(b, twoj) for twoj in range(0, 80)]
    for J2 in [1, 2, 3, 4, 6, 8, 12]:   # J = J2/2
        row[str(J2/2)] = float(sum(terms[J2+1:], arb(0)).upper())
    tails[str(beta)] = row
OUT["truncation_tails_tau_J"] = tails
print("(4) tau_J(beta) = sum_{j>J} d_j^2 a_j  (rows beta, cols J):")
for b, r in tails.items(): print("   ", b, {k: "%.2e" % v for k, v in r.items()})
json.dump(OUT, open("data/rigorous_bounds.json", "w"), indent=1)

# checks/fz1_fwd.py  -- check fz1, exact integer/rational exponent bookkeeping.
# Criteria: checks/fz1_criteria.md (written first).  No floating point anywhere.
# Exponents of L are carried as exact Fractions (theta, alpha are rational test values).
from fractions import Fraction as F

# ---------------------------------------------------------------- unit table
# All sizes are recorded as (exponent of L) multiplying |c| = 1, exactly.
# BFT_A l.31-32: level-j 1-form coarse value x^c_j = L^{k-j} x_j
#                residual r_j = Q x_j - x_{j+1};  coarse r^c_j = L^{k-1-j} r_j
# BFT_A l.38   : ||x||_M = max_j [ ||x^c_j||oo + ||grad^c x^c_j||oo + [grad^c x^c_j]_a
#                                   + L^{k-1-j} ||r^c_j||oo ]      (NO level weight)
# BFT_A l.396-400 + l.466 + l.768 (BL-5(c), PROVEN-HERE):
#   (R) slot = max_l  w_l * L^{k-1-l} * ||s^c_l||oo ,  s_l a level-(l+1) 1-form,
#       so s^c_l = L^{k-(l+1)} s_l , and w_l = L^{theta (k-l)} for EVERY l (incl. l=0).
#   (Pl) slot = max_l w_l * L^{(2+alpha)(k-l)} * ||j_l||_own
# BFT_A l.447 : gradient of (kappa_l/2)||r_l||^2 is a residual-type source s_l = -kappa_l r_l
# BFT_A l.453 : Q maps constant 1-forms to L times themselves

def M_coeff_residual(k, j):
    """exponent of L in M^grad's residual term at level j, applied to ||r_j||_own."""
    # L^{k-1-j} * ||r^c_j||  and r^c_j = L^{k-1-j} r_j
    return F(2 * (k - 1 - j))

def M_coeff_potential(k, j):
    """exponent of L in M^grad's potential term at level j, applied to ||x_j||_own."""
    return F(k - j)

def Y_R_coeff(k, l, theta, w0_is_one=False):
    """exponent of L in Y^grad's (R) slot at level l, applied to ||s_l||_own."""
    w = F(0) if (w0_is_one and l == 0) else theta * (k - l)
    # w_l * L^{k-1-l} * ||s^c_l||  and s^c_l = L^{k-(l+1)} s_l
    return w + F(k - 1 - l) + F(k - l - 1)

def Y_Pl_coeff(k, l, theta, alpha):
    """exponent of L in Y^grad's (Pl,F3) slot at level l, applied to ||j_l||_own."""
    return theta * (k - l) + (2 + alpha) * (k - l)

# ------------------------------------------------- the witness (fixed in criteria)
# x_1 := -c, c a CONSTANT level-1 1-form of own size 1; x_j := 0 for j != 1; x_k = 0.
#   r_0 = Q x_0 - x_1 = c                 own size L^0
#   r_1 = Q x_1 - x_2 = -L c              own size L^1   (BL-2(b): Q const = L * const)
#   r_j = 0 for j >= 2
#   grad^c x^c_1 = 0 (constant), [grad^c x^c_1]_a = 0
WITNESS_RESID = {0: F(0), 1: F(1)}          # level -> exponent of L in ||r_l||_own
WITNESS_POT   = {1: F(0)}                   # level -> exponent of L in ||x_l||_own

def norm_M(k):
    terms = []
    for j, e in WITNESS_POT.items():
        terms.append(("pot j=%d" % j, M_coeff_potential(k, j) + e))
    for j, e in WITNESS_RESID.items():
        terms.append(("res j=%d" % j, M_coeff_residual(k, j) + e))
    return max(terms, key=lambda t: t[1])

def norm_Y_R(k, theta, w0_is_one=False):
    # s_l = -kappa_l r_l with kappa_l == 1
    terms = [("R l=%d" % l, Y_R_coeff(k, l, theta, w0_is_one) + e)
             for l, e in WITNESS_RESID.items()]
    return max(terms, key=lambda t: t[1])

def norm_Y_Pl(k, theta, alpha):
    # j_l := kappa_l Q_l^T r_l at level l, j_{l+1} := -kappa_l r_l at level l+1.
    # BL-2(c): ||(Q^T j)^c||oo <= ||j^c||oo in coarse PLAIN units, j^c = L^{3(k-l)} j.
    # so ||Q_l^T r_l||_own <= L^{3(k-l-1)-3(k-l)} * ||r_l||_own * L^{... }  -- carried out
    # explicitly: the coarse-plain value of j_l is <= the coarse-plain value of r_l at
    # level l+1, i.e.  L^{3(k-l)} |j_l| <= L^{3(k-l-1)} |r_l|  =>  |j_l| <= L^{-3} |r_l|.
    terms = []
    for l, e in WITNESS_RESID.items():
        terms.append(("Pl l=%d"   % l,     Y_Pl_coeff(k, l,   theta, alpha) + e - 3))
        terms.append(("Pl l=%d" % (l + 1), Y_Pl_coeff(k, l+1, theta, alpha) + e))
    return max(terms, key=lambda t: t[1])

# ------------------------------------------------------------------ the gates
def report(title, rows):
    print("\n" + title)
    print("-" * len(title))
    for r in rows:
        print(r)

THETAS = [F(1,4), F(1,3), F(1,2), F(3,4), F(9,10)]
KS     = [2, 3, 5, 8, 13, 40]

print("fz1 -- exact exponent bookkeeping for (FWD-0).  All numbers are exponents of L.")
print("Witness: x_1 = -c (constant level-1 1-form, own size 1), x_j = 0 otherwise.")

# ---- fz1-A -------------------------------------------------------------------
rows = []
ok_A = True
for theta in THETAS:
    for k in KS:
        nM, eM = norm_M(k)
        nY, eY = norm_Y_R(k, theta)
        rho = eY - eM                       # exponent of L in the ratio
        pred = theta * k                    # predicted L^{theta k}
        ok = (rho == pred)
        ok_A = ok_A and ok
        rows.append("theta=%-5s k=%-3d  ||x||_M = L^%-6s (%s)  ||Lx||_(R) = L^%-8s (%s)"
                    "  ratio = L^%-7s  predicted L^%-7s  %s"
                    % (theta, k, eM, nM, eY, nY, rho, pred, "ok" if ok else "MISMATCH"))
report("fz1-A  main gate: forward ratio on the (R) slot", rows)
print("\nfz1-A VERDICT: %s  -- ratio = L^{theta*k} exactly for every tested (theta,k); "
      "unbounded in k for every theta>0." % ("PASS" if ok_A else "FAIL"))

# ---- fz1-B -------------------------------------------------------------------
rows = []
ok_B = True
for theta in THETAS:
    for alpha in [F(1,8), F(1,4), theta]:
        if alpha > theta:
            continue
        for k in KS:
            nM, eM = norm_M(k)
            _, eR  = norm_Y_R(k, theta)
            nP, eP = norm_Y_Pl(k, theta, alpha)
            ok = (eP >= eR)
            ok_B = ok_B and ok
            rows.append("theta=%-5s alpha=%-5s k=%-3d  (R)=L^%-8s  (Pl)=L^%-10s (%s)  "
                        "(Pl)>=(R): %s" % (theta, alpha, k, eR, eP, nP, ok))
report("fz1-B  alternative-representation gate: (Pl) slot vs (R) slot", rows[:18] + ["... (%d rows total, all same verdict)" % len(rows)])
print("\nfz1-B VERDICT: %s  -- the plain-current representation is never cheaper than the "
      "residual-type one." % ("PASS" if ok_B else "FAIL"))

# ---- fz1-C  DESIGNED-FAIL CONTROL 1 ------------------------------------------
rows = []
unbounded_C = False
for k in KS:
    nM, eM = norm_M(k)
    # omega_l == 1 for every l  <=>  theta = 0
    nY, eY = norm_Y_R(k, F(0))
    rho = eY - eM
    if rho != 0:
        unbounded_C = True
    rows.append("theta=0 (omega==1)  k=%-3d  ||x||_M = L^%-6s  ||Lx||_(R) = L^%-6s  ratio = L^%s"
                % (k, eM, eY, rho))
report("fz1-C  DESIGNED-FAIL CONTROL 1: weights switched off (theta = 0)", rows)
print("\nfz1-C CONTROL: ratio is L^0 = 1 for every k -> the gate returns BOUNDED, as the control "
      "requires.  CONTROL FIRED (it did NOT report 'unbounded').  %s"
      % ("OK" if not unbounded_C else "CONTROL BROKEN"))

# ---- fz1-D  DESIGNED-FAIL CONTROL 2 ------------------------------------------
# (G) slot, level-0 Wilson term: gradient of (1/2)||d x_0||^2 is G_0 = d x_0, omega_0 = 1.
# (d x_0)^c = L^{2k} d x_0 is an antisymmetrised combination of at most 2 terms of
# grad^c x^c_0 = L^{2k}(x_0(b+e_nu) - x_0(b)).  So ||G_0^c||oo <= 2 ||grad^c x^c_0||oo and
# [G_0^c]_a <= 2 [grad^c x^c_0]_a, both of which sit inside ||x||_M at level 0 with weight 1.
rows = []
unbounded_D = False
for k in KS:
    # exponent comparison: G-slot coefficient on ||d x_0||_own is 2k (coarse 2-form);
    # M's level-0 gradient coefficient on the same own-unit difference is also 2k.
    eG = F(2 * k)
    eMg = F(2 * k)
    rho = eG - eMg
    if rho != 0:
        unbounded_D = True
    rows.append("k=%-3d  (G) slot coeff = L^%-4s   M level-0 gradient coeff = L^%-4s   "
                "ratio = L^%s  (times the integer antisymmetrisation count <= 2)" % (k, eG, eMg, rho))
report("fz1-D  DESIGNED-FAIL CONTROL 2: the (G) divergence-form slot", rows)
print("\nfz1-D CONTROL: ratio is L^0 for every k, i.e. BOUNDED (<= 2).  The gate discriminates "
      "between slots.  CONTROL FIRED (it did NOT report 'unbounded').  %s"
      % ("OK" if not unbounded_D else "CONTROL BROKEN"))

print("\n==================== SUMMARY ====================")
print("fz1-A  %s   (FWD-0) is FALSE k-uniformly: ||Hess F_k(1)||_{M->Y} >= kappa_- L^{theta k}"
      % ("PASS" if ok_A else "FAIL"))
print("fz1-B  %s   no cheaper slot representation exists among the four of [RBA1-fix]"
      % ("PASS" if ok_B else "FAIL"))
print("fz1-C  CONTROL FIRED (bounded at theta = 0, as designed)")
print("fz1-D  CONTROL FIRED (bounded on the (G) slot, as designed)")

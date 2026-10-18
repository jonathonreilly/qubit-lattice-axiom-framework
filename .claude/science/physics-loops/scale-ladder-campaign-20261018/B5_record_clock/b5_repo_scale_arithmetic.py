"""B5 repo-scale arithmetic: where the certified tolerances come from, and what
the literal (nominal-clock) phase metric would demand at repo scale.

All inputs are copied from the certified notes (read-only):
  S = docs/STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md (main)
  B = docs/MEDIATED_FINITE_BOND_PRECISION_BOUNDED_THEOREM_NOTE_2026-10-18.md   (PR #9695 head 0118d39a)
  O = docs/MEDIATED_ONSITE_TOLERANCE_BOUNDED_THEOREM_NOTE_2026-10-18.md        (PR #9696 head 2321c078)
  P = docs/MEDIATED_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md  (path structure)
Pure arithmetic; no dynamics.  PASS/FAIL lines test stated relations only.
"""
import math

def check(name, cond, detail):
    print(f"{'PASS' if cond else 'FAIL'}  {name}: {detail}")

# ---- design couplings: M ~ 1.2 v t_max, T ~ 20-25/lambda --------------------
S = dict(lam=1e-13, g=5e-8, T=2e14, M=50_000_000, bond=1e-6, onsite=1e-19)
Md = dict(lam=3.1e-18, g=5e-8, T=8e18, M=1_920_000_000_011, bond=1e-13, onsite=1e-26)
for nm, d in [("structured", S), ("mediated", Md)]:
    v = 2 * d["g"]
    print(f"{nm}: lam*T={d['lam']*d['T']:.1f}  M/(v*2T)={d['M']/(v*2*d['T']):.3f}  "
          f"bond*M={d['bond']*d['M']:.3g}  onsite/lam={d['onsite']/d['lam']:.3g}  onsite*M={d['onsite']*d['M']:.3g}")
check("R1 both designs tie M to T and T to 1/lam",
      all(15 < d["lam"] * d["T"] < 30 and 1.0 < d["M"] / (2 * d["g"] * 2 * d["T"]) < 1.5 for d in (S, Md)),
      "so 'scales like 1/M', 'like 1/T' and 'like lam' are confounded in the certified family")
r_bond = (S["bond"] * S["M"]) / (Md["bond"] * Md["M"])
check("R2 certified bond tolerances are NOT ~1/M across the two devices",
      r_bond > 100 or r_bond < 0.01, f"(tol*M)_structured/(tol*M)_mediated = {r_bond:.3g}")

# ---- mediated bond certificate: increment < 5.3e6*eps (note B) -------------
coef_b, nominal_inf, cut = 5.3e6, 0.00045445500576, 0.00004
print(f"mediated bond: increment at eps=1e-13: {coef_b*1e-13:.2e}; eps allowed for total<1e-3: "
      f"{(1e-3-nominal_inf-cut)/coef_b:.2e}")
check("R3 bond 1e-13 is a budget choice (eps up to ~1e-10 keeps complete error <1e-3)",
      (1e-3 - nominal_inf - cut) / coef_b > 50 * 1e-13, "the certificate itself has no T or M factor (uniform for all t>=8e18)")
# composition of the analytic coefficient (note B): B_travel = 4*461*sqrt(j/pi)*8.1e4
j = 0.0028
print(f"  B_travel coefficient ~ {4*461*math.sqrt(j/math.pi)*8.1e4:.3g} (note: <4.86e6); "
      f"sqrt(lam)||F||_2 term from 50*1000*lam/R^2: {5e4*math.sqrt(math.pi/2):.3g}")

# ---- mediated onsite certificate: increment < 1.36e20*xi (note O) ----------
coef_o = 1.36e20
print(f"mediated onsite: coef*lam = {coef_o*Md['lam']:.3g}  (B_d=O(xi/lam)); increment at 1e-26: {coef_o*1e-26:.2e}")
check("R4 onsite certificate is linear in xi/lam (coef*lam is O(10^2), lam-independent form)",
      10 < coef_o * Md["lam"] < 1e4, "absolute onsite tolerance ~ lam ~ 1/T ~ 1/M by design coupling")

# ---- the literal-clock (nominal scalar) obligation ------------------------
# mediated path structure (note P): m=12, n1=n2=2m-1=23, n3=m=12; path l has 2n_l heads,
# bonds gamma_l, gamma_l and alternating J_m,q,...,J_m (n_l J_m's, n_l-1 q's).
m = 12; ns = [2 * m - 1, 2 * m - 1, m]
heads = 3 + sum(2 * n for n in ns)
check("R5 mediated added-head count reproduces the note's 119", heads == 119, f"heads={heads}")
Jm, q, gmax = 1e-3, 5e-4, (1e-3 - 5e-4) / 4
W = [Jm] * sum(ns) + [q] * sum(n - 1 for n in ns) + [gmax] * 6
Wsum, W2 = sum(W), math.sqrt(sum(w * w for w in W))
tmax = 2 * Md["T"]
for eps in [1e-13]:
    print(f"literal clock at eps=1e-13, t=1.6e19: worst dC*t = {Wsum*eps*tmax:.3g} rad, rms (uniform errors) = {W2*eps/math.sqrt(3)*tmax:.3g} rad")
check("R6 certified mediated bond box is useless under the nominal-clock literal metric",
      Wsum * 1e-13 * tmax > math.pi, "the notes avoid this by putting exp(-itC(w)) (ACTUAL scalar) into the target")
eps_lit = 1e-3 / (Wsum * tmax)
print(f"  literal-clock requirement (worst case, 1e-3): eps <= {eps_lit:.2g}  (~1/(W_sum*T))")
# structured source: C_src = kappa+a1+a2, squared-bond errors e -> amplitude e/2
kap = math.sqrt(3 * j * S["lam"]); Csrc = kap + S["lam"] / math.sqrt(3) + S["lam"] * math.sqrt(8 / 3)
ph = Csrc * S["bond"] / 2 * 2 * S["T"]
print(f"structured: C_src={Csrc:.3g}, worst literal phase at e=1e-6, t=4e14: {ph:.3g} rad; "
      f"requirement e <= {2e-3/(Csrc*2*S['T']):.2g}")
check("R7 structured-source box also relies on the actual-scalar target", ph > 1e-3,
      "consistent with the note: 'One cannot omit exp(-itC_src(actual))'")

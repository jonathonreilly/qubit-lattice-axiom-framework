#!/usr/bin/env python3
# na1 -- background-vertex exponent bookkeeping.  Criteria: checks/na1_criteria.md (written first).
# Exact integer/rational arithmetic in plain python.  No numpy, no sympy, no BLAS, no lock needed.
from fractions import Fraction as Fr

SYMS = ("1", "d", "tc", "tr", "ta")            # tc = theta_w^c, tr = theta_w^r, ta = theta_A

class Lin(dict):                                # linear form over SYMS with Fraction coefficients
    def __init__(self, **kw):
        super().__init__({s: Fr(0) for s in SYMS}); 
        for k, v in kw.items(): self[k] = Fr(v)
    def __add__(s, o): r = Lin(); [r.__setitem__(k, s[k] + o[k]) for k in SYMS]; return r
    def __sub__(s, o): r = Lin(); [r.__setitem__(k, s[k] - o[k]) for k in SYMS]; return r
    def __rmul__(s, c): r = Lin(); [r.__setitem__(k, Fr(c) * s[k]) for k in SYMS]; return r
    def ev(s, **v): return s["1"] + sum(s[k] * Fr(v[k]) for k in SYMS[1:])
    def __str__(s):
        t = [("" if s[k] == 1 and k != "1" else str(s[k])) + ("" if k == "1" else k)
             for k in SYMS if s[k] != 0]
        return " + ".join(t).replace("+ -", "- ") if t else "0"

ONE, D, TC, TR, TA = (Lin(**{"1": 1}), Lin(d=1), Lin(tc=1), Lin(tr=1), Lin(ta=1))
Z = Lin()

# ---- primitive ingredients (criteria table).  Each returns (coeff of n, constant), both Lin.
def P1():  return (D - TC,            Z)          # l1 mass, differentiated level-0 response   [NORMS l.563]
def P2():  return (D - TR,            TR)         # l1 mass, level-j residual response         [NORMS l.564]
def P3():  return (D - TA,            Z)          # l1 mass, level-j potential response        [NORMS l.565]
def P4():  return (-1 * TC,           Z)          # sup curvature response per unit potential  [NORMS l.566]
def P5():  return (-1 * TA,           Z)          # sup potential response per unit potential  [NORMS l.567]
def P6(corrupt=False):                            # own-units background curvature at level j  [BFT-1 / N1-4 / N2]
    return (Z, Z) if corrupt else (-1 * TC, Z)
def P7():  return (-1 * TR,           TR)         # own-units background soft fluctuation      [J-str (c) / (C_g-th)]

def add(*ps):
    a = Z; b = Z
    for (x, y) in ps: a = a + x; b = b + y
    return (a, b)

def families(corrupt_P6=False):
    """Each family: (name, list of (coeff-of-n, const) contributions), for the two delta-placements."""
    F = {}
    # ---------- Wilson (level 0; n = k) ----------
    F["W 1-deriv  (delta in the differentiated slot)"] = add(P1(), P5(), P5())
    F["W 1-deriv  (delta in an undiff. slot)"]         = add(P3(), P4(), P5())
    F["W 3-deriv  (delta in a differentiated slot)"]   = add(P6(corrupt_P6), P1(), P4(), P4())
    F["W 0-deriv  (delta in an undiff. slot)"]         = add(P6(corrupt_P6), P3(), P5(), P5())
    # ---------- soft at level j (n = k - j) ----------
    F["S 1-deriv  (delta in the residual slot)"]       = add(P2(), P5(), P5())
    F["S 1-deriv  (delta in a potential slot)"]        = add(P3(), P7(), P5())
    F["S 3-deriv  (delta in a residual slot)"]         = add(P7(), P2(), P7(), P7())
    F["S 0-deriv  (delta in a potential slot)"]        = add(P7(), P3(), P5(), P5())
    return F

def report(title, corrupt_P6=False, **wts):
    print("=" * 78); print(title); print("=" * 78)
    F = families(corrupt_P6)
    rows = []
    for name, (cn, c0) in F.items():
        v = cn.ev(**wts) if wts else None
        rows.append((name, cn, c0, v))
        print(f"  {name:48s}  leading = [{str(cn):22s}]   const = [{str(c0)}]"
              + (f"   -> {v}" if v is not None else ""))
    return rows

out = []
print("na1 -- background-vertex exponent bookkeeping (criteria: na1_criteria.md)\n")

# ---------------- na1-A : CONTROL on the ingredient table -------------------------------------
rows = report("na1-A  symbolic exponents (control: the 1-derivative rows must equal NORMS l.650-651)")
F = families()
exp_W1 = D - TC - 2 * TA                       # NORMS l.650:  (d - tc - 2 ta) k
exp_S1 = D - TR - 2 * TA                       # NORMS l.651:  (d - tr - 2 ta) n + tr
okA = all(dict(F[k][0]) == dict(exp_W1) for k in F if k.startswith("W 1-deriv")) \
   and all(dict(F[k][0]) == dict(exp_S1) for k in F if k.startswith("S 1-deriv")) \
   and all(dict(F[k][1]) == dict(TR)     for k in F if k.startswith("S 1-deriv")) \
   and all(dict(F[k][1]) == dict(Z)      for k in F if k.startswith("W 1-deriv"))
print(f"\nna1-A  (1-derivative families reproduce NORMS Sec.N7 exactly): {'PASS' if okA else 'FAIL'}\n")

# ---------------- na1-B : the four new families -----------------------------------------------
pre = {"W 3-deriv": D - 4 * TC,
       "W 0-deriv": D - TC - 3 * TA,
       "S 3-deriv": D - TR - 2 * TC - TA,        # <-- as PRE-REGISTERED in na1_criteria.md
       "S 0-deriv": D - TR - 3 * TA}
print("na1-B  pre-registered vs computed leading coefficients:")
okB = True
for key, p in pre.items():
    got = [F[k][0] for k in F if k.startswith(key)][0]
    m = dict(got) == dict(p); okB &= m
    print(f"  {key:12s} pre-registered [{str(p):26s}]  computed [{str(got):26s}]  {'match' if m else 'MISMATCH'}")
print(f"na1-B: {'PASS' if okB else 'FAIL'}\n")

# ---------------- na1-C : verdict at the delivered weight pair ---------------------------------
W = dict(d=4, tc=2, tr=3, ta=1)
rows = report("na1-C  at (d, theta_w^c, theta_w^r, theta_A) = (4, 2, 3, 1)", **W)
new = [(n, v) for (n, cn, c0, v) in rows if "3-deriv" in n or "0-deriv" in n]
mar = [(n, v) for (n, cn, c0, v) in rows if n.startswith("W 1-deriv")]
okC = all(v <= -1 for _, v in new) and all(v == 0 for _, v in mar)
print(f"\n  new families (must all be <= -1): {[(n.split('(')[0].strip(), str(v)) for n, v in new]}")
print(f"  1-deriv Wilson (must be 0, marginal): {[str(v) for _, v in mar]}")
print(f"na1-C: {'PASS' if okC else 'FAIL'}\n")

# ---------------- na1-D : critical dimension of each new family --------------------------------
print("na1-D  largest d for which each family's leading coefficient is < 0, at (tc,tr,ta)=(2,3,1):")
okD = True
for name, cn, c0, v in rows:
    if "1-deriv" in name: continue
    # leading(d) = cn["d"]*d + (rest);  solve < 0
    rest = cn.ev(d=0, tc=2, tr=3, ta=1)
    assert cn["d"] == 1
    dcrit = -rest                                  # coefficient < 0  <=>  d < dcrit
    okD &= (dcrit > 4)
    print(f"  {name:48s}  subcritical for d < {dcrit}")
print(f"na1-D (all critical dimensions > 4): {'PASS' if okD else 'FAIL'}\n")
# for comparison, the 1-derivative families:
for name, cn, c0, v in rows:
    if "1-deriv" in name:
        print(f"  [compare] {name:40s} subcritical for d < {-cn.ev(d=0, **{k: W[k] for k in ('tc','tr','ta')})}")

# ---------------- na1-E : DESIGNED-FAIL control (theta_w^c = 0, theta_A clipped at 0) ----------
print()
WE = dict(d=4, tc=0, tr=3, ta=0)
rowsE = report("na1-E  DESIGNED-FAIL CONTROL: theta_w^c = 0 (the (CL-3) weightless form), theta_A = 0", **WE)
newE = [v for (n, cn, c0, v) in rowsE if "3-deriv" in n or "0-deriv" in n]
marE = [v for (n, cn, c0, v) in rowsE if n.startswith("W 1-deriv")]
failedE = not (all(v <= -1 for v in newE) and all(v == 0 for v in marE))
print(f"\n  na1-C re-evaluated at this input: {'FAIL' if failedE else 'PASS'}")
print(f"na1-E control {'PASSED (the gate CAN fail)' if failedE else 'NOT PASSED -- na1 verdicts are VOID'}\n")

# ---------------- na1-F : second DESIGNED-FAIL control (corrupt P6) ----------------------------
rowsF = report("na1-F  DESIGNED-FAIL CONTROL: P6 corrupted (background curvature does not decay)",
               corrupt_P6=True, **W)
newF = [v for (n, cn, c0, v) in rowsF if "3-deriv" in n or "0-deriv" in n]
marF = [v for (n, cn, c0, v) in rowsF if n.startswith("W 1-deriv")]
failedF = not (all(v <= -1 for v in newF) and all(v == 0 for v in marF))
print(f"\n  na1-C re-evaluated with P6 corrupted: {'FAIL' if failedF else 'PASS'}")
print(f"na1-F control {'PASSED (the gate CAN fail)' if failedF else 'NOT PASSED -- na1 verdicts are VOID'}\n")

print("=" * 78)
print(f"SUMMARY  na1-A {'PASS' if okA else 'FAIL'} | na1-B {'PASS' if okB else 'FAIL'} | "
      f"na1-C {'PASS' if okC else 'FAIL'} | na1-D {'PASS' if okD else 'FAIL'} | "
      f"na1-E control {'PASSED' if failedE else 'NOT PASSED'} | na1-F control {'PASSED' if failedF else 'NOT PASSED'}")

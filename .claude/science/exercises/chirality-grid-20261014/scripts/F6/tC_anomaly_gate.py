"""T-C: anomaly gate on the framework's own mirror halves.  F6 route agent, 2026-10-14.

Every lattice field carries fixed on-site SM charges, chosen as the left-handed-basis charges of one
generation: Q(3,2,1/6), u^c(3b,1,-2/3), d^c(3b,1,1/3), L(1,2,-1/2), e^c(1,1,1), nu^c(1,1,0).
At a node of hand chi = -1 (left) the Weyl field carries the field's charges; at a node of hand +1 (right)
it is, in left-handed basis, the conjugate rep.

Split W (two-component walker, block 77 / A1 above): 8 corners k in {0,1}^3 (units of pi), hand (-1)^{hw+1}
so that hw = 1 is left-handed (sign convention irrelevant).  Light = hw 1.  Mirror = hw 0, 2, 3.
Corner translation charges: s_v(k) = v.k mod 2 for each nonzero v in {0,1}^3 (7 Z2 subgroups).

Split K (Kogut-Susskind / K2a): per field 2 left Weyl with T_d-charge 0 (light) and 2 right Weyl with
T_d-charge 1 (mirror).  Only Z2^d is used (other translations are not diagonal on Weyl components).
"""
from fractions import Fraction as Fr
import itertools

# (name, SU3 rep: +1 for 3, -1 for 3bar, 0 singlet; SU2 dim; Y; B-L)
GEN16 = [("Q", +1, 2, Fr(1, 6), Fr(1, 3)), ("uc", -1, 1, Fr(-2, 3), Fr(-1, 3)), ("dc", -1, 1, Fr(1, 3), Fr(-1, 3)),
         ("L", 0, 2, Fr(-1, 2), Fr(-1)), ("ec", 0, 1, Fr(1), Fr(1)), ("nuc", 0, 1, Fr(0), Fr(1))]
GEN15 = GEN16[:-1]

def weyls(fields, conj):
    """Expand a multiplet list into (su3, su2dim, Y, X) entries per Weyl field (colour x isospin multiplicity kept as counts)."""
    out = []
    for name, c3, d2, Y, BL in fields:
        X = 5 * BL - 4 * Y
        if conj:
            c3, Y, X = -c3, -Y, -X
        out.append(dict(c3=c3, d2=d2, Y=Y, X=X, mult=(3 if c3 else 1) * d2))
    return out

def coeffs(entries):
    """entries: list of (weyl-dict, s) with s a dict of Z2 charges."""
    A = dict(SU3cubed=0, Ycubed=Fr(0), Ygrav=Fr(0), SU3sqY=Fr(0), SU2sqY=Fr(0), Witten=0, Z16=0)
    mixed = {}
    for w, s in entries:
        m = w["mult"]
        A["SU3cubed"] += w["c3"] * w["d2"]
        A["Ycubed"] += m * w["Y"] ** 3
        A["Ygrav"] += m * w["Y"]
        if w["c3"]:
            A["SU3sqY"] += w["d2"] * w["Y"]          # T(3)=1/2 dropped (overall factor)
        if w["d2"] == 2:
            A["SU2sqY"] += (3 if w["c3"] else 1) * w["Y"]
            A["Witten"] += (3 if w["c3"] else 1)
        # Spin-Z4^X: Z16 counts Weyl with X = 1 mod 4 as +1, X = 3 mod 4 as -1 (X odd for all fields here)
        x = int(w["X"]) % 4
        A["Z16"] += m * (1 if x == 1 else -1 if x == 3 else 0)
        for key, sv in s.items():
            d = mixed.setdefault(key, dict(Z2_SU3sq=0, Z2_SU2sq=0, Z2_Y6sq=0, Z2_grav=0))
            if sv:
                d["Z2_SU3sq"] += (w["d2"] if w["c3"] else 0)          # number of triplets (index units)
                d["Z2_SU2sq"] += ((3 if w["c3"] else 1) if w["d2"] == 2 else 0)
                d["Z2_Y6sq"] += m * int(6 * w["Y"]) ** 2
                d["Z2_grav"] += m
    A["Witten"] %= 2
    A["Z16"] %= 16
    for key in mixed:
        for k2 in mixed[key]:
            mixed[key][k2] %= 2
    return A, mixed

def report(label, entries):
    A, mixed = coeffs(entries)
    nz = {k: v for k, v in A.items() if v != 0}
    nzm = {k: {a: b for a, b in d.items() if b} for k, d in mixed.items()}
    nzm = {k: d for k, d in nzm.items() if d}
    print(f"{label}")
    print(f"    exact/global: {dict((k, str(v)) for k, v in A.items())}")
    print(f"    nonzero: {nz if nz else 'none'};  Ibanez-Ross mod-2 mixed nonzero: {nzm if nzm else 'none'}")
    return nz, nzm

corners = list(itertools.product((0, 1), repeat=3))
vs = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
results = {}
for gname, gen in (("16 (with nu^c)", GEN16), ("15 (no nu^c)", GEN15)):
    print(f"===== content per field set: {gname} =====")
    # ---- split W ----
    light, mirror = [], []
    nlight_weyl = 0
    for k in corners:
        hw = sum(k)
        left = (hw % 2 == 1)
        s = {f"v={v}": sum(a * b for a, b in zip(v, k)) % 2 for v in vs}
        for w in weyls(gen, conj=not left):
            (light if hw == 1 else mirror).append((w, s))
            if hw == 1:
                nlight_weyl += w["mult"]
    print(f"  walker split: light Weyl count = {nlight_weyl} (all left-handed), corners hw=1: 3")
    rW_l = report("  W light (hw=1)", light)
    rW = report("  W mirror (hw=0,2,3)", mirror)
    rW_all = report("  W total (all 8 corners)", light + mirror)
    # ---- split K ----
    lightK, mirrorK = [], []
    for copy in range(2):
        for w in weyls(gen, conj=False):
            lightK.append((w, {"Td": 0}))
        for w in weyls(gen, conj=True):
            mirrorK.append((w, {"Td": 1}))
    rK = report("  K mirror (T_d odd, 2 x conj)", mirrorK)
    results[gname] = (rW, rK)
print("===== verdict =====")
for gname, (rW, rK) in results.items():
    passW = not rW[0] and not rW[1]
    passK = not rK[0] and not rK[1]
    print(f"{gname}: walker mirror passes = {passW}; KS mirror passes = {passK}")

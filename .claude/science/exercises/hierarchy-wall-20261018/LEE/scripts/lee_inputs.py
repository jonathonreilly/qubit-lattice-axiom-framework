"""LEE-1 part (ii): input robustness of v_cand, inputs fixed in ../PREREG.md.
Part (iii) at the end is a POST-HOC diagnostic (not pre-registered): best F0
member at each EJ plaquette input."""
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lee_family as LF

MPL = 1.2209e19
MPL_RED = MPL / math.sqrt(8 * math.pi)
VOBS = 246.22
P0 = 0.5934

def vcand(P, M=MPL):
    return M * (7 / 8) ** 0.25 * ((1 / (4 * math.pi)) / P ** 0.25) ** 16

V0 = vcand(P0)
d0 = V0 / VOBS - 1

rows = [  # id, P central, sigma, class
    ("P0 licence", P0, 5e-5, "baseline"),
    ("P1 YT +/-0.0006", P0, 6e-4, "EJ"),
    ("P2 April ens.", 0.59369, 2e-5, "EJ"),
    ("P3 heatbath", 0.59372, 4e-5, "reported"),
    ("M1 1 taste", P0 + 0.0062, 2e-4, "EJ"),
    ("M2a 2 tastes RW", P0 + 0.0119, 11e-4, "EJ"),
    ("M2b 2 tastes HMC", P0 + 0.0072, 25e-4, "EJ"),
    ("M4a 4 tastes HMC", P0 + 0.0212, 11e-4, "EJ"),
    ("M4b 4 tastes lin", P0 + 0.026, 7e-4, "EJ"),
    ("Q 4^4 MC", 0.5973, 6e-4, "reported"),
]
print(f"baseline v_cand = {V0:.4f} GeV, delta0 = {100*d0:+.4f} %, 10|delta0| = {1000*abs(d0):.3f} %")
print(f"{'input':18s} {'<P>':>9s} {'v exact':>9s} {'v lin(-4)':>9s} {'shift%':>8s} {'x|d0|':>7s} "
      f"{'1sig range of v (GeV)':>22s} {'dev vs v_obs%':>13s} class")
fires = []
for nm, P, s, cl in rows:
    v = vcand(P)
    vlin = V0 * (1 - 4 * (P - P0) / P0)
    sh = v / V0 - 1
    lo, hi = vcand(P + s), vcand(P - s)
    if nm.startswith("P1"):
        sh = vcand(P0 - s) / V0 - 1  # the stated band's edge
    ratio = abs(sh) / abs(d0)
    print(f"{nm:18s} {P:9.5f} {v:9.3f} {vlin:9.3f} {100*sh:+8.3f} {ratio:7.1f} "
          f"   [{lo:7.2f}, {hi:7.2f}] {100*(v/VOBS-1):+13.3f} {cl}")
    if cl == "EJ" and ratio > 10:
        fires.append(nm)
for nm, v in (("M8 8 tastes", 193.0), ("M16 16 tastes", 163.0)):
    print(f"{nm:18s} {'':9s} {v:9.3f} {'':9s} {100*(v/V0-1):+8.3f} {abs(v/V0-1)/abs(d0):7.1f}  as reported on main     reported")
vr = vcand(P0, MPL_RED)
print(f"G-red M_Pl/sqrt(8pi): v = {vr:.3f} GeV, shift {100*(vr/V0-1):+.2f} %, x|d0| = {abs(vr/V0-1)/abs(d0):.0f} (not EJ under primary rule)")
print(f"M_Pl elasticity +1: CODATA rel. sigma 1.1e-5 -> {1.1e-5/abs(d0):.3f} |d0|")
print("EJ inputs firing the >10|delta0| clause:", fires)
print("EJ inputs keeping v within 1% of v_obs:",
      [nm for nm, P, s, cl in rows if cl == "EJ" and abs(vcand(P) / VOBS - 1) <= 0.01])

# (iii) post-hoc: best F0 member at each EJ plaquette value
print("\n(iii) POST-HOC: best F0 member at each plaquette input (same family shape, couplings recomputed)")
import importlib
for nm, P, s, cl in rows:
    if cl == "reported" and not nm.startswith("P3"):
        continue
    u0 = P ** 0.25; ab = 1 / (4 * math.pi)
    aLM = ab / u0; asv = ab / u0 ** 2
    C = [("a_bare", ab), ("a_LM", aLM), ("a_s(v)", asv), ("u0", u0), ("<P>", P),
         ("a_bare/4pi", ab / (4 * math.pi)), ("a_LM/4pi", aLM / (4 * math.pi)),
         ("a_s(v)/4pi", asv / (4 * math.pi)), ("1-u0", 1 - u0), ("1-<P>", 1 - P)]
    mem = LF.family(C, [("MPl", MPL)])
    best = sorted(mem, key=lambda m: abs(math.log(m[0] / VOBS)))[:3]
    cand = MPL * (7 / 8) ** 0.25 * aLM ** 16
    print(f"  {nm:18s} candidate dev {100*(cand/VOBS-1):+.3f}% | best: " +
          "; ".join(f"{b[1].replace('MPl ','')} {100*(b[0]/VOBS-1):+.3f}%" for b in best))

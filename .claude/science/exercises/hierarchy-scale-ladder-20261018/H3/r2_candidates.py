"""HIER-3 R2: framework candidates for the colour coupling at the first coloured rung,
their strong scales in every reading, and the distance to the W_v window. Own code."""
import math, sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rgcommon as rg

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

FOURPI = 4 * math.pi
REPO = "/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790"
W_HI, W_LO, TV = 2.0e-16, 2.0e-18, rg.V_OBS / rg.M_PL
G2_INSIDE_MAX = 0.3606   # r1.log: largest g^2 inside W_v over all contents, rungs, definitions
G2_INSIDE_MIN = 0.1673   # r1.log: smallest g^2 inside W_v (pure SU(3), b = 1, MU1)

# ---- C1-C3: the beta = 6 family ----
cands = {}
for Pname, P in [("B1 0.5934", 0.5934), ("point 0.59369", 0.59369)]:
    u0 = P ** 0.25
    cands[f"C1 g_bare^2=1"] = 1.0
    cands[f"C2a 4pi alpha_LM = 1/u0 [{Pname}]"] = 1 / u0
    cands[f"C2b 4pi alpha_s(v) = 1/u0^2 [{Pname}]"] = 1 / u0 ** 2
    cands[f"C2c g_MF^2 = 1/<P> [{Pname}]"] = 1 / P
    cands[f"C2d g_P^2 = -3 ln<P> [{Pname}]"] = -3 * math.log(P)
check("alpha_LM regression 0.090668 (HONEST_STATUS:395)",
      abs(1 / 0.5934 ** 0.25 / FOURPI - 0.090668) < 2e-6)
check("alpha_s(v) regression 0.10330382 (ALPHA_S_DERIVED:237)",
      abs(1 / math.sqrt(0.5934) / FOURPI - 0.10330382) < 1e-8)

def decades(g2, content, loops, scheme_ratio=1.0, b=1):
    """log10(M_Pl / Lambda_MS) when g2 is read at mu = M_Pl/b in a scheme with
    Lambda_MS/Lambda_scheme = scheme_ratio. content: A pure, B nf=6, C X2' kappa=0.1."""
    Mcut = rg.M_PL / b
    a = g2 / FOURPI
    nf = {"A": 0, "B": 6, "C": 6}[content]
    mu = Mcut
    if content == "C":
        a2, _ = rg.run_alpha(a, Mcut, 0.1 * Mcut, 12, loops)
        if a2 is None:
            return float('nan')
        a, mu = a2, 0.1 * Mcut
    try:
        L = scheme_ratio * rg.Lambda(mu, a, nf, loops)
    except (ValueError, OverflowError):
        return float('nan')
    return math.log10(rg.M_PL / L)

need_lo = math.log10(1 / W_HI)   # minimal decades to be inside W_v
need_hi = math.log10(1 / W_LO)
print(f"W_v needs log10(M_Pl/Lambda*) in [{need_lo:.2f}, {need_hi:.2f}] (centre {math.log10(1/TV):.2f})")
print("\ncandidate                                  g^2     alpha    best-case decades (reading)        "
      "short of W_v   g2/g2_max_inside")
rows = []
for name, g2 in cands.items():
    best, lab = -1, ""
    for content in ["A", "B", "C"]:
        for loops in [1, 2]:
            for sname, r in [("MSbar", 1.0), ("Wilson-bare", 28.809)]:
                d = decades(g2, content, loops, r)
                if d == d and d > best:
                    best, lab = d, f"{content},{loops}-loop,{sname}"
    rows.append((name, g2, best))
    print(f"{name:42s} {g2:6.4f}  {g2/FOURPI:.4f}   {best:6.2f} ({lab:24s})   {need_lo-best:6.2f}     {g2/G2_INSIDE_MAX:5.2f}")
worst_gap = min(need_lo - r[2] for r in rows)
check("every C1-C3 candidate is outside W_v in its most favourable perturbative reading",
      worst_gap > 0, f"(smallest shortfall {worst_gap:.2f} decades)")
check("every C1-C3 candidate exceeds the largest in-window g^2 by >= 2.7x",
      min(g2 for _, g2, _ in rows) / G2_INSIDE_MAX > 2.7)

# ---- non-perturbative beta = 6 (pure gauge) from the repo certificate ----
print("\n== beta = 6 non-perturbative (pure SU(3)), repo certificate on origin/main ==")
raw = subprocess.run(["git", "-C", REPO, "show",
                      "origin/main:outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json"],
                     capture_output=True, text=True, check=True).stdout
cert = json.loads(raw)
ss = cert["scale_setting"]
r0a = ss["global_r0_over_a"]; sig = ss["global_cornell_fit"]["sigma"]; e = ss["global_cornell_fit"]["e"]
md = cert.get("metadata", {})
print(f"  metadata keys: {sorted(md.keys())[:12]}")
for k in ["beta", "g_bare", "action", "gauge_group"]:
    if k in md: print(f"  metadata.{k} = {md[k]}")
check("certificate r0/a = sqrt((1.65-e)/sigma)", abs(math.sqrt((1.65 - e) / sig) - r0a) < 1e-9, f"{r0a:.4f}")
r0L = 0.602   # Lambda_MS r0, pure SU(3) (comparator, ALPHA collaboration)
for b in [1, 2, 5, 19, 35]:
    for rname, rr in [("repo 5.006", r0a), ("lit 5.368", 5.368)]:
        Lrat = r0L / rr / b
        sq = math.sqrt(sig) / b
        print(f"  b={b:2d} r0/a={rname}: Lambda_MS/M_Pl = {Lrat:.3e} ({math.log10(1/Lrat):.2f} decades), "
              f"sqrt(sigma)/M_Pl = {sq:.3e}; short of W_v by {need_lo - math.log10(1/Lrat):.2f} decades")
check("beta = 6 on the grid: Lambda_MS within 2.5 decades of M_Pl for every b <= 35",
      math.log10(35 * max(r0a, 5.368) / r0L) < 2.5)

# ---- C5: one-loop block matching across a rung of size b ----
print("\n== C5 rung matching (one loop): g^2 at the coarse rung from g^2 = 1 at the fine rung ==")
for nf, lab in [(0, "pure"), (6, "nf=6")]:
    b0 = (11 - 2 * nf / 3) / (16 * math.pi ** 2)
    s = []
    for b in [2, 5, 19, 35]:
        inv = 1.0 - 2 * b0 * math.log(b)
        s.append(f"b={b}: {1/inv:.3f}" if inv > 0 else f"b={b}: strong")
    need = (1 / G2_INSIDE_MAX - 1.0) / (2 * b0)
    print(f"  {lab}: " + ", ".join(s) + f"; moving g^2 = 1 to <= {G2_INSIDE_MAX} needs a Lambda ratio "
          f"exp({need:.2f}) = {math.exp(need):.2e}")
print("  heat-kernel vs Wilson (PR #9702 :206): Lambda ratio 1.819 -> shift log10(1.819) = "
      f"{math.log10(1.819):.3f} decades")

# ---- C6: alpha_s(v) placed at mu = v (declared B4), run to M_Pl ----
print("\n== C6: alpha_s(v) = 0.10330382 at mu = v (B4), two-loop, nf = 6 above 172.69 GeV ==")
v_h = 246.282818290129
a_pl, _ = rg.run_alpha(0.10330382, v_h, rg.M_PL, 6, 2)
L6 = rg.Lambda(v_h, 0.10330382, 6, 2)
amz = rg.piecewise_down(0.10330382, v_h, [(172.69, 6), (rg.M_Z, 5)], 2)
L5 = rg.Lambda(rg.M_Z, amz, 5, 2)
print(f"  g^2(M_Pl) = {FOURPI*a_pl:.4f} (alpha = {a_pl:.5f}); inside the W_v g^2 band? "
      f"{G2_INSIDE_MIN <= FOURPI*a_pl <= G2_INSIDE_MAX}")
print(f"  its strong scale: Lambda^(6)/M_Pl = {L6/rg.M_PL:.3e}, Lambda^(5) = {L5:.4f} GeV "
      f"({math.log10(rg.M_PL/L6):.2f} decades; W_v needs {need_lo:.2f}-{need_hi:.2f})")
in_Wv = W_LO <= L6 / rg.M_PL <= W_HI
check("C6 is outside W_v (it reproduces QCD, not v)", not in_Wv)
check("C6 is inside the secondary W_QCD band (0.021-2.1 GeV)", 0.021 <= L5 <= 2.1, f"{L5:.3f} GeV")
print("  C6 consumes mu = v (the hierarchy readout) as its matching scale: CIRCULAR.")

# ---- C7: the direct Wilson-loop ruler ----
a_fm = ss["global_a_fm"]
hbarc = 0.1973269804  # GeV fm
ainv = hbarc / a_fm
print(f"\n== C7: certificate a = {a_fm:.4f} fm -> a^-1 = {ainv:.3f} GeV; M_Pl/a^-1 = {rg.M_PL/ainv:.3e} "
      f"({math.log10(rg.M_PL/ainv):.2f} decades) -- the ruler r0 = 0.5 fm supplies them: CIRCULAR.")
print(f"  equivalently: the beta = 6 colour lattice of the alpha_s lanes is b = {rg.M_PL/ainv:.2e} grid spacings")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

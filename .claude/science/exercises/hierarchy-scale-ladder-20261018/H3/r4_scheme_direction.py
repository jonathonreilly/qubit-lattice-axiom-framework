"""HIER-3 R4: direction of the Wilson-bare -> MSbar conversion at beta = 6, and the
Wilson beta of the observed colour coupling at M_Pl. Own code."""
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
rL = 28.809
b0 = 11 / (16 * math.pi ** 2)
# (i) one-loop: 1/g_MS^2(1/a) = 1/g0^2 - 2 b0 ln(Lambda_MS/Lambda_L)
inv = 1.0 - 2 * b0 * math.log(rL)
a_ms_1l = 1 / (FOURPI * inv)
print(f"(i) one-loop: 1/g_MS^2(1/a) = 1 - {2*b0*math.log(rL):.4f} = {inv:.4f} -> alpha_MS(1/a) = {a_ms_1l:.4f}")
check("(i) Wilson-bare 0.0796 converts to a LARGER MSbar alpha", a_ms_1l > 1 / FOURPI, f"{a_ms_1l:.4f} > 0.0796")
# (ii) non-perturbative: Lambda_MS a = 0.602 / (r0/a)
raw = subprocess.run(["git", "-C", REPO, "show",
                      "origin/main:outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json"],
                     capture_output=True, text=True, check=True).stdout
r0a = json.loads(raw)["scale_setting"]["global_r0_over_a"]
for lab, rr in [("repo r0/a", r0a), ("lit r0/a", 5.368)]:
    Lam_a = 0.602 / rr
    out = []
    for loops in [2, 4]:
        try:
            out.append(rg.alpha_from_Lambda(1.0, Lam_a, 0, loops))
        except ValueError:
            out.append(float('nan'))
    print(f"(ii) {lab} = {rr:.3f}: Lambda_MS a = {Lam_a:.4f}; alpha_MS(mu=1/a) = {out[0]:.4f} (2-loop), "
          f"{out[1]:.4f} (4-loop); at mu = pi/a: {rg.alpha_from_Lambda(math.pi, Lam_a, 0, 2):.4f} (2-loop)")
    check(f"(ii) beta = 6 theory has alpha_MS(1/a) > 0.0796 [{lab}]", min(out) > 1 / FOURPI)
# (iii) Wilson beta of the observed colour coupling at M_Pl (pure-gauge one-loop conversion)
g2_obs = 0.2372   # r1.log: SM two-loop g3(M_Pl)^2 from alpha_s(MZ) = 0.1180
inv0 = 1 / g2_obs + 2 * b0 * math.log(rL)
print(f"(iii) g_MS^2(M_Pl) = {g2_obs} -> Wilson-bare g0^2 = {1/inv0:.4f}, beta = 6/g0^2 = {6*inv0:.1f} "
      f"(pure-gauge one-loop conversion; content-dependent at O(1))")
check("(iii) the observed colour coupling at M_Pl is far from beta = 6", 6 * inv0 > 6 * 3)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

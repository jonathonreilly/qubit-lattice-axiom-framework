"""F1 (lane RF): the khronometric (healthy Horava IR) window after GW170817.

Formulas are from Gumrukcuoglu-Saravani-Sotiriou, PRD 97, 024032 (2018), arXiv:1711.08845
(read from the fetched text, eqs. 3-15), parameters (alpha, beta, gamma) of the covariant
khronometric action; GSS gamma = lambda_Horava - 1 when beta = 0.
Bounds:
  GW170817:  -3e-15 <= c_T - 1 <= 7e-16           (GSS eq. 13)
  weak-field PPN: |alpha1| < 1e-4, |alpha2| < 4e-7 (GSS eq. 11, Will's review)
  strong-field (pulsars): |alpha1^| < 1e-5 (Shao-Wex 2012), |alpha2^| < 1.6e-9 (Shao et al. 2013,
     1307.2552). Strong-field hats include sensitivities; Barausse 1907.05958: sensitivities vanish
     at alpha = beta = 0. Here they are used as if sensitivities were negligible (a reading).
  BBN: |(alpha+3gamma+beta)/(2+3gamma+beta)| < 1/8   (GSS eq. 10)
  stability/unitarity: 0<alpha<2, beta<1, (2+3gamma+beta)/(gamma+beta) > 0
  Cherenkov (conservative): c_S >= 1
  Strong coupling (GSS eq. 15): M_SC ~ sqrt(alpha) M c_S^{-1/2} for c_S^2 > 1.
"""
import numpy as np

def cT2(a, b, g):
    return 1.0 / (1.0 - b)

def cS2(a, b, g):
    return (2 - a) * (g + b) / (a * (1 - b) * (2 + 3 * g + b))

def alpha1(a, b, g):
    return -4 * (a - 2 * b) / (1 - b)

def alpha2(a, b, g):
    return ((a - 2 * b) / (2 - a)) * (1 - (a - 2 * b) * (1 + b + 2 * g) / ((1 - b) * (b + g)))

def bbn(a, b, g):
    return (a + 3 * g + b) / (2 + 3 * g + b)

def allowed(a, b, g, strong=False, cher=True):
    ok = (0 < a < 2) and (b < 1) and ((2 + 3 * g + b) / (g + b) > 0 if (g + b) != 0 else False)
    if not ok:
        return False
    cT = np.sqrt(cT2(a, b, g))
    if not (-3e-15 <= cT - 1 <= 7e-16):
        return False
    a1b, a2b = (1e-5, 1.6e-9) if strong else (1e-4, 4e-7)
    if abs(alpha1(a, b, g)) > a1b or abs(alpha2(a, b, g)) > a2b:
        return False
    if abs(bbn(a, b, g)) > 1 / 8:
        return False
    if cher and cS2(a, b, g) < 1:
        return False
    return True

print("== 1. GW170817 alone: c_T^2 = 1/(1-beta) ==")
for b in [1e-15, -1e-15, 2e-15, -6e-15]:
    print(f"  beta={b:+.0e}: c_T-1 = {np.sqrt(cT2(0,b,0))-1:+.2e}")
print("  -> |beta| <~ 1e-15 (both signs bounded, GSS eq. 14)")

print("\n== 2. beta = 0 section: maximal alpha allowed vs gamma ==")
for strong in (False, True):
    tag = "strong-field (1e-5, 1.6e-9)" if strong else "weak-field (1e-4, 4e-7)"
    print(f"  bounds: {tag}")
    for g in [1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 0.05, 0.1]:
        alphas = np.logspace(-14, 0, 4001)
        ok = [a for a in alphas if allowed(a, 0.0, g, strong=strong)]
        # also look for the cancellation branch alpha ~ gamma/(1+2gamma)
        if ok:
            amax = max(ok)
            amin = min(ok)
            print(f"    gamma={g:.0e}: allowed alpha in [{amin:.1e}, {amax:.1e}] (grid), "
                  f"c_S at amax = {np.sqrt(cS2(amax,0,g)):.2e}")
        else:
            print(f"    gamma={g:.0e}: no allowed alpha on grid")

print("\n== 3. the two branches (beta = 0) ==")
print("  alpha2 = (alpha/(2-alpha)) * (1 - alpha(1+2gamma)/gamma)")
print("  branch (i): alpha << gamma -> alpha2 ~ alpha/2 -> alpha <~ 2|alpha2|max")
print("  branch (ii): alpha ~ gamma/(1+2gamma) (cancellation) and alpha1 = -4alpha -> gamma ~ alpha <~ 2.5e-6;")
print("               but then c_S^2 = (2-a)g/(a(2+3g)) ~ 1 -> borderline Cherenkov.")
for g in [1e-6, 2e-6]:
    a_c = g / (1 + 2 * g)
    print(f"    gamma={g:.0e}, alpha=gamma/(1+2gamma)={a_c:.3e}: alpha1={alpha1(a_c,0,g):.2e}, "
          f"alpha2={alpha2(a_c,0,g):.2e}, c_S^2={cS2(a_c,0,g):.4f}, BBN={bbn(a_c,0,g):.2e}")

print("\n== 4. natural-prior volume (tuning measure) ==")
rng = np.random.default_rng(1)
N = 2_000_000
a = rng.uniform(0, 2, N)
g = rng.uniform(-0.3, 1.0, N)
# beta: fraction of a natural O(1) interval is |dbeta| ~ 1e-15 -> factor 1e-15 analytically
b = 0.0
with np.errstate(divide="ignore", invalid="ignore"):
    ok = (a > 0) & (a < 2) & ((2 + 3*g) / g > 0)
    ok &= np.abs(-4*a) <= 1e-4
    ok &= np.abs((a/(2-a))*(1 - a*(1+2*g)/g)) <= 4e-7
    ok &= np.abs((a + 3*g)/(2 + 3*g)) <= 1/8
cnt = int(ok.sum())
print(f"  (alpha,gamma) uniform in [0,2]x[-0.3,1], beta=0, weak-field PPN, no Cherenkov: "
      f"fraction allowed = {cnt}/{N} = {cnt/N:.2e}")
print("  (beta adds a factor ~1e-15 of an O(1) interval)")

print("\n== 5. strong-coupling scale at sample allowed points (M = reduced Planck) ==")
for a_, g_ in [(1e-6, 0.01), (1e-9, 0.01), (1e-9, 0.1), (1e-12, 0.01), (1e-15, 0.01)]:
    cs2 = cS2(a_, 0, g_)
    msc = np.sqrt(a_) * cs2 ** (-0.25)
    print(f"  alpha={a_:.0e}, gamma={g_}: allowed(weak)={allowed(a_,0,g_)}, allowed(strong)={allowed(a_,0,g_,strong=True)}, "
          f"c_S={np.sqrt(cs2):.2e}, M_SC/M ~ {msc:.1e}  (~{msc*2.4e18:.1e} GeV)")
print("  alpha -> 0 (Barausse/Franchini region alpha=beta=0): c_S -> inf, M_SC -> 0 (khronon strongly coupled).")

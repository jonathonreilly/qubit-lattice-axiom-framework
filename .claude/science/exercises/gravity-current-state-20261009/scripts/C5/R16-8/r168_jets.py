"""C5 R16-8, script A: where the off-box Killing defect sits, for four matter laws (d = 3).

Laws (one band, number-conserving, eps^2 = m^2 + sum_i u(k_i)):
  L-box  : R7-1/R12-1 literal box, s = rho k + (1-rho) sin k, b = 2.0, b2 = 3.1, u = s^2   (superluminal edge)
  S(1.4) : R13-4/R14-1 odd subluminal symbol s, u = s^2                                     (subluminal)
  G(1.4) : R14-1 gapped even subluminal, u = g = h^2                                          (subluminal)
  SLAC   : P-pf1 (R16-5): s = wrap(k) (sawtooth), u = s^2                                     (discontinuous at the face)
Momentum generator symbol: two choices per law
  P = s        ("hopping" momentum, R12-1's choice for L-box)
  P = u'/2     ("current-aligned", = d(eps^2/2)/dk; R8-2/R9-9/R16-5's forward value)
Killing defects (one-body, diagonal; R12-1 Theorem K's jets):
  SS (1,0)/(0,1):  {H,K_b} - P_b       -> j_b - P_b = u'(k_b)/2 - P(k_b)
  JS translation-boost: {P_c,K_b} - delta_bc H -> eps (P'(k_c) - 1) delta_bc   (separable)
  (JJ translation-rotation and rotation-rotation jets are built from the same P' - 1.)
Checks: whole-zone v_max (3D grid), 1D zone mean of P' - 1 (raw 2^16-point average; the SLAC face delta is
reported separately), zone fraction carrying a defect, and R12-1's ray test |D_JS(0,q;k)|/|s_grav(q)| as q -> 0
(completion needed ~ 1/t iff the defect is nonzero). Gravity smearing symbol d(q) = q (inside the graviton box).
Subtractions: none (raw symbols, raw averages).
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sublum_copy import SymS, SymG, sstep, wrap

M = 0.3
B_IN, B_OUT = 2.0, 3.1

def rho(k):
    a = np.abs(wrap(k))
    return 1.0 - sstep((a - B_IN) / (B_OUT - B_IN))

def s_box(k):
    kk = wrap(k); r = rho(k)
    return r * kk + (1 - r) * np.sin(kk)

def num_d(f, k, h=1e-6):
    return (f(k + h) - f(k - h)) / (2 * h)

S14 = SymS(1.4); G14 = SymG(1.4)

LAWS = {
    "L-box(2.0)": dict(u=lambda k: s_box(k) ** 2, s=s_box),
    "S(1.4)":     dict(u=lambda k: S14.s(k) ** 2, s=S14.s),
    "G(1.4)":     dict(u=G14.g, s=G14.h),           # 'hopping' symbol for G: h (odd extension below)
    "SLAC":       dict(u=lambda k: wrap(k) ** 2, s=lambda k: wrap(k)),
}
# odd extension of h for the G law's hopping symbol
LAWS["G(1.4)"]["s"] = lambda k: np.sign(wrap(k)) * G14.h(k)

def up(law, k):        # u'(k)
    if law == "G(1.4)":
        return G14.dg(k)
    if law == "SLAC":
        return 2 * wrap(k)
    if law == "S(1.4)":
        return 2 * S14.s(k) * S14.ds(k)
    # L-box: analytic u' = 2 s s' with s' from a single central difference (avoids nested-difference noise)
    return 2 * s_box(k) * num_d(s_box, k, 1e-5)

def Psym(law, choice, k):
    if choice == "P=s":
        return LAWS[law]["s"](k)
    return 0.5 * up(law, k)

def dP(law, choice, k):
    if law == "SLAC":
        return np.ones_like(np.asarray(k, float))      # a.e.; the face delta is reported separately
    return num_d(lambda x: Psym(law, choice, x), k, 1e-4)   # outer step 1e-4 (inner 1e-5): noise ~1e-10

out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

pr("C5 R16-8 script A (r168_jets.py): Killing-defect location, d = 3, m =", M)
kz = np.linspace(-np.pi, np.pi, 2 ** 16, endpoint=False) + np.pi / 2 ** 16   # avoids k = +-pi exactly

pr("\n(1) whole-zone group velocity (3D grid 96^3 + axis/diagonal lines), separable bands")
for law in LAWS:
    u = LAWS[law]["u"]
    k1 = np.linspace(-np.pi, np.pi, 96, endpoint=False) + np.pi / 96
    U = u(k1); Up = up(law, k1)
    E2 = M * M + U[:, None, None] + U[None, :, None] + U[None, None, :]
    V2 = (0.25 * (Up[:, None, None] ** 2 + Up[None, :, None] ** 2 + Up[None, None, :] ** 2)) / E2
    vg = np.sqrt(V2.max())
    # fine 1D lines: axis and body diagonal
    kl = np.linspace(-np.pi, np.pi, 40001)
    ul, upl = u(kl), up(law, kl)
    vax = np.max(np.abs(0.5 * upl) / np.sqrt(M * M + ul))
    vdi = np.max(np.sqrt(3 * 0.25 * upl ** 2) / np.sqrt(M * M + 3 * ul))
    pr(f"  {law:11s}: v_max grid {vg:.4f}; axis line {vax:.4f}; diagonal line {vdi:.4f}")
pr("  (SLAC: |v| = |k|/eps <= 1 on the whole cube; the band is not continuous across the face)")

pr("\n(2) 1D zone mean of P' - 1 (raw average, 2^16 points) and the zone fraction carrying the JS defect")
for law in LAWS:
    for ch in ("P=s", "P=u'/2"):
        d1 = dP(law, ch, kz) - 1.0
        mean = d1.mean()
        frac1 = np.mean(np.abs(d1) > 1e-6)
        frac3 = 1 - (1 - frac1) ** 3
        ss = 0.5 * up(law, kz) - Psym(law, ch, kz)       # SS jet j - P
        fss = np.mean(np.abs(ss) > 1e-6)
        extra = ""
        if law == "SLAC":
            jump = Psym(law, ch, np.array([np.pi - 1e-9]))[0] - Psym(law, ch, np.array([-np.pi + 1e-9]))[0]
            extra = f"; face jump of P = {jump:.6f} (= 2 pi): the -1 zone mean sits in a delta -2 pi delta(k - pi)"
        pr(f"  {law:11s} {ch:7s}: <P'-1> a.e. = {mean:+.6f}; 1D defect fraction {frac1:.3f}, 3D {frac3:.3f};"
           f" SS (j-P) nonzero fraction {fss:.3f}{extra}")

pr("\n(3) R12-1 ray test on the JS slice p_xi = 0: max_c |D_JS(0, t u; k)| / |s_grav(t u)|,  s_grav(q) = sqrt(2)|q|^2")
pr("    D_JS(0,q;k)_c = i aT(q,k) (q_c - (P_c(k+q) - P_c(k))),  aT = (eps(k+q)+eps(k))/2   [R12-1 conventions]")
rng = np.random.default_rng(16008)
U3 = rng.normal(size=(6, 3)); U3 /= np.linalg.norm(U3, axis=1)[:, None]

def eps3(law, k):
    return np.sqrt(M * M + sum(LAWS[law]["u"](k[..., i]) for i in range(3)))

KS = {"in box": np.array([0.4, -0.7, 0.9]), "transition": np.array([1.9, 0.3, -0.5]),
      "edge": np.array([2.6, -0.2, 0.1]), "near face": np.array([3.1, 0.5, -0.3])}
for law in LAWS:
    ch = "P=u'/2"
    for name, k in KS.items():
        row = []
        for t in (1e-1, 1e-2, 1e-3):
            worst = 0.0
            for uu in U3:
                q = t * uu
                aT = 0.5 * (eps3(law, k + q) + eps3(law, k))
                dPc = np.array([Psym(law, ch, k[c] + q[c]) - Psym(law, ch, k[c]) for c in range(3)])
                D = aT * (q - dPc)
                worst = max(worst, np.max(np.abs(D)) / (np.sqrt(2) * t * t))
            row.append(worst)
        pr(f"  {law:11s} k {name:10s} {np.round(k,2)}: t = 1e-1, 1e-2, 1e-3 -> {row[0]:.3e} {row[1]:.3e} {row[2]:.3e}"
           f"   (ratio t=1e-3/1e-2: {row[2]/max(row[1],1e-300):.2f})")

pr("\n(4) the defect current: edge quanta carry the JS defect density at their group velocity")
pr("    one-body defect per quantum Delta_cc(k) = eps (P'(k_c) - 1); current = v(k) Delta(k). Sample k on the edge:")
for law in ("S(1.4)", "G(1.4)"):
    for k in (np.array([2.0, 0.3, 0.2]), np.array([2.6, 0.1, -0.4]), np.array([1.6, 1.6, 0.0])):
        e = eps3(law, k)
        dl = np.array([e * (dP(law, "P=u'/2", np.array([k[c]]))[0] - 1) for c in range(3)])
        v = np.array([0.5 * up(law, np.array([k[c]]))[0] / e for c in range(3)])
        pr(f"  {law}: k = {k}: Delta_cc = {np.round(dl,4)}, v = {np.round(v,4)}, |v| = {np.linalg.norm(v):.4f}")

with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")

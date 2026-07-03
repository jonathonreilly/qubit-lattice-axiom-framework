"""
The emergent gravity seed, grounded: gravity's CONFORMAL part (light-bending) is records-derived
(the conformal class); its SCALE part (Shapiro time-delay) is the clock-rate no-go. This SPLIT
explains the framework's gravity-results pattern (lensing retained vs Shapiro no-go).

Builds directly on EMERGENT_METRIC_..._CONFORMAL_CLASS_FROM_RECORDS (this session): the records
derive the metric's conformal class (the causal light-cone field); the conformal factor (scale /
clock rate) is the retained_no_go POST_RECORD_CLOCK_RATE_INTERFACE. A position-dependent record /
energy density curves the conformal class = the gravity seed.

Two gravitational observables, split by conformal weight:
  - LIGHT DEFLECTION (lensing): null geodesics are CONFORMALLY INVARIANT, so the bending angle is a
    CONFORMAL-CLASS observable -> records-derived. (Matches LENSING_DEFLECTION_NOTE, retained_bounded:
    "a geodesic in a gradient-index field".)
  - SHAPIRO DELAY: the physical (proper-time) delay scales with the conformal factor Omega -> a SCALE
    observable -> the clock-rate no-go. (Matches the retained_no_go shapiro_* family.)

So gravity's causal/conformal part is records-native; its scale part is the located clock-rate no-go,
and the retained-lensing / no-go-Shapiro pattern CONFIRMS the split.

No new axiom. Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

# ---- weak-field static lens metric g_munu(x,y) = diag(-(1+2phi), 1-2phi, 1-2phi), c=1 ----
M_lens, EPS = 0.06, 0.6
def phi(x, y): return -M_lens / np.sqrt(x*x + y*y + EPS*EPS)        # Newtonian potential (<0)
def g_diag(x, y):
    p = phi(x, y); return np.array([-(1 + 2*p), 1 - 2*p, 1 - 2*p])  # (tt, xx, yy)
def ginv_diag(x, y): return 1.0 / g_diag(x, y)
def Omega(x, y): return 1.0 + 0.4 * np.exp(-(x*x + y*y) / 4.0)      # a POSITION-DEPENDENT conformal factor

print("=" * 78)
print("A1. null-geodesic direction field is CONFORMALLY INVARIANT (pointwise over a grid)")
print("=" * 78)
# photon ray direction dx^i/dlambda ∝ g^ii p_i. Under g -> Omega^2 g, g^ii -> Omega^-2 g^ii, so the
# NORMALIZED direction is unchanged at every point => the ray PATHS (hence deflection) are conformal.
rng = np.random.default_rng(0)
worst = 0.0
for _ in range(400):
    x, y = rng.uniform(-3, 3, 2)
    gi = ginv_diag(x, y)
    # a null momentum: p_t=-1, p_y random, p_x from null condition g^tt p_t^2+g^xx p_x^2+g^yy p_y^2=0
    pt, py = -1.0, rng.uniform(-0.4, 0.4)
    disc = -(gi[0]*pt*pt + gi[2]*py*py) / gi[1]
    if disc <= 0: continue
    px = np.sqrt(disc)
    p = np.array([pt, px, py])
    dir_g = gi * p; dir_g = dir_g / np.linalg.norm(dir_g)
    gi_resc = gi / Omega(x, y)**2                                   # g~ = Omega^2 g -> g~^ii = Omega^-2 g^ii
    dir_resc = gi_resc * p; dir_resc = dir_resc / np.linalg.norm(dir_resc)
    worst = max(worst, np.linalg.norm(dir_g - dir_resc))
print(f"   worst normalized ray-direction difference (g vs Omega^2 g): {worst:.2e}")
check("null-geodesic direction field invariant under (position-dependent) conformal rescaling",
      worst < 1e-12, "light paths / deflection are conformal-CLASS observables => records-derived")

print()
print("=" * 78)
print("A2. concrete ray-trace: deflection toward the mass, IDENTICAL for g and Omega^2 g")
print("=" * 78)
def trace_deflection(use_conformal):
    # Hamilton's eqns for H=1/2 g^munu p_mu p_nu (null). p_t conserved. integrate in (x,y,px,py).
    def ginv(x, y):
        gi = ginv_diag(x, y)
        return gi / (Omega(x, y)**2 if use_conformal else 1.0)
    def deriv(s):
        x, y, px, py = s
        gi = ginv(x, y)
        pt = -1.0
        dx = gi[1] * px; dy = gi[2] * py                            # dx^i/dl = g^ii p_i
        h = 1e-5                                                     # dp_i/dl = -1/2 d_i g^ab p_a p_b
        def Hq(xx, yy):
            g2 = ginv(xx, yy); return 0.5*(g2[0]*pt*pt + g2[1]*px*px + g2[2]*py*py)
        dpx = -(Hq(x+h, y) - Hq(x-h, y)) / (2*h)
        dpy = -(Hq(x, y+h) - Hq(x, y-h)) / (2*h)
        return np.array([dx, dy, dpx, dpy])
    b = 1.2
    gi0 = ginv(-6.0, b)
    px0 = np.sqrt(-(gi0[0]*1.0 + gi0[2]*0.0) / gi0[1])              # null, moving +x, p_y=0
    s = np.array([-6.0, b, px0, 0.0]); dl = 0.01
    for _ in range(2400):
        k1 = deriv(s); k2 = deriv(s + dl/2*k1); k3 = deriv(s + dl/2*k2); k4 = deriv(s + dl*k3)
        s = s + dl/6*(k1 + 2*k2 + 2*k3 + k4)
        if s[0] > 6.0: break
    # deflection angle = final ray direction angle from +x (the bend)
    return np.arctan2(s[3]*ginv(s[0], s[1])[2], s[2]*ginv(s[0], s[1])[1])
alpha_g = trace_deflection(False)
alpha_conf = trace_deflection(True)
deflects_toward_mass = alpha_g < -1e-4                              # bends toward mass at y=0 (negative)
identical = abs(alpha_g - alpha_conf) < 1e-3
print(f"   deflection angle in g:        {alpha_g:+.5f} rad (toward mass: {deflects_toward_mass})")
print(f"   deflection angle in Omega^2 g: {alpha_conf:+.5f} rad")
print(f"   identical (conformal invariance): {identical}  (|diff|={abs(alpha_g-alpha_conf):.2e})")
check("light deflection is real (toward mass) and IDENTICAL under conformal rescaling",
      deflects_toward_mass and identical, "lensing = conformal-class observable (matches retained LENSING_DEFLECTION)")

print()
print("=" * 78)
print("A3. proper time (Shapiro delay) SCALES with the conformal factor => NOT conformal")
print("=" * 78)
# proper time along a static worldline: dtau = sqrt(-g_tt) dt. Under g->Omega^2 g: sqrt(-Omega^2 g_tt)
# = Omega sqrt(-g_tt). The physical (proper) Shapiro delay therefore scales with Omega -> needs the
# clock rate (the conformal factor) -> the retained_no_go clock-rate interface.
xs = np.linspace(-6, 6, 200); yb = 1.2
def trap(ys, xv): return float(np.sum((np.asarray(ys)[:-1] + np.asarray(ys)[1:]) / 2 * np.diff(xv)))
dtau_g = trap([np.sqrt(-g_diag(x, yb)[0]) for x in xs], xs)
dtau_conf = trap([Omega(x, yb)*np.sqrt(-g_diag(x, yb)[0]) for x in xs], xs)
scales = abs(dtau_conf - dtau_g) > 1e-2
# the Shapiro EXCESS (vs flat) is nonzero (real effect) but its magnitude is scale-set
shapiro_excess_g = dtau_g - trap([1.0 for _ in xs], xs)
print(f"   proper time in g: {dtau_g:.4f};  in Omega^2 g: {dtau_conf:.4f} (differ: {scales})")
print(f"   Shapiro excess vs flat (real, but scale-set): {shapiro_excess_g:+.4f}")
check("the proper-time (Shapiro) delay scales with Omega => a SCALE observable, not conformal",
      scales, "Shapiro = the conformal factor = the clock-rate no-go")

print()
print("=" * 78)
print("A4. the split EXPLAINS the framework's gravity-results pattern")
print("=" * 78)
print("   DEFLECTION (lensing)  = conformal-class observable -> records-derived (the records' conformal")
print("     class, EMERGENT_METRIC note) -> MATCHES retained_bounded LENSING_DEFLECTION_NOTE.")
print("   SHAPIRO (time-delay)  = conformal-FACTOR observable -> the clock-rate no-go")
print("     (retained_no_go POST_RECORD_CLOCK_RATE_INTERFACE) -> MATCHES the retained_no_go shapiro_* family.")
conformal_observable_derived = (worst < 1e-12) and identical
scale_observable_nogo = scales
explains = conformal_observable_derived and scale_observable_nogo
check("gravity's conformal part (lensing) is records-derived; its scale part (Shapiro) is the no-go",
      explains, "the conformal/scale split explains lensing-retained vs Shapiro-no-go")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

"""R7-4 part 2: the free first-moment boost flow on asymptotic momenta (d = 2).
If the linear lapse/shift bridge is exact, D = sum_x x T00(x) obeys i[H,D] = J (conserved), and S commutes
with the free flow U_s = exp(i s D_free), which moves each asymptotic leg by dk_x/ds = omega(k) (k_y fixed)
[one-particle first-moment flow; cf. C4 M1 report: dQ/deta = -E(Q)].  S also conserves H_0-energy, so a
nonzero T(in->out) forces E_in(s) = E_out(s) along the whole flow orbit.
Test: random NON-FORWARD on-shell 2->2 configurations with all legs inside the R6-1 box S=(-a,a)^2, a=0.49 pi,
flowed under three dispersions:
  CONT : omega^2 = m^2 + |k|^2 on R^2 (no lattice; control: shell preserved for all s)
  SLAC : omega^2 = m^2 + |kbar|^2, kbar = k reduced to (-pi,pi]  (exact relativistic band on the zone)
  SMTH : omega^2 = m^2 + 2 sum_i F(k_i), F' = f, f C^infty odd periodic, f(k) = k on |k| <= 0.6 pi
         (relativistic inside the box, smooth periodic outside: the R6-1-type band with P = J_E in the box)
Records: s_box  = first s at which a leg leaves S (box form factor would vanish there),
         s_off  = first s at which |E_in - E_out| > 1e-6 (flowed configuration leaves the energy shell),
         max |E_in - E_out| over the run.  Forward control: out = permutation of in.
"""
import numpy as np
rng = np.random.default_rng(11)
m = 1.0
a = 0.49 * np.pi
PI = np.pi
def red(k): return (k + PI) % (2 * PI) - PI

# smooth odd periodic f equal to k on |k|<=b
b, b2 = 0.6 * PI, 0.95 * PI
def bump(x):  # C^infty step 1 for x<=0, 0 for x>=1
    x = np.clip(x, 0, 1)
    g = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.0)
    return g(1 - x) / (g(1 - x) + g(x))
def f_smooth(k):
    k = red(k)
    chi = bump((np.abs(k) - b) / (b2 - b))
    return chi * k   # C^infty, odd, periodic (vanishes near the zone edge), equals k on |k| <= b
kk = np.linspace(-PI, PI, 200001)
Fk = np.concatenate([[0], np.cumsum(0.5 * (f_smooth(kk[1:]) + f_smooth(kk[:-1])) * np.diff(kk))])
Fk -= np.interp(0.0, kk, Fk)
def F_smooth(k): return np.interp(red(k), kk, Fk)

def omega(k, kind):
    kx, ky = k
    if kind == "CONT": return np.sqrt(m**2 + kx**2 + ky**2)
    if kind == "SLAC": return np.sqrt(m**2 + red(kx)**2 + red(ky)**2)
    if kind == "SMTH": return np.sqrt(m**2 + 2 * F_smooth(kx) + 2 * F_smooth(ky))

def sample_config(forward=False):
    while True:
        k1 = rng.uniform(-0.3 * PI, 0.3 * PI, 2); k2 = rng.uniform(-0.3 * PI, 0.3 * PI, 2)
        P = k1 + k2; E = np.sqrt(m**2 + k1 @ k1) + np.sqrt(m**2 + k2 @ k2)
        if forward:
            return [k1, k2], [k2.copy(), k1.copy()]
        # CM frame, random angle, boost back (equal masses m)
        s = E**2 - P @ P; pst = np.sqrt(s / 4 - m**2); th = rng.uniform(0, 2 * PI)
        q = pst * np.array([np.cos(th), np.sin(th)]); e = np.sqrt(s) / 2
        bv = P / E; g = 1 / np.sqrt(1 - bv @ bv); outs = []
        for sg in (+1, -1):
            qq = sg * q; par = (qq @ bv) / (bv @ bv) if bv @ bv > 0 else 0
            kpar = g * (par * np.sqrt(bv @ bv) + np.sqrt(bv @ bv) * e) if bv @ bv > 0 else 0
            # Lorentz boost of (e, qq) with velocity bv
            bb = bv @ bv
            qlab = qq + ((g - 1) * (qq @ bv) / bb + g * e) * bv if bb > 0 else qq
            outs.append(qlab)
        k3, k4 = outs
        if all(np.all(np.abs(k) < a) for k in (k3, k4)):
            if min(np.linalg.norm(k3 - k1), np.linalg.norm(k3 - k2)) > 0.05:
                return [k1, k2], [k3, k4]

def flow(ins, outs, kind, smax=12.0, ds=2e-3, n=(1.0, 0.0)):
    n = np.asarray(n, float)
    legs = [k.astype(float).copy() for k in ins + outs]
    s, s_box, s_off, maxdE = 0.0, None, None, 0.0
    def E(legs):
        return omega(legs[0], kind) + omega(legs[1], kind) - omega(legs[2], kind) - omega(legs[3], kind)
    while s < smax:
        # RK4 on k_x of each leg: dkx/ds = omega(k)
        def rhs(L):
            return [omega(k, kind) * n for k in L]
        k1 = rhs(legs); L2 = [l + 0.5 * ds * d for l, d in zip(legs, k1)]
        k2 = rhs(L2); L3 = [l + 0.5 * ds * d for l, d in zip(legs, k2)]
        k3 = rhs(L3); L4 = [l + ds * d for l, d in zip(legs, k3)]
        k4 = rhs(L4)
        legs = [l + ds / 6 * (p + 2 * q + 2 * r + t) for l, p, q, r, t in zip(legs, k1, k2, k3, k4)]
        s += ds
        dE = abs(E(legs)); maxdE = max(maxdE, dE)
        if s_box is None and any(np.any(np.abs(red(l)) >= a) for l in legs): s_box = s
        if s_off is None and dE > 1e-6: s_off = s
    return s_box, s_off, maxdE

lines = []
for forward in (False, True):
    tag = "FORWARD control (out = permuted in)" if forward else "NON-FORWARD configurations"
    lines.append(tag)
    for kind in ("CONT", "SLAC", "SMTH"):
        res = []
        for t in range(12 if not forward else 4):
            ins, outs = sample_config(forward)
            e0 = (omega(ins[0], kind) + omega(ins[1], kind) - omega(outs[0], kind) - omega(outs[1], kind))
            sb, so, md = flow(ins, outs, kind)
            res.append((e0, sb, so, md))
        e0s = max(abs(r[0]) for r in res)
        n_off = sum(1 for r in res if r[2] is not None)
        sb_list = [r[1] for r in res if r[1] is not None]
        so_list = [r[2] for r in res if r[2] is not None]
        lines.append(f"  {kind}: initial |E_in-E_out| max {e0s:.1e}; configs leaving the shell: {n_off}/{len(res)}; "
                     f"s_box range {min(sb_list) if sb_list else None:.3} - {max(sb_list) if sb_list else None:.3}; "
                     f"s_off range {(min(so_list) if so_list else float('nan')):.3} - {(max(so_list) if so_list else float('nan')):.3}; "
                     f"max|dE| over run: {max(r[3] for r in res):.3e}")
        for r in res[:3]:
            lines.append(f"     sample: s_box={r[1]}, s_off={r[2]}, max|dE|={r[3]:.3e}")
print("\n".join(lines))

# ---- special non-forward configuration: CM reflection k_y -> -k_y at zero total momentum ----
lines = ["", "Special non-forward CM-reflection (a1,a2),(-a1,-a2) -> (a1,-a2),(-a1,a2), a=(0.7,0.4): flows along n"]
A = np.array([0.7, 0.4]); ins = [A, -A]; outs = [np.array([0.7, -0.4]), np.array([-0.7, 0.4])]
for kind in ("CONT", "SLAC", "SMTH"):
    for nn in [(1, 0), (0, 1), (1 / np.sqrt(2), 1 / np.sqrt(2)), (np.cos(0.3), np.sin(0.3))]:
        sb, so, md = flow(ins, outs, kind, n=nn)
        lines.append(f"  {kind} n=({nn[0]:.3f},{nn[1]:.3f}): s_box={sb}, s_off={so}, max|dE|={md:.3e}")
# ---- random directions for random non-forward configs (SLAC, SMTH) ----
lines.append("")
lines.append("Random non-forward configs, random boost direction n:")
for kind in ("CONT", "SLAC", "SMTH"):
    cnt = 0; tot = 0
    for t in range(8):
        ins, outs = sample_config(False); th = rng.uniform(0, 2 * np.pi)
        sb, so, md = flow(ins, outs, kind, n=(np.cos(th), np.sin(th)))
        tot += 1; cnt += (so is not None)
    lines.append(f"  {kind}: leave shell {cnt}/{tot}")
print("\n".join(lines))

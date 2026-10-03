"""A27 check 1 (carried reading): a record whose locked content is carried by a smooth
hopping change and re-cut every tick (option A).  Supplied 1D/3D single-excitation toy.

H = -J sum_i (|i><i+1| + h.c.), J = 1.  <d|exp(-iHt)|0> = i^d J_d(2t).  Dose per tick x = 2 J tau.
 - w_out: weight carried beyond the star in one tick (what a star-only instrument cannot cut back).
 - clip rule: record steps one site toward the content (sign of displacement), content pulled back
   to the record's new site (linear, complete, but its Kraus maps |y><z| reach as far as the tails).
 - R1 rule without clipping: record lands where the content is (breaks I2 with prob w_out).
 - Zeno: at fixed change-time T the clipped record's variance (T/tau)(1-J0^2) -> 0 as tau -> 0.
"""
import signal
import numpy as np
from scipy.special import jv
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

signal.alarm(55)

def w_out_1d(x):
    return 1 - jv(0, x)**2 - 2*jv(1, x)**2

def w_out_3d(x):
    return 1 - jv(0, x)**6 - 6*jv(1, x)**2*jv(0, x)**4

def var_clip(x):
    return 1 - jv(0, x)**2

def var_r1(x):
    return x**2/2

print("Table A: per tick, J = 1, dose x = 2*J*tau")
print(f"{'x':>6} {'J*tau':>6} {'w_out 1D':>10} {'w_out 3D':>10} {'P(move)':>9} {'var clip':>9} {'var R1':>8} {'D clip':>8} {'D R1':>7}")
for x in [0.05, 0.1, 0.2, 0.5, 1.0, 1.65, 2.0, 3.0, 4.0]:
    tau = x/2
    print(f"{x:6.2f} {tau:6.3f} {w_out_1d(x):10.3e} {w_out_3d(x):10.3e} {var_clip(x):9.4f} "
          f"{var_clip(x):9.4f} {var_r1(x):8.4f} {var_clip(x)/(2*tau):8.4f} {var_r1(x)/(2*tau):7.4f}")

res = minimize_scalar(lambda x: -var_clip(x)/x, bounds=(0.2, 5.0), method="bounded")
xs = res.x
print(f"\nBest clipped mobility: D_max = {var_clip(xs)/xs:.4f} J at dose x = {xs:.4f} (J*tau = {xs/2:.4f}); "
      f"w_out there = {w_out_1d(xs):.4f}")
for R in [1, 2, 3, 4]:
    tail = 1 - jv(0, xs)**2 - 2*sum(jv(d, xs)**2 for d in range(1, R+1))
    print(f"   content beyond distance {R} at D_max dose: {tail:.3e}")

# Exact chain check: propagate the record-position law under the clip rule and under R1.
N, c, n_ticks = 81, 40, 10
Hm = -(np.eye(N, k=1) + np.eye(N, k=-1))
print("\nTable B: exact chain (N=81) after 10 ticks vs formula n*var")
for x in [0.2, 1.0, xs, 3.0]:
    tau = x/2
    U = expm(-1j*Hm*tau)
    K = np.abs(U)**2                      # K[z, y] = |<z|U|y>|^2
    clipK = np.zeros((N, N))
    for y in range(N):
        col = K[:, y]
        clipK[y, y] += col[y]
        if y+1 < N:
            clipK[y+1, y] += col[y+1:].sum()
        if y-1 >= 0:
            clipK[y-1, y] += col[:y].sum()
    p_clip = np.zeros(N); p_clip[c] = 1
    p_r1 = p_clip.copy()
    for _ in range(n_ticks):
        p_clip = clipK @ p_clip
        p_r1 = K @ p_r1
    pos = np.arange(N) - c
    v_clip = (p_clip*pos**2).sum() - (p_clip*pos).sum()**2
    v_r1 = (p_r1*pos**2).sum() - (p_r1*pos).sum()**2
    print(f"  x={x:5.3f}: clip var {v_clip:9.5f} (formula {n_ticks*var_clip(x):9.5f}); "
          f"R1 var {v_r1:9.5f} (formula {n_ticks*var_r1(x):9.5f}); max record step clip = 1 site")

# Zeno at fixed change-time T: record (re-cut every tick) vs uncut content (ballistic 2 T^2).
T = 4.0
print(f"\nTable C: fixed change-time T = {T} (units 1/J); uncut content variance 2T^2 = {2*T*T:.1f}")
for tau in [0.01, 0.05, 0.1, 0.25, 0.5, xs/2, 1.0, 2.0]:
    n = T/tau
    print(f"  tau={tau:6.3f}: ticks {n:7.1f}; clipped-record var {n*var_clip(2*tau):8.4f}; "
          f"unclipped-R1 var {n*var_r1(2*tau):8.4f}; leak per tick w_out {w_out_1d(2*tau):.2e}")

# Ratio form of the star-restricted renormalized odds is not affine (A9 Theorem 1 => signals
# under steering).  sigma1 = |x+1>, sigma2 = (|x-1> + |x+2>)/sqrt2, steered 50/50.
def renorm_odds(rho, star=(0, 1, 2)):          # sites x-1, x, x+1, x+2 -> indices 0..3
    w = np.real(np.diag(rho))[list(star)]
    return w/w.sum()                            # (left, stay, right)
s1 = np.zeros((4, 4)); s1[2, 2] = 1
v = np.zeros(4); v[0] = v[3] = 1/np.sqrt(2); s2 = np.outer(v, v)
steered = 0.5*renorm_odds(s1) + 0.5*renorm_odds(s2)
mixed = renorm_odds(0.5*s1 + 0.5*s2)
print("\nRenormalized star odds (left, stay, right): steered", np.round(steered, 6),
      " unsteered", np.round(mixed, 6), " TV =", round(0.5*np.abs(steered-mixed).sum(), 6))

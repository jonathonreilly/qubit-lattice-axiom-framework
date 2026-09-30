#!/usr/bin/env python3
"""Kill-check of T56 factor-2 claim.  Author: Claude Sonnet 5.5 (same family as attacker/supervisor).
Independent of the attacker's code: Numerov radial integration with PHYSICAL k = mu*v_rel,
mpmath Coulomb functions, and the lane's own convention (k = v_rel) shown explicitly.
Units: particle mass m = 1, reduced mass mu = 1/2, so 2*mu*alpha = alpha and
u'' + (k^2 + alpha/r) u = 0, k = mu*v_rel = v_rel/2.
"""
import numpy as np, math
import mpmath as mp

def S_numerov(alpha, k, rmax_over_lambda=400, h_per_lambda=400):
    """S = |psi(0)|^2 / |psi_free(0)|^2 from u''=-(k^2+alpha/r)u, u~r at 0, Numerov."""
    lam = 1.0/k
    rmax = rmax_over_lambda*lam*2*math.pi
    h = 2*math.pi*lam/h_per_lambda
    n = int(rmax/h)
    r = h*np.arange(1, n+1)          # r_1..r_n ; r_0 = 0
    f = -(k*k + alpha/r)             # u'' = f u
    u = np.zeros(n+1)
    # u(0)=0 ; start with series u ~ r - (alpha/2) r^2 (leading terms, since u''=-(alpha/r)u -> u2=-alpha/2)
    u[0] = 0.0
    r1 = h
    u[1] = r1 - 0.5*alpha*r1**2 + (alpha**2/12 - k*k/6)*r1**3
    # Numerov: (1 - h^2 f_{n+1}/12) u_{n+1} = 2(1+5h^2 f_n/12)u_n - (1 - h^2 f_{n-1}/12) u_{n-1}
    # f at r=0 is singular; use series u''(r) = -(alpha/r)u -> finite; f_0 * u_0 = -alpha (u/r -> 1)
    # handle the first step with f0*u0 := -alpha  (u_0=0 so use W0 = f0*u0 = -alpha)
    W = np.zeros(n+1)
    W[0] = -alpha
    for i in range(1, n+1):
        W[i] = f[i-1]*u[i]
    # generic recursion in terms of W = f*u: u_{n+1} = 2u_n - u_{n-1} + h^2 (W_{n+1}+10W_n+W_{n-1})/12 ; W_{n+1}=f_{n+1}u_{n+1}
    for i in range(1, n):
        fi1 = f[i]              # f at r_{i+1}
        rhs = 2*u[i] - u[i-1] + h*h*(10*W[i] + W[i-1])/12
        u[i+1] = rhs/(1 - h*h*fi1/12)
        W[i+1] = fi1*u[i+1]
    # amplitude from last two points with local wavenumber (WKB correction)
    kk = math.sqrt(k*k + alpha/r[-1])
    up = (u[-1]-u[-3])/(2*h)
    A2 = (u[-2]**2 + (up/kk)**2)*kk/k   # amplitude^2 in units where free u = sin(kr)/k -> A_free^2 = 1/k^2
    # free: u_free = sin(kr)/k => A_free^2 = 1/k^2 with u'(0)=1
    return (1.0/k**2)/A2

def S_2pi(eta):
    z = 2*math.pi*eta
    return z/(-math.expm1(-z)) if abs(z) > 1e-12 else 1.0
def S_pi(x):
    z = math.pi*x
    return z/(-math.expm1(-z)) if abs(z) > 1e-12 else 1.0

print("Numerov with PHYSICAL k = mu*v_rel = v_rel/2 (m=1). eta = mu*alpha/k = alpha/v_rel")
print(f"{'alpha':>7} {'v_rel':>6} {'S_num':>9} {'S_2pi(a/v_rel)':>15} {'S_pi(a/v_rel)':>14} {'S_pi(a/k)=note conv':>20}")
rows = []
for alpha, vrel in [(0.05,0.4),(0.092,0.4),(0.092,0.1),(0.15,0.1),(0.15,0.5),(0.2,0.25),(-0.05,0.4),(-0.02,0.2)]:
    k = vrel/2
    sn = S_numerov(alpha, k)
    eta = alpha/vrel
    rows.append((alpha, vrel, sn, S_2pi(eta), S_pi(alpha/vrel), S_pi(alpha/k)))
    print(f"{alpha:7.3f} {vrel:6.2f} {sn:9.5f} {S_2pi(eta):15.5f} {S_pi(alpha/vrel):14.5f} {S_pi(alpha/k):20.5f}")

print("\nArchived note 1946_SOMMERFELD_LATTICE_GREENS_NOTE table row: alpha_s=0.092, v_rel=0.40, zeta=0.3067 (alpha_eff=C_F*alpha_s=0.12267), S_analytic=1.5579.")
ae = 4/3*0.092
print("  Numerov with the note's convention k = v_rel = 0.4 :", round(S_numerov(ae, 0.4),5), "(agrees with its pi-form 1.5579: the check only validates the code, with k:=v_rel)")
print("  Numerov with physical k = mu*v_rel = 0.2           :", round(S_numerov(ae, 0.2),5), " ; 2pi form S(2 pi alpha_eff/v_rel) =", round(S_2pi(ae/0.4),5))

# mpmath Coulomb function cross-check: psi = F0(eta_c, kr)/(kr), S = C0^2
mp.mp.dps = 30
def S_mp(alpha, vrel):
    eta_c = -alpha/vrel     # attractive: eta_c = mu*V0.../k ; sign conv: repulsive positive
    # C0^2 = 2 pi eta_c/(exp(2 pi eta_c)-1)
    return float(2*mp.pi*eta_c/(mp.exp(2*mp.pi*eta_c)-1))
# verify small-rho slope of coulombf gives C0
def C0_from_coulombf(alpha, vrel):
    eta_c = -alpha/vrel
    rho = mp.mpf('1e-8')
    return float((mp.coulombf(0, eta_c, rho)/rho)**2)
for alpha, vrel in [(0.092,0.4),(0.15,0.1)]:
    print(f"mp coulombf slope^2 alpha={alpha} vrel={vrel}: {C0_from_coulombf(alpha, vrel):.5f}  2pi formula: {S_mp(alpha, vrel):.5f}")

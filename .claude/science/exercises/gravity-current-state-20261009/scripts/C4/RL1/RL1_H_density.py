"""RL1 (H): metric-aware (scalar) sprinkling density rho(1+eta) cannot repair the one-hop link mean, first order, plane-wave Ricci lens.
With density rho(1+eta(z)) the void exponent is rho(pi/24)tau^4 [nu + <eta>_w + ...], w = 6 lam(Lam-lam)/Lam^3, so link/GR = 1 needs
   <eta>_w(y,x) = -(ln nu + ln Delta)(y,x)   for every pair (y,x) on the ray  (first order).
LHS = (6/Lam^3) * [quadratic polynomial in (u_y,u_x) with coefficients the moments M0,M1,M2 of eta along the ray].
Exact sandwich (G-L lane A propagators) for a weak Ricci lens: fit the best (M0,M1,M2) by least squares over pairs with both ends
OUTSIDE the lens (the weakest demand) and report the residual relative to |ln nu + ln Delta|.  Analytic: RHS ~ R0 ab((a+b)^2+ab) is quartic,
so the residual cannot vanish (proved at first order)."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-L/gl_A_planewave.py").read().split('if __name__ == "__main__":')[0])
U1, U2 = 0.48, 0.52
for kk in [0.02, 0.1, 0.3]:
    ks = (kk/0.04, kk/0.04)   # isotropic Ricci (matter) lens, integrated strength kk
    rows = []; rhs = []
    for uy in np.linspace(-2.0, 0.40, 13):
        for ux in np.linspace(0.60, 3.0, 13):
            nu, D, _, _ = nu_delta(ks, uy, ux, n=40001)
            assert np.isfinite(D) and D > 0 and kk*(0.5-uy)*(ux-0.5)/(ux-uy) < 0.9, "caustic"
            Lam = ux-uy
            # <eta>_w = (6/Lam^3) int (u-uy)(ux-u) eta du = (6/Lam^3)[ -M2 + (ux+uy) M1 - ux uy M0 ]
            rows.append(np.array([-ux*uy, ux+uy, -1.0])*6/Lam**3); rhs.append(-(np.log(nu)+np.log(D)))
    A = np.array(rows); b = np.array(rhs)
    sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    res = A@sol-b
    print("lens strength %.2f: |ln nu + ln Delta| range %.3e..%.3e ; best scalar-density fit residual: max %.3e, rms %.3e (rms/rms(rhs) = %.3f)"
          % (kk, np.abs(b).min(), np.abs(b).max(), np.abs(res).max(), np.sqrt((res**2).mean()), np.sqrt((res**2).mean()/(b**2).mean())))

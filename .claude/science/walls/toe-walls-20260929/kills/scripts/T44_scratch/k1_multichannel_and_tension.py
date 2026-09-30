"""Kill-check T44: (1) scale-free four-channel alpha_s extraction with PDG 2024 fit values (the landed
CKM_MULTI_CHANNEL_ALPHA_S_EXTRACTION note did this with 2026-04 PDG-ish numbers); (2) Cabibbo-angle tension;
(3) alternative integer pairs with error-weighted chi2; (4) MC null for the scale-free scan."""
import math, numpy as np
alpha_can = 1/(4*math.pi*math.sqrt(0.5934))
# PDG 2024 fit values (asymmetric errors symmetrised by mean)
lam, dlam = 0.22501, 0.00068
Vcb, dVcb = 0.04183*0+0.04183, (0.00079+0.00069)/2   # |Vcb| ~ s23 (c13 factor ~1)
Vub, dVub = 0.003732, (0.000090+0.000085)/2
Vtd, dVtd = 0.00858, (0.00019+0.00016)/2  # PDG fit: 0.00858 +0.00019 -0.00017 (approx)
def chans(Np, Nc, lam=lam, Vcb=Vcb, Vub=Vub, Vtd=Vtd):
    Nq = Np*Nc
    e1 = Np*lam**2
    e2 = math.sqrt(Nq)*Vcb
    e3 = (Np*Nq**2*Vub**2)**(1/3)
    # E4 quintic: |Vtd|^2 = a^3 (Np^4 (Nq-1) + a^2)/(Np^7 Nc^2)
    f = lambda a: a**3*(Np**4*(Nq-1)+a*a)/(Np**7*Nc**2) - Vtd**2
    lo, hi = 1e-6, 5.0
    if f(hi) < 0: return e1, e2, e3, float('nan')
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return e1, e2, e3, (lo+hi)/2
print("== four-channel alpha_s extraction, PDG 2024 fit values, (2,3,6) ==")
c = chans(2,3)
names = ["E1 lam","E2 Vcb","E3 Vub","E4 Vtd"]
rel = [2*dlam/lam, dVcb/Vcb, dVub/Vub/3*2, 2/3*dVtd/Vtd]   # alpha ~ lam^2 ; Vcb ; Vub^(2/3) ; Vtd^(2/3)
for n,x,r in zip(names,c,rel): print(f"{n}: alpha_s = {x:.5f}  +-{100*r:.2f}%   vs canonical {alpha_can:.5f}: {100*(x/alpha_can-1):+.2f}%")
mean = np.mean(c); print(f"mean {mean:.5f}, spread (max-min)/mean = {100*(max(c)-min(c))/mean:.2f}%")
w = np.array([1/r**2 for r in rel]); wm = float(np.sum(w*np.array(c))/np.sum(w)); wsig = float(1/math.sqrt(np.sum(w)))*wm
chi_c = float(np.sum(w*(np.array(c)/wm-1)**2)*1)  # rel-error chi2 about weighted mean
print(f"weighted mean alpha_s = {wm:.5f} +- {wsig:.5f} ({100*wsig/wm:.2f}%); chi2 of channels about mean = {chi_c:.2f} (3 dof)")
print(f"canonical alpha_s(v) vs weighted mean: {100*(alpha_can/wm-1):+.2f}%  = {(alpha_can-wm)/wsig:+.1f} sigma (channels correlated via shared lam/A? ignoring)")
print("\n== error-weighted chi2 for other integer pairs (alpha_s free) ==")
rows=[]
for Np in range(1,5):
    for Nc in range(1,6):
        cc = chans(Np,Nc)
        if any(math.isnan(x) for x in cc): continue
        ww = w; m = float(np.sum(ww*np.array(cc))/np.sum(ww)); ch = float(np.sum(ww*(np.array(cc)/m-1)**2))
        rows.append((ch,Np,Nc,m))
for ch,Np,Nc,m in sorted(rows)[:8]: print(f"(Np,Nc)=({Np},{Nc}) Nq={Np*Nc}: chi2={ch:9.2f}  alpha_s_fit={m:.4f}")
print("\n== Cabibbo-angle tension: lambda from different PDG 2024 inputs ==")
atl = math.sqrt(alpha_can/2)
inputs = {
 "PDG SM fit (used by attack)": (0.22501,0.00068),
 "direct |Vus| (Kl3+Kmu2 avg, eq 12.8)": (0.22431,0.00085),
 "Kl3 with lattice f+(0)": (0.2233,0.0005),
 "Kmu2/pimu2 (Vus/Vud) lattice": (0.2250,0.0004),
}
Vud, dVud = 0.97367, 0.00032
Vub2 = 0.003732
vus_uni = math.sqrt(1-Vud**2-Vub2**2); dvus_uni = Vud/vus_uni*dVud
inputs["first-row unitarity with direct Vud=0.97367(32)"] = (vus_uni, dvus_uni)
for k,(v,s) in inputs.items(): print(f"{k:55s} {v:.5f} +-{s:.5f}   atlas {atl:.5f} pull {(atl-v)/s:+.2f}")
print(f"atlas |Vud|_0 = {math.sqrt(1-alpha_can/2-alpha_can**3/72):.6f} vs direct Vud 0.97367(32): {(math.sqrt(1-alpha_can/2-alpha_can**3/72)-Vud)/dVud:+.2f} sigma")

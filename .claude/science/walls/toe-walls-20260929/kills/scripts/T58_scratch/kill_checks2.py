import math, sys
sys.dont_write_bytecode = True
exec(open('t58_chain_test.py').read().split('res = {}')[0])
for k in [0.5, 1.0, 2.0, 4.0]:
    r = chain({"K00": k}); print(f"K00={k}: eta/obs={r['eta']:.4f} K={r['K']:.2f} kappa={r['kappa']:.5f} eps={abs(r['eps']):.3e}")
# DI check along the ladder at fixed Y0 and with Y0 retuned to keep m3 fixed
Y0b = 0.653**2/64
for kB in [7,8,9]:
    r = chain({"kB":kB,"kA":kB-1})
    m1=r["M1"]; m3g = Y0b**2*V_EW**2/m1; eDI = 3/(16*PI)*m1*m3g/V_EW**2
    print(f"kB={kB}: eta={r['eta']:.4g}  |eps|/eps_DI={abs(r['eps'])/eDI:.3f}")
# ladder rung with g_weak retuned so m3 = 0.0506 eV: g^4 ∝ M1 -> g = 0.653*(M1/M1_8)^(1/4)
for kB in [7,9]:
    r0 = chain({"kB":kB,"kA":kB-1}); scale = (r0["M1"]/chain({})["M1"])**0.25
    g = 0.653*scale
    r = chain({"kB":kB,"kA":kB-1,"g_weak":g})
    print(f"kB={kB} with g_weak retuned to {g:.3f} (m3={r['m3_light_eV']:.4f} eV): eta/obs={r['eta']:.4g} K={r['K']:.2f}")

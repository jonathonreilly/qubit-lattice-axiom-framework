# Y1-B: s_eff >= c*T_obs (source demonstrably emitting over the observing baseline); plus non-lensed sanity rows
import math
lP=1.616255e-35; Gpc=3.0857e25; c=2.998e8; lk=7.9e-20; AU=1.496e11; pc=3.0857e16; yr=3.156e7
r=math.sqrt((lP/lk)**4)/lk
rows=[('lensed source, 1 Gpc, T_obs=1 s',Gpc,c*1),('lensed source, 1 Gpc, T_obs=8 h',Gpc,c*8*3600),
('lensed source, 1 Gpc, T_obs=1 yr',Gpc,c*yr),('lensed source, 5 Gpc, T_obs=1 yr',5*Gpc,c*yr),
('Sun, 1 AU, shining 4.6 Gyr',AU,c*4.6e9*yr),('Sun, 1 AU, T_obs=1 s',AU,c*1),
('star at 10 pc, T_obs=1 s',10*pc,c*1),('lab lamp 1 m, on 1 h',1.0,c*3600)]
print(f"{'case':40s} {'tau(m)':>9s} {'n_var c_low=0.628':>17s} {'n_var k_h=2.735':>16s}")
for nm,D,s in rows:
    tau=math.sqrt(2*D*s+s*s)
    print(f"{nm:40s} {tau:9.2e} {0.628*r*tau:17.3e} {2.735*r*tau:16.3e}")
# in-band penalty heuristic (SUGGESTED): rapidity cut-off ln(1/z) vs soft window ln(2 gamma_b)
for D,s in ((Gpc,c*yr),(Gpc,3.0)):
    z=0.628*math.sqrt((lP/lk)**4)
    gb=math.sqrt(D/(2*s))
    print(f"D={D:.2e} s={s:.2e}: ln(1/z)={math.log(1/z):.1f}, ln(2 gamma_b)={math.log(2*gb):.1f}, crude end penalty exp(-{2*(math.log(1/z)-math.log(2*gb))+2*math.log(gb):.0f})")

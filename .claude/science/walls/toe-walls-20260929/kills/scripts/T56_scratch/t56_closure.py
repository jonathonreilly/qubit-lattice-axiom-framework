import math, json, sys
sys.argv=['x']
exec(open('t56_test.py').read().split("# ---------------------------------------------------------------- T2")[0].split("# ---------------------------------------------------------------- T1")[0])
import mpmath as mp
mp.mp.dps=30
exec("R_BASE=31/9")
src=open('t56_test.py').read()
# reuse lane kernel definitions
start=src.index("mp.mp.dps = 30"); end=src.index('P("== T1 reproduction gate')
exec(src[start:end])
K=1.07e9; xF=25; m=3940.53; ETA_OBS=6.12e-10
def eta(alpha_x, R): return K*xF/(math.sqrt(106.75)*1.2209e19*math.pi*alpha_x**2*R*3.65e7)*m*m
rows=[]
def add(name, ax, R):
    e=eta(ax,R); rows.append(dict(case=name, alpha_X=ax, R=R, eta=e, dev=e/ETA_OBS-1)); print(f" {name:64s} alpha_X={ax:.4f} R={R:6.3f} eta={e:.3e} ({e/ETA_OBS-1:+.1%})")
add("lane as written: alpha_X=alpha_LM, R=5.477 (S=1.59 from alpha_GUT~0.048)", 0.09067, 5.477)
add("one alpha = alpha_LM, lane June kernel R(alpha_LM)", 0.09067, lane_R(0.09067,1))
add("one alpha = alpha_LM, corrected kernel R(alpha_LM)", 0.09067, lane_R(0.09067,2))
a_pin=0.04381
add("one alpha = pin of R_obs in corrected kernel (0.0438)", a_pin, lane_R(a_pin,2))
a_half=0.09067/2
add("one alpha = alpha_LM/2 in corrected kernel", a_half, lane_R(a_half,2))
# alpha_X needed given corrected R(alpha_LM)
json.dump(rows, open('t56_closure.json','w'), indent=1)

import json, numpy as np, math
M='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt'
d=json.load(open(f'{M}/outputs/alpha_s_wilson_loop_production/ensemble_24x24x24x48_unsmeared.json'))
W=np.array(d['raw_wilson_loops']); print(W.shape)
Wm=W.mean(0)[:4,:4]
Wsym=0.5*(Wm+Wm.T)
def w(R,T): return Wsym[R-1,T-1]
CF=4/3
print('Creutz chi(R,R) and force-scheme coupling alpha_qq(r=R-1/2)=r^2 chi/C_F  (24^3x48 repo ensemble)')
rows=[]
for R in range(2,5):
    chi=-math.log(w(R,R)*w(R-1,R-1)/(w(R,R-1)*w(R-1,R)))
    r=R-0.5
    a=r*r*chi/CF
    rows.append((r,chi,a)); print(f'R={R} r={r} chi={chi:.4f} alpha_qq={a:.3f}')
# targets
P=0.5934; ab=1/(4*math.pi); u0=P**0.25
tg={n:ab/u0**n for n in (0,1,2,4)}
print('couplings alpha_bare/u0^n:',{n:round(v,4) for n,v in tg.items()})
b0=11.0
# one-loop pure-gauge dictionary anchored at repo's certificate alpha_qq(R=1)=0.2544 (r=a, mu=1/a) and at my Creutz r=1.5
for name,(a0,q0) in {'cert R=1 (a=0.2544)':(0.25443766543149016,1.0),'Creutz r=1.5':(rows[0][2],1/1.5)}.items():
    print('anchor',name)
    for n,v in tg.items():
        lnq=2*math.pi*(1/v-1/a0)/b0
        print(f'  n={n}: alpha={v:.4f}  q/q0=exp({lnq:.2f})={math.exp(lnq):.1f}  -> q = {q0*math.exp(lnq):.1f}/a  (BZ edge pi/a=3.14/a)')

"""T51 S1: closed-form scan of the lane's Z3 texture M(r)=[[A,0,0],[0,rB,B],[0,B,rB]], Y = y0 I.
Light masses m = y^2 v^2 / |M_R eigenvalue|. Constants as in L10_scratch/diag_benchmark.py."""
import numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9            # eV * GeV  => m[eV] = c / M[GeV]
A = MPl*aLM**7; B = MPl*aLM**8
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3); RAT = (0.0268, 0.0328)

def masses(r, Bscale=1.0):
    """RH eigenvalues |A|, B'(1+r), B'(1-r); B' = Bscale*B. returns (m_singlet, m_even, m_odd) in eV"""
    Bp = B*Bscale
    return c/A, c/(Bp*(1+r)), c/(Bp*(1-r))

def no_lane(r, Bscale=1.0):
    """U_e = I: singlet is nu_e, solar pair = {singlet, even}; nu3 = odd (lane labels by mass)."""
    ms, me, mo = masses(r, Bscale)
    m1, m2, m3 = sorted([ms, me, mo])
    return dict(dm21=m2**2-m1**2, dm31=m3**2-m1**2, R=(m2**2-m1**2)/(m3**2-m1**2), S=m1+m2+m3, m=(m1,m2,m3))

def io_branch(r, Bscale=1.0):
    """U_e != I: singlet = nu3 (lightest), solar pair = {even, odd} (heavy pair)."""
    ms, me, mo = masses(r, Bscale)
    m3 = ms; ma, mb = sorted([me, mo])   # ma<mb ; nu1=ma, nu2=mb
    dsol = mb**2-ma**2
    datm = 0.5*(ma**2+mb**2) - m3**2       # mean |dm2_3l| of the two heavy states
    return dict(dsol=dsol, datm=datm, datm_hi=mb**2-m3**2, datm_lo=ma**2-m3**2, R=dsol/datm, S=m3+ma+mb, m=(m3,ma,mb))

print('alpha_LM', aLM, ' A/B', A/B)
b = no_lane(aLM/2); print('benchmark NO/lane:', b)
print('IO reading of same benchmark:', io_branch(aLM/2))

# monotonic scan, B fixed at rung 8 (retained anchor)
rs = np.linspace(1e-4, 0.999, 200000)
R_fixedB = np.array([no_lane(r)['R'] for r in rs[::100]])
print('monotone decreasing (B fixed, NO/lane), first/last', R_fixedB[0], R_fixedB[-1], np.all(np.diff(R_fixedB)<=1e-12))
for r in [0.0, 0.045, 0.1, 0.2, 0.3, 0.5, 0.6, 2/3, 0.68, 0.7]:
    d = no_lane(r); print(f' r={r:.3f}  R={d["R"]:.4f}  dm21={d["dm21"]:.3e} dm31={d["dm31"]:.3e}  Sigma={d["S"]*1e3:.1f} meV')

# window in r for the ratio, B fixed
def window(fun, key, lo, hi, rgrid):
    ok = [r for r in rgrid if lo <= fun(r)[key] <= hi]
    return (min(ok), max(ok)) if ok else None
rg = np.linspace(1e-4, 0.99, 100000)
print('NO/lane, B fixed at rung 8: R in RAT for r in', window(no_lane,'R',*RAT,rg))
# re-anchored so that the largest light mass (nu3) stays at the retained 50.55 meV: Bscale=(1-a/2)/(1-r)
def no_lane_reanch(r):
    return no_lane(r, Bscale=(1-aLM/2)/(1-r))
print('NO/lane, nu3 fixed at retained value (B re-anchored): R in RAT for r in', window(no_lane_reanch,'R',*RAT,rg))
for r in [0.60,0.65,2/3,0.68,0.70,0.72]:
    d = no_lane_reanch(r); print(f' reanch r={r:.3f} m={[round(x*1e3,2) for x in d["m"]]} meV dm21={d["dm21"]:.3e} dm31={d["dm31"]:.3e} R={d["R"]:.4f} Sigma={d["S"]*1e3:.1f}')
# joint pass in NO/lane with re-anchoring: dm21 in SOL, dm31 in ATM, Sigma<72
ok = [r for r in rg if SOL[0] <= no_lane_reanch(r)['dm21'] <= SOL[1] and ATM[0] <= no_lane_reanch(r)['dm31'] <= ATM[1]]
print('NO/lane re-anchored: dm21 & dm31 both in boxes for r in', (min(ok),max(ok)) if ok else None)
if ok:
    print('  Sigma there:', no_lane_reanch(ok[0])['S']*1e3, no_lane_reanch(ok[-1])['S']*1e3, ' B*/B =', (1-aLM/2)/(1-ok[0]), (1-aLM/2)/(1-ok[-1]))

# IO branch: doublet gap must be in SOL and mean singlet gap in ATM
print('\nIO branch, B fixed at rung 8:')
for r in [aLM/2, aLM/4, aLM/8, aLM/10, aLM/12, aLM**2, aLM**2/2, 2*aLM**2, aLM**3]:
    d = io_branch(r)
    print(f' r={r:.5f} (r/alpha={r/aLM:.4f}) dsol={d["dsol"]:.3e} datm_mean={d["datm"]:.3e} hi={d["datm_hi"]:.3e} lo={d["datm_lo"]:.3e}  R={d["R"]:.4f} Sigma={d["S"]*1e3:.1f} meV',
          ' SOL' if SOL[0]<=d['dsol']<=SOL[1] else '', ' ATM' if ATM[0]<=d['datm']<=ATM[1] else '')
okS = [r for r in rg if SOL[0] <= io_branch(r)['dsol'] <= SOL[1]]
print('IO branch: doublet gap in SOL box for r in', (min(okS),max(okS)) if okS else None)
okA = [r for r in rg if ATM[0] <= io_branch(r)['datm'] <= ATM[1]]
print('IO branch: mean singlet gap in ATM box for r in', (min(okA),max(okA)) if okA else None, ' (r=alpha^2 =', aLM**2, ')')
# both (B fixed)
both = [r for r in okS if ATM[0] <= io_branch(r)['datm'] <= ATM[1]]
print('IO both boxes, B fixed:', (min(both),max(both)) if both else None)
# with the note's convention: atmospheric = heavier doublet member minus singlet (repo 2.54e-3 style)
bothH = [r for r in okS if ATM[0] <= io_branch(r)['datm_hi'] <= ATM[1]]
print('IO both boxes with atm := heaviest^2 - lightest^2:', (min(bothH),max(bothH)) if bothH else None)

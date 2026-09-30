"""T51 S2: staircase-family scan for the lane's Z3 texture with universal Y.
Family: singlet A = cA*alpha^kA*MPl, doublet anchor B = cB*alpha^kB*MPl, doublet split r.
RH eigenvalues A, B(1+r), B(1-r).  Two label branches:
  NO/lane (U_e=I, singlet = nu_e in the solar pair): pass = dm31 in ATM, dm21 in SOL, Sigma<72 meV
  IO      (singlet = nu3):                            pass = doublet gap in SOL, some atm gap in ATM (lenient), and (report) Sigma<72
"""
import itertools, numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3); RAT=(0.0268,0.0328)

def ev(A, B, r):
    ms, me, mo = c/A, c/(B*(1+r)), c/(B*(1-r))
    m1,m2,m3 = sorted([ms,me,mo])
    no = dict(dm21=m2**2-m1**2, dm31=m3**2-m1**2, S=m1+m2+m3)
    no['ok'] = (SOL[0]<=no['dm21']<=SOL[1]) and (ATM[0]<=no['dm31']<=ATM[1])
    no['okS'] = no['ok'] and no['S']<0.072
    ma, mb = sorted([me,mo]); m3i = ms
    io = dict(dsol=mb**2-ma**2, atm=[0.5*(ma**2+mb**2)-m3i**2, mb**2-m3i**2, ma**2-m3i**2], S=m3i+ma+mb)
    io['ok'] = (SOL[0]<=io['dsol']<=SOL[1]) and any(ATM[0]<=a<=ATM[1] for a in io['atm']) and (ms<min(me,mo))
    io['okS'] = io['ok'] and io['S']<0.072
    return no, io

def run(cs, ks, rs, label):
    n=0; hits_no=[]; hits_io=[]; hits_noS=0; hits_ioS=0
    for cA,cB,kA,kB,r in itertools.product(cs,cs,ks,ks,rs):
        A=cA*aLM**kA*MPl; B=cB*aLM**kB*MPl
        no,io = ev(A,B,r); n+=1
        if no['ok']: hits_no.append((cA,kA,cB,kB,r))
        if io['ok']: hits_io.append((cA,kA,cB,kB,r))
        hits_noS += no['okS']; hits_ioS += io['okS']
    print(f'[{label}] N={n}  NO/lane hits (dm21&dm31)={len(hits_no)} (with Sigma<72: {hits_noS});  IO hits (dsol&atm)={len(hits_io)} (with Sigma<72: {hits_ioS})')
    return n,hits_no,hits_io

ks = range(5,11)
# strict: c=1, retained r=alpha/2 and the historic alpha^2 candidate
n,h1,h2 = run([1.0], ks, [aLM/2, aLM**2], 'strict c=1, r in {a/2,a^2}')
print('  IO hits:', h2)
print('  NO hits:', h1)
# medium: c in {1/2,1,2}, r in a small natural set
rset = [aLM/2, aLM, aLM**2, aLM**2/2, 2*aLM**2, aLM/4, aLM/8, aLM**3, 0.5, 1/3, 2/3, 0.25, 0.75]
n,h3,h4 = run([0.5,1.0,2.0], ks, rset, 'loose c in {1/2,1,2}, 13 r-values')
print('  NO hits (first 20):', h3[:20]); print('  IO hits (first 20):', h4[:20])
print('  NO hits with Sigma<72:')
for cA,cB,kA,kB,r in h3:
    A=cA*aLM**kA*MPl; B=cB*aLM**kB*MPl; no,_=ev(A,B,r)
    if no['okS']: print('   ',(cA,kA,cB,kB,round(r,5)), {k:(round(vv*1e3,2) if k=='S' else float('%.3g'%vv)) for k,vv in no.items() if k in ('dm21','dm31','S')})

# null: log-uniform random (A,B,r) with the same ranges; hit rate for each branch
rng = np.random.default_rng(51)
N=2_000_000
lA = rng.uniform(np.log(aLM**10*MPl/2), np.log(aLM**5*MPl*2), N)
lB = rng.uniform(np.log(aLM**10*MPl/2), np.log(aLM**5*MPl*2), N)
r  = np.exp(rng.uniform(np.log(1e-3), np.log(0.9), N))
A=np.exp(lA); B=np.exp(lB)
ms, me, mo = c/A, c/(B*(1+r)), c/(B*(1-r))
M = np.sort(np.stack([ms,me,mo]),axis=0); m1,m2,m3=M
dm21=m2**2-m1**2; dm31=m3**2-m1**2; S=m1+m2+m3
okNO=(SOL[0]<=dm21)&(dm21<=SOL[1])&(ATM[0]<=dm31)&(dm31<=ATM[1])
okNOS=okNO&(S<0.072)
ma=np.minimum(me,mo); mb=np.maximum(me,mo)
dsol=mb**2-ma**2; atm=0.5*(ma**2+mb**2)-ms**2
okIO=(SOL[0]<=dsol)&(dsol<=SOL[1])&(ATM[0]<=atm)&(atm<=ATM[1])&(ms<ma)
print(f'null (log-uniform A,B in rungs 5..10 +-2x, r log-uniform 1e-3..0.9), N={N}: p(NO/lane)={okNO.mean():.2e}  p(NO & Sigma<72)={okNOS.mean():.2e}  p(IO, mean atm)={okIO.mean():.2e}')
print('expected null hits in loose family (N_loose*p):  NO ->', 3*3*6*6*len(rset)*okNO.mean(), '  IO ->', 3*3*6*6*len(rset)*okIO.mean())
print('expected null hits in strict family:  NO ->', 36*2*okNO.mean(), '  IO ->', 36*2*okIO.mean())

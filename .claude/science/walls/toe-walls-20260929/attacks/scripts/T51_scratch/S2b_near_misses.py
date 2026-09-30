"""T51 S2b: near misses of the natural staircase family (NO/lane and IO), Sigma reported."""
import itertools, numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
SOLc, ATMc = 7.41e-5, 2.51e-3           # central values (NuFit 5.3 as quoted in repo: 7.41e-5, ~2.51e-3)
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3)

def dev(x, ctr): return abs(np.log(x/ctr))
def ev(A,B,r):
    ms,me,mo = c/A, c/(B*(1+r)), c/(B*(1-r))
    m1,m2,m3 = sorted([ms,me,mo])
    no = (m2**2-m1**2, m3**2-m1**2, m1+m2+m3, (m1,m2,m3))
    ma,mb = sorted([me,mo])
    io = (mb**2-ma**2, 0.5*(ma**2+mb**2)-ms**2, ms+ma+mb, (ms,ma,mb)) if ms<ma else None
    return no, io
def scan(cs, ks, rs):
    rows_no=[]; rows_io=[]
    for cA,cB,kA,kB,r in itertools.product(cs,cs,ks,ks,rs):
        A=cA*aLM**kA*MPl; B=cB*aLM**kB*MPl
        no,io = ev(A,B,r)
        rows_no.append((max(dev(no[0],SOLc),dev(no[1],ATMc)), (cA,kA,cB,kB,round(r,5)), no))
        if io: rows_io.append((max(dev(io[0],SOLc),dev(io[1],ATMc)), (cA,kA,cB,kB,round(r,5)), io))
    rows_no.sort(key=lambda t:t[0]); rows_io.sort(key=lambda t:t[0])
    return rows_no, rows_io
ks=range(5,11)
rset=[aLM/2,aLM,aLM**2,aLM**2/2,2*aLM**2,aLM/4,aLM/8,aLM**3,0.5,1/3,2/3,0.25,0.75]
for label,cs in [('c in {1/2,1,2}',[0.5,1,2]),('c in {1/3,1/2,1,2,3}',[1/3,0.5,1,2,3])]:
    no,io=scan(cs,ks,rset)
    print('==',label,' family size',len(no))
    print(' best NO/lane (worst-of-two log-deviation; hit needs both dm21 & dm31 inside 3-sigma boxes):')
    for d,k,v_ in no[:5]: print('   dev=%.3f'%d, k, 'dm21=%.3e dm31=%.3e Sigma=%.1f meV'%(v_[0],v_[1],v_[2]*1e3))
    print(' best IO:')
    for d,k,v_ in io[:5]: print('   dev=%.3f'%d, k, 'dsol=%.3e atm(mean)=%.3e Sigma=%.1f meV'%(v_[0],v_[1],v_[2]*1e3))
    inbox_no=[t for t in no if SOL[0]<=t[2][0]<=SOL[1] and ATM[0]<=t[2][1]<=ATM[1]]
    inbox_io10=[t for t in io if SOL[0]<=t[2][0]<=SOL[1] and 0.9*ATMc<=t[2][1]<=1.1*ATMc]
    print(' in both 3-sigma boxes: NO/lane', len(inbox_no), '; IO with atm within 10% of 2.51e-3:', len(inbox_io10))
    for t in inbox_io10[:8]: print('    IO10 hit', t[1], 'dsol=%.3e atm=%.3e Sigma=%.1f'%(t[2][0],t[2][1],t[2][2]*1e3))

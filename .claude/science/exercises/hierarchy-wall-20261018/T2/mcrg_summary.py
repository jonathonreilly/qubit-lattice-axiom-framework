"""Summarise M2: complex pairs (with the registered counting rule) and the smallest-|y| non-leading even eigenvalue per (L, step, k)."""
import numpy as np, io, contextlib, sys
from mcrg import run, load
specs=[('data/s1_L16.bin',2,[1],16),('data/s1_L24.bin',2,[1],24),('data/s1_L32.bin',3,[1,2],32),('data/s2_L48.bin',3,[1,2],48),('data/s2_L64.bin',4,[1,2,3],64)]
import glob,os
if os.path.exists('data/s3_L48.bin') and 'watchdog' in open('data/s3_L48.log').read(): specs.append(('data/s3_L48.bin',3,[1,2],'48b'))
if os.path.exists('data/s3_L64.bin') and 'watchdog' in open('data/s3_L64.log').read(): specs.append(('data/s3_L64.bin',4,[1,2,3],'64b'))
rows=[]
for f,nl,st,L in specs:
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): out=run(f,nl,st,str(L))
    Ln=int(str(L).rstrip('b'))
    for (lab,n0,sec,k,y,ere,eim) in out: rows.append((lab,Ln>>(n0+1),n0,sec,k,y,ere,eim))
print('== complex pairs (|Im y|>1e-9): label final step sector k : y, Im/sigma')
cp=[]
for lab,fin,n0,sec,k,y,ere,eim in rows:
    for v,er,ei in zip(y,ere,eim):
        if v.imag>1e-9: cp.append((lab,fin,n0,sec,k,v,ei)); print(f'  L{lab} final {fin}^3 step {n0}->{n0+1} {sec} k={k}: y={v.real:+.3f}{v.imag:+.3f}i  Im/sigma={v.imag/max(ei,1e-9):.1f}  |Re y|={abs(v.real):.2f}')
print('  count:',len(cp),' with |Re y|<=0.06:',sum(abs(c[5].real)<=0.06 for c in cp),' with Im>3 sigma:',sum(c[5].imag>3*c[6] for c in cp))
print('== even sector: smallest |y| among non-leading eigenvalues, final >= 8^3, k>=2')
for lab,fin,n0,sec,k,y,ere,eim in rows:
    if sec!='even' or k<2: continue
    i=1+np.argmin(np.abs(y[1:])); print(f'  L{lab} final {fin:2d}^3 step {n0}->{n0+1} k={k}: y_t={y[0].real:+.3f}({ere[0]:.3f})  min|y| other: {y[i].real:+.3f}({ere[i]:.3f})'+('  [final<8: not counted]' if fin<8 else ''))

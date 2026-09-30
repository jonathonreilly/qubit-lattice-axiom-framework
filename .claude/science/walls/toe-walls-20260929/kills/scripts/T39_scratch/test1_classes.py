import numpy as np, itertools, math
from fractions import Fraction
from common import fold
DC=0.22222205        # centre of windows (e,mu | r=1/2, PDG2024)
DOMAIN=np.pi/3
WINS={'tight':1.0e-6,'mid':2.5e-5,'lane':5.3e-5}
H=60                 # height cap
def cand_list():
    out=[]  # (class, height, label, angle in fundamental domain)
    # A: (p/n) pi, n<=H, gcd=1
    for n in range(1,H+1):
        for p in range(1,2*n):
            if math.gcd(p,n)==1: out.append(('A: (p/n)pi',n,f'{p}pi/{n}',float(fold(np.pi*p/n))))
    # B: bare rationals p/q, folded (angle p/q rad, 0<p/q<3)
    for q in range(1,H+1):
        for p in range(1,3*q):
            if math.gcd(p,q)==1: out.append(('B: p/q rad',q,f'{p}/{q}',float(fold(p/q))))
    # C1: arctan(y/x), Gaussian integers, x,y<=H
    for x in range(1,H+1):
        for y in range(1,H+1):
            if math.gcd(x,y)==1: out.append(('C1: arctan(y/x)',max(x,y),f'atan({y}/{x})',float(fold(math.atan2(y,x)))))
    # C2: arccos(p/q), arcsin(p/q)
    for q in range(2,H+1):
        for p in range(1,q):
            if math.gcd(p,q)==1:
                out.append(('C2: arccos(p/q)',q,f'acos({p}/{q})',float(fold(math.acos(p/q)))))
                out.append(('C2: arcsin(p/q)',q,f'asin({p}/{q})',float(fold(math.asin(p/q)))))
    # C3: arg(x + y*omega), Eisenstein integers, |x|,|y|<=H  (omega = exp(2 pi i/3))
    w=np.exp(2j*np.pi/3)
    for x in range(-H,H+1):
        for y in range(-H,H+1):
            if (x,y)!=(0,0) and math.gcd(abs(x),abs(y))==1 and max(abs(x),abs(y))<=H:
                z=x+y*w; out.append(('C3: arg(x+y*omega)',max(abs(x),abs(y)),f'arg({x}+{y}w)',float(fold(np.angle(z)))))
    # C4: arccos(sqrt(p/q))
    for q in range(2,H+1):
        for p in range(1,q):
            if math.gcd(p,q)==1: out.append(('C4: arccos(sqrt(p/q))',q,f'acos(sqrt({p}/{q}))',float(fold(math.acos(math.sqrt(p/q))))))
    # C5: cos(3 delta)=p/q  => delta=(1/3)arccos(p/q), p/q in (-1,1)
    for q in range(1,H+1):
        for p in range(-q+1,q):
            if math.gcd(abs(p),q)==1: out.append(('C5: cos3d=p/q',q,f'cos3d={p}/{q}',float(fold(math.acos(p/q)/3))))
    return out
C=cand_list()
print('total candidates (with folding, incl. duplicates across classes):',len(C))
classes=sorted(set(c[0] for c in C))
for wname,w in WINS.items():
    print(f'\n=== window {wname}: half-width {w:.1e} about delta_c={DC} ===')
    print('%-24s %-10s %-34s %-10s %-10s'%('class','#cand<=9','hits (height<=H, label:height:offset)','null@9','null@H'))
    for cl in classes:
        cs=[c for c in C if c[0]==cl]
        n9=len([c for c in cs if c[1]<=9]); nH=len(cs)
        hits=sorted([(c[1],c[2],c[3]-DC) for c in cs if abs(c[3]-DC)<=w])
        hs=', '.join(f'{l}:h{h}:{o:+.1e}' for h,l,o in hits[:4])+(' ...' if len(hits)>4 else '')
        print('%-24s %-10d %-34s %-10.2e %-10.2e'%(cl,n9,hs if hs else '-',n9*2*w/DOMAIN,nH*2*w/DOMAIN))
    # global: distinct candidate angles up to height 9, all classes: null expectation
    n9all=len([c for c in C if c[1]<=9]); 
    print('all classes height<=9: #cand=%d null expected hits=%.2e ; height<=%d: #cand=%d null=%.2e'%(n9all,n9all*2*w/DOMAIN,H,len(C),len(C)*2*w/DOMAIN))
# lowest-height hit per class in the tight window
print('\n--- lowest-height hit per class (tight / mid / lane) ---')
for cl in classes:
    row=[]
    for wname,w in WINS.items():
        cs=[c for c in C if c[0]==cl and abs(c[3]-DC)<=w]
        row.append(min(((c[1],c[2]) for c in cs),default=None))
    print('%-24s'%cl,row)

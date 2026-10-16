# Real form over Q: z_j = x_j + i y_j, w_j = x_j - i y_j.  The equation set is closed
# under the conjugation (d <-> -d, UU^dag <-> itself^dag), so Re E and Im E generate the
# same ideal; all coefficients become rational.
import sys, sympy as sp
from peel import eqs_for
from setup import GROUPS, build, conjA
name=sys.argv[1]
basis,z,A=build(GROUPS[name],'z'); m=len(z)
w=sp.symbols(f'w0:{m}')
Ad=conjA(A,z,w)
eqs=eqs_for(A,Ad,lambda d: True)
x=sp.symbols(f'x0:{m}',real=True); y=sp.symbols(f'y0:{m}',real=True)
sub={**{z[j]:x[j]+sp.I*y[j] for j in range(m)},**{w[j]:x[j]-sp.I*y[j] for j in range(m)}}
out=set()
for e in eqs:
    e=sp.expand(e.subs(sub))
    re,im=sp.expand(sp.re(e)),sp.expand(sp.im(e))
    for p in (re,im):
        if p!=0: out.add(p)
vars_=[v for j in range(1,m) for v in (x[j],y[j])]+[x[0],y[0]]
s=lambda e: str(e).replace('**','^')
with open(f'sysR_{name}.sing','w') as f:
    f.write(f'ring r=0,({",".join(map(str,vars_))}),dp;\n')
    f.write('ideal J=\n'+',\n'.join(s(e) for e in out)+';\n')
print(name,len(out),'real eqs',len(vars_),'vars')

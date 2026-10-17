"""3D-mobile charge test: exists iff Ext^3_R(M,R) != 0 over Laurent ring (M = syndromes / im eps).
Writes one Singular file per rule and runs it."""
import sys, pickle, subprocess, time
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
W='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
RUN='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/runsing.sh'
def mono(p):  # x^{-p} * xyz
    e=[1-p[0],1-p[1],1-p[2]]
    return '*'.join(f'{v}^{k}' for v,k in zip('xyz',e) if k) or '1'
def eps_matrix(gens):
    rows=[]
    for S in gens:
        row=[]
        for part in ('z','x'):       # P_x pairs with g_z, P_z pairs with g_x
            for a in range(3):
                terms=[mono(POS[i]) for i in range(7) if (LZ if part=='z' else LX)[S[3*i+a]]]
                row.append('+'.join(terms) if terms else '0')
        rows.append(row)
    return rows
def sing_file(name, gens):
    rows=eps_matrix(gens); m=len(rows)
    ent=','.join(','.join(r) for r in rows)
    txt=f'''LIB "homolog.lib";
ring r=2,(x,y,z),dp;
option(redSB);
matrix E[{m}][6]={ent};
module N=E;
int i;
for(i=2;i<=3;i++){{
 module X=Ext_R(i,N);
 ideal a=quotient(X,freemodule(nrows(X)));
 ideal s=sat(a,x*y*z);
 s=std(s);
 print("{name} Ext^"+string(i)+" localized: dim(ann)="+string(dim(s))+"  isZero="+string(size(reduce(1,s))==0));
}}
quit;
'''
    f=W+f'mob_{name}.sing'; open(f,'w').write(txt); return f
def run(name,gens):
    t=time.time(); f=sing_file(name,gens)
    out=subprocess.run([RUN,f],stdin=subprocess.DEVNULL,capture_output=True,text=True,timeout=3000)
    print(out.stdout.strip(), out.stderr.strip()[:300], f'({time.time()-t:.1f}s)'); sys.stdout.flush()


sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import to21
def ext_test(name, gens7):
    t = time.time(); f = sing_file(name, [to21(S) for S in gens7])
    out = subprocess.run([RUN, f], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=3000)
    return out.stdout.strip().replace('\n', ' | ') + ' (%.1fs)' % (time.time() - t)

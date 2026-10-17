"""3D-mobile charge test: exists iff Ext^3_R(M,R) != 0 over Laurent ring (M = syndromes / im eps).
Writes one Singular file per rule and runs it."""
import sys, pickle, subprocess, time
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
W='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/'
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

def e(a,s): v=[0,0,0]; v[a]=s; return tuple(v)
# sanity 1: rule A (unsoldered 8x toric) -> expect Ext^3 nonzero
A=[0]*21
for a in range(3):
    for s in (1,-1): A[3*PIDX[e(a,s)]+a]=1
Bs=[]
for c in range(3):
    a,b=[k for k in range(3) if k!=c]; B=[0]*21
    for s in (1,-1): B[3*PIDX[e(a,s)]+b]=3; B[3*PIDX[e(b,s)]+a]=3
    Bs.append(tuple(B))
which=sys.argv[1:] or ['sanity','sets']
if 'sanity' in which:
    run('A_unsoldered',[tuple(A)]+Bs)
    # sanity 2: stack of 2D toric codes in xy planes (2D-mobile only) -> expect Ext^3 zero, Ext^2 nonzero
    A2=[0]*21; A2[0]=1; A2[3*PIDX[(-1,0,0)]+0]=1; A2[1]=1; A2[3*PIDX[(0,-1,0)]+1]=1
    B2=[0]*21; B2[0]=3; B2[3*PIDX[(0,1,0)]+0]=3; B2[1]=3; B2[3*PIDX[(1,0,0)]+1]=3
    run('toric2D_stack',[tuple(A2),tuple(B2)])
    # 187-family member A' = X_x(+-e_x) Y_y(+-e_y) Z_z(+-e_z)
    Ap=[0]*21
    for a in range(3):
        for s in (1,-1): Ap[3*PIDX[e(a,s)]+a]=a+1
    D=pickle.load(open(W+'B.pkl','rb')); reps,cl=D['reps'],D['cliques']; big=max(cl,key=len)
    idx=[u for u in range(len(reps)) if tuple(Ap) in reps[u][1]]
    print("A' orbit index",idx,'in 187 set:',[u in big for u in idx],'sign',[reps[u][1][tuple(Ap)] for u in idx])
    run('Aprime_187member',[tuple(Ap)])
if 'sets' in which:
    bases=pickle.load(open(W+'bases.pkl','rb'))
    for k,(c,basis) in enumerate(sorted(bases.items(),key=lambda kv:len(kv[0]))):
        if len(c)>100: continue
        run(f'set{k}_n{len(c)}',[S for _,S in basis])

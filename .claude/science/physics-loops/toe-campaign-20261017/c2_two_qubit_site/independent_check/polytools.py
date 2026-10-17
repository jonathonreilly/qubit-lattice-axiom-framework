"""Build polynomial excitation/stabilizer data for a rule (list of 7-site strings) and analyse in Singular."""
import subprocess, os, re
from orbits import site, comm, name, D
RUN='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/runsing.sh'
OPS=[1,2,4,8]  # spin X, spin Z, flav X, flav Z (single-qubit, as 4-bit labels)
def mono(v):
    # x^v0 y^v1 z^v2 with v>=0
    s=[]
    for e,c in zip(v,'xyz'):
        if e==1: s.append(c)
        elif e>1: s.append('%s^%d'%(c,e))
    return '*'.join(s) if s else '1'
def poly(terms):
    from collections import Counter
    c=Counter(terms); t=[mono(v) for v,k in c.items() if k%2]
    return '+'.join(t) if t else '0'
def eps_matrix(rule):
    # entry (g, op) = sum_r comm(op, g[r]) x^{-r}, times xyz (shift +1)
    rows=[]
    for g in rule:
        row=[]
        for op in OPS:
            row.append(poly([tuple(1-site[r][k] for k in range(3)) for r in range(7) if comm(op,g[r])]))
        rows.append(row)
    return rows
def sigma_vectors(rule):
    # symplectic vector of g: components (sx, sz, fx, fz) = sum_r bit x^{r}, times xyz
    vecs=[]
    for g in rule:
        v=[]
        for b in range(4):
            v.append(poly([tuple(1+site[r][k] for k in range(3)) for r in range(7) if g[r]>>b&1]))
        vecs.append(v)
    return vecs
def sing_header():
    return 'LIB "homolog.lib";\nring S=2,(x,y,z),dp;\noption(redSB);\n'
def local_logical_candidates(rule):
    labs=set(g[r] for g in rule for r in range(7))
    return [op for op in range(1,16) if all(comm(op,l)==0 for l in labs)]
def analyse_script(rule, extra=''):
    t=len(rule)
    E=eps_matrix(rule); V=sigma_vectors(rule)
    cands=local_logical_candidates(rule)
    s=sing_header()
    s+='matrix E[%d][4]=%s;\n'%(t,','.join(e for row in E for e in row))
    s+='module Im = module(E);\n'
    s+='module E3 = Ext_R(3, Im);\n'
    s+='ideal A3 = quotient(E3, freemodule(nrows(E3)));\n'
    s+='ideal A3s = sat(A3, x*y*z);\n'
    s+='print("EXT3ZERO "+string(size(reduce(1, std(A3s)))==0));\n'
    s+=extra
    s+='ring T=2,(w,x,y,z),dp;\n'
    s+='matrix Vm[4][%d]=%s;\n'%(t,','.join(V[j][i] for i in range(4) for j in range(t)))
    s+='module N = module(Vm), (w*x*y*z+1)*gen(1),(w*x*y*z+1)*gen(2),(w*x*y*z+1)*gen(3),(w*x*y*z+1)*gen(4);\n'
    s+='N=std(N);\n'
    for op in cands:
        vec='+'.join(['x*y*z*gen(%d)'%(b+1) for b in range(4) if op>>b&1])
        s+='print("INGROUP %d "+string(size(reduce(%s,N))==0));\n'%(op,vec)
    s+='quit;\n'
    return s
def analyse(rule,tag='a',extra=''):
    out=run(analyse_script(rule,extra),tag)
    ext=re.search(r'EXT3ZERO (\d)',out)
    ing={int(a):int(b) for a,b in re.findall(r'INGROUP (\d+) (\d)',out)}
    ll=[op for op,v in ing.items() if v==0]
    return dict(ext3zero=int(ext.group(1)) if ext else None, local_logicals=ll, out=out)
def run(script, tag):
    fn=D+'tmp_%s.sing'%tag
    open(fn,'w').write(script)
    r=subprocess.run(['bash',RUN,fn],stdin=subprocess.DEVNULL,capture_output=True,text=True,timeout=3000)
    return r.stdout+r.stderr

def laurent_mono(t):
    # x^t as w-power times monomial in ring T (w = 1/(xyz))
    m=min(0,*t); e=[a-m for a in t]
    s=mono(e)
    if m<0: s=s+'*w^%d'%(-m)
    return s
TRIPLES={'diag':[(1,-1,0),(0,1,-1),(1,1,0)],'even':[(2,0,0),(0,2,0),(0,0,2)],'unit':[(1,0,0),(0,1,0),(0,0,1)],
         'mixed':[(1,-1,0),(1,1,0),(0,0,1)]}
def syn_vec(rule, op):
    # syndrome vector (over generators) of single-site label op at origin, as Singular vector, times xyz
    comps=[poly([tuple(1-site[r][k] for k in range(3)) for r in range(7) if comm(op,g[r])]) for g in rule]
    return '['+','.join(comps)+']'
def recordfree_script(rule, ll, triples=None):
    triples=triples or TRIPLES
    t=len(rule)
    comml=[op for op in range(1,16) if all(comm(op,l)==0 for l in ll)]
    s='LIB "elim.lib";\nring T=2,(w,x,y,z),dp; option(redSB);\n'
    s+='module Fr='+','.join('(w*x*y*z+1)*gen(%d)'%(i+1) for i in range(t))+';\n'
    s+='module Im = Fr,'+','.join(syn_vec(rule,op) for op in (1,2,4,8))+'; Im=std(Im);\n'
    s+='module Rf = Fr'+''.join(','+syn_vec(rule,op) for op in comml)+'; Rf=std(Rf);\n'
    for nm,tr in triples.items():
        for k,tt in enumerate(tr):
            s+='module Q%d = std(quotient(Rf, ideal(1+%s)));\n'%(k,laurent_mono(tt))
        s+='module Qi = std(intersect(Q0,Q1,Q2));\n'
        s+='print("RF %s "+string(size(reduce(Qi,Im))==0));\n'%nm
    s+='quit;\n'
    return s
def recordfree(rule, ll, tag='rf', triples=None):
    out=run(recordfree_script(rule,ll,triples),tag)
    res=dict((a,int(b)) for a,b in re.findall(r'RF (\w+) (\d)',out))
    if len(res)!=len(triples or TRIPLES): print(out)
    return res

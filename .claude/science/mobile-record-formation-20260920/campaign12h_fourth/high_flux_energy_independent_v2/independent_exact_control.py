#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Independent PRE path control: no imported model builders or expected values.
Amplitudes are formal monomials in square roots of exact spin ladder weights.
Inner products pair equal endpoints, hence every ladder-bond exponent is even.
Replacing pairs gives rational exact expressions in n,C. Rotor sets weights=1.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import platform
import sys
import time
import sympy as sp
HERE = Path(__file__).resolve().parent
A = (0, 3, 5, 6)
EDGES = tuple((a,b) for a in range(8) for b in range(a+1,8) if (a ^ b) in (1,2,4))
EI = {e:i for i,e in enumerate(EDGES)}
V = tuple({(0,1):1,(1,3):1,(2,3):-1,(0,2):-1}.get(e,0) for e in EDGES)
N, C = sp.symbols('n C', integer=True)
Q0 = tuple(int(a in A) for a in range(8))
PSI = {(Q0, (0,)*len(EDGES)): {(): Fraction(1)}}
def addterm(out, state, mon, coefficient):
    if not coefficient:return
    target = out.setdefault(state, {})
    target[mon] = target.get(mon, 0) + coefficient
    if not target[mon]:del target[mon]
    if not target:del out[state]
def append_bond(mon, edge, offset):return tuple(sorted(mon + ((edge, offset),)))
def shifted(state, edge, k):
    q, d = state
    dd = list(d)
    bond = (edge, d[edge] + min(k,0))
    dd[edge] += k
    return tuple(dd), bond
def wcount(q):return sum(q[a] == 0 for a in A)
def gauss(state):
    q,d = state
    div=[0]*8
    for (u,v),ee in zip(EDGES,d):div[u]+=ee;div[v]-=ee
    return tuple(div) == tuple(q[i]-int(i in A) for i in range(8))
def hop(vector, target_w):
    out={}
    for state, terms in vector.items():
        q,d=state
        for e,(u,v) in enumerate(EDGES):
            for source,dest in ((u,v),(v,u)):
                if not q[source] or q[dest]:continue
                k=-q[source] if source==u else q[source]
                qq=list(q);qq[dest]=qq[source];qq[source]=0
                if wcount(qq)!=target_w:continue
                dd,bond=shifted(state,e,k)
                newstate=(tuple(qq),dd)
                assert gauss(newstate)
                for mon,coef in terms.items():addterm(out,newstate,append_bond(mon,*bond),-coef)
    return out
def birth(vector, edge, charge):
    out={};u,v=EDGES[edge]
    for state,terms in vector.items():
        q,d=state
        if q[u] or q[v]:continue
        qq=list(q);qq[u]=charge;qq[v]=-charge
        dd,bond=shifted(state,edge,charge)
        newstate=(tuple(qq),dd)
        assert gauss(newstate) and wcount(qq)==0
        for mon,coef in terms.items():addterm(out,newstate,append_bond(mon,*bond),coef)
    return out
def combine(*vectors):
    out={}
    for vector in vectors:
        for state,terms in vector.items():
            for mon,coef in terms.items():addterm(out,state,mon,coef)
    return out
def scale(vector, factor):return {s:{m:factor*c for m,c in t.items()} for s,t in vector.items()}
def dvalue(state):
    q,d=state;value=0
    for e,(u,v) in enumerate(EDGES):
        a,b=(u,v) if u in A else (v,u)
        if q[a] and not q[b]:
            k=-q[a] if a==u else q[a]
            electric=N*V[e]+d[e]
            value+=electric*(electric+k)
    return sp.expand(value)
def diagonal_d(vector):return {s:{m:c*dvalue(s) for m,c in t.items()} for s,t in vector.items()}
def inner_bonds(left,right):
    result=defaultdict(lambda:0)
    for state,lt in left.items():
        rt=right.get(state,{})
        for ml,cl in lt.items():
            for mr,cr in rt.items():
                counts=defaultdict(int)
                for b in ml+mr:counts[b]+=1
                assert all(v%2==0 for v in counts.values()),(state,ml,mr)
                paired=tuple(b for b,c in sorted(counts.items()) for _ in range(c//2))
                result[paired]+=cl*cr
    return {k:sp.expand(v) for k,v in result.items() if v!=0}
def expression(poly, rotor=False):
    value=0
    for mon,coefficient in poly.items():
        term=coefficient
        if not rotor:
            for e,l in mon:
                electric=N*V[e]+l
                term*=1-electric*(electric+1)/C
        value+=term
    return sp.factor(sp.expand(value))
def inner(left,right,rotor=False):return expression(inner_bonds(left,right),rotor)
def z(vector):return hop(hop(vector,1),2)
def h4_form(vector,rotor=False):
    # Cube C_1=0; C_0=M+D/C. M=A* A, not a scalar on outputs.
    zvec=z(vector)
    zpart=-inner(zvec,zvec,rotor)/2
    if rotor:return zpart
    return sp.factor(zpart-inner(hop(vector,1),hop(diagonal_d(vector),1))/C)
def serialize(value):
    if isinstance(value,dict):return {str(k):serialize(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [serialize(v) for v in value]
    if isinstance(value,(sp.Basic,Fraction)):return str(value)
    return value
def coefficient_at_high_flux(expr,power):
    s,x=sp.symbols('S x',positive=True)
    return sp.factor(sp.limit(expr.subs({N:x*s,C:s*(s+1)})/s**power,s,sp.oo))
def main():
    start=time.time()
    assert gauss(next(iter(PSI)))
    assert all(sum((1 if v==i else -1 if w==i else 0)*e for (v,w),e in zip(EDGES,V))==0 for i in range(8))
    av=hop(PSI,1)
    resolved={(e,c):scale(birth(av,e,c),-1) for e in range(12) for c in (1,-1)}
    coherent={e:combine(resolved[(e,1)],resolved[(e,-1)]) for e in range(12)}
    data={'edges':EDGES,'circulation':V,'input_D':dvalue(next(iter(PSI))),
          'input_Z_rotor_norm_squared':inner(z(PSI),z(PSI),True),
          'input_M_spin':inner(av,av),'input_H4_spin':h4_form(PSI),
          'input_H4_rotor':h4_form(PSI,True),'instruments':{}}
    for label,channels in [('resolved',resolved),('coherent',coherent)]:
        rotor_rate=0;spin_rate=0;rotor_gain_d=0;spin_gain_d=0;rotor_gain_h=0;spin_gain_h=0;rows=[]
        for mark,vec in channels.items():
            rate_r=inner(vec,vec,True);rate_s=inner(vec,vec)
            gain_d_r=inner(vec,diagonal_d(vec),True);gain_d_s=inner(vec,diagonal_d(vec))
            gain_h_r=h4_form(vec,True);gain_h_s=h4_form(vec)
            rotor_rate+=rate_r;spin_rate+=rate_s;rotor_gain_d+=gain_d_r;spin_gain_d+=gain_d_s
            rotor_gain_h+=gain_h_r;spin_gain_h+=gain_h_s
            rows.append({'mark':mark,'output_basis_states':len(vec),'rate_rotor':rate_r,'rate_spin':rate_s,
                         'D_gain_rotor':gain_d_r,'D_gain_spin':gain_d_s,'H4_gain_rotor':gain_h_r,'H4_gain_spin':gain_h_s})
        d0=data['input_D']
        drift_d_r=sp.factor(rotor_gain_d-rotor_rate*d0)
        drift_d_s=sp.factor(sp.expand(spin_gain_d-spin_rate*d0))
        drift_h_r=sp.factor(rotor_gain_h-rotor_rate*data['input_H4_rotor'])
        drift_h_s=sp.factor(spin_gain_h-spin_rate*data['input_H4_spin'])
        data['instruments'][label]={'rotor_rate':sp.factor(rotor_rate),'spin_rate':sp.factor(spin_rate),
            'rotor_D_gain':sp.factor(rotor_gain_d),'rotor_D_drift':drift_d_r,'spin_D_drift':drift_d_s,
            'rotor_H4_gain':sp.factor(rotor_gain_h),'rotor_H4_drift':drift_h_r,'spin_H4_drift':drift_h_s,
            'high_flux_rate':coefficient_at_high_flux(spin_rate,0),
            'high_flux_D_drift_over_S2':coefficient_at_high_flux(drift_d_s,2),
            'high_flux_H4_drift':coefficient_at_high_flux(drift_h_s,0),'marks':rows}
        print(label,'rate=',sp.factor(rotor_rate),'D drift=',drift_d_r,'H4 drift=',drift_h_r,flush=True)
        print(label,'spin rate=',sp.factor(spin_rate),'spin D drift=',drift_d_s,flush=True)
        print(label,'high-flux rate=',data['instruments'][label]['high_flux_rate'],
              'D drift / S²=',data['instruments'][label]['high_flux_D_drift_over_S2'],
              'H4 drift=',data['instruments'][label]['high_flux_H4_drift'],flush=True)
    selected={}
    for label,vec in [('resolved_plus',resolved[(EI[(0,1)],1)]),('resolved_minus',resolved[(EI[(0,1)],-1)]),
                      ('coherent',coherent[EI[(0,1)]])]:
        outcomes=[]
        for state,terms in sorted(vec.items()):
            single={state:terms}
            outcomes.append({'q':state[0],'electric_offset':state[1],'D':dvalue(state),
                             'rotor_weight':inner(single,single,True),'spin_weight':inner(single,single)})
        nr=inner(vec,vec,True);ns=inner(vec,vec)
        dr=inner(vec,diagonal_d(vec),True)/nr;ds=inner(vec,diagonal_d(vec))/ns
        varr=sp.factor(inner(diagonal_d(vec),diagonal_d(vec),True)/nr-dr**2)
        vars=sp.factor(inner(diagonal_d(vec),diagonal_d(vec))/ns-ds**2)
        selected[label]={'outcomes':outcomes,'rotor_norm_squared':nr,'spin_norm_squared':ns,
             'rotor_D_mean':sp.factor(dr),'rotor_D_variance':varr,'spin_D_mean':sp.factor(ds),
             'spin_D_variance':vars,'rotor_H4_mean':sp.factor(h4_form(vec,True)/nr),
             'spin_H4_mean':sp.factor(h4_form(vec)/ns),
             'high_flux_weight':coefficient_at_high_flux(ns,0),
             'high_flux_D_mean_over_S2':coefficient_at_high_flux(ds,2),
             'high_flux_D_variance_over_S4':coefficient_at_high_flux(vars,4)}
        print('selected',label,serialize(selected[label]),flush=True)
    data['selected_mark_01']=selected
    fixed_n_limits={label:{k:sp.factor(sp.limit(row[k],C,sp.oo)) for k in ('spin_rate','spin_D_drift','spin_H4_drift')}
                    for label,row in data['instruments'].items()}
    data['fixed_n_limits']=fixed_n_limits
    for label,row in data['instruments'].items():
        for sk,rk in [('spin_rate','rotor_rate'),('spin_D_drift','rotor_D_drift'),('spin_H4_drift','rotor_H4_drift')]:
            assert sp.simplify(fixed_n_limits[label][sk]-row[rk])==0
    data['elapsed_seconds']=time.time()-start;data['python']=sys.version;data['sympy']=sp.__version__;data['platform']=platform.platform()
    (HERE/'EXACT_RESULTS.json').write_text(json.dumps(serialize(data),indent=2)+'\n')
    print('fixed-n rotor limit identities checked; elapsed',data['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

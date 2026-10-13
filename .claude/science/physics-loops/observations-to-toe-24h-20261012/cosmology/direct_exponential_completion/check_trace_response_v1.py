#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
import sympy as s
P=Path(__file__).resolve().parent
def main():
    freeze=json.loads((P/'TRACE_RESPONSE_FREEZE_v1.json').read_text())
    for r in freeze['inputs']:assert hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
    u,x,y,pu,px,py,sig,pressure,nu=s.symbols('u x y pu px py sig pressure nu',real=True)
    coords=[u,x,y];vel=s.Matrix([pu,px,py]);t=s.exp(-u);D=1+s.Rational(2,3)*(x*x+y*y)
    g=s.Matrix([t/4,4*t/(9*D),t/(3*D)]);W=s.Rational(3,2)*(1-t)**2+t*t*(x*x/2+y*y/3+nu*u*u/2)
    B=1+s.Rational(2,3)*sig;h=-(sig+pressure)/B;T=sum(g[i]*vel[i]**2 for i in range(3))
    acc=[]
    for i in range(3):
        con=vel[i]*sum(s.diff(g[i],coords[j])*vel[j] for j in range(3))-sum(s.diff(g[j],coords[i])*vel[j]**2 for j in range(3))/2
        force=s.diff(W,coords[i])+(t*(sig-3*pressure)/2 if i==0 else 0)
        acc.append(-(3+h)*vel[i]-(con+force/B)/g[i])
    C=2*(W+sig*(1-2*t))/(3*B)+T/3+t*pu-1+t
    Cp=sum(s.diff(C,coords[i])*vel[i]+s.diff(C,vel[i])*acc[i] for i in range(3))-3*(sig+pressure)*s.diff(C,sig)
    sub={u:0,pu:0,px:-3*x/2,py:-2*y,sig:x*x+y*y};tau=y*y-3*pressure
    targets={'initial_coefficient':(C,0),'initial_u_acceleration':(acc[0],-2*tau/D),'initial_physical_coefficient_slope':(Cp,-8*tau/(3*D))}
    rows=[]
    for name,(expr,want) in targets.items():
        got=s.factor(expr.subs(sub,simultaneous=True));res=s.factor(s.together(got-want));rows.append(dict(name=name,actual=str(got),expected=str(want),residual=str(res),passed=res==0))
    assert all(x['passed'] for x in rows)
    f=P/'TRACE_RESPONSE_RESULTS_v1.json';assert not f.exists();f.write_text(json.dumps(dict(scope='Exact local response identities for the matched limiting state; no later-state or empirical assertion.',checks=rows,counts=dict(passed=len(rows),failed=0)),indent=2)+'\n');print(rows)
if __name__=='__main__':main()

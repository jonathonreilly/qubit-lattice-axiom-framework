#!/usr/bin/env python3
"""Separate predeclared fixed-state coefficient controls; no trajectory inference."""
from pathlib import Path
import hashlib, importlib.util, json, datetime
import mpmath as m
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ex_source',P/'check_exponential_v1.py')
ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
m.mp.dps=90
checks=[];rows=[]
def ck(n,v,b):
    checks.append(dict(name=n,passed=bool(abs(v)<=b),error=m.nstr(abs(v),35),bound=m.nstr(b,35)))
def calc(k,st):
    u,x,y,pu,px,py,sigma=map(m.mpf,st)
    a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));al=m.sqrt(a);E=m.exp(2*al*u);F=1+s*E
    c=dict(a=a,b=k,s=s,nu=m.mpf(1),lambda_x=(1-k)/al,lambda_y=(1+k)/al)
    K,U,B=ex.raw_mp([u,x,y],c);CB=B*B;ab=al/F;T=sum(q*v*v for q,v in zip(K,[pu,px,py]))
    hg=1+2*sigma/3;h=2*(U+CB**2*sigma/(1+k))/(3-T);hj=h*(1+ab*pu)**2/CB
    t=m.exp(-u);D=1+2*(x*x+y*y)/3;V=x*x/2+y*y/3
    W=lambda v:m.mpf('1.5')*(1-m.exp(-v))**2+m.exp(-2*v)*(V+v*v/2)
    kg=[t/4,4*t/(9*D),t/(3*D)];tb=sum(q*v*v for q,v in zip(kg,[pu,px,py]))
    C=2*(W(u)+sigma*(1-2*t))/(3*hg)+tb/3+t*pu-1+t
    uu=m.diff(lambda v:ex.raw_mp([v,x,y],c)[1],u,2)
    return dict(K=[K[i]/k-kg[i] for i in range(3)],potential=(U-m.mpf('1.5'))/k-W(u),
                coupling=(CB-1)/k-(1-t),physical=(hj/hg-1)/k-C,
                curvature=uu/K[0]-m.diff(W,u,2)/kg[0],GN=CB*(1+ab*ab/K[0])/(1+k)-1,
                C=C,actual_scaled=(hj/hg-1)/k)
def main():
    freeze=json.loads((P/'COEFFICIENT_FREEZE_v1.json').read_text())
    for z in freeze['inputs']:assert hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256']
    states=[['0','.7','.3','0','-.8','-.4','1.2'],['.2','1.1','.8','.03','-.5','-.2','2.1'],['-.3','.6','1.2','-.04','-.2','-.7','.8'],['1','.3','.7','.2','-.1','-.4','.4'],['-1','.2','.4','-.1','.2','-.3','1.3']]
    for i,st in enumerate(states):
        for ks in ['.001','.00001','.0000001']:
            k=m.mpf(ks);q=calc(k,st);tag=f'{i}.{ks}'
            for j,v in enumerate(q['K']):ck(tag+f'.K{j}',v,100*k)
            for key in ['potential','coupling','physical']:ck(tag+'.'+key,q[key],100*k)
            ck(tag+'.curvature',q['curvature'],10000*k);ck(tag+'.GN',q['GN'],100*k*k)
            rows.append(dict(state=st,k=ks,values={key:[m.nstr(v,45) for v in val] if isinstance(val,list) else m.nstr(val,45) for key,val in q.items()}))
    for z in freeze['inputs']:assert hashlib.sha256(Path(z['path']).read_bytes()).hexdigest()==z['sha256']
    out=dict(scope='Fixed bounded-state asymptotic consistency controls. Not error bounds for solutions.',rows=rows,checks=checks,counts=dict(passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks)))
    f=P/'COEFFICIENT_RESULTS_v1.json';assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(out['counts'])
if __name__=='__main__':main()

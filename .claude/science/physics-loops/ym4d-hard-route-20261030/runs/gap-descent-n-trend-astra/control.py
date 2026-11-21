#!/usr/bin/env python3
from leakage import *
# Regression on n=3 checks the extension, not new evidence for the old result.
if __name__=='__main__':
    x=point(3,2.4,2.4,10,12,32)
    data=json.loads((PREV/'leak_sweep.json').read_text())
    ref=next(y['values'][0] for y in data['grid'] if y['n']==3 and y['beta']==2.4)
    x['reference']=ref;x['difference_from_reference']=x['difference']-ref['difference']
    assert abs(x['difference_from_reference'])<1e-10,x
    # Compare streamed and full tensor contractions directly, n=4 tiny cutoff.
    A,Q,n=3,9,4;theta=np.arange(1,Q+1)*np.pi/(Q+1)
    chi=np.sin(np.arange(1,Q+1)[:,None]*theta)/np.sin(theta)
    V=(np.sqrt(2/(Q+1))*np.sin(theta)*chi[:A]).T
    r=base.ratios(2.4,Q);Z=(chi.T*r[:Q]**4)@chi;e=np.exp(2.4*(np.cos(theta)-1))
    v=np.sin(np.arange(A**n)+.2).reshape((A,)*n);errs=[]
    for omit in [-1,0,1,2]:
        F=np.ones((Q,)*n)
        for a in range(n):F*=e.reshape((1,)*a+(Q,)+(1,)*(n-a-1))
        for a in range(n-1):
            if a!=omit:F*=Z.reshape((1,)*a+(Q,Q)+(1,)*(n-a-2))
        target=prior.transform(F*prior.transform(v,V),V.T)
        errs.append(float(np.max(np.abs(chain(v,V,e,Z,omit)-target))))
    assert max(errs)<1e-12,errs
    x['streamed_contraction_errors']=errs
    Path(__file__).with_suffix('.json').write_text(json.dumps(x,indent=2)+'\n')
    print(json.dumps(x),flush=True)

#!/usr/bin/env python3
"""Exact finite checks of fixed-order local sampling and sign cancellation.

Target real Gaussians; arbitrary local conditional densities are handled by
the separate KL chain-rule proof. No native schedule or latent-message no-go.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
import json
from pathlib import Path
import sympy as s


def cycle(n,frustrated=False):
    q=3*s.eye(n)
    edges=set()
    for j in range(n):
        k=(j+1)%n
        value=1 if frustrated and j==n-1 else -1
        q[j,k]=q[k,j]=value
        edges.add(frozenset((j,k)))
    return q,edges


class Gaussian:
    def __init__(self,q,edges):
        self.q=q
        self.c=q.inv()
        self.n=q.rows
        self.edges=edges
        assert all(q[:j,:j].det()>0 for j in range(1,self.n+1))

    @lru_cache(None)
    def conditional(self,v,past):
        if not past:
            return s.zeros(1,0),self.c[v,v]
        row=self.c.extract([v],past)*self.c.extract(past,past).inv()
        variance=self.c[v,v]-(row*self.c.extract(past,[v]))[0]
        return row,variance

    @lru_cache(None)
    def marginal_precision(self,subset):
        future=tuple(i for i in range(self.n) if i not in subset)
        if not future:
            return self.q.extract(subset,subset)
        return (self.q.extract(subset,subset)-self.q.extract(subset,future)*
                self.q.extract(future,future).inv()*self.q.extract(future,subset))

    def evaluate(self,order,full_check=True):
        regression=s.zeros(self.n)
        noise=s.zeros(self.n)
        ratio=s.Integer(1)
        failures=[]
        stages=[]
        for index,v in enumerate(order):
            past=tuple(order[:index])
            parents=tuple(u for u in past if frozenset((u,v)) in self.edges)
            full_row,full_var=self.conditional(v,past)
            local_row,local_var=self.conditional(v,parents)
            ratio*=local_var/full_var
            for j,u in enumerate(parents):
                regression[v,u]=local_row[j]
            noise[v,v]=local_var
            prefix=past+(v,)
            marginal=self.marginal_precision(prefix)
            assert full_var==1/marginal[-1,-1]
            for j,u in enumerate(past):
                assert full_row[j]==-marginal[-1,j]/marginal[-1,-1]
                if u not in parents and full_row[j]!=0:
                    failures.append(dict(site=v,past_nonneighbor=u,coefficient=str(full_row[j])))
            stages.append(dict(site=v,parents=parents,full_variance=str(full_var),
                               local_variance=str(local_var),full_regression=[str(x) for x in full_row]))
        ratio=s.factor(ratio)
        assert ratio>=1
        assert (ratio==1)==(len(failures)==0)
        if full_check:
            inverse=(s.eye(self.n)-regression).inv()
            generated=inverse*noise*inverse.T
            assert s.factor(generated.det()/self.c.det())==ratio
            assert s.trace(generated.inv()*self.c)==self.n
            assert (generated==self.c)==(ratio==1)
        return dict(order=order,exp_twice_minimum_kl=str(ratio),missing_past=failures,stages=stages)


def main():
    attractive=Gaussian(*cycle(4))
    signed=Gaussian(*cycle(4,True))
    results={}
    for label,model in [('attractive_cycle4',attractive),('frustrated_cycle4',signed)]:
        cases=[model.evaluate(order) for order in permutations(range(4))]
        counts=Counter(row['exp_twice_minimum_kl'] for row in cases)
        results[label]=dict(precision=[[str(x) for x in model.q.row(j)] for j in range(4)],
                            covariance=[[str(x) for x in model.c.row(j)] for j in range(4)],
                            ratio_counts=dict(counts),cases=cases)
    assert results['attractive_cycle4']['ratio_counts']=={'64/63':16,'49/45':8}
    assert results['frustrated_cycle4']['ratio_counts']=={'64/63':16,'1':8}
    witness=attractive.evaluate((0,1,2,3))
    assert witness['stages'][2]['full_regression']==['1/8','3/8']
    assert witness['stages'][2]['full_variance']=='3/8'
    assert signed.evaluate((0,2,1,3))['exp_twice_minimum_kl']=='1'

    # Independently write the signed-cycle sampler instead of reusing the
    # covariance regression helper or numerical elimination.
    a=s.zeros(4)
    a[1,0]=a[1,2]=a[3,2]=s.Rational(1,3)
    a[3,0]=-s.Rational(1,3)
    noise=s.diag(s.Rational(3,7),s.Rational(1,3),s.Rational(3,7),s.Rational(1,3))
    generated=(s.eye(4)-a).inv()*noise*(s.eye(4)-a).T.inv()
    assert generated==signed.c
    assert (s.eye(4)-a).T*noise.inv()*(s.eye(4)-a)==signed.q
    results['signed_sampler']=dict(regression=[[str(x) for x in a.row(j)] for j in range(4)],
                                   noise_variances=[str(noise[j,j]) for j in range(4)],
                                   exact_covariance_match=True)
    extra=[]
    for n in (5,6):
        model=Gaussian(*cycle(n))
        counts=Counter(model.evaluate(order,False)['exp_twice_minimum_kl']
                       for order in permutations(range(n)))
        assert '1' not in counts
        extra.append(dict(cycle_length=n,orders=sum(counts.values()),
                          minimum_ratio=str(min(s.Rational(x) for x in counts)),
                          ratio_counts=dict(counts)))
    results['longer_attractive_cycles']=extra
    results['scope']='fixed order and raw target scalar histories; messages, adaptive schedules, joint writes and native law selection not excluded'
    Path(__file__).with_name('BLOCK5_GAUSSIAN_ORDER_CHECK.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in results.items()},indent=2))


if __name__=='__main__':
    main()

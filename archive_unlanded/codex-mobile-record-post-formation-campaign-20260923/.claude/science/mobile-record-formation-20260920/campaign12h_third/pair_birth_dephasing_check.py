#!/usr/bin/env python3
"""Exact finite controls for occupation monitoring and pair-birth completion.

The all-finite-graph proof is analytic in the companion note. This runner
checks a complete four-site model and a symbolic two-vacancy waiting time.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json
import sympy as s
from sympy.polys.domains import QQ_I

HERE=Path(__file__).resolve().parent
EDGES=[(0,1),(1,2),(2,3),(0,3)]


def hopping(basis,kappa):
    where={z:i for i,z in enumerate(basis)};H=s.zeros(len(basis))
    for j,z in enumerate(basis):
        for a,b in EDGES:
            if ((z>>a)&1)!=((z>>b)&1):
                H[where[z^(1<<a)^(1<<b)],j]+=kappa
    return H


def symbolic_waiting_time():
    k,b,d=s.symbols('kappa beta d',positive=True,real=True)
    basis=[z for z in range(16) if z.bit_count()==2]
    H=hopping(basis,k)
    adjacent=lambda z:any(z==(1<<a)+(1<<bb) for a,bb in EDGES)
    O=[i for i,z in enumerate(basis) if not adjacent(z)]
    A=[i for i,z in enumerate(basis) if adjacent(z)]
    assert len(O)==2 and len(A)==4
    Gamma=s.diag(*(b*int(adjacent(z)) for z in basis))
    dark=s.zeros(6,1);dark[O[0]]=1;dark[O[1]]=-1
    rho0=dark*dark.T/2
    assert H*dark==s.zeros(6,1) and Gamma*dark==s.zeros(6,1)
    integrated_y=1/(16*k)
    integrated_a=1/(4*b)
    integrated_c=-1/(2*d)
    integrated_q=1/(4*(b+d))
    integrated_r=1/(4*(b+2*d))
    integrated_o=-integrated_c+integrated_a+2*integrated_q+integrated_r+(d+b/2)/(16*k*k)
    X=s.zeros(6)
    for i,zi in enumerate(basis):
        for j,zj in enumerate(basis):
            if i in O and j in O:
                X[i,j]=integrated_o if i==j else integrated_c
            elif i in A and j in A:
                X[i,j]=integrated_a if i==j else integrated_q if zi&zj else integrated_r
            elif i in O:
                X[i,j]=s.I*integrated_y
            else:
                X[i,j]=-s.I*integrated_y
    derivative=-s.I*(H*X-X*H)-(Gamma*X+X*Gamma)/2
    for site in range(4):
        q=s.diag(*((z>>site)&1 for z in basis))
        derivative+=d*(q*X*q-(q*X+X*q)/2)
    residual=(derivative+rho0).applyfunc(s.factor)
    assert residual==s.zeros(6)
    mean=1/d+3/(2*b)+1/(b+d)+1/(2*(b+2*d))+(2*d+b)/(16*k*k)
    assert s.factor(s.trace(X)-mean)==0
    assert mean.subs({k:1,b:1,d:1})==s.Rational(161,48)
    assert s.limit(d*mean,d,0,dir='+')==1
    assert s.limit(mean/d,d,s.oo)==1/(8*k*k)
    assert s.limit(mean/b,b,s.oo)==1/(16*k*k)
    return dict(holes_basis=basis,opposite_pair_indices=O,
                mean_from_dark_state=str(mean),at_unit_parameters='161/48',
                complete_symbolic_transient_density_equation_exact=True,
                small_d_times_mean='1',large_d_mean_over_d='1/(8*kappa^2)',
                large_beta_mean_over_beta='1/(16*kappa^2)',
                conditions='H_0=0; kappa>0, beta>0, d>0; pair birth beta on every cycle edge; local dephasing d at every site')


def finite_stationarity():
    basis=[z for z in range(16) if z.bit_count()%2==0]
    where={z:i for i,z in enumerate(basis)};I=s.eye(len(basis));Q=s.diag(*(z.bit_count() for z in basis))
    Pfull=s.zeros(len(basis));Pfull[where[0],where[0]]=1
    results=[]
    for name,kappa,d,edges in [('all_birth_with_monitoring',1,1,EDGES),
                              ('all_birth_without_monitoring',1,0,EDGES),
                              ('one_birth_source_with_monitoring',1,1,EDGES[:1]),
                              ('no_birth',1,1,[]),('no_hopping',0,1,EDGES)]:
        H=hopping(basis,kappa)
        assert H*Q==Q*H
        L=-s.I*(s.kronecker_product(I,H)-s.kronecker_product(H.T,I))
        for a,b in edges:
            B=s.zeros(len(basis));mask=(1<<a)+(1<<b)
            for j,z in enumerate(basis):
                if z&mask==mask:B[where[z^mask],j]=1
            assert Q*B-B*Q==-2*B
            K=B.T*B
            L+=s.kronecker_product(B,B)-(s.kronecker_product(I,K)+s.kronecker_product(K.T,I))/2
        for site in range(4):
            q=s.diag(*((z>>site)&1 for z in basis))
            assert q*Q==Q*q
            L+=d*(s.kronecker_product(q,q)-(s.kronecker_product(I,q)+s.kronecker_product(q.T,I))/2)
        assert L*Pfull.vec()==s.zeros(len(basis)**2,1)
        assert (I.vec().T*L)==s.zeros(1,len(basis)**2)
        # Work over the exact Gaussian rationals; generic symbolic elimination
        # is unnecessary and was archived after a performance interruption.
        nullity=L.rows-L.to_DM().convert_to(QQ_I).rank()
        results.append(dict(case=name,kappa=kappa,d=d,birth_edges=edges,
                            Hilbert_even_parity_dimension=len(basis),Liouville_dimension=L.rows,
                            exact_stationary_operator_nullity=nullity,
                            full_occupation_stationary=True,trace_preservation_exact=True))
    expected=[1,4,1,3,3]
    assert [r['exact_stationary_operator_nullity'] for r in results]==expected
    return results


def main():
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                status='author_exact_finite_controls_independent_check_pending',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                symbolic_waiting=symbolic_waiting_time(),stationarity=finite_stationarity(),
                scope='Complete four-site even-hole sector and exact all-positive-parameter two-vacancy waiting time. General graph convergence is a separate analytic theorem; no thermodynamic or native-law claim.')
    encoded=json.dumps(result,indent=2)+'\n';(HERE/'PAIR_BIRTH_DEPHASING_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()

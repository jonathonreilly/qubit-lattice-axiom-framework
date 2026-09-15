"""Exact source identities and separate symmetric-tensor rank checks.

The geometry bundle is passed by the primary runner. Only this source is read
for an integrity hash; no mutable external scientific data is loaded.
"""
from __future__ import annotations
import json,hashlib,time
from pathlib import Path
import sympy as s
AUDIT_TIMEOUT_SEC = 180

def run(m):
    started=time.monotonic()
    Q,w,z,p,sets,E,C,G=m.Q,m.w,m.z,m.p,m.sets,m.E,m.C,m.G
    zero=lambda A: all(s.cancel(s.expand(x))==0 for x in A)
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    static={w[3]:1}; nu=s.Symbol('nu',real=True)
    qnu=s.Matrix([(int(3 in A)-nu*len(A-{3}))*(1+s.prod(z[a] for a in A)) for A in sets])
    qnu=qnu.subs(static); Qs=Q.subs(static); Cs=C.subs(static); ps=p.subs(static)
    Es=[h.subs(static) for h in E]; lap=s.expand(ps.dot(ps))
    Hnu=sum((Es[i]*qnu[i] for i in range(15)),s.zeros(4))
    uvec=s.Matrix([-nu*w[0]/2,-nu*w[1]/2,-nu*w[2]/2,s.Rational(1,2)])
    check('all_phase_exponent_body',zero(Cs*qnu))
    check('all_phase_exponent_gauge',zero(Hnu-s.diag(-2*nu,-2*nu,-2*nu,2)-s.I*(ps*uvec.T+uvec*ps.T)))
    T=s.zeros(4); T[3,3]=-nu*lap
    for a in range(3):
        for b in range(3):T[a,b]=(1-nu)*(lap*int(a==b)-ps[a]*ps[b])/2
    J=s.Matrix([s.trace(h.applyfunc(m.minus)*T) for h in Es])
    check('geometric_all_phase_exponent_source',zero(Qs*qnu-J))
    e_tau=s.zeros(15,1);e_tau[m.idx[frozenset((3,))]]=1
    check('geometric_all_phase_static_poisson',zero(Qs*qnu.subs(nu,1)+lap*e_tau))
    check('wrong_poisson_sign_rejected',not zero(Qs*qnu.subs(nu,1)-lap*e_tau))
    check('constant_mode_any_exponent',zero(Qs.subs({x:1 for x in w[:3]})*qnu.subs({x:1 for x in w[:3]})))

    phi=s.Matrix(1,15,lambda a,i:Es[i][3,3]/2)
    Psp=s.eye(3)-ps[:3,0]*ps[:3,0].T/lap
    psi=s.Matrix(1,15,lambda a,i:-s.trace(Psp*Es[i][:3,:3])/4)
    Gs=G.subs(static)
    check('phi_gauge_annihilation_all_phases',zero(phi*Gs))
    check('psi_gauge_annihilation_all_phases',zero(psi*Gs))
    check('phi_endpoint_mean',zero(phi*qnu.subs(nu,1)-s.ones(1)))
    check('psi_endpoint_mean',zero(psi*qnu.subs(nu,1)-s.ones(1)))
    check('hyperdiagonal_readout_zero',phi[0,14]==0 and psi[0,14]==0)
    for a in range(3):
        check('scalar_seam_periodicity_'+str(a),zero(psi.subs(w[a],-w[a])-psi))

    fixtures=[('origin',[1,1,1,1],4),
              ('static_axis_nyquist',[s.I,1,1,1],10),
              ('static_two_components',[s.I,s.Rational(3,5)+s.I*s.Rational(4,5),1,1],10),
              ('complex_axis_shell',[s.I,1,1,s.sqrt(2)-1],8),
              ('complex_axis_off_shell',[s.I,1,1,s.Rational(1,2)],10)]
    ranks=[]
    for name,values,expected in fixtures:
        sub=dict(zip(w,values))
        matrix=Q.subs(sub).applyfunc(s.simplify)
        rank=matrix.rank()
        check('exact_rank_'+name,rank==expected)
        ranks.append({'fixture':name,'rank':rank,'expected':expected})

    # Direct symmetric-matrix operator: no edge map or geometric Hessian used here.
    def F(v,H):
        d=(v.T*v)[0];u=H*v;t=s.trace(H)
        return d*H-v*u.T-u*v.T+(v*v.T)*t+s.eye(4)*((v.T*H*v)[0]-d*t)
    components=[(a,a) for a in range(4)]+list(__import__('itertools').combinations(range(4),2))
    basis=[]
    for a,b in components:
        h=s.zeros(4);h[a,b]=h[b,a]=1;basis.append(h)
    for name,v,rank in [('nonnull',s.Matrix([1,2,0,0]),6),('null',s.Matrix([1,0,0,s.I]),4)]:
        mat=s.Matrix(10,10,lambda i,j:F(v,basis[j])[components[i]])
        check('direct_fierz_operator_rank_'+name,mat.rank()==rank)
        for a in range(4):
            u=s.eye(4)[:,a]
            check('direct_fierz_gauge_'+name+'_'+str(a),F(v,v*u.T+u*v.T)==s.zeros(4))

    v=s.Matrix([2,0,0,0]);d=4;Pi=s.eye(4)-v*v.T/d
    T=s.Matrix([[0,0,0,0],[0,1,2,3],[0,2,-1,4],[0,3,4,5]])
    U=s.Matrix([[0,0,0,0],[0,2,1,-2],[0,1,3,1],[0,-2,1,4]])
    def sol(A):return -4*(A-Pi*s.trace(A)/2)/d
    HT,HU=sol(T),sol(U)
    check('source_inverse_normalization',-F(v,HT)/4==T)
    check('source_reciprocity',s.trace(U*HT)==s.trace(T*HU))
    # Verify tensor off-diagonal factor on the actual q-source lift.
    sub={w[0]:s.I,w[1]:1,w[2]:1,w[3]:1}
    edgeJ=s.Matrix([s.trace(h.applyfunc(m.minus)*T) for h in E]).subs(sub)
    wrongT=T.copy()
    for a in range(4):
        for b in range(4):
            if a!=b:wrongT[a,b]/=2
    wrongJ=s.Matrix([s.trace(h.applyfunc(m.minus)*wrongT) for h in E]).subs(sub)
    check('missing_offdiagonal_source_factor_rejected',edgeJ!=wrongJ)

    out={'status':'passed','scope':'exact Laurent static identities and finite algebraic rank fixtures; same author, no physical graviton conclusion',
         'checks':checks,'count':len(checks),'rank_fixtures':ranks,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'elapsed_sec':time.monotonic()-started}

    return out

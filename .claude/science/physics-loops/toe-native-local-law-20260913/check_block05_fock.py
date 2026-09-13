"""Small Fock-space and native Pauli-word challenges for BLOCK05.

The finite interacting ground-state checks do not establish an interacting
thermodynamic response. Couplings outside the small-coupling theorem's
unknown interval are merely declared finite test cases.
"""
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic()
    checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        d=a-b
        vals=list(d) if isinstance(d,s.MatrixBase) else [d]
        check(name,all(s.simplify(x)==0 for x in vals))
    def near(name,a,b,tol=2e-9):
        residual=float(np.max(abs(np.asarray(a)-np.asarray(b))))
        check(name,residual<tol,max_residual=residual,tolerance=tol)
    c=[]
    for j in range(6):
        a=s.zeros(64)
        for word in range(64):
            if word&(1<<j):
                a[word^(1<<j),word]=(-1)**((word&((1<<j)-1)).bit_count())
        c.append(a)
    ident=s.eye(64)
    occ=[a.H*a for a in c]
    sigma1=s.Matrix([[0,1],[1,0]])
    sigma3=s.diag(1,-1)
    hop=(-sigma3+s.I*sigma1)/2
    bonds=[]
    for x in range(2):
        bond=s.zeros(64)
        for i in range(2):
            for j in range(2):
                term=hop[i,j]*c[2*x+i].H*c[2*(x+1)+j]
                bond+=term+term.H
        bonds.append(bond)
    lam=s.symbols('lam',real=True)
    ox=[s.Rational(5,2)*(occ[2*x]-occ[2*x+1])
        +lam*(occ[2*x]-ident/2)*(occ[2*x+1]-ident/2) for x in range(3)]
    hx=[o+sum((bonds[j]/2 for j in range(2) if x in(j,j+1)),s.zeros(64))
        for x,o in enumerate(ox)]
    ham=sum(hx,s.zeros(64))
    totaln=sum(occ,s.zeros(64))
    eq('exact_interacting_number_conservation',ham*totaln,totaln*ham)
    eq('exact_local_energy_continuity',
       s.I*(ham*hx[0]-hx[0]*ham)
       +sum((s.I*(hx[0]*hx[y]-hx[y]*hx[0]) for y in(1,2)),s.zeros(64)),s.zeros(64))
    check('current_is_nonzero',hx[0]*hx[1]-hx[1]*hx[0]!=s.zeros(64))
    results=[]
    sector=[word for word in range(64) if word.bit_count()==3]
    check('declared_three_particle_sector',len(sector)==20)
    for strength in(-20,-5,-1,-.2,0,.2,1,5,20):
        op=[np.array(o.subs(lam,strength).extract(sector,sector),complex) for o in ox]
        bb=[np.array(b.extract(sector,sector),complex) for b in bonds]
        hh=sum(op)+sum(bb)
        values,vectors=np.linalg.eigh(hh)
        check('finite_many_body_gap_'+str(strength),values[1]-values[0]>1e-6,
              gap=float(values[1]-values[0]))
        ground=vectors[:,0]
        energies=[a+sum((bb[j]/2 for j in range(2) if x in(j,j+1)),np.zeros_like(a))
                  for x,a in enumerate(op)]
        off=np.array([vectors[:,1:].conj().T@h@ground for h in energies])
        chi=-2*np.einsum('xi,yi,i->xy',off.conj(),off,1/(values[1:]-values[0])).real
        bmean=[float(np.vdot(ground,b@ground).real) for b in bb]
        contact=np.zeros((3,3))
        for x,b in enumerate(bmean):
            v=np.zeros(3)
            v[x],v[x+1]=1,-1
            contact-=b*np.outer(v,v)/4
        cc=chi+contact
        near('interacting_arithmetic_uniform_null_'+str(strength),chi@np.ones(3),np.zeros(3))
        check('interacting_arithmetic_sign_'+str(strength),np.max(np.linalg.eigvalsh(chi))<1e-10)
        direction=np.array([1.,-2.,1.])
        # The preserved 45-digit convergence diagnosis resolves the first
        # lambda=-20 failure as the five-point formula's O(step^4) error.
        step=.0005 if abs(strength)>=10 else .001
        record={'lambda':strength,'gap':float(values[1]-values[0]),
                'ground_number':float(np.vdot(ground,np.array(totaln.extract(sector,sector),float)@ground).real),
                'chiA_direction':float(direction@chi@direction),
                'chiC_direction':float(direction@cc@direction),'bond_energy':bmean}
        for kind,target in(('A',chi),('C',cc)):
            es={}
            for n in(-2,-1,0,1,2):
                N=1+n*step*direction
                factors=[(N[x]+N[x+1])/2 if kind=='A' else np.sqrt(N[x]*N[x+1]) for x in range(2)]
                hn=sum(N[x]*op[x] for x in range(3))+sum(factors[x]*bb[x] for x in range(2))
                e=np.linalg.eigvalsh(hn)[0]
                es[n]=e
            second=(-es[2]+16*es[1]-30*es[0]+16*es[-1]-es[-2])/(12*step**2)
            predicted=direction@target@direction
            near('actual_interacting_energy_curvature_'+kind+'_'+str(strength),
                 second,predicted,tol=2e-6)
        results.append(record)
        if strength==.2:
            check('interacting_response_is_exercised',record['chiA_direction']<-.001)

    # Exact symplectic Pauli words on a 4-by-2 rectangle. Every edge is a
    # physical edge qubit; this is a small literal carrier, not CAR matrices.
    vertices=[(x,y) for x in range(4) for y in range(2)]
    edges=[]
    for v in vertices:
        for delta in((1,0),(0,1)):
            w=(v[0]+delta[0],v[1]+delta[1])
            if w in vertices:
                edges.append(tuple(sorted((v,w))))
    edges.sort()
    ei={e:i for i,e in enumerate(edges)}
    incident={v:sorted([e for e in edges if v in e]) for v in vertices}
    # Ignore the scalar phase for commutation; X and Z masks suffice.
    def mul(a,b):
        return a[0]^b[0],a[1]^b[1]
    def commute(a,b):
        return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0
    def edgeword(v,w):
        e=tuple(sorted((v,w)))
        z=0
        for endpoint in(v,w):
            for f in incident[endpoint]:
                if f<e:
                    z^=1<<ei[f]
        return 1<<ei[e],z
    def parity(v):
        return 0,sum(1<<ei[e] for e in incident[v])
    candidates=[e for e in edges if e[0][0]==e[1][0] and e[0][0]%2==1]
    protected=[e for e in edges if e not in candidates]
    cycles=[]
    for x in range(3):
        path=[(x,0),(x+1,0),(x+1,1),(x,1),(x,0)]
        word=(0,0)
        for v,w in zip(path,path[1:]):
            word=mul(word,edgeword(v,w))
        cycles.append(word)
    generators=[edgeword(*e) for e in protected]+[parity(v) for v in vertices]
    for i,a in enumerate(generators):
        check('native_generator_cycle_centrality_'+str(i),all(commute(a,c) for c in cycles))
        check('native_generator_candidate_Z_'+str(i),
              all(commute(a,(0,1<<ei[e])) for e in candidates))
    check('two_literal_candidate_record_edges',len(candidates)==2)
    # A missed direct candidate would be rejected by its own Z commutator.
    check('candidate_hopping_negative_control',
          all(not commute(edgeword(*e),(0,1<<ei[e])) for e in candidates))
    eq('native_quartic_identity',
       (1-2*s.symbols('n0'))*(1-2*s.symbols('n1'))/4,
       (s.symbols('n0')-s.Rational(1,2))*(s.symbols('n1')-s.Rational(1,2)))

    out={'status':'PASS','checks':len(checks),'details':checks,
         'finite_interacting_probes':results,
         'elapsed_seconds':time.monotonic()-start,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Finite three-cell, three-particle-sector author checks; large couplings are outside any claimed Weyl RG interval. No interacting thermodynamic convexity, infrared coefficient or quantum gravity claimed.'}
    (HERE/'BLOCK05_FOCK_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2))


if __name__=='__main__':
    run()

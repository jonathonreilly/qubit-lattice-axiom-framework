#!/usr/bin/env python3
"""Exact local coefficient assembly, axial necessary subsystem; not full closure.

See ../NONLINEAR_CONTRACT.md. No production science runner is imported.
Sparse dictionaries use integer positions on the infinite lattice, not a torus.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
import json
import os
from pathlib import Path
import time

for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')


def budget():
    deadline = json.loads((RUNTIME / 'DEADLINE.json').read_text())['deadline_epoch']
    if time.time() >= deadline or (RUNTIME / 'STOP_REQUESTED.json').exists():
        raise RuntimeError('Campaign stop/deadline: preserve current partial evidence')


# A variable is (kind, component, integer position). h,p components 0,1,2.
def v(kind, component=0, pos=0):
    return kind, component, pos


def canon(mon):
    """A translation class of a complete globally summed monomial."""
    if not mon:
        return ()
    offset = min(a[2] for a in mon)
    return tuple(sorted((kind, comp, pos-offset) for kind, comp, pos in mon))


def poly(terms):
    out = defaultdict(Q)
    for coeff, mon in terms:
        out[tuple(sorted(mon))] += Q(coeff)
    return {k: c for k, c in out.items() if c}


def translated(mon, shift):
    return tuple((kind, comp, pos+shift) for kind, comp, pos in mon)


def bracket(f, g):
    """{sum_trans f,sum_trans g}; align each conjugate differentiated slot.

    Iteration over repeated factors supplies their derivative multiplicities.
    The one surviving common translation is quotiented by canon.
    """
    out = defaultdict(Q)
    for fm, fc in f.items():
        for gm, gc in g.items():
            for i, a in enumerate(fm):
                if a[0] not in ('h', 'p'):
                    continue
                for j, b in enumerate(gm):
                    if a[1] != b[1] or (a[0], b[0]) not in (('h','p'), ('p','h')):
                        continue
                    sign = 1 if a[0] == 'h' else -1
                    shift = a[2]-b[2]
                    key = canon(fm[:i]+fm[i+1:]+translated(gm[:j]+gm[j+1:], shift))
                    out[key] += sign*fc*gc
    return {k: c for k, c in out.items() if c}


def rename(f, a, b):
    return poly((c, tuple((b if t == a else t, comp, pos) for t,comp,pos in m))
                for m,c in f.items())


def add(*pieces):
    out = defaultdict(Q)
    for factor, f in pieces:
        for m, c in f.items():
            out[m] += factor*c
    return {m:c for m,c in out.items() if c}


def quotient(f):
    out = defaultdict(Q)
    for m,c in f.items():
        out[canon(m)] += c
    return {m:c for m,c in out.items() if c}


def remove_smearing(f, kind):
    return quotient(poly((c, tuple(a for a in m if a[0] != kind)) for m,c in f.items()))


def smear_f0(g):
    """Substitute X_s = N_s M_(s+1)-M_s N_(s+1) in G."""
    out = []
    for m,c in g.items():
        x, = [a for a in m if a[0] == 'X']
        rest = tuple(a for a in m if a[0] != 'X')
        pos = x[2]
        out.extend(((c, rest+(v('N',pos=pos),v('M',pos=pos+1))),
                    (-c, rest+(v('M',pos=pos),v('N',pos=pos+1)))))
    return quotient(poly(out))


def c1(kind):
    return poly((4*c, (v(kind),v('h',i,pos)))
                for i in (1,2) for pos,c in ((-1,1),(0,-2),(1,1)))


def t2(kind):
    return poly([(Q(1,8),(v(kind),v('p',i),v('p',i))) for i in range(3)] +
                [(Q(-1,4),(v(kind),v('p',i),v('p',j)))
                 for i in range(3) for j in range(i+1,3)])


def g1(kind='X'):
    return poly(((2,(v(kind),v('p',0))),(-2,(v(kind),v('p',0,1)))))


def continuum_t3():
    # (2 sum h_i P_i^2 - trP sum h_i P_i
    #  - trh/2*(sum P_i^2 - (trP)^2/2))/4.
    terms = []
    for i in range(3):
        terms.append((Q(1,2),(v('h',i),v('p',i),v('p',i))))
        for j in range(3):
            terms.append((Q(-1,4),(v('h',i),v('p',i),v('p',j))))
            terms.append((Q(-1,8),(v('h',i),v('p',j),v('p',j))))
            for k in range(3):
                terms.append((Q(1,16),(v('h',i),v('p',j),v('p',k))))
    return poly(terms)


class System:
    def __init__(self):
        self.names = []
        self.rows = defaultdict(dict)
        self.rhs = {}

    def new(self, name):
        self.names.append(name)
        return len(self.names)-1

    def put(self, family, mon, col, val):
        if val:
            key = (family, mon)
            self.rows[key][col] = self.rows[key].get(col,Q(0))+val
            if not self.rows[key][col]:
                del self.rows[key][col]

    def putpoly(self, family, f, col, factor=1):
        for mon,c in f.items():
            self.put(family, mon, col, factor*c)

    def target(self, family, mon, val):
        key = (family,mon)
        self.rows[key]  # include zero-left rows
        self.rhs[key] = Q(val)

    def save(self,path):
        ordered = sorted(self.rows, key=repr)
        payload = {'columns':self.names,'rows':[
            {'id':i,'key':repr(k),'coefficients':[[j,str(c)] for j,c in sorted(self.rows[k].items())],
             'rhs':str(self.rhs.get(k,Q(0)))} for i,k in enumerate(ordered)]}
        path.write_text(json.dumps(payload,separators=(',',':'))+'\n')
        return payload


def assemble(radius=1, continuum=True, mixed=False):
    budget()
    s = System()
    hs = [v('h',i,x) for i in range(3) for x in range(-radius,radius+1)]
    ps = [v('p',i,x) for i in range(3) for x in range(-radius,radius+1)]
    eh = [v('h',i,x) for i in range(3) for x in range(1-radius,radius+1)]
    ep = [v('p',i,x) for i in range(3) for x in range(1-radius,radius+1)]
    # V2: every unordered pair, arbitrary N-density, no IBP deletion.
    for mon in combinations_with_replacement(hs,2):
        col = s.new('V2:'+repr(mon))
        f = poly(((1,(v('N'),)+mon),))
        cc = add((1,bracket(f,t2('M'))),(1,bracket(t2('N'),rename(f,'N','M'))))
        s.putpoly('CC2',cc,col)
        s.putpoly('uniform_V2',remove_smearing(f,'N'),col)
        if mixed:
            s.putpoly('GC1',bracket(g1(),f),col)
    uniform = poly((c,(v('h',1,x),v('h',2,y)))
                   for x,cx in ((0,-1),(1,1)) for y,cy in ((0,-1),(1,1))
                   for c in (-2*cx*cy,))
    for mon,c in quotient(uniform).items():
        s.target('uniform_V2',mon,c)
    # T3: h times an arbitrary unordered pair of momenta.
    for h in hs:
        for pair in combinations_with_replacement(ps,2):
            mon = (h,)+pair
            col = s.new('T3:'+repr(mon))
            f = poly(((1,(v('N'),)+mon),))
            cc = add((1,bracket(c1('N'),rename(f,'N','M'))),(1,bracket(f,c1('M'))))
            s.putpoly('CC2',cc,col)
            if continuum:
                m = tuple(sorted((a,b,0) for a,b,_ in mon))
                s.put('continuum_T3',m,col,Q(1))
    if continuum:
        for mon,c in continuum_t3().items():
            s.target('continuum_T3',mon,c)
    # G2 density anchored on the x+1/2 bond.
    for h,p in product(eh,ep):
        col = s.new('G2:'+repr((h,p)))
        f = poly(((1,(v('X'),h,p)),))
        s.putpoly('CC2',smear_f0(f),col,-1)
        if mixed:
            s.putpoly('GC1',bracket(f,c1('N')),col)
            gg = add((1,bracket(g1(),rename(f,'X','Y'))),
                     (1,bracket(f,g1('Y'))))
            s.putpoly('GG1',gg,col)
        if continuum:
            comp = (h[1],p[1])
            s.put('continuum_G2_0',comp,col,Q(1))
            s.put('continuum_G2_dh',comp,col,Q(2*h[2]-1,2))
            s.put('continuum_G2_dp',comp,col,Q(2*p[2]-1,2))
    if continuum:
        for i,j in product(range(3), repeat=2):
            s.target('continuum_G2_dh',(i,j),(-1 if i==0 else 1) if i==j else 0)
            s.target('continuum_G2_dp',(i,j),-2 if i==j==0 else 0)
    # F1: at radius one the only antisymmetric lapse pair is the bond ends.
    # Larger radii allow EVERY pair of vertex smearings in the edge ball.
    lapse_sites = list(range(1-radius,radius+1))
    for h in eh:
        for ni in lapse_sites:
            for mi in lapse_sites:
                if ni >= mi:
                    continue
                col = s.new('F1:'+repr((h,ni,mi)))
                density = []
                for gm,gc in g1().items():
                    rest = tuple(a for a in gm if a[0]!='X')
                    density.extend(((gc,rest+(h,v('N',pos=ni),v('M',pos=mi))),
                                    (-gc,rest+(h,v('M',pos=ni),v('N',pos=mi)))))
                s.putpoly('CC2',quotient(poly(density)),col,-1)
                if continuum:
                    s.put('continuum_F1',(h[1],),col,Q(mi-ni))
    if continuum:
        for i in range(3):
            s.target('continuum_F1',(i,),-1 if i==0 else 0)
    if mixed:
        # U0(X,N) is vertex-centred: bond bases -R,...,R-1 and lapse sites -R,...,R.
        for xp,np in product(range(-radius,radius),range(-radius,radius+1)):
            col=s.new('U0:'+repr((xp,np)))
            terms=[]
            for mon,c in c1('N').items():
                rest=tuple(a for a in mon if a[0]!='N')
                terms.append((c,rest+(v('X',pos=xp),v('N',pos=np))))
            s.putpoly('GC1',quotient(poly(terms)),col,-1)
            if continuum:
                s.put('continuum_U0_0',(),col,Q(1))
                s.put('continuum_U0_dN',(),col,Q(np))
                s.put('continuum_U0_dX',(),col,Q(2*xp+1,2))
        if continuum:
            s.target('continuum_U0_dN',(),1)
        # V0(X,Y) on an edge, all antisymmetric pairs in its ball.
        for xp in range(-radius,radius+1):
            for yp in range(xp+1,radius+1):
                col=s.new('V0:'+repr((xp,yp)))
                terms=[]
                for mon,c in g1().items():
                    rest=tuple(a for a in mon if a[0]!='X')
                    terms.extend(((c,rest+(v('X',pos=xp),v('Y',pos=yp))),
                                  (-c,rest+(v('Y',pos=xp),v('X',pos=yp)))))
                s.putpoly('GG1',quotient(poly(terms)),col,-1)
                if continuum:
                    s.put('continuum_V0',(),col,Q(yp-xp))
        if continuum:
            s.target('continuum_V0',(),1)
    return s


def eliminate(payload, prime=None):
    """Sparse exact row elimination, preserving a dual inconsistency witness.

    For modular arithmetic only inconsistency in that field is reported;
    this is not, by itself, a rational impossibility certificate.
    """
    convert = (lambda x: (Q(x).numerator*pow(Q(x).denominator,-1,prime))%prime) if prime else Q
    clean = (lambda x:x%prime) if prime else (lambda x:x)
    inv = (lambda x:pow(x,-1,prime)) if prime else (lambda x:1/x)
    basis = {}
    for row in payload['rows']:
        if row['id'] % 100 == 0:
            budget()
        coeff = {j:convert(c) for j,c in row['coefficients']}
        rhs = convert(row['rhs'])
        witness = {row['id']:convert(1)}
        while coeff:
            pivot = min(coeff)
            factor = coeff[pivot]
            if pivot not in basis:
                factor_inv = inv(factor)
                coeff = {j:clean(c*factor_inv) for j,c in coeff.items()}
                rhs = clean(rhs*factor_inv)
                witness = {j:clean(c*factor_inv) for j,c in witness.items()}
                basis[pivot] = coeff,rhs,witness
                break
            bc,br,bw = basis[pivot]
            for j,c in bc.items():
                new = clean(coeff.get(j,0)-factor*c)
                if new: coeff[j]=new
                elif j in coeff: del coeff[j]
            rhs = clean(rhs-factor*br)
            for j,c in bw.items():
                new = clean(witness.get(j,0)-factor*c)
                if new: witness[j]=new
                elif j in witness: del witness[j]
        else:
            if rhs:
                return {'consistent':False,'rank_before_conflict':len(basis),'rhs':str(rhs),
                        'witness':[[j,str(c)] for j,c in sorted(witness.items())],
                        'prime':prime,'conflict_row':row['id']}
    return {'consistent':True,'rank':len(basis),'nullity':len(payload['columns'])-len(basis),'prime':prime}


def verify_witness(payload, result):
    left = defaultdict(Q)
    right = Q(0)
    for rid,c in result['witness']:
        factor=Q(c)
        row = payload['rows'][rid]
        for j,val in row['coefficients']:
            left[j]+=factor*Q(val)
        right+=factor*Q(row['rhs'])
    assert all(c==0 for c in left.values()) and right != 0
    assert right==Q(result['rhs'])
    return len(result['witness']),str(right)


def checks():
    # Direct fundamental sign and derivative-multiplicity tests.
    assert bracket(poly(((1,(v('h'),)),)),poly(((1,(v('p'),)),))) == {():Q(1)}
    assert bracket(poly(((1,(v('p'),)),)),poly(((1,(v('h'),)),))) == {():Q(-1)}
    assert bracket(poly(((1,(v('h'),v('h'))),)),poly(((1,(v('p'),v('p'))),))) == {canon((v('h'),v('p'))):Q(4)}
    lhs = add((1,bracket(c1('N'),t2('M'))),(1,bracket(t2('N'),c1('M'))))
    assert lhs == smear_f0(g1())
    print('Control: standard Poisson signs, multiplicities and signed axial seed PASS',flush=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--radius',type=int,default=1)
    ap.add_argument('--no-continuum',action='store_true')
    ap.add_argument('--rational',action='store_true')
    ap.add_argument('--mixed',action='store_true')
    args=ap.parse_args()
    budget(); checks()
    stem=f'axial_r{args.radius}'+('_no_continuum' if args.no_continuum else '')+('_mixed' if args.mixed else '')
    started=time.time()
    system=assemble(args.radius,not args.no_continuum,args.mixed)
    payload=system.save(HERE/(stem+'_system.json'))
    groups=defaultdict(int)
    for key in system.rows: groups[key[0]]+=1
    nnz=sum(len(row) for row in system.rows.values())
    print(json.dumps({'columns':len(system.names),'rows':len(system.rows),'nonzero_entries':nnz,'families':dict(groups),'assembly_seconds':time.time()-started}),flush=True)
    result=eliminate(payload,None if args.rational else 1000003)
    result['seconds']=time.time()-started
    (HERE/(stem+('_rational' if args.rational else '_modular')+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    if not result['consistent'] and args.rational:
        print('Exact dual certificate independently recombined:',verify_witness(payload,result),flush=True)
    print(json.dumps({k:v for k,v in result.items() if k!='witness'}),flush=True)
    print('Scope: axial necessary CC degree-two subsystem; no full algebra, 3D solution, formal review or audit verdict.',flush=True)


if __name__=='__main__':
    main()

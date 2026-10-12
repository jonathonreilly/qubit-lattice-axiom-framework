"""Exact finite author checks, distinct twirl and contraction constructions."""
import itertools
import json
import sys
import sympy as s

variant = sys.argv[1] if len(sys.argv) > 1 else 'baseline'
assert variant in ('baseline', 'drop_contractions', 'drop_crossing_sign')
I2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
G = [s.kronecker_product(*([Z]*j+[m]+[I2]*(2-j)))
     for j in range(3) for m in (X, Y)]
ONE, ZERO = s.eye(8), s.zeros(8)
E = s.eye(6)
parity = s.I*G[0]*G[1]*G[2]*G[3]*G[4]*G[5]
rows = []


def scalar(z):
    return s.expand(z)


def clean(m):
    return m.applyfunc(scalar)


def field(v):
    return sum((v[k]*G[k] for k in range(6)), ZERO)


def prod(values):
    out = ONE
    for x in values:
        out = clean(out*x)
    return out


def wick(vectors, covariance):
    if not vectors:
        return s.Integer(1)
    if len(vectors) % 2:
        return s.Integer(0)
    return scalar(sum((-1)**(j-1)*covariance(vectors[0],vectors[j])
                      *wick(vectors[1:j]+vectors[j+1:],covariance)
                      for j in range(1,len(vectors))))


def expect_word(vectors, q):
    if variant == 'drop_contractions':
        return prod([field(q*v) for v in vectors])
    out = ZERO
    for flags in itertools.product((0, 1), repeat=len(vectors)):
        ran = [q*v for v,bit in zip(vectors,flags) if not bit]
        comp = [(E-q)*v for v,bit in zip(vectors,flags) if bit]
        crossings = sum(flags[i] and not flags[j]
                        for i in range(len(flags)) for j in range(i+1,len(flags)))
        sign = 1 if variant == 'drop_crossing_sign' else (-1)**crossings
        coefficient = wick(comp, lambda f,g:(f.T*g)[0])
        out += sign*coefficient*prod([field(v) for v in ran])
    return clean(out)


def twirl(matrix, units):
    out = matrix
    for u in units:
        out = clean((out+u*out*u.adjoint())/2)
    return out


def record(name, actual, expected):
    a,e = clean(actual),clean(expected)
    residual = clean(a-e)
    rows.append(dict(name=name,passed=(residual==s.zeros(*residual.shape)),
                     actual=[[str(x) for x in row] for row in a.tolist()],
                     expected=[[str(x) for x in row] for row in e.tolist()],
                     residual=[[str(x) for x in row] for row in residual.tolist()]))


def num(name, actual, expected):
    record(name,s.Matrix([[actual]]),s.Matrix([[expected]]))


rotation = E.copy()
for j,k in ((0,2),(1,4)):
    r = E.copy()
    r[j,j] = r[k,k] = s.Rational(3,5)
    r[j,k] = -s.Rational(4,5)
    r[k,j] = s.Rational(4,5)
    rotation = rotation*r
basis = [rotation[:,j] for j in range(6)]
vectors = [E[:,0],E[:,1],(3*E[:,0]+4*E[:,2])/5,
           (E[:,1]+2*E[:,3])/3,(2*E[:,2]-E[:,4]+E[:,5])/4,
           (E[:,0]+E[:,1]+E[:,4])/2]
words = [(),(0,),(0,0),(0,1),(0,2),(2,3),(0,1,2),
         (0,1,2,3),(0,2,0,4),(1,3,4,5),(0,1,2,3,4,5),(0,1,0,1,2,2)]
record('rational_orthogonal_rotation',rotation.T*rotation,E)
for rank in (2,4):
    q = sum((u*u.T for u in basis[:rank]),s.zeros(6))
    units = [parity*field(u) for u in basis[rank:]]
    prefix = 'rank_'+str(rank)+'/'
    record(prefix+'projection',q*q,q)
    for j,(u,e) in enumerate(zip(units,basis[rank:])):
        record(prefix+'unitary_'+str(j),u*u.adjoint(),ONE)
        reflection = E-2*e*e.T
        for k in (0,2,5):
            record(prefix+'reflection_'+str(j)+'_'+str(k),
                   u*G[k]*u.adjoint(),field(reflection*E[:,k]))
    for indices in words:
        vs = [vectors[j] for j in indices]
        label = ','.join(map(str,indices)) or 'empty'
        actual = expect_word(vs,q)
        oracle = twirl(prod([field(v) for v in vs]),units)
        record(prefix+'word/'+label,actual,oracle)
        record(prefix+'idempotent/'+label,twirl(actual,units),actual)
    u,v = basis[0],basis[1]
    left,right = field(u),field(v)
    test = prod([field(x) for x in vectors[:3]])
    record(prefix+'bimodular',twirl(left*test*right,units),
           left*twirl(test,units)*right)
    record(prefix+'range_fixed',twirl(left*right,units),left*right)
    comp,ran = field(basis[-1]),field(basis[0])
    witness = s.I*comp*ran
    record(prefix+'kernel_square',witness*witness,ONE)
    record(prefix+'kernel_image',expect_word([basis[-1],basis[0]],q),ZERO)
    rho = clean(prod([ONE+s.I*field(basis[j])*field(basis[j+1])
                      for j in range(0,rank,2)])/8)
    num(prefix+'density_trace',s.trace(rho),1)
    scale = 8//(2**(rank//2))
    record(prefix+'density_positive_projection',scale*rho*scale*rho,scale*rho)
    covariance = s.Matrix(6,6,lambda i,j:scalar(s.trace(rho*G[i]*G[j])))
    range_cov = clean(q*covariance*q)
    complete_cov = range_cov+E-q
    record(prefix+'pure_range_covariance',range_cov*range_cov/4,range_cov/2)
    record(prefix+'covariance_complement',covariance,complete_cov)
    record(prefix+'covariance_self_duality',complete_cov+complete_cov.conjugate(),2*E)
    num(prefix+'omitted_complement_normalization',
        (basis[-1].T*range_cov*basis[-1])[0],0)
    num(prefix+'required_complement_normalization',
        (basis[-1].T*complete_cov*basis[-1])[0],1)
    for indices in words:
        if len(indices) not in (2,4,6):
            continue
        vs=[vectors[j] for j in indices]
        density_moment=scalar(s.trace(rho*prod([field(v) for v in vs])))
        wick_moment=wick(vs,lambda f,g:(f.T*complete_cov*g)[0])
        num(prefix+'density_wick/'+','.join(map(str,indices)),density_moment,wick_moment)
        filtered=scalar(s.trace(rho*expect_word(vs,q)))
        num(prefix+'pullback_state/'+','.join(map(str,indices)),filtered,density_moment)

result=dict(variant=variant,sympy=s.__version__,rows=rows,
            passed=sum(r['passed'] for r in rows),failed=sum(not r['passed'] for r in rows),
            scope='Exact finite algebra controls, not a proof of infinite-dimensional density, locality or quotient claims; root is author.')
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['failed']==0 else 1)

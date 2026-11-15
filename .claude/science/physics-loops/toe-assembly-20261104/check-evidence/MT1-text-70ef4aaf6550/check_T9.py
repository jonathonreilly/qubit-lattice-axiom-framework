# Theorem 9: boost algebra. Operators act on vector-valued polynomials in q; x_j = i d/dq_j. Exact (sympy).
import sympy as sp, itertools
q=sp.symbols('q1:4',real=True); v=sp.symbols('v',positive=True)
s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-sp.I],[sp.I,0]]); s3=sp.Matrix([[1,0],[0,-1]]); I2=sp.eye(2)
kron=sp.kronecker_product
reps={'Pauli (2-dim)':[v*s1,v*s2,v*s3],
      'reducible 4-dim, sigma x diag':[v*kron(s1,s3),v*kron(s2,s3),v*kron(s3,s3)],
      'left-handed -sigma (2-dim)':[-v*s1,-v*s2,-v*s3]}
def run(N,name,expect=True):
    d=N[0].shape[0]
    fs=[sp.Function(f'f{a}')(*q) for a in range(d)]; F=sp.Matrix(fs)
    x=lambda j,G: sp.I*G.diff(q[j])
    h=lambda G: sum((q[j]*N[j] for j in range(3)),sp.zeros(d,d))*G
    K=lambda i,G: (x(i,h(G))+h(x(i,G)))/2
    eps=sp.LeviCivita
    L=lambda k,G: sum((eps(k,a,b)*x(a,q[b]*G) for a in range(3) for b in range(3)),sp.zeros(d,1))
    SN=[-(sp.I/(4*v**2))*sum((eps(k,a,b)*N[a]*N[b] for a in range(3) for b in range(3)),sp.zeros(d,d)) for k in range(3)]
    J=lambda k,G: L(k,G)+SN[k]*G
    ok=True
    for i in range(3):
        for j in range(3):
            lhs=K(i,K(j,F))-K(j,K(i,F))
            rhs=-sp.I*v**2*sum((eps(i,j,k)*J(k,F) for k in range(3)),sp.zeros(d,1))
            ok&= sp.simplify(sp.expand(lhs-rhs))==sp.zeros(d,1)
    comm=all(sp.simplify(sp.expand(J(k,h(F))-h(J(k,F))))==sp.zeros(d,1) for k in range(3))
    cas=sp.simplify(sum((s*s for s in SN),sp.zeros(d,d)))==sp.Rational(3,4)*sp.eye(d)
    su2=all(sp.simplify(SN[a]*SN[b]-SN[b]*SN[a]-sp.I*sum((eps(a,b,c)*SN[c] for c in range(3)),sp.zeros(d,d)))==sp.zeros(d,d) for a in range(3) for b in range(3))
    print(f'{name}: [K_i,K_j]=-i v^2 eps(L+S^N): {ok}; [J,h_1]=0: {comm}; S^N su(2): {su2}; Casimir 3/4: {cas}')
    return ok and comm and cas and su2
allok=all(run(N,n) for n,N in reps.items())
# control: flip the sign of S^N in the claimed identity -> must fail
N=reps['Pauli (2-dim)']; d=2
fs=[sp.Function(f'f{a}')(*q) for a in range(d)]; F=sp.Matrix(fs)
x=lambda j,G: sp.I*G.diff(q[j]); h=lambda G: sum((q[j]*N[j] for j in range(3)),sp.zeros(d,d))*G
K=lambda i,G: (x(i,h(G))+h(x(i,G)))/2
eps=sp.LeviCivita
SN=[-(sp.I/(4*v**2))*sum((eps(k,a,b)*N[a]*N[b] for a in range(3) for b in range(3)),sp.zeros(d,d)) for k in range(3)]
Lk=lambda k,G: sum((eps(k,a,b)*x(a,q[b]*G) for a in range(3) for b in range(3)),sp.zeros(d,1))
lhs=K(0,K(1,F))-K(1,K(0,F)); bad=-sp.I*v**2*(Lk(2,F)-SN[2]*F)
ctrl= sp.simplify(sp.expand(lhs-bad))!=sp.zeros(d,1)
print('control (L - S^N rejected):',ctrl)
# control: non-Clifford N (anisotropic) -> [K_i,K_j] is not of the form  -i v^2 eps (L+S^N)
N=[v*s1,v*s2,2*v*s3]
h=lambda G: sum((q[j]*N[j] for j in range(3)),sp.zeros(d,d))*G
K=lambda i,G: (x(i,h(G))+h(x(i,G)))/2
SN=[-(sp.I/(4*v**2))*sum((eps(k,a,b)*N[a]*N[b] for a in range(3) for b in range(3)),sp.zeros(d,d)) for k in range(3)]
lhs=K(1,K(2,F))-K(2,K(1,F)); rhs=-sp.I*v**2*(Lk(0,F)+SN[0]*F)
ctrl2= sp.simplify(sp.expand(lhs-rhs))!=sp.zeros(d,1)
print('control (non-Clifford triple rejected):',ctrl2)
print('ALL PASS' if allok and ctrl and ctrl2 else 'SOME FAIL')

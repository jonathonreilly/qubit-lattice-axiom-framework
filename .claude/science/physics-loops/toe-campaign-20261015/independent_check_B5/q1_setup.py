# Q1: D3-covariant one-qubit walks. V = a0 + i a.sigma, a0,a real trig polys with support {-1,0,1}^3
import sympy as sp, itertools
c = sp.symbols('c1:4'); s = sp.symbols('s1:4')
basis1 = lambda a: [1, c[a], s[a]]
B = [sp.Mul(*t) for t in itertools.product(basis1(0),basis1(1),basis1(2))]
R3 = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
R2 = sp.Matrix([[0,-1,0],[-1,0,0],[0,0,-1]])
def act(expr, M):
    # expr(k) -> expr(M k)
    sub = {}
    for a in range(3):
        row = M.row(a); j = [i for i in range(3) if row[i]!=0][0]; sg = row[j]
        sub[c[a]] = c[j]; sub[s[a]] = sg*s[j]
    return sp.expand(expr.subs(sub, simultaneous=True))
def coeffvec(expr):
    P = sp.Poly(sp.expand(expr), *c, *s)
    return [P.coeff_monomial(b) for b in B]
# unknown coefficients
X = [[sp.Symbol(f'x{comp}_{i}') for i in range(27)] for comp in range(4)]
F = [sum(X[comp][i]*B[i] for i in range(27)) for comp in range(4)]
eqs = []
for M in (R3, R2):
    eqs += [e for e in coeffvec(act(F[0],M)-F[0])]
    av = sp.Matrix(F[1:]); lhs = sp.Matrix([act(f,M) for f in F[1:]]); rhs = M*av
    for i in range(3):
        eqs += coeffvec(lhs[i]-rhs[i])
allx = [x for row in X for x in row]
sol = sp.solve(eqs, allx, dict=True)[0]
Fs = [sp.expand(f.subs(sol)) for f in F]
free = sorted(set().union(*[f.free_symbols for f in Fs]) - set(c) - set(s), key=str)
print('free params', len(free), free)
for f in Fs: print(f)
# norm condition
N = sp.expand(sum(f**2 for f in Fs) - 1)
# reduce s^2 -> 1-c^2
for a in range(3):
    N = sp.expand(N.subs(s[a]**2, 1-c[a]**2))
    N = sp.expand(sp.Poly(N, s[a]).as_expr())
# remaining powers of s up to 1 after repeated reduction
def red(e):
    e = sp.expand(e)
    for a in range(3):
        P = sp.Poly(e, s[a]); out = 0
        for (k,), co in P.terms():
            out += co * (s[a]**(k%2)) * (1-c[a]**2)**(k//2)
        e = sp.expand(out)
    return e
N = red(sum(f**2 for f in Fs) - 1)
P = sp.Poly(N, *c, *s)
coeqs = [co for _, co in P.terms()]
print('num eqs', len(coeqs))
import pickle
pickle.dump((free, Fs, coeqs), open('q1.pkl','wb'))
with open('q1.sing','w') as fh:
    vars_ = ','.join(str(v) for v in free)
    fh.write(f'option(redSB); ring r=0,({vars_}),dp;\n')
    fh.write('ideal I=' + ',\n'.join(str(e).replace('**','^') for e in coeqs) + ';\n')
    fh.write('ideal J=std(I); dim(J); J;\nLIB "primdec.lib"; list L=minAssGTZ(I); L;\nquit;\n')

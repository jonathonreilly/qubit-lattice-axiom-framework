"""Branch pickle with sqrt(3) coefficients -> Singular over Q(a), a^2 = 3."""
import pickle, sys, sympy as sp
d = pickle.load(open(sys.argv[1], 'rb')); free, red = d['free'], d['red']
Y = sp.symbols(f'y0:{len(free)}'); a = sp.Symbol('a')
sub = dict(zip(free, Y))
out = set()
for e in red:
    q = sp.Poly(sp.expand(e.subs(sub).subs(sp.sqrt(3), a)), *Y)
    terms = []
    for mon, c in q.terms():
        c = sp.expand(c)
        assert c.free_symbols <= {a}, c
        m = '*'.join(f'{y}^{k}' if k > 1 else str(y) for y, k in zip(Y, mon) if k > 0) or '1'
        terms.append(f'({str(c).replace("**", "^")})*{m}')
    out.add('+'.join(terms))
names = ','.join(str(y) for y in Y)
open(sys.argv[2], 'w').write(f'''option(redSB);
ring r=(0,a),({names}),dp;
minpoly = a^2-3;
ideal I=
{",".join(sorted(out))};
ideal J=std(I);
print("size"); print(size(J)); print("dim"); print(dim(J)); print("vdim"); print(vdim(J));
if (size(J) == 1 && deg(J[1]) == 0) {{ print("INFEASIBLE: 1 in ideal"); }}
''')
print(len(free), 'vars', len(out), 'eqs')

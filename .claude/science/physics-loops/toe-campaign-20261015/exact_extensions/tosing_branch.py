"""Write a Singular modStd input for a branch pickle, splitting complex equations into real and imaginary parts."""
import pickle, sys, sympy as sp
d = pickle.load(open(sys.argv[1], 'rb'))
free, red = d['free'], d['red']
Y = sp.symbols(f'zz0:{len(free)}', real=True)
sub = dict(zip(free, Y))
out = set()
for e in red:
    P = sp.Poly(sp.expand(e.subs(sub, simultaneous=True)), *Y)
    re = sum(sp.re(c) * sp.prod([y ** k for y, k in zip(Y, m)]) for m, c in P.terms())
    im = sum(sp.im(c) * sp.prod([y ** k for y, k in zip(Y, m)]) for m, c in P.terms())
    for part in (re, im):
        part = sp.expand(part)
        if part != 0:
            # clear denominators, keep rational coefficients; sqrt factors are not expected here
            q = sp.Poly(part, *Y)
            assert all(c.is_rational for c in q.coeffs()), q.coeffs()[:3]
            terms = []
            for mon, c in q.terms():
                m = '*'.join(f'{y}^{k}' if k > 1 else str(y) for y, k in zip(Y, mon) if k > 0) or '1'
                terms.append(f'({c})*{m}')
            out.add('+'.join(terms))
names = [str(y) for y in Y]
body = ',\n'.join(sorted(out))
open(sys.argv[2], 'w').write(f'''option(redSB);
LIB "modstd.lib";
ring r=0,({",".join(names)}),dp;
ideal I=
{body};
ideal J=modStd(I);
print("dim"); print(dim(J)); print("vdim"); print(vdim(J));
int i; int p;
for(i=1;i<={len(names)};i++){{ p=1; while(reduce(var(i)^p,J)!=0 && p<12){{p++;}} print(string(var(i))+" power "+string(p)); }}
''')
print(len(free), 'vars', len(out), 'real equations')

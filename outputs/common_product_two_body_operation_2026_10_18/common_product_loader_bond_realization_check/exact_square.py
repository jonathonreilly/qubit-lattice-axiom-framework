"""Exact independent characteristic-polynomial check; Delta scaled to one.
No numerical eigenvalues, fitting, simulations or parameter sweep.
"""
import sympy as s
x,E=s.symbols('x E')
for omega in (1,-1):
    # Ancilla complement basis (|n> + omega |15-n>)/sqrt(2), 0<=n<8.
    # Gauge all data-column signs into omega=product(o_r).
    H=s.zeros(8)
    for n in range(8):
        bits=[(n>>r)&1 for r in range(4)]
        H[n,n]=sum(bits[r]!=bits[(r+1)%4] for r in range(4))
        for r in range(4):
            flipped=n^(1<<r)
            rep=min(flipped,15-flipped)
            H[rep,n]+=x*(1 if flipped<8 else omega)
    assert H==H.T
    cp=s.factor(H.charpoly(E).as_expr())
    print('omega =',omega)
    print('exact characteristic polynomial =',cp)
    # Implicit expansion of the unique E=0 eigenvalue; independently
    # solve coefficients of the exact determinant, not Feshbach paths.
    c2,c4,c6=s.symbols('c2 c4 c6')
    expr=s.series(cp.subs(E,c2*x**2+c4*x**4+c6*x**6),x,0,8).removeO().expand()
    sol={}
    for degree,c in ((2,c2),(4,c4),(6,c6)):
        sol[c]=s.solve(expr.coeff(x,degree).subs(sol),c)[0]
    print('low eigenvalue coefficients =',sol)
    assert sol[c2]==-2
    assert sol[c4]==-s.Rational(1,2)-s.Rational(5,2)*omega
    print('zero-field low-root derivative =',s.diff(cp,E).subs({x:0,E:0}))
print('Exact coefficient identities verified in both product sectors.')

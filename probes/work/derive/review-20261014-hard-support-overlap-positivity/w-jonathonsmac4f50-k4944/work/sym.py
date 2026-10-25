import sympy as sp, itertools, time
w=sp.symbols('w',positive=True); dl=sp.symbols('delta',positive=True)
d=sp.symbols('d0 d1 d2',real=True)
I=sp.I
def Ctrace(Lx=3, dl_val=None, wv=None):
    dd=sp.symbols('d0:%d'%Lx,real=True)
    total=0
    for perm in itertools.permutations(range(Lx)):
        # perm gives ascending order: dd[perm[0]]<dd[perm[1]]<...
        rank={perm[i]:i for i in range(Lx)}
        f=1
        for x in range(Lx):
            xp=(x+1)%Lx
            sgn=1 if rank[xp]>rank[x] else -1   # sign of d_{x+1}-d_x
            s=dd[xp]-dd[x]
            arg=w*(dl - sgn*s/2)
            f=f*(sp.exp(I*arg)-sp.exp(-I*arg))/(2*I)
        f=sp.expand(f)
        # integrate nested: lowest var from -dl to next, ...
        vars_=[dd[p] for p in perm]
        # innermost integration variable is the largest? do outermost = smallest: integrate largest first with limits (prev, dl)
        expr=f
        for i in range(Lx-1,-1,-1):
            v=vars_[i]
            lo = vars_[i-1] if i>0 else -dl
            hi = dl
            # integrate term by term
            new=0
            for term in sp.Add.make_args(sp.expand(expr)):
                new+=sp.integrate(term,(v,lo,hi))
            expr=new
        total+=expr
    return total
t=time.time()
tot=Ctrace(3)
tot=sp.simplify(tot*(2/w)**3)
print(time.time()-t)
print(tot)
for wv in (6,7,8,9,10):
    print(wv, sp.N(tot.subs({w:wv,dl:sp.Rational(3,5)}),20))
import pickle; pickle.dump(tot,open('work/C3.pkl','wb'))

import sympy as sp, random, pickle
from cont2d import *
pieces=pickle.load(open('cont2d_pieces.pkl','rb'))
V1,V2,T2,T3=[pieces[k] for k in ('V1','V2','T2','T3')]
piece={1:K*V1,2:T2+K*V2,3:T3}
br2=0
for i in (1,2,3):
    br2+=PB(N*piece[i],M*piece[4-i])
xi0,xi1=structure_function()
rhs=degpart(sp.expand(lie_G(xi0)),2)+degpart(sp.expand(lie_G(xi1)),1)
diff=sp.expand(br2-rhs)
random.seed(4)
def rp(deg=3, ydep=True):
    return sum(sp.Rational(random.randint(-3,3),random.randint(1,3))*x**i*y**j for i in range(4) for j in range(4) if i+j<=deg and (ydep or j==0))
def test(label, ydep, hxy_on):
    jets={}
    for f in FIELDS_H+FIELDS_P+[N,M]:
        if not hxy_on and f in (hxy,Pxy): jets[f]=sp.Integer(0)
        else: jets[f]=rp(3,ydep)
    pt={x:sp.Rational(1,3),y:sp.Rational(1,5)}
    vals=[]
    for f in FIELDS_H+FIELDS_P:
        e=EL(diff,f).subs(jets).doit().subs(pt)
        vals.append(sp.nsimplify(e))
    print(label, ['0' if v==0 else 'NZ' for v in vals])
test("y-indep, hxy off", False, False)
test("y-dep,  hxy off", True, False)
test("y-indep, hxy on ", False, True)
test("y-dep,  hxy on  ", True, True)

import sympy as sp, pickle
c1,c2,c3,s1,s2,s3,C,Sn=sp.symbols('c1 c2 c3 s1 s2 s3 C Sn')
e=sp.symbols('e')
q0,qv=pickle.load(open('S_pal.pkl','rb'))
ks=sp.symbols('k1 k2 k3',real=True)
def ser(x,n):
    return sp.expand(sp.series(x.subs({C:sp.cos(e/2),Sn:sp.sin(e/2)}),e,0,n).removeO())
Q=[ser(x,5) for x in qv]
N=[sp.expand(Q[i].coeff(e,1)+e**2*Q[i].coeff(e,3)) for i in range(3)]
# k-derivations: replace c_j=cos k_j, s_j=sin k_j
rep={c1:sp.cos(ks[0]),c2:sp.cos(ks[1]),c3:sp.cos(ks[2]),s1:sp.sin(ks[0]),s2:sp.sin(ks[1]),s3:sp.sin(ks[2])}
Nk=[x.subs(rep) for x in N]
def Phi(a,b):
    da=[sp.diff(x,ks[a]) for x in Nk]; db=[sp.diff(x,ks[b]) for x in Nk]
    cr=[da[1]*db[2]-da[2]*db[1],da[2]*db[0]-da[0]*db[2],da[0]*db[1]-da[1]*db[0]]
    trip=sum(Nk[i]*cr[i] for i in range(3))
    return trip, sum(x**2 for x in Nk)
t=sp.symbols('t',positive=True)
n=(sp.Rational(2,3),sp.Rational(1,3),sp.Rational(2,3))   # unit vector
sub={ks[i]:sp.pi/2+t*n[i] for i in range(3)}
trip,nn=Phi(0,1)
# density: trip / nn^{3/2}
dens=trip/nn**sp.Rational(3,2)
d_e=sp.series(dens.subs(sub),e,0,3).removeO()
d0=sp.simplify(d_e.coeff(e,0)); d2=sp.simplify(d_e.coeff(e,2))
print('Phi12 e^0 :',sp.series(d0,t,0,0))
r=sp.series(sp.simplify(d2/d0),t,0,2)
print('ratio e^2/e^0 series in t:',r)

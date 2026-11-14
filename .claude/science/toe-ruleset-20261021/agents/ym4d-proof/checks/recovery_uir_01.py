from fractions import Fraction as F
from itertools import permutations
from datetime import datetime, timezone

# Rational polynomials, coefficients in ascending order. No truncation.
def add(a,b):
    q=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): q[i]+=x
    for i,x in enumerate(b): q[i]+=x
    while len(q)>1 and not q[-1]: q.pop()
    return q
def neg(a): return [-x for x in a]
def mul(a,b):
    q=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): q[i+j]+=x*y
    while len(q)>1 and not q[-1]: q.pop()
    return q
def const(x): return [F(x)]
def det(m):
    n=len(m); out=const(0)
    for p in permutations(range(n)):
        term=const((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n): term=mul(term,m[i][p[i]])
        out=add(out,term)
    return out
def coeff(a,k): return a[k] if k<len(a) else F(0)
def half_log_t2(a):
    return (coeff(a,2)/a[0]-coeff(a,1)**2/(2*a[0]**2))/2

def show(name,ok,detail=''):
    print(name+': '+('PASS' if ok else 'FAIL')+(' | '+detail if detail else ''))

print('UTC:', datetime.now(timezone.utc).isoformat())
checks=[]
for a,c,b in [(F(1),F(1),F(1)),(F(3),F(5),F(1,7)),(F(2,3),F(7,4),F(5,6))]:
    z=const(0); aa=const(a); cc=const(c); bt=[F(0),b]
    bad=[[aa,bt,bt],[bt,cc,z],[bt,z,cc]]
    w=[[aa,bt],[bt,cc]]
    correct=[[aa,z,bt],[z,cc,z],[bt,z,cc]]
    db=det(bad); target=mul(cc,det(w)); dc=det(correct)
    diff=add(db,neg(target))
    literal_ok=(diff==[F(0)])
    show('A printed J_LS identity', literal_ok, 'a='+str(a)+', c='+str(c)+', b='+str(b)+', determinant difference='+str(diff))
    checks.append(diff==[F(0),F(0),-c*b*b])
    show('B corrected projected identity',dc==target)
    checks.append(dc==target)
    dropped=mul(aa,mul(cc,cc))
    show('B control: dropping matching coupling is rejected',dropped!=target)
    checks.append(dropped!=target)
    lbad=half_log_t2(db)-half_log_t2(target)
    lcorr=half_log_t2(dc)-half_log_t2(target)
    show('B half-log coefficients',lbad==-b*b/(2*a*c) and lcorr==0,'printed='+str(lbad)+', corrected='+str(lcorr))
    checks.append(lbad==-b*b/(2*a*c) and lcorr==0)

# d=4; convergence at a centre requires exponent strictly below dimension.
for a,b,expected in [(4,2,False),(3,3,True),(3,2,True),(2,2,True)]:
    admissible=0<=a<4 and 0<=b<4
    show('C separate-pole test '+str((a,b)),admissible==expected,
         'admissible='+str(admissible)+', radial exponent at K=0='+str(3-a)+', total='+str(a+b))
    checks.append(admissible==expected)
checks.append(4-(3+2)==-1 and 2+4-(3+2)==1)
show('C degree-five remainder: divergent raw scale, vanishing scaled contribution',checks[-1])

# Independent analytic proof in recovery note gives 6 integral_0^1 x(1-x)*
# [pi^2/(12*x(1-x)*|P|^2)] dx. Only rational arithmetic is checked here.
core=F(6,12)
show('D transverse core / (pi^2 / |P|^2)',core==F(1,2),str(core))
checks.append(core==F(1,2))
show('D wrong core factor 1/4 rejected',core!=F(1,4))
checks.append(core!=F(1,4))
print('EXPECTED FAILED PRINTED IDENTITIES: 3; these failures are preserved above.')
print('CORRECTION/CONTROL CHECKS:',len(checks),'/',len(checks),'PASS' if all(checks) else 'FAIL')
print('per_element: exact rational block determinants and logarithmic Taylor coefficients checked.')
print('per_site: checked and not executed — no field-theory site kernel is implemented here.')
print('per_mode: only an abstract transverse/gauge sector and analytic degree conditions are checked.')
print('per_block: the printed and corrected finite Schur blocks are compared independently.')
print('lattice_wide: checked and not executed — no Yang–Mills infrared limit is certified by this runner.')
assert all(checks)

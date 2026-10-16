"""Post-exposure original-equation correspondence; no author imports or file reads."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import json,sys
import sympy as s
checks=[]
def zero(name,expr):
    r=s.factor(s.cancel(s.expand(expr)))
    checks.append({"name":name,"pass":r==0,"residual":str(r)})
    print(("PASS " if r==0 else "FAIL ")+name,file=sys.stderr,flush=True)
def truth(name,value,detail=None):
    checks.append({"name":name,"pass":bool(value),"detail":None if detail is None else str(detail)})
    print(("PASS " if value else "FAIL ")+name,file=sys.stderr,flush=True)

# Start from the independently derived Hamiltonian and uneliminated scalar,
# using arbitrary local jets rather than importing the author helper.
h,b,x,xp,bp,bpp,kap,K,R=s.symbols("h b x xp bp bpp kappa K R",nonzero=True)
P,Pp,J,Jp,Jpp=s.symbols("P Pp J Jp Jpp")
q=b*x;ell=h-q;L=bp/b;Lp=bpp/b-bp**2/b**2;qp=bp*x+b*xp
w=J/b
wp=Jp/b-bp*J/b**2
wpp=Jpp/b-2*bp*Jp/b**2+(2*bp**2/b**3-bpp/b**2)*J
F=-xp-(3*h-2*q)*x
delta=(-2*K*P-6*ell*(Pp+ell*P)-x*wp+x*x*P-F*w)/R
raw=s.expand(b*(wpp+(3*h-2*q)*wp+(K+kap)*w+b*R*delta-4*x*Pp+2*F*P))
derived=[raw.coeff(Jp),raw.coeff(J)-K,-raw.coeff(Pp),-s.diff(raw,P,K),-raw.coeff(P).subs(K,0)]
author=[3*ell-2*L,kap+b*xp+3*h*q-2*q*q+L*L-Lp-3*ell*L,
        6*b*b*ell+4*q,2*b*b,6*b*b*ell*ell+2*b*xp+6*h*q-5*q*q]
for name,a,c in zip(["a","c","d","e","f"],derived,author):zero("original scalar gives author coefficient "+name,a-c)
zero("damping gives q without critical-B division",h-(derived[0]+2*L)/3-q)
zero("curvature inverse from original scalar",derived[1]-qp-3*h*q+2*q*q-2*q*L-L*L+Lp+3*h*L-kap)
zero("common source ratio equals independent s",2*qp-2*s.Symbol("hp")-2*h*q+(2-1/b**2)*q*q-(-2*s.Symbol("hp")+2*qp-2*h*q+2*q*q-x*x))
zero("field reflection preserves independent ratio",(-x)/(-b)-x/b)

# Gain law from inverse differentiation, separate from recorded forward test.
a,c,d,e,f,z,zp,G=s.symbols("a c d e f z zp G",nonzero=True)
Pt,Pt1,Jt,Jt1,Jt2=s.symbols("Pt Pt1 Jt Jt1 Jt2")
orig=Jpp+K*J+a*Jp+c*J-d*Pp-e*K*P-f*P
inv={J:Jt/G,Jp:(Jt1-z*Jt)/G,Jpp:(Jt2-2*z*Jt1+(z*z-zp)*Jt)/G,
     P:Pt/G,Pp:(Pt1-z*Pt)/G}
record=s.expand(G*orig.subs(inv,simultaneous=True))
at=record.coeff(Jt1);ct=record.coeff(Jt)-K;dt=-record.coeff(Pt1)
et=-s.diff(record,Pt,K);ft=-record.coeff(Pt).subs(K,0)
for name,got,expected in [("a",at,a-2*z),("c",ct,c-a*z+z*z-zp),("d",dt,d),("e",et,e),("f",ft,f-d*z)]:
    zero("inverse differentiation gives gain coefficient "+name,got-expected)
zero("curvature unwarping",ct+at*z+z*z+zp-c)
zero("force coefficient unwarping",ft+dt*z-f)

# A new exact rank-five check on the pre-exposure power family.
T=s.symbols("tau",positive=True)
ms=[s.Rational(1,10),s.Rational(1,8),s.Rational(1,6),s.Rational(1,5),s.Rational(1,4)]
def ratio(m):return (8*m*m+12*m+3)/(2*m+3)
def wave(m):
    zz=m*(m+1)
    return zz*(8*zz+9)/(3-8*zz)
D=s.Matrix([[-m*ratio(m),-ratio(m),m,wave(m),1] for m in ms])
rhs=s.Matrix([(m*(m-1)+wave(m))*ratio(m) for m in ms])
det=s.factor(D.det())
truth("independent exact full modes attain author rank five",det!=0,det)
theta=D.inv()*rhs
for label,got,expected in zip(["a","c","d","e","f"],theta,[s.Rational(3,2),s.Rational(9,4),5,2,s.Rational(9,4)]):
    zero("five-coefficient solve on independent modes "+label,got-expected)

# The fifth member is checked in the original Einstein-time equations.
m=ms[0];Y=ratio(m);LL=wave(m);U=T**m;sf=Y*U
A=s.sqrt(2*T);aE=A;HE=1/A;vE=1/A;rE=1/(2*T);rho=rE/A;V=s.Rational(3,4)/T
DE=lambda ex:A*s.diff(ex,T)
DP=lambda ex:DE(ex)/vE
AEphi=DP(A);Vphi=DP(V);FE=Vphi+rho*AEphi;muE=DP(Vphi)+rho*DP(AEphi)
vel=(2*Y-8*m-4)*T**(m+1);vd=vel/A
den=(-(8*LL+5)-12*m+(2-2*m)*Y)*U
ke=4*LL/aE**2
zero("fifth mode original momentum",2*(DE(U)+HE*U)-vE*sf+rE*vd)
zero("fifth mode original Hamiltonian",2*(ke*U+3*HE*(DE(U)+HE*U))+vE*DE(sf)-vE*vE*U+Vphi*sf+rE*(den+sf))
zero("fifth mode original spatial trace",2*(DE(DE(U))+4*HE*DE(U)+(2*DE(HE)+3*HE*HE)*U)-vE*DE(sf)+vE*vE*U+Vphi*sf)
zero("fifth mode original scalar",DE(DE(sf))+3*HE*DE(sf)+(ke+muE)*sf-4*vE*DE(U)+2*FE*U+rho*AEphi*den)
zero("fifth mode original bare continuity",DE(den)-3*DE(U)-ke*vd)
zero("fifth mode original dust Euler",DE(vd)+vE*vd+U+sf)

# A different positive common gain. The inverse takes exact recorded jets.
gain=T**s.Rational(2,7)*s.exp(T/11)
mat=[];yy=[]
for m in ms:
    pp=gain*T**m;jj=ratio(m)*pp;kv=wave(m)/T**2
    mat.append([s.factor(-s.diff(jj,T)/pp),-ratio(m),s.factor(s.diff(pp,T)/pp),kv,s.Integer(1)])
    yy.append(s.factor((s.diff(jj,T,2)+kv*jj)/pp))
CM=s.Matrix(mat);cy=s.Matrix(yy);epoch=s.Integer(2)
M0=CM.subs(T,epoch);M1=CM.diff(T).subs(T,epoch);M2=CM.diff(T,2).subs(T,epoch)
y0=cy.subs(T,epoch);y1=cy.diff(T).subs(T,epoch);y2=cy.diff(T,2).subs(T,epoch)
th=M0.inv()*y0;th1=M0.inv()*(y1-M1*th);th2=M0.inv()*(y2-M2*th-2*M1*th1)
truth("recorded exact matrix remains full rank",M0.det()!=0,s.factor(M0.det()))
B=th[3]/2;B1=th1[3]/2;B2=th2[3]/2
ll=B1/(2*B);ll1=B2/(2*B)-B1*B1/(2*B*B)
hh=1/epoch;hp=-1/epoch**2
n=th[2]-6*B*hh;denominator=4-6*B
qr=n/denominator
qrp=((th1[2]-6*B1*hh-6*B*hp)*denominator+6*B1*n)/denominator**2
drift=(3*(hh-qr)-2*ll-th[0])/2
driftp=(3*(hp-qrp)-2*ll1-th1[0])/2
cphysical=th[1]+th[0]*drift+drift**2+driftp
kr=cphysical-qrp-3*hh*qr+2*qr**2-2*qr*ll-ll**2+ll1+3*hh*ll
fphysical=th[4]+th[2]*drift
fexpected=6*B*(hh-qr)**2+2*(qrp-qr*ll)+6*hh*qr-5*qr**2
for name,got,expected in [
    ("B",B,1),("L",ll,0),("L prime",ll1,0),("q",qr,1/(2*epoch)),("q prime",qrp,-1/(2*epoch**2)),
    ("gain drift",drift,s.Rational(2,7)/epoch+s.Rational(1,11)),("gain drift prime",driftp,-s.Rational(2,7)/epoch**2),
    ("kappa",kr,s.Rational(7,4)/epoch**2),("remaining f",fphysical,fexpected)]:
    zero("independent gain recorded-jet inverse "+name,got-expected)

out={"stage":"After author exposure; correspondence and alternative exact fixtures",
     "author_imports_or_runtime_reads":False,"software":{"python":sys.version.split()[0],"sympy":s.__version__},
     "checks":checks,"summary":{"passed":sum(q["pass"] for q in checks),"failed":sum(not q["pass"] for q in checks)},
     "rank_five_fixture":{"exponents":[str(m) for m in ms],"determinant_tau_one":str(det),"recovered_coefficients":[str(v) for v in theta]},
     "gain_fixture":{"gain":str(gain),"epoch":str(epoch),"recovered_coefficient_jets":[[str(v) for v in th],[str(v) for v in th1],[str(v) for v in th2]],
                     "recovered_gain_drift":str(drift),"recovered_gain_drift_prime":str(driftp),"recovered_kappa":str(kr)}}
print(json.dumps(out,indent=2))
raise SystemExit(int(out["summary"]["failed"]!=0))


"""Narrow root-suggested joint-gain correspondence on an exact critical chart."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import json,sys
import sympy as s
checks=[]
def z(name,e):
    r=s.factor(s.cancel(s.expand(e)));checks.append({"name":name,"pass":r==0,"residual":str(r)})
    print(("PASS " if r==0 else "FAIL ")+name,file=sys.stderr,flush=True)
def ok(name,v,detail=None):
    checks.append({"name":name,"pass":bool(v),"detail":str(detail)})
    print(("PASS " if v else "FAIL ")+name,file=sys.stderr,flush=True)
# Trace gain law by inverse differentiation.
a,c,e,f,h,hp,G,dr,drp=s.symbols("a c e f h hp gain drift driftprime")
P,P1,P2,J,J1=s.symbols("P P1 P2 J J1")
trace=2*P2+8*h*P1+(4*hp+6*h*h)*P-a*P1-c*P-e*J1-f*J
Pt,Pt1,Pt2,Jt,Jt1=s.symbols("Pt Pt1 Pt2 Jt Jt1")
trans=s.expand(G*trace.subs({P:Pt/G,P1:(Pt1-dr*Pt)/G,P2:(Pt2-2*dr*Pt1+(dr*dr-drp)*Pt)/G,J:Jt/G,J1:(Jt1-dr*Jt)/G},simultaneous=True))
base=2*Pt2+8*h*Pt1+(4*hp+6*h*h)*Pt
co=[a+4*dr,c-a*dr+8*h*dr-2*dr*dr+2*drp,e,f-e*dr]
z("trace common-gain transformation",trans-(base-sum(v*w for v,w in zip(co,[Pt1,Pt,Jt1,Jt]))))
z("trace derivative-of-slip coefficient invariant",s.diff(base-trans,Jt1)-e)
# Independent critical background and full modes.
T=s.symbols("tau",positive=True);C=s.sqrt(s.Rational(3,2))
A=s.sqrt(2*T);aE=A;H=1/A;v=C/A
r=1/(4*T);rho=r/A;V=s.Rational(7,8)/T
DE=lambda q:A*s.diff(q,T)
DP=lambda q:DE(q)/v
b=s.factor(DP(A)/A);F=s.factor(DP(V)+rho*DP(A));mu=s.factor(DP(DP(V))+rho*DP(DP(A)))
z("critical background Friedmann",3*H*H-v*v/2-r-V)
z("critical background Raychaudhuri",-2*DE(H)-v*v-r)
z("critical background original scalar",DE(v)+3*H*v+F)
z("critical background bare dust",DE(rho)+3*H*rho)
z("critical B exactly two thirds",b*b-s.Rational(2,3))
z("critical fixed-density curvature",mu/A**2-s.Rational(5,4)/T**2)
ok("critical dust density positive",r.is_positive,r)
ms=[s.Rational(1,20),s.Rational(1,16),s.Rational(1,12),s.Rational(1,10),s.Rational(1,8)]
def Y(m):return (16*m*m+24*m+7)/(6*m+7)
def LL(m):
    zz=m*(m+1)
    return 3*zz*(16*zz+7)/(7-48*zz)
for m in ms:
    P0=T**m;J0=Y(m)*P0;w=C*J0;ke=4*LL(m)/aE**2
    Z=(6*Y(m)-16*m-8)*T**(m+1);vel=Z/A
    delta=(-16*LL(m)-24*m-9+6*(1-m)*Y(m))*P0
    prefix="critical full mode "+str(m)+" "
    z(prefix+"momentum",2*(DE(P0)+H*P0)-v*w+r*vel)
    z(prefix+"Hamiltonian",2*(ke*P0+3*H*(DE(P0)+H*P0))+v*DE(w)-v*v*P0+DP(V)*w+r*(delta+b*w))
    z(prefix+"spatial trace",2*(DE(DE(P0))+4*H*DE(P0)+(2*DE(H)+3*H*H)*P0)-v*DE(w)+v*v*P0+DP(V)*w)
    z(prefix+"scalar",DE(DE(w))+3*H*DE(w)+(ke+mu)*w-4*v*DE(P0)+2*F*P0+rho*DP(A)*delta)
    z(prefix+"bare continuity",DE(delta)-3*DE(P0)-ke*vel)
    z(prefix+"dust Euler",DE(vel)+b*v*vel+P0+b*w)
    ok(prefix+"positive wave number",LL(m)>0,4*LL(m))
D5=s.Matrix([[-m*Y(m),-Y(m),m,LL(m),1] for m in ms])
D4=s.Matrix([[m,1,m*Y(m),Y(m)] for m in ms])
det5=s.factor(D5.det());det4=s.factor(D4[:4,:].det())
ok("critical simultaneous scalar rank five",det5!=0,det5)
ok("critical simultaneous trace rank four",det4!=0,det4)
# Exact recorded jets; no true gain or background coupling is an inverse input.
gain=T**s.Rational(2,7)*s.exp(T/11)
h=1/T;hp=-1/T**2
mat5=[];mat4=[];y5=[];y4=[]
for m in ms:
    pp=gain*T**m;jj=Y(m)*pp;kk=LL(m)/T**2
    mat5.append([s.factor(-s.diff(jj,T)/pp),-Y(m),s.factor(s.diff(pp,T)/pp),kk,1])
    y5.append(s.factor((s.diff(jj,T,2)+kk*jj)/pp))
    mat4.append([s.factor(s.diff(pp,T)/pp),1,s.factor(s.diff(jj,T)/pp),Y(m)])
    y4.append(s.factor(2*s.diff(pp,T,2)/pp+8*h*s.diff(pp,T)/pp+4*hp+6*h*h))
D5=s.Matrix(mat5);D4=s.Matrix(mat4);y5=s.Matrix(y5);y4=s.Matrix(y4);epoch=s.Integer(2)
def recover_jets(D,y,n):
    D0=D[:n,:].subs(T,epoch);D1=D[:n,:].diff(T).subs(T,epoch);D2=D[:n,:].diff(T,2).subs(T,epoch)
    y0=y[:n,:].subs(T,epoch);y1=y[:n,:].diff(T).subs(T,epoch);y2=y[:n,:].diff(T,2).subs(T,epoch)
    inverse=D0.inv();t0=inverse*y0;t1=inverse*(y1-D1*t0);t2=inverse*(y2-D2*t0-2*D1*t1)
    return t0,t1,t2
th5,th51,th52=recover_jets(D5,y5,5)
th4,th41,th42=recover_jets(D4,y4,4)
for i in range(5):
    z("recorded trace row "+str(i+1),(D4.subs(T,epoch)*th4-y4.subs(T,epoch))[i])
B=th5[3]/2;Bp=th51[3]/2;Bpp=th52[3]/2
g=th4[2];gp=th41[2];qr=B*g;qp=Bp*g+B*gp
L=Bp/(2*B);Lp=Bpp/(2*B)-Bp*Bp/(2*B*B);hh=1/epoch;hp=-1/epoch**2
drift=(3*(hh-qr)-2*L-th5[0])/2
driftp=(3*(hp-qp)-2*Lp-th51[0])/2
cp=th5[1]+th5[0]*drift+drift*drift+driftp
kap=cp-qp-3*hh*qr+2*qr*qr-2*qr*L-L*L+Lp+3*hh*L
trace_a=th4[0]-4*drift
trace_c=th4[1]+6*qr*drift-8*hh*drift+2*drift**2-2*driftp
trace_f=th4[3]+g*drift
for name,got,expected in [
    ("B",B,s.Rational(2,3)),("trace G",g,s.Rational(3,4)/epoch),("q",qr,1/(2*epoch)),("q prime",qp,-1/(2*epoch**2)),
    ("gain drift",drift,s.Rational(2,7)/epoch+s.Rational(1,11)),("gain drift prime",driftp,-s.Rational(2,7)/epoch**2),
    ("kappa",kap,s.Rational(5,4)/epoch**2),("trace damping",trace_a,6*qr),("trace potential",trace_c,4*qp+8*hh*qr-2*qr**2-qr*g),
    ("trace slip",trace_f,gp+3*(hh-qr)*g-2*hp+2*qp-2*hh*qr+2*qr**2),
    ("critical denominator truly zero",4-6*B,0)]:
    z("combined recorded-jet inverse "+name,got-expected)
out={"stage":"Post-exposure correspondence to root's combined-gain suggestion; before combined author-code exposure",
     "checks":checks,"summary":{"passed":sum(v["pass"] for v in checks),"failed":sum(not v["pass"] for v in checks)},
     "critical_fixture":{"B":str(b*b),"exponents":[str(m) for m in ms],"scalar_rank_determinant":str(det5),"trace_rank_minor":str(det4),
                         "gain":str(gain),"epoch":str(epoch),"recovered_q":str(qr),"recovered_drift":str(drift),"recovered_kappa":str(kap)},
     "software":{"python":sys.version.split()[0],"sympy":s.__version__},"empirical_validation":False}
print(json.dumps(out,indent=2))
raise SystemExit(int(out["summary"]["failed"]!=0))


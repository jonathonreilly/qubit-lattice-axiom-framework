"""Independent matter-clock controls; no author imports or repository reads."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import json
import sys
import sympy as S

rows=[]
def note(message):
    print(message,file=sys.stderr,flush=True)
def zero(name,expression):
    residual=S.factor(S.cancel(expression))
    good=residual==0
    rows.append({"name":name,"pass":bool(good),"residual":str(residual)})
    note(("PASS " if good else "FAIL ")+name)
def truth(name,value,detail=None):
    good=bool(value)
    row={"name":name,"pass":good}
    if detail is not None:row["detail"]=str(detail)
    rows.append(row)
    note(("PASS " if good else "FAIL ")+name)

note("Direct lapse, scale-factor and scalar variation")
t=S.symbols("t",positive=True)
M,rho0=S.symbols("M rho0",positive=True)
aa=S.Function("a")(t);nn=S.Function("n")(t);ph=S.Function("phi")(t)
AF=S.Function("A")(ph);VF=S.Function("V")(ph)
ad=S.diff(aa,t);vd=S.diff(ph,t)
L=-3*M**2*aa*ad**2/nn+aa**3*vd**2/(2*nn)-nn*aa**3*VF-nn*rho0*AF
gauge=lambda e:e.subs(nn,1).doit()
lapse=gauge(S.diff(L,nn)/aa**3)
scale=gauge((S.diff(S.diff(L,ad),t)-S.diff(L,aa))/(-3*aa**2))
scalar=gauge((S.diff(S.diff(L,vd),t)-S.diff(L,ph))/aa**3)
HE=ad/aa;rr=rho0*AF/aa**3
fried=3*M**2*HE**2-vd**2/2-VF-rr
accel=M**2*(2*S.diff(aa,t,2)/aa+HE**2)+vd**2/2-VF
zero("lapse gives Friedmann with positive dust",lapse-fried)
zero("scale-factor variation before constraints",scale-accel)
zero("Raychaudhuri uses acceleration minus Friedmann",scale-lapse-(2*M**2*S.diff(HE,t)+vd**2+rr))
zero("particle action scalar charge sign",scalar-(S.diff(ph,t,2)+3*HE*vd+S.diff(VF,ph)+rho0*S.diff(AF,ph)/aa**3))
zero("bare particle conservation gives Einstein exchange",S.diff(rr,t)+3*HE*rr-S.diff(AF,ph)/AF*vd*rr)

note("Independent jet algebra in matter time")
X,X1,X2=S.symbols("x x1 x2",real=True)
h,h1,h2,h3,b,b1,b2,b3,k,k1=S.symbols("h h1 h2 h3 b b1 b2 b3 kappa kappa1",real=True)
jets=[(h,h1),(h1,h2),(h2,h3),(b,b1),(b1,b2),(b2,b3),(k,k1)]
dtpartial=lambda e:sum(S.diff(e,a)*d for a,d in jets)
dtfull=lambda e:dtpartial(e)+S.diff(e,X)*X1+S.diff(e,X1)*X2
u=h-b*X
Q=(2*b**2-1)*X**2+2*(b1-b*h)*X-2*h1
dust=2*b*X1+Q
zero("Raychaudhuri physical-time density",dust-(-2*(dtfull(u)+b*X*u)-X**2))
ss,ss1,AA=S.symbols("s s1 A",positive=True)
zero("Einstein dust exchange yields physical-time transport",
     (2*b*X*ss+ss1)+(3*u-b*X)*ss-(ss1-(2*b*X-3*h)*ss))
force=-X1-3*h*X+2*b*X**2
Ed=S.expand(dtfull(dust)-(2*b*X-3*h)*dust)
Em=S.expand(-(dtfull(force)+2*b*X*force-k*X+3*b*u*dust))
C=3*h-2*b*X-6*b**2*u
R=(3*h1+k)*X+(6*b*h-2*b1)*X**2-4*b**2*X**3-3*b*u*Q
zero("mass transport gives retained second-order equation",Em-(X2+C*X1+R))
zero("dust second-order coefficients",Ed-(2*b*X2+(4*b1+4*b*h-2*X)*X1+dtpartial(Q)-(2*b*X-3*h)*Q))
z=3*u**2-X**2/2-ss
zprime=dtfull(z)+S.diff(z,ss)*ss1
scalar_retained=X*(X1+b*X**2+3*u*X+b*ss)+zprime+2*b*X*z
ray_h1=b1*X+b*X1-b*X*u-(X**2+ss)/2
zero("undifferentiated scalar follows from retained equations",
     (scalar_retained-(-ss1+(2*b*X-3*h)*ss)).subs(h1,ray_h1))
c4=6*b**4-2*b**2+1
Delta=c4*X-2*b1-b*h*(6*b**2-1)
N=S.expand((Ed-2*b*Em+2*Delta*X1)/2)
truth("eliminated numerator has no velocity derivatives",not (N.has(X1) or N.has(X2)))
Ncompact=(dtpartial(Q)+(3*h-2*b*X+6*b**2*u)*Q
          -2*b*((3*h1+k)*X+(6*b*h-2*b1)*X**2-4*b**2*X**3))/2
zero("independent elimination matches compact numerator",N-Ncompact)
zero("elimination identity",Ed-2*b*Em+2*Delta*X1-2*N)
zero("denominator slope is strictly positive completed square",c4-(6*(b**2-S.Rational(1,6))**2+S.Rational(5,6)))
n3=b*(1-b**2)*(6*b**2+1)
n2=2*b*(1-3*b**2)*b1+(12*b**4-4*b**2-S.Rational(3,2))*h
n1=b2+2*(1+3*b**2)*h*b1+2*b*(3*b**2-1)*h1-3*b*(1+2*b**2)*h**2-b*k
n0=-h2-3*h*(1+2*b**2)*h1
for power,expected in [(3,n3),(2,n2),(1,n1),(0,n0)]:
    zero("hand numerator coefficient x^"+str(power),S.Poly(N,X).coeff_monomial(X**power)-expected)

note("Polynomial construction and independent leading-balance checks")
P=S.expand(Delta**2*dtpartial(N)-Delta*N*dtpartial(Delta)
           +Delta*N*S.diff(N,X)-N**2*S.diff(Delta,X)
           +C*N*Delta**2+R*Delta**3)
flow=N/Delta
mass_on_flow=dtpartial(flow)+S.diff(flow,X)*flow+C*flow+R
zero("polynomial equals denominator-cleared mass equation",S.together(Delta**3*mass_on_flow)-P)
poly=S.Poly(P,X);lead=poly.coeff_monomial(X**6)
expected_lead=-b**2*c4*(6*b**2-1)*(12*b**2-7)
truth("generic polynomial degree is six",poly.degree()==6)
zero("hand degree-six leading coefficient",lead-expected_lead)
balance=c4**3*(2*(n3/c4)**2+S.Poly(C,X).coeff_monomial(X)*(n3/c4)+S.Poly(R,X).coeff_monomial(X**3))
zero("independent large-x mass balance",balance-expected_lead)
zero("transported density numerator leading coefficient",
     S.Poly(S.expand(2*b*N+Q*Delta),X).coeff_monomial(X**3)-(6*b**2-1))
special={h:2,h1:-3,h2:5,h3:-7,b1:0,b2:0,b3:0,k:11,k1:13}
degrees={}
for name,bvalue in [("zero",S.Integer(0)),("one",S.Integer(1)),("critical_one_sixth",S.sqrt(6)/6),("critical_seven_twelfths",S.sqrt(21)/6)]:
    specialized=S.Poly(P.subs(special).subs(b,bvalue),X)
    degrees[name]=specialized.degree()
truth("identically zero coupling has degree at most four",degrees["zero"]<=4,degrees["zero"])
truth("unit coupling retains sixth degree",degrees["one"]==6,degrees["one"])
truth("first critical squared coupling loses leading degree",degrees["critical_one_sixth"]<=5,degrees["critical_one_sixth"])
truth("second critical squared coupling loses leading degree",degrees["critical_seven_twelfths"]<=5,degrees["critical_seven_twelfths"])
instant_zero=S.Poly(P.subs({**special,b:0,b1:1}),X)
truth("an isolated coupling zero may have fifth degree",instant_zero.degree()==5)
zero("isolated-zero fifth coefficient is minus bprime",instant_zero.coeff_monomial(X**5)+1)

T=S.symbols("tau",positive=True)
def jet_values(ht,bt,kt):
    return {h:ht,h1:S.diff(ht,T),h2:S.diff(ht,T,2),h3:S.diff(ht,T,3),
            b:bt,b1:S.diff(bt,T),b2:S.diff(bt,T,2),b3:S.diff(bt,T,3),
            k:kt,k1:S.diff(kt,T)}
fixture_results={}
def power_fixture(name,p,c,hcoef,xcoef,scoef,kcoef,singular=False):
    note("Forward power fixture "+name)
    q=3*p-2;at=t**p;phi=c*S.log(t);v=c/t;AE=t**q
    r=(2*p-c**2)/t**2;rho=r/AE;V=(3*p**2-2*p+c**2/2)/t**2
    phider=lambda e:S.diff(e,t)/v
    alpha=phider(AE)/AE
    tau=t**(q+1)/(q+1)
    kap=S.cancel((phider(phider(V))+rho*phider(phider(AE)))/AE**2)
    zero(name+" Friedmann",3*(p/t)**2-v**2/2-V-r)
    zero(name+" Raychaudhuri",-2*S.diff(p/t,t)-v**2-r)
    zero(name+" scalar equation",S.diff(v,t)+3*(p/t)*v+phider(V)+alpha*r)
    zero(name+" dust equation",S.diff(r,t)+3*(p/t)*r-alpha*v*r)
    zero(name+" matter clock derivative",S.diff(tau,t)-AE)
    zero(name+" transformed expansion",S.diff(S.log(AE*at),t)/AE-hcoef/tau)
    zero(name+" transformed scalar speed",v/AE-xcoef/tau)
    zero(name+" transformed density",r/AE**2-scoef/tau**2)
    zero(name+" fixed-rho response",kap-kcoef/tau**2)
    bt=S.cancel(q/c);ht=hcoef/T;xt=xcoef/T;kt=kcoef/T**2
    j=jet_values(ht,bt,kt);j.update({X:xt,X1:S.diff(xt,T),X2:S.diff(xt,T,2)})
    zero(name+" direct density",dust.subs(j)-scoef/T**2)
    zero(name+" direct dust transport",Ed.subs(j))
    zero(name+" direct curvature compatibility",Em.subs(j))
    dv=S.factor(Delta.subs(j));nv=S.factor(N.subs(j))
    pv=S.factor(P.subs(j))
    zero(name+" polynomial necessity",pv)
    truth(name+" positive density coefficient",scoef>0)
    truth(name+" nonzero velocity coefficient",xcoef!=0)
    if singular:
        zero(name+" singular elimination denominator",dv)
        zero(name+" singular elimination numerator",nv)
    else:
        truth(name+" nonzero elimination denominator",dv!=0)
        zero(name+" first-order flow",S.diff(xt,T)-nv/dv)
        zero(name+" density-dependent curvature increment",
             kap-(phider(phider(V))+S.diff(alpha,t)/v*r)/AE**2-bt**2*r/AE**2)
        truth(name+" wrong curvature rejects same history",S.factor(Em.subs({**j,k:kt+1}))!=0)
    fixture_results[name]={"b":str(bt),"delta":str(dv),"N":str(nv),"density_coefficient":str(scoef),"curvature_coefficient":str(kcoef)}

power_fixture("regular_p2",S.Integer(2),S.Integer(1),S.Rational(6,5),S.Rational(1,5),S.Rational(3,25),S.Rational(82,25))
power_fixture("singular_positive_history",S.Rational(12,17),S.Rational(4,17),S.Rational(14,19),S.Rational(4,19),S.Rational(392,361),S.Rational(2410,361),True)

note("Variable coupling fixture and all required input jets")
Av=2*t-t**3;rv=2/t**2-1;rh=t**-3;Vv=t**-2+S.Rational(1,2);vv=S.Integer(1)
D=lambda e:S.cancel(S.diff(e,t)/Av)
xv=1/Av;bv=S.cancel(S.diff(Av,t)/Av)
hv=S.cancel((1/t+S.diff(Av,t)/Av)/Av)
sv=S.cancel(rv/Av**2)
kv=S.cancel((S.diff(Vv,t,2)+rh*S.diff(Av,t,2))/Av**2)
zero("varying fixture Friedmann",3/t**2-vv**2/2-Vv-rv)
zero("varying fixture Raychaudhuri",2/t**2-vv**2-rv)
zero("varying fixture scalar",3/t+S.diff(Vv,t)+bv*rv)
zero("varying fixture dust",S.diff(rv,t)+3*rv/t-bv*rv)
zero("varying fixture clock derivative",S.diff(t**2-t**4/4,t)-Av)
zero("varying fixture expansion formula",hv-4*(1-t**2)/(t**2*(2-t**2)**2))
zero("varying fixture speed formula",xv-1/(t*(2-t**2)))
zero("varying fixture density formula",sv-1/(t**4*(2-t**2)))
zero("varying fixture response formula",kv-6*(1-t**2)/(t**6*(2-t**2)**2))
zero("varying direct density",
     -2*(D(hv-bv*xv)+bv*xv*(hv-bv*xv))-xv**2-sv)
zero("varying direct dust transport",D(sv)-(2*bv*xv-3*hv)*sv)
fv=-D(xv)-3*hv*xv+2*bv*xv**2
zero("varying direct mass transport",D(fv)+2*bv*xv*fv-kv*xv+3*bv*(hv-bv*xv)*sv)
loc=S.Rational(1,2)
local={}
for symbols,expr in [([h,h1,h2,h3],hv),([b,b1,b2,b3],bv),([k,k1],kv),([X,X1,X2],xv)]:
    current=expr
    for symbol in symbols:
        local[symbol]=S.cancel(current.subs(t,loc))
        current=D(current)
ld=S.cancel(Delta.subs(local));ln=S.cancel(N.subs(local))
truth("varying local elimination chart exists",ld!=0,ld)
truth("varying local physical density positive",sv.subs(t,loc)>0)
zero("varying local first-order flow",local[X1]-ln/ld)
zero("varying local polynomial",P.subs(local))
truth("varying local wrong curvature fails filter",S.cancel(P.subs({**local,k:local[k]+1}))!=0)
truth("varying fixture exercises nonzero b third derivative",local[b3]!=0,local[b3])
truth("varying fixture exercises nonzero response derivative",local[k1]!=0,local[k1])

note("Normalization, missing integration constants and continuous ambiguity")
lam=S.symbols("lambda",positive=True)
ap=(5*T)**S.Rational(4,5)
aj=(5*T)**S.Rational(6,5)
xp=1/(5*T);bp=S.Integer(4);sp=3/(25*T**2)
phip=S.log(5*T)/5
Ap=lam*ap;Vp=lam**2*S.Rational(17,2)*(5*T)**S.Rational(-2,5)
rp=Ap**2*sp;rhop=rp/Ap
dp=lambda e:S.diff(e,T)/xp
zero("normalization preserves coupling",S.diff(Ap,T)/Ap-bp*xp)
zero("normalization preserves response",(dp(dp(Vp))+rhop*dp(dp(Ap)))/Ap**2-S.Rational(82,25)/T**2)
zero("normalization rescales bare comoving density",rhop*(aj/Ap)**3-3/lam**2)
zero("registered physical density fixes A squared",sp/(rhop/Ap**3)-Ap**2)
zero("registered bare normalization fixes A squared",sp*aj**3/(3/lam**2)-Ap**2)
cc,dd=S.symbols("affine_slope affine_constant",real=True)
extra=cc*phip+dd
zero("affine potential invisible to curvature",dp(dp(extra)))
zero("linear potential changes original scalar force",dp(extra)-cc)
truth("constant potential changes Friedmann",(-extra).subs({cc:0,dd:1})==-1)
cf=S.symbols("c",nonzero=True,real=True)
family=jet_values(S.Rational(2,3)/T,S.Integer(0),2/T**2)
family_candidate={**family,X:cf/T,X1:-cf/T**2,X2:2*cf/T**3}
zero("uncoupled family direct density",dust.subs(family_candidate)-(S.Rational(4,3)-cf**2)/T**2)
zero("uncoupled family dust transport",Ed.subs(family_candidate))
zero("uncoupled family mass compatibility",Em.subs(family_candidate))
zero("uncoupled family entire filter vanishes",P.subs(family))
zero("uncoupled family first-order flow",S.cancel((N/Delta).subs(family_candidate))+cf/T**2)
truth("uncoupled positive-speed member is physical",S.Rational(4,3)-S.Rational(1,4)>0)
truth("uncoupled negative-speed member is physical",S.Rational(4,3)-1>0)

result={"scope":"Independent exact synthetic action-first matter-clock controls; no author matter-clock exposure or empirical validation",
        "software":{"python":sys.version.split()[0],"sympy":S.__version__},
        "summary":{"passed":sum(r["pass"] for r in rows),"failed":sum(not r["pass"] for r in rows)},
        "checks":rows,
        "algebra":{"numerator":str(N),"denominator":str(Delta),"polynomial":str(P),
                   "degree":poly.degree(),"degree_six_coefficient":str(S.factor(lead)),
                   "specialized_degrees":degrees},
        "forward_fixtures":fixture_results,
        "variable_fixture_local_jets":{str(a):str(v) for a,v in local.items()},
        "variable_fixture_local_delta":str(ld),
        "author_matter_clock_sources_read":False,
        "author_matter_clock_code_imported":False}
print(json.dumps(result,indent=2))
raise SystemExit(int(result["summary"]["failed"]!=0))

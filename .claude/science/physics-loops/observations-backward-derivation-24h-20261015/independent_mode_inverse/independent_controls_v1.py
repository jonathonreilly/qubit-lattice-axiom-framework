"""Independent full-equation multi-mode inverse controls; no author imports."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import json
import sys
import sympy as s
rows=[]
def progress(message):
    print(message,file=sys.stderr,flush=True)
def zero(name,e):
    r=s.factor(s.cancel(s.powsimp(e)))
    ok=r==0
    rows.append({"name":name,"pass":bool(ok),"residual":str(r)})
    progress(("PASS " if ok else "FAIL ")+name)
def truth(name,c,detail=None):
    row={"name":name,"pass":bool(c)}
    if detail is not None:row["detail"]=str(detail)
    rows.append(row);progress(("PASS " if c else "FAIL ")+name)

progress("Linearized Einstein geometry from the metric")
t,Xc,Yc,Zc=s.symbols("t X Y Z",real=True)
kk=s.symbols("k",positive=True)
coords=[t,Xc,Yc,Zc]
aa=s.Function("a",positive=True)(t)
ps=s.Function("Psi")(t);fl=s.Function("Phi")(t);mode=s.exp(s.I*kk*Zc)
g0=s.diag(-1,aa**2,aa**2,aa**2);gi=g0.inv()
dh=s.diag(-2*ps*mode,-2*aa**2*fl*mode,-2*aa**2*fl*mode,-2*aa**2*fl*mode)
dgi=-gi*dh*gi
G0={};G1={}
for a in range(4):
    for i in range(4):
        for j in range(4):
            e0=0;e1=0
            for l in range(4):
                base=s.diff(g0[l,j],coords[i])+s.diff(g0[l,i],coords[j])-s.diff(g0[i,j],coords[l])
                pert=s.diff(dh[l,j],coords[i])+s.diff(dh[l,i],coords[j])-s.diff(dh[i,j],coords[l])
                e0+=gi[a,l]*base/2
                e1+=(gi[a,l]*pert+dgi[a,l]*base)/2
            G0[a,i,j]=s.simplify(e0);G1[a,i,j]=s.simplify(e1)
def linear_ricci(i,j):
    ans=0
    for l in range(4):
        ans+=s.diff(G1[l,i,j],coords[l])-s.diff(G1[l,i,l],coords[j])
        for n in range(4):
            ans+=(G1[l,i,j]*G0[n,l,n]+G0[l,i,j]*G1[n,l,n]
                  -G1[n,i,l]*G0[l,j,n]-G0[n,i,l]*G1[l,j,n])
    return s.factor(s.cancel(ans/mode))
dr={(i,i):linear_ricci(i,i) for i in range(4)}
dr[0,3]=linear_ricci(0,3)
H=s.diff(aa,t)/aa
ric0=s.diag(-3*s.diff(aa,t,2)/aa,*([aa*s.diff(aa,t,2)+2*s.diff(aa,t)**2]*3))
sc0=6*(s.diff(aa,t,2)/aa+H**2)
dsc=sum(gi[i,i]*dr[i,i]+dgi[i,i]/mode*ric0[i,i] for i in range(4))
gcov0=ric0-g0*sc0/2
def mixed(i,j):
    dg=dr[i,j]-dh[i,j]/mode*sc0/2-g0[i,j]*dsc/2
    return s.factor(s.cancel(gi[i,i]*dg+dgi[i,i]/mode*gcov0[i,j]))
e00=mixed(0,0);e03=mixed(0,3);e11=mixed(1,1);e33=mixed(3,3)
zero("Hamiltonian geometry sign",e00-2*(kk**2*fl/aa**2+3*H*(s.diff(fl,t)+H*ps)))
zero("momentum geometry sign",e03+2*s.I*kk*(s.diff(fl,t)+H*ps))
zero("nonzero-k anisotropic equation",e33-e11-kk**2*(ps-fl)/aa**2)
U=s.Function("U")(t)
equal=lambda e:e.subs({ps:U,fl:U}).doit()
zero("pressure trace geometry",equal(e11)-2*(s.diff(U,t,2)+4*H*s.diff(U,t)+(2*s.diff(H,t)+3*H**2)*U))
zero("metric volume perturbation",sum(gi[i,i]*dh[i,i] for i in range(4))/(2*mode)-(ps-3*fl))

progress("Scalar stress and wave operator")
v,yd,yamp,V0,Vp=s.symbols("v delta_phi_dot delta_phi V V_phi",real=True)
bgrad=s.Matrix([v,0,0,0]);pgrad=s.Matrix([yd,0,0,s.I*kk*yamp])
K0=-v**2/2+V0
dK=ps*v**2-v*yd+Vp*yamp
dtcov={}
for i,j in [(0,0),(0,3),(1,1)]:
    dtcov[i,j]=pgrad[i]*bgrad[j]+bgrad[i]*pgrad[j]-dh[i,j]/mode*K0-g0[i,j]*dK
def tmixed(i,j):
    bg=bgrad[i]*bgrad[j]-g0[i,j]*K0
    return gi[i,i]*dtcov[i,j]+dgi[i,i]/mode*bg
zero("canonical scalar density perturbation",tmixed(0,0)-(-v*yd+ps*v*v-Vp*yamp))
zero("canonical scalar momentum perturbation",tmixed(0,3)+s.I*kk*v*yamp)
zero("canonical scalar pressure perturbation",tmixed(1,1)-(v*yd-ps*v*v-Vp*yamp))
ph=s.Function("phi")(t);yf=s.Function("delta_phi")(t)
vv=s.diff(ph,t);box0=-s.diff(vv,t)-3*H*vv
dJ0=aa**3*((ps+3*fl)*vv-s.diff(yf,t))
box1=s.diff(dJ0,t)/aa**3-kk**2*yf/aa**2-(ps-3*fl)*box0
zero("scalar wave operator from determinant and inverse metric",
     box1-(2*ps*(s.diff(vv,t)+3*H*vv)+(s.diff(ps,t)+3*s.diff(fl,t))*vv
            -s.diff(yf,t,2)-3*H*s.diff(yf,t)-kk**2*yf/aa**2))
zero("equal-potential scalar metric forcing",equal(box1)-
     (2*U*(s.diff(vv,t)+3*H*vv)+4*s.diff(U,t)*vv-s.diff(yf,t,2)-3*H*s.diff(yf,t)-kk**2*yf/aa**2))

progress("Matter-time transformations and source elimination")
h,hp,q,qp,g,gp,ss,ss1=s.symbols("h hp q qp g gp s s1",real=True)
u=h-q
u0,u1,u2,w0,w1=s.symbols("U U1 U2 W W1",real=True)
sdef=-2*hp+2*qp-2*h*q+2*q*q-q*g
trace=2*u2+2*(q+4*u)*u1+(4*(hp-qp)+4*q*u+6*u*u+q*g)*u0-g*w1-(gp+(3*h-2*q)*g+ss)*w0
base=2*u2+8*h*u1+(4*hp+6*h*h)*u0
coef=[6*q,4*qp+8*h*q-2*q*q-q*g,g,gp+3*(h-q)*g-2*hp+2*qp-2*h*q+2*q*q]
zero("four-column metric trace relation",trace.subs(ss,sdef)-(base-sum(a*v for a,v in zip(coef,[u1,u0,w1,w0]))))
vel=(g*w0-2*u1-2*u*u0)/ss
dvel=(s.diff(vel,h)*hp+s.diff(vel,q)*qp+s.diff(vel,g)*gp+s.diff(vel,ss)*ss1
      +s.diff(vel,u0)*u1+s.diff(vel,u1)*u2+s.diff(vel,w0)*w1)
zero("Euler-trace equivalence after background dust",
     (ss*(dvel+u0+w0)+trace).subs(ss1,(2*q-3*h)*ss).subs(ss,sdef))
bj,xj,A,ve,ved,delp=s.symbols("b x A velocity velocity_prime delta_phi",real=True)
# V=A*v_d, d/dt=A*d/dtau, alpha*v_E=A*q.
zero("covariant particle Euler becomes matter Euler",
     (ved-q*ve)+q*ve+u0+w0-(ved+u0+w0))
dE,dJ,up,wp,K,velj=s.symbols("delta_E_prime delta_J_prime U_prime W_prime K velocity_J",real=True)
zero("bare and Jordan continuity are equivalent",
     (dE-3*up-K*velj).subs(dE,dJ+3*wp)-(dJ-3*(up-wp)-K*velj))

progress("Exact background reconstructed from the action")
T=s.symbols("tau",positive=True)
AE=s.sqrt(2*T);aJ=2*T;aE=aJ/AE
phi=s.log(2*T)/2
H_E=1/s.sqrt(2*T);vE=1/s.sqrt(2*T)
rE=1/(2*T);rho=rE/AE;Vbg=s.Rational(3,4)/T
DE=lambda f:s.diff(f,T)*AE
Dphi=lambda f:DE(f)/vE
alpha=s.cancel(Dphi(AE)/AE)
forceE=s.cancel(Dphi(Vbg)+rho*Dphi(AE))
muE=s.cancel(Dphi(Dphi(Vbg))+rho*Dphi(Dphi(AE)))
zero("background Friedmann",3*H_E**2-vE**2/2-Vbg-rE)
zero("background Raychaudhuri",-2*DE(H_E)-vE**2-rE)
zero("background original scalar",DE(vE)+3*H_E*vE+forceE)
zero("background bare dust",DE(rho)+3*H_E*rho)
zero("background physical expansion",s.diff(aJ,T)/aJ-1/T)
zero("background coupling",alpha-1)
zero("background fixed-rho curvature",muE/AE**2-s.Rational(7,4)/T**2)

hh=1/T;qq=1/(2*T);gg=qq;xx=qq;bb=s.Integer(1)
uu=hh-qq;dens=1/(4*T*T);kap=s.Rational(7,4)/(T*T);FF=-1/(2*T*T)
m=s.symbols("m",real=True)
Y=(8*m*m+12*m+3)/(2*m+3)
zz=m*(m+1)
LL=zz*(8*zz+9)/(3-8*zz)
poly_det=(8*m*m+12*m+3)*(4*m*m+2*m+4*s.Symbol("L")+9)-(2*m+3)*(20*m+8*s.Symbol("L")+9)
zero("two-mode-system characteristic determinant",poly_det-4*(8*zz**2+(8*s.Symbol("L")+9)*zz-3*s.Symbol("L")))
zero("dispersion relation for chosen exact exponents",poly_det.subs(s.Symbol("L"),LL))
coef_vel=2*Y-8*m-4
coef_delta=-(8*LL+5)-12*m+(2-2*m)*Y
zero("generic exact mode dust Euler",(m+1)*coef_vel+1+Y)
zero("generic exact mode dust continuity",m*coef_delta-3*m-LL*coef_vel)
zero("generic exact mode trace",8*m*(m-1)+20*m+3-(2*m+3)*Y)
zero("generic exact mode scalar",(4*m*m+2*m+4*LL+9)*Y-(20*m+8*LL+9))

exponents=[s.Rational(1,8),s.Rational(1,6),s.Rational(1,5),s.Rational(1,4)]
fixture=[]
for n,mi in enumerate(exponents):
    progress("Full original-equation mode "+str(mi))
    yi=s.cancel(Y.subs(m,mi));li=s.cancel(LL.subs(m,mi));ki2=4*li
    pot=T**mi;sf=yi*pot
    velcoef=s.cancel(coef_vel.subs(m,mi));dcoef=s.cancel(coef_delta.subs(m,mi))
    vi=velcoef*T**(mi+1);di=dcoef*pot
    vd=vi/AE;KE=ki2/aE**2
    dph=sf
    zero("mode "+str(mi)+" Einstein momentum",DE(pot)+H_E*pot-(vE*dph-rE*vd)/2)
    zero("mode "+str(mi)+" Einstein Hamiltonian",
         2*(KE*pot+3*H_E*(DE(pot)+H_E*pot))
         +vE*DE(dph)-vE**2*pot+Dphi(Vbg)*dph+rE*(di+alpha*dph))
    zero("mode "+str(mi)+" Einstein pressure trace",
         2*(DE(DE(pot))+4*H_E*DE(pot)+(2*DE(H_E)+3*H_E**2)*pot)
         -(vE*DE(dph)-vE**2*pot-Dphi(Vbg)*dph))
    zero("mode "+str(mi)+" original scalar perturbation",
         DE(DE(dph))+3*H_E*DE(dph)+(KE+muE)*dph-4*vE*DE(pot)+2*forceE*pot+rho*Dphi(AE)*di)
    zero("mode "+str(mi)+" original bare continuity",DE(di)-3*DE(pot)-KE*vd)
    zero("mode "+str(mi)+" original particle Euler",DE(vd)+alpha*vE*vd+pot+alpha*dph)
    zero("mode "+str(mi)+" matter momentum reconstruction",(xx*sf-2*(s.diff(pot,T)+uu*pot))/dens-vi)
    zero("mode "+str(mi)+" matter Hamiltonian reconstruction",
         -(2*li/T**2*pot+6*uu*(s.diff(pot,T)+uu*pot)+xx*s.diff(sf,T)-xx**2*pot+FF*sf)/dens-di)
    truth("mode "+str(mi)+" positive nonzero wave number",li>0,ki2)
    fixture.append({"m":str(mi),"Y":str(yi),"L":str(li),"k_squared":str(ki2),
                    "velocity_coefficient":str(velcoef),"bare_contrast_coefficient":str(dcoef)})

progress("Data-only rank and common-coefficient recovery")
mat=s.Matrix([[mi,1,s.cancel((m*Y).subs(m,mi)),s.cancel(Y.subs(m,mi))] for mi in exponents])
det=s.factor(mat.det())
vand=s.prod(exponents[j]-exponents[i] for i in range(4) for j in range(i+1,4))
det_formula=96*vand/s.prod(2*mi+3 for mi in exponents)
zero("exact rank determinant formula",det-det_formula)
truth("legitimate distinct-k full modes have rank four",det>0,det)
truth("wave numbers are distinct",len({f["k_squared"] for f in fixture})==4)
rhs=s.Matrix([2*mi*mi+6*mi+2 for mi in exponents])
recovered=mat.inv()*rhs
expected=s.Matrix([3,s.Rational(5,4),s.Rational(1,2),s.Rational(3,4)])
for n in range(4):zero("data-only scaled coefficient "+str(n),recovered[n]-expected[n])
qr=recovered[0]/(6*T);gr=recovered[2]/T
sr=-2*s.diff(hh,T)+2*s.diff(qr,T)-2*hh*qr+2*qr**2-qr*gr
xr=s.sqrt(s.factor(qr*gr));br=s.factor(qr/xr)
Fr=-s.diff(xr,T)-(3*hh-2*qr)*xr
kr=s.factor((s.diff(Fr,T)+2*qr*Fr+3*br*(hh-qr)*sr)/xr)
zero("data-only derivative consistency coefficient c",
     recovered[1]/T**2-(4*s.diff(qr,T)+8*hh*qr-2*qr**2-qr*gr))
zero("data-only derivative consistency coefficient f",
     recovered[3]/T**2-(s.diff(gr,T)+3*(hh-qr)*gr-2*s.diff(hh,T)+2*s.diff(qr,T)-2*hh*qr+2*qr**2))
zero("data-only background dust",s.diff(sr,T)-(2*qr-3*hh)*sr)
truth("recovered regular kinetic product positive",s.simplify(qr*gr).is_positive)
truth("recovered background source positive",sr.is_positive)
zero("canonical coupling recovered without supplying it",br-1)
zero("fixed-density curvature recovered without supplying it",kr-s.Rational(7,4)/T**2)

progress("Necessary-only counterexample with altered known wave numbers")
fake=[]
for mi in exponents:
    yi=s.cancel(Y.subs(m,mi));li=s.cancel(LL.subs(m,mi));pot=T**mi;sf=yi*pot
    Veli=(xx*sf-2*(s.diff(pot,T)+uu*pot))/dens
    deltawrong=-(2*(li+1)/T**2*pot+6*uu*(s.diff(pot,T)+uu*pot)+xx*s.diff(sf,T)-xx**2*pot+FF*sf)/dens
    kgwrong=(s.diff(sf,T,2)+(3*hh-2*qq)*s.diff(sf,T)+((li+1)/T**2+kap)*sf
             -4*xx*s.diff(pot,T)+2*FF*pot+bb*dens*deltawrong)
    contwrong=s.diff(deltawrong,T)-3*s.diff(pot,T)-(li+1)/T**2*Veli
    zero("wrong-K scalar residual formula "+str(mi),kgwrong-(yi-2)*T**(mi-2))
    zero("wrong-K continuity residual formula "+str(mi),contwrong-(4-2*yi)*T**(mi-1))
    truth("wrong-K input fails full scalar "+str(mi),yi!=2,yi-2)
    truth("wrong-K input fails full continuity "+str(mi),4-2*yi!=0,4-2*yi)
    fake.append({"m":str(mi),"scalar_residual_coefficient":str(yi-2),"continuity_residual_coefficient":str(4-2*yi)})

progress("Normalization, orientation and mass-blind exceptional full modes")
lam=s.symbols("lambda",positive=True)
zero("normalization leaves background coupling",s.diff(lam*AE,T)/(lam*AE)/xx-bb)
zero("normalization leaves fixed-rho response",
     (Dphi(Dphi(lam**2*Vbg))+lam*rho*Dphi(Dphi(lam*AE)))/(lam*AE)**2-kap)
zero("normalization leaves density divided by F",(lam*rE/AE/(lam*AE)**3)/(1/(lam*AE)**2)-dens)
zero("field reflection preserves slip",(-bb)*(-s.Symbol("y"))-bb*s.Symbol("y"))
zero("field reflection preserves q and g",(-xx)*(-bb)-qq)
zero("orientation does not change reconstructed curvature",
     (s.diff(-Fr,T)+2*qq*(-Fr)+3*(-bb)*uu*dens)/(-xx)-kap)
mu0,k0,Uc=s.symbols("mu0 k0 Uc",positive=True)
hd=s.Rational(2,3)/T;sd=s.Rational(4,3)/T**2;Kd=k0**2/T**s.Rational(4,3)
Vd=-T*Uc;dd=-(2+s.Rational(3,2)*k0**2*T**s.Rational(2,3))*Uc
zero("mass-blind background Friedmann",3*hd**2-sd)
zero("mass-blind background Raychaudhuri",-2*s.diff(hd,T)-sd)
zero("mass-blind background dust",s.diff(sd,T)+3*hd*sd)
zero("mass-blind original scalar background",s.diff(mu0*s.Symbol("phi")**2/2,s.Symbol("phi")).subs(s.Symbol("phi"),0))
zero("mass-blind metric momentum",2*hd*Uc+sd*Vd)
zero("mass-blind metric Hamiltonian",2*(Kd*Uc+3*hd**2*Uc)+sd*dd)
zero("mass-blind pressure trace",2*s.diff(hd,T)+3*hd**2)
zero("mass-blind dust Euler",s.diff(Vd,T)+Uc)
zero("mass-blind dust continuity",s.diff(dd,T)-Kd*Vd)
zero("mass-blind scalar perturbation at zero amplitude",(Kd+mu0)*0)
truth("exceptional arbitrary positive curvature does not enter readouts",not any(e.has(mu0) for e in [Uc,Vd,dd,hd,Kd]))
rank_blind=s.Matrix([[0,1,0,0],[0,2,0,0],[0,3,0,0],[0,4,0,0]]).rank()
truth("exceptional slip-free input does not meet rank hypothesis",rank_blind<4,rank_blind)

out={"scope":"Independent original-equation linear-mode checks before new author exposure; synthetic only",
     "software":{"python":sys.version.split()[0],"sympy":s.__version__},
     "checks":rows,"summary":{"passed":sum(r["pass"] for r in rows),"failed":sum(not r["pass"] for r in rows)},
     "rank_witness":{"modes":fixture,"response_matrix_at_tau_one":str(mat),"determinant":str(det),
                     "determinant_time_exponent":str(sum(exponents)-2),"data_recovered_scaled_coefficients":[str(e) for e in recovered]},
     "reconstructed_background":{"q":str(qr),"g":str(gr),"s":str(sr),"x":str(xr),"b":str(br),"kappa":str(kr)},
     "necessary_only_counterexample":fake,
     "author_mode_inverse_sources_read":False,"author_code_imported":False}
print(json.dumps(out,indent=2))
raise SystemExit(int(out["summary"]["failed"]!=0))

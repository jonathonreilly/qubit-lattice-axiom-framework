#!/usr/bin/env python3
"""Root's first-order action/constraint controls; no empirical input or fit."""
import hashlib
import json
from pathlib import Path
import sys

import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]


def zero(name,expr):
    r=s.factor(s.cancel(s.trigsimp(expr)))
    checks.append({"name":name,"pass":r==0,"residual":str(r)})


def truth(name,condition,evidence):
    checks.append({"name":name,"pass":bool(condition),"evidence":str(evidence)})


t,z,eps=s.symbols("t z eps",real=True)
wave,M=s.symbols("wave M",positive=True)
a,ph,u,psi,phi,rhob,delta,U=[s.Function(n)(t) for n in ['a','ph','u','psi','phi','rhob','delta','U']]
co=s.cos(wave*z)
pertfield=ph+eps*u*co
volume=a**3*(1+eps*(psi-3*phi)*co)
gtt=-1+2*eps*psi*co
gzz=(1+2*eps*phi*co)/a**2
box=(s.diff(volume*gtt*s.diff(pertfield,t),t)+s.diff(volume*gzz*s.diff(pertfield,z),z))/volume
box1=s.simplify(s.diff(box,eps).subs(eps,0)/co)
expectedbox=-s.diff(u,t,2)-3*s.diff(a,t)/a*s.diff(u,t)-wave**2*u/a**2+s.diff(ph,t)*(s.diff(psi,t)+3*s.diff(phi,t))+2*psi*(s.diff(ph,t,2)+3*s.diff(a,t)/a*s.diff(ph,t))
zero("linear covariant Box from determinant and inverse metric",box1-expectedbox)

# A conformally flat spatial geometry, independently evaluated in ADM form.
omega=s.log(a)-eps*phi*co
R3=s.exp(-2*omega)*(-4*s.diff(omega,z,2)-2*s.diff(omega,z)**2)
R31=s.diff(R3,eps).subs(eps,0)/co
zero("spatial scalar curvature perturbation",R31+4*wave**2*phi/a**2)
Kdiag=-(s.diff(a,t)/a-eps*s.diff(phi,t)*co)*(1-eps*psi*co)
Kpart1=s.diff(6*Kdiag**2,eps).subs(eps,0)/co
zero("extrinsic Hamiltonian term",Kpart1+12*s.diff(a,t)/a*(s.diff(phi,t)+s.diff(a,t)/a*psi))

# Particle-number continuity, using bare PROPER density and the perturbed lapse.
rho=rhob*(1+eps*delta*co)
fourzero=1-eps*psi*co
fourz=eps*s.diff(U*co,z)/a**2
continuity=s.diff(volume*rho*fourzero,t)+s.diff(volume*rho*fourz,z)
cont1=s.diff(continuity,eps).subs(eps,0).subs(s.diff(rhob,t),-3*s.diff(a,t)/a*rhob)/(a**3*rhob*co)
zero("bare current conservation gives density and velocity equation",cont1-(s.diff(delta,t)-3*s.diff(phi,t)-wave**2*U/a**2))

H,v,vd,alpha,r,mu,force,P,Pd,ud,udd,K2,S,Vp=s.symbols("H v vd alpha r mu force P Pd ud udd K2 S Vp",real=True)
uu=s.symbols("uu",real=True)
# The field force must include the dust energy perturbation alpha*r*u.
depsilon=S+v*ud-v*v*P+(Vp+alpha*r)*uu
zero("proper dust and scalar energy use force Vp+alpha r",depsilon.subs(Vp,force-alpha*r)-(S+v*ud-v*v*P+force*uu))
constraint=K2*P+3*H*(Pd+H*P)+(S+v*ud-v*v*P+force*uu)/(2*M*M)
geom=(R31+Kpart1).subs({phi:P,psi:P,s.diff(phi,t):Pd,s.diff(a,t):H*a,wave**2:K2*a**2})
zero("Hamiltonian ADM constraint equals displayed Fourier equation",geom-2*(S+v*ud-v*v*P+force*uu)/M**2+4*constraint)

boxalg=box1.subs({s.diff(u,t,2):udd,s.diff(u,t):ud,s.diff(ph,t,2):vd,
                 s.diff(ph,t):v,s.diff(a,t):H*a,s.diff(psi,t):Pd,s.diff(phi,t):Pd,
                 psi:P,phi:P,u:uu,wave**2:K2*a*a})
scalar=udd+3*H*ud+(K2+mu)*uu+alpha*S-4*v*Pd+2*force*P
zero("full scalar equation follows from varied source at fixed bare rho",(boxalg-mu*uu-alpha*S).subs(vd,-3*H*v-force)+scalar)

Ssolve=s.solve(constraint,S)[0]
eliminated=udd+(3*H-alpha*v)*ud+(K2+mu-alpha*force)*uu-2*M*M*alpha*K2*P-(6*M*M*alpha*H+4*v)*Pd-(6*M*M*alpha*H*H-alpha*v*v-2*force)*P
zero("source elimination retains off-minimum force and metric derivatives",scalar.subs(S,Ssolve)-eliminated)

# Derive Euler by differentiating A*a^2*coordinate_velocity = A*grad(U).
Ud,theta,thetad=s.symbols("Ud theta thetad",real=True)
EulerU=Ud+alpha*v*U+P+alpha*uu
theta_derivative=-K2*Ud+2*H*K2*U
zero("particle momentum gives theta friction 2H+alpha v",(theta_derivative+(2*H+alpha*v)*(-K2*U)-K2*(P+alpha*uu))+K2*EulerU)
# ADM momentum: div(K^j_i-delta^j_i K)=-2 grad(Pdot+H P).
momentum=Pd+H*P-(v*uu+r*theta/K2)/(2*M*M)
zero("momentum constraint including scalar and dust velocity",(-2*(Pd+H*P)-(r*(-theta/K2)-v*uu)/M**2)+2*momentum)

# Conformal metric directly expanded about the matter-time background.
Aj=s.symbols("Aj",positive=True)
time_metric=-(1+2*eps*P)*(1+eps*alpha*uu)**2
spatial_metric=(1-2*eps*P)*(1+eps*alpha*uu)**2
PsiJ=-s.diff(time_metric,eps).subs(eps,0)/2
PhiJ=-s.diff(spatial_metric,eps).subs(eps,0)/2
zero("matter metric lapse potential",PsiJ-(P+alpha*uu))
zero("matter metric curvature potential",PhiJ-(P-alpha*uu))
zero("Weyl sum unchanged",PsiJ+PhiJ-2*P)
zero("conditional slip ratio",(PsiJ-PhiJ)/(PsiJ+PhiJ)-alpha*uu/P)

b=M*alpha
B=6*b*b*H*H-alpha*alpha*v*v-2*alpha*force
T=(6*b*b*H+4*alpha*v)*Pd/P-alpha/P*(udd+(3*H-alpha*v)*ud)
Cobs=alpha*uu/P
identity=(K2+mu-alpha*force)*Cobs-2*b*b*K2-B-T
zero("exact response identity follows without quasistatics",identity-alpha/P*eliminated)
zero("naive Yukawa residual accounting",(K2+mu)*Cobs-2*b*b*K2-alpha*force*Cobs-B-T-identity)
zero("uncoupled ratio zero does not require scalar zero",Cobs.subs(alpha,0))

# The clock/field transformation includes derivatives of A in v-dot.
h,x,xp,bb,kap=s.symbols("h x xp bb kap",real=True)
AE=s.symbols("AE",positive=True)
v_m=M*AE*x
H_m=AE*(h-bb*x)
vd_m=M*AE**2*(xp+bb*x*x)
force_m=-vd_m-3*H_m*v_m
zero("matter-time background force",force_m/AE**2+M*(xp+3*h*x-2*bb*x*x))
sub={alpha:bb/M,v:v_m,H:H_m,force:force_m,mu:AE**2*kap}
deff=kap+bb*xp+3*bb*h*x-2*bb*bb*x*x
seff=2*bb*xp+6*bb*h*x+6*bb*bb*h*h-12*bb**3*h*x+(6*bb**4-5*bb*bb)*x*x
zero("matter-time denominator is not bare curvature",((mu-alpha*force)/AE**2).subs(sub)-deff)
zero("matter-time source offset",(B/AE**2).subs(sub)-seff)

# Exact values on the already action-checked forward history at Einstein t=1:
# M=A=H=v=alpha=1; vdot=-1; F=-2; mu=7; h=2,x=1,x'=-2,kappa=7.
background={M:1,H:1,v:1,alpha:1,force:-2,mu:7}
zero("off-minimum forward background effective denominator",(mu-alpha*force).subs(background)-9)
zero("off-minimum forward background source offset",B.subs(background)-9)
matter_background={M:1,AE:1,h:2,x:1,xp:-2,bb:1,kap:7}
zero("same forward background in matter clock denominator",deff.subs(matter_background)-9)
zero("same forward background in matter clock source",seff.subs(matter_background)-9)

# These are algebraic instantaneous forcing examples, NOT full physical modes.
# S and udd are solved from the two equations; no assumption that other mode
# equations hold is made. They expose the bookkeeping error of pole=mu.
examples=[]
for kv in [s.Rational(1),s.Rational(10),s.Rational(100)]:
    selected={**background,K2:kv,P:1,Pd:s.Rational(1,7),uu:s.Rational(2,5),ud:s.Rational(1,3)}
    sv=s.factor(Ssolve.subs(selected))
    av=s.factor(s.solve(scalar,udd)[0].subs({**selected,S:sv}))
    full={**selected,S:sv,udd:av}
    zero(f"algebraic source example K2={kv} constraint",constraint.subs(full))
    zero(f"algebraic source example K2={kv} scalar equation",scalar.subs(full))
    zero(f"algebraic source example K2={kv} response identity",identity.subs(full))
    lhs=s.factor(((K2+mu)*Cobs-2*b*b*K2).subs(full))
    rhs=s.factor((alpha*force*Cobs+B+T).subs(full))
    truth(f"controlled residual triangle bound K2={kv}",abs(lhs)<=sum(abs(s.factor(term.subs(full))) for term in [alpha*force*Cobs,B,T]),lhs)
    examples.append({"K2":str(kv),"S":str(sv),"udd":str(av),"naive_numerator_residual":str(lhs),"identity_rhs":str(rhs)})

mutations={
    "omit alpha*r*u from total density":(alpha*r*uu).subs({alpha:1,r:2,uu:3}),
    "omit lapse force term in KG":(2*force*P).subs({force:-2,P:1}),
    "drop metric time source":((6*M*M*alpha*H+4*v)*Pd).subs({**background,Pd:1}),
    "identify effective denominator with mu":(-alpha*force).subs(background),
    "omit off-minimum numerator":B.subs(background),
    "omit mass-dependent Euler friction":(alpha*v*theta).subs({alpha:1,v:1,theta:2}),
}
for name,residual in mutations.items():
    truth("detect mutation: "+name,residual!=0,residual)

names=[Path(__file__).name,"SCALAR_RESPONSE_DERIVATION_v1.md","SCALAR_RESPONSE_NEUTRAL_CONTRACT_v1.json"]
result={"author":"/root","kind":"exact action/constraint mathematics and synthetic algebraic controls",
        "sympy":s.__version__,"source_sha256":{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in names},
        "checks":checks,"passed":sum(c["pass"] for c in checks),"failed":sum(not c["pass"] for c in checks),
        "algebraic_examples":examples,
        "limits":["Source elimination is necessary; not the full mode solution", "No empirical measurement map completed",
                  "T not set to zero or observationally bounded", "Clock/action/dust/linearization premises retained"]}
print(json.dumps(result,indent=2,sort_keys=True))
sys.exit(int(result['failed']>0))

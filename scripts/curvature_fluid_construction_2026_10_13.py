#!/usr/bin/env python3
"""Parent-authored conditional fluid/curvature reconstruction, no data fit."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction
import itertools
import mpmath as mp
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"outputs/curvature_fluid_construction_2026_10_13"
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
    "docs/CURVATURE_FLUID_CONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "outputs/curvature_fluid_construction_2026_10_13/NUMERICAL_FIXTURES_v1.json",
    "outputs/curvature_fluid_construction_2026_10_13/OFF_TRAJECTORY_FIXTURES_v2.json",
    "outputs/curvature_fluid_construction_2026_10_13/imports.json",
]
CHECKS=[]

def rat(v):
    return Fraction(str(v))

def val(v):
    v=rat(v)
    return mp.mpf(v.numerator)/v.denominator

def fmt(v):
    return mp.nstr(v,75)

def check(name,passed,**detail):
    CHECKS.append(dict(name=name,passed=bool(passed),**detail))

def near(name,actual,expected,tol="1e-65"):
    err=abs(actual-expected)/max(mp.mpf(1),abs(expected))
    check(name,err<=mp.mpf(tol),actual=fmt(actual),expected=fmt(expected),
          normalized_error=fmt(err),tolerance=tol)

def exact(name,expr):
    red=sp.factor(sp.cancel(expr))
    check(name,red==0,reduced=str(red))

def symbolic():
    a,b,s,q,zet,hv,nu=sp.symbols("a b s q zeta hv nu",positive=True)
    u,x,y=sp.symbols("u x y",real=True)
    coords=(u,x,y)
    al=sp.sqrt(a)
    D=1+sp.Rational(2,3)*(1+b)*(x*x+y*y)
    K=sp.diag(1,4*b/(9*D),b/(3*D))
    V0=hv**2*(sp.Rational(3,2)+(b/2-al*u+2*a*u*u/b)*x*x+b*y*y/3+nu*u*u/2)
    V1=hv**2*((b/2+al*b*u+2*a*u*u/b)*x*x+b*y*y/3)
    Q0,Qx,Qy,RR=sp.symbols("Q0 Qx Qy RR")
    A2=sp.exp(2*al*u)
    L0=RR/2-Q0-2*V0
    L1=A2*RR/2+3*a*A2*sp.Symbol("grad_u_sq")-Qx-Qy-2*V1
    # q variation is performed in the unreduced action, with zeta independent.
    raw=q*L0+zet*L1
    exact("symbolic.q_original",sp.diff(raw,q)-L0)
    fixed_sector=q*(L0+s*L1)
    exact("symbolic.q_wrong_difference",sp.diff(fixed_sector,q)-L0-s*L1)
    F=1+s*A2
    j=1+(1-3*a)*s*A2
    ku=(1-3*a*s*A2)/F+sp.Rational(3,4)*(sp.diff(F,u)/F)**2
    exact("symbolic.frame_u",ku-j/F**2)
    for i in (1,2):
        exact("symbolic.frame_transverse_"+str(i),
              ((q+zet)*K[i,i]/(q+zet*A2)).subs(zet,q*s)-(1+s)*K[i,i]/F)
    X,Y=hv**2*x*x,hv**2*y*y
    H=hv*sp.sqrt(D)
    velocity=sp.Matrix([0,-sp.Rational(3,2)*H*x,-2*H*y])
    acceleration=sp.Matrix([sum(sp.diff(velocity[i],coords[jj])*velocity[jj] for jj in range(3)) for i in range(3)])
    T=(velocity.T*K*velocity)[0]
    W=V0+s*V1+sp.Rational(3,2)*s*hv**2*A2**2
    rm,rr=2*q*(1+s)*X,2*q*(1+s)*Y
    hd=-(1+b)*(X+4*Y/3)
    Ricci=6*(2*H*H+hd)
    exact("symbolic.kinetic",T-b*(X+4*Y/3))
    exact("symbolic.ricci",Ricci-12*hv**2-2*(1+b)*X)
    exact("symbolic.friedmann",3*q*(1+s)*H**2-rm-rr-q*(1+s)*T-2*q*W.subs(u,0))
    exact("symbolic.raychaudhuri",-2*q*(1+s)*hd-rm-4*rr/3-2*q*(1+s)*T)
    exact("symbolic.u_equation",-2*q*sp.diff(W,u).subs(u,0)+al*q*s*Ricci-al*rm)
    for i in (1,2):
        connection=0
        for l in range(3):
            for m in range(3):
                gamma=(sp.diff(K[i,m],coords[l])+sp.diff(K[i,l],coords[m])-sp.diff(K[l,m],coords[i]))/(2*K[i,i])
                connection+=gamma*velocity[l]*velocity[m]
        residual=acceleration[i]+3*H*velocity[i]+connection+sp.diff(W,coords[i]).subs(u,0)/((1+s)*K[i,i])
        exact("symbolic.scalar_"+str(i),residual)
    exact("symbolic.original_L0_orbit",Ricci/2+T-2*V0.subs(u,0)-(3*hv**2+(1+b)*X+2*b*Y/3))
    Ac,Bc,Cc=2*a*(1+s)/b,al*(s*b-1),b*(1+s)/2
    exact("symbolic.positive_discriminant",4*Ac*Cc-Bc**2-a*(3+(2-b)*s)*(1+(2+b)*s))
    priorV=hv**2*(sp.Rational(3,2)+(a/2-al*u+2*u*u)*x*x+a*y*y/3+nu*u*u/2)
    exact("symbolic.original_potential_recovered",V0.subs(b,a)-priorV)
    # Actual residuals when the admitted extra scalar operators are absent.
    fried_no=3*q*(1+s)*H**2-rm-rr-q*T-2*q*(V0+sp.Rational(3,2)*s*hv**2*A2**2).subs(u,0)
    ue_no=-2*q*sp.diff(V0+sp.Rational(3,2)*s*hv**2*A2**2,u).subs(u,0)+al*q*s*Ricci-al*rm
    exact("symbolic.omission_friedmann",fried_no-2*q*s*b*(X+Y))
    exact("symbolic.omission_u",ue_no-2*q*s*al*b*X)
    # Local density normalization: Newton has scalar exchange as well as tensor.
    kk=a/(1+(1-3*a)*s)
    GN=(1+kk)/(8*sp.pi*q*(1+s))
    exact("symbolic.measured_G",H**2-hv**2-(8*sp.pi*GN/3)*(1+b)/(1+kk)*(rm+rr))
    kval=sp.symbols("k",positive=True)
    an=(1-kval)*(1+3*kval)/4
    sn=(1+kval)/(kval*(1-3*kval))
    exact("symbolic.null_k",kk.subs({a:an,s:sn})-kval)
    exact("symbolic.equal_null_speed",(1+an)/(1+kval)-(5-3*kval)/4)
    exact("symbolic.split_null_speed",(1+kval)/(1+kval)-1)
    # Canonical vacuum Hessian from the transformed potential, not a mass input.
    kh=sp.diag(j/F**2,(1+s)*K[1,1]/F,(1+s)*K[2,2]/F)
    vh=W/F**2
    origin={u:0,x:0,y:0}
    expected=[(nu*(1+s)+12*a*s)/(1+(1-3*a)*s),sp.Rational(9,4),sp.Integer(2)]
    for i in range(3):
        mi=(sp.diff(vh,coords[i],2)/kh[i,i]).subs(origin)*(1+s)/hv**2
        exact("symbolic.mass_"+str(i),mi-expected[i])
    return {"count":len(CHECKS),"omitted_friedmann":str(sp.factor(fried_no)),
            "omitted_u":str(sp.factor(ue_no)),"wrong_q_term":str(s*L1)}

def metric_potential(u,x,y,a,b,s,nu):
    """High-precision original and transformed coefficients."""
    al=mp.sqrt(a); E=mp.exp(2*al*u); F=1+s*E
    D=1+mp.mpf(2)/3*(1+b)*(x*x+y*y)
    J=1+(1-3*a)*s*E
    K=[J/F**2,(1+s)*4*b/(9*D*F),(1+s)*b/(3*D*F)]
    V0=mp.mpf("1.5")+(b/2-al*u+2*a*u*u/b)*x*x+b*y*y/3+nu*u*u/2
    V1=(b/2+al*b*u+2*a*u*u/b)*x*x+b*y*y/3
    W=V0+s*V1+mp.mpf("1.5")*s*E*E
    return K,W/F**2,F,D,W,V0,V1

def rational_response(a,b,s):
    a,b,s=map(rat,(a,b,s))
    k=a/(1+(1-3*a)*s)
    beta=-a*(1-3*a)*s*(1+s)/(1+(1-3*a)*s)**2
    dg=-2*k/(1+k)
    db=beta*k/(2*(1+k)**2)
    return dict(k=k,beta_D=beta,delta_gamma=dg,delta_beta=db,eta=4*db-dg,
                S_squared=(1+b)/(1+k),restoring_coefficient=2*a/b)

def inverse_b(k,S2):
    b=rat(S2)*(1+rat(k))-1
    return dict(b=str(b),status="admitted" if 0<b<Fraction(1,3) else "excluded")

def full_einstein_functions(phi,a,b,s,nu):
    """All finite-field functions in Hhat_v=Hv/sqrt(1+s) units."""
    u,x,y=phi
    al=np.sqrt(a); E=np.exp(2*al*u); z=s*E; F=1+z; J=1+(1-3*a)*z
    D=1+2*(1+b)*(x*x+y*y)/3
    K=np.array([J/F**2,(1+s)*4*b/(9*F*D),(1+s)*b/(3*F*D)])
    dk=np.zeros((3,3))
    dk[0,0]=K[0]*2*al*z*((1-3*a)/J-2/F)
    dk[0,1:]=K[1:]*(-2*al*z/F)
    dk[1,1:]=K[1:]*(-4*(1+b)*x/(3*D))
    dk[2,1:]=K[1:]*(-4*(1+b)*y/(3*D))
    fc=b*(1+s)/2+al*(s*b-1)*u+2*a*(1+s)*u*u/b
    W=1.5+fc*x*x+b*(1+s)*y*y/3+nu*u*u/2+1.5*s*E*E
    dW=np.array([(al*(s*b-1)+4*a*(1+s)*u/b)*x*x+nu*u+6*al*s*E*E,
                 2*fc*x,2*b*(1+s)*y/3])
    U=(1+s)*W/F**2
    dU=(1+s)*dW/F**2
    dU[0]-=U*4*al*z/F
    return K,dk,U,dU,al/F

def full_n_rhs(N,state,a,b,s,nu):
    phi,p=state[:3],state[3:6]; sm,sr=state[6:8]
    K,dk,U,dU,alB=full_einstein_functions(phi,a,b,s,nu)
    norm=np.dot(K,p*p)
    H2=2*(sm+sr+U)/(3-norm)
    if H2<=0 or not np.isfinite(H2):
        raise ValueError(("Invalid Friedmann chart",N,H2,norm))
    h=-(sm+4*sr/3)/H2-norm
    con=(p*(p@dk)-dk@(p*p)/2)/K
    force=dU.copy();force[0]+=alB*sm
    acc=-(3+h)*p-con-force/(K*H2)
    return np.r_[p,acc,(-3+alB*p[0])*sm,-4*sr]


def additional_general_equation_controls():
    # Independent original-action momentum oracle, differentiated by SymPy.
    # Do not use full_einstein_functions or its supplied connection derivative.
    u,x,y,a,b,s,nu=sp.symbols("u x y a b s nu",real=True)
    phi=(u,x,y)
    al=sp.sqrt(a);E=sp.exp(2*al*u);F=1+s*E
    D=1+sp.Rational(2,3)*(1+b)*(x*x+y*y)
    K=sp.Matrix([(1+(1-3*a)*s*E)/F**2,(1+s)*4*b/(9*F*D),(1+s)*b/(3*F*D)])
    V0=sp.Rational(3,2)+(b/2-al*u+2*a*u*u/b)*x*x+b*y*y/3+nu*u*u/2
    V1=(b/2+al*b*u+2*a*u*u/b)*x*x+b*y*y/3
    U=(1+s)*(V0+s*V1+sp.Rational(3,2)*s*E*E)/F**2
    derivK=sp.Matrix(3,3,lambda i,j:sp.diff(K[j],phi[i]))
    derivU=sp.Matrix([sp.diff(U,v) for v in phi])
    fn=sp.lambdify((u,x,y,a,b,s,nu),(K,derivK,U,derivU,al/F),"numpy",cse=True)
    fixtures=json.loads((HERE/"OFF_TRAJECTORY_FIXTURES_v2.json").read_text())
    count=0
    for av,bv,sv,nv in itertools.product(fixtures["a"],fixtures["b"],fixtures["s"],fixtures["nu"]):
        for state in fixtures["states"]:
            st=np.array(state,dtype=float);pos,pp=st[:3],st[3:6];sm,sr=st[6:8]
            km,dk,uv,du,ab=fn(*pos,av,bv,sv,nv)
            km=np.asarray(km).ravel();du=np.asarray(du).ravel()
            hn2=2*(sm+sr+uv)/(3-np.dot(km,pp*pp));hn=np.sqrt(hn2)
            vel=hn*pp;momentum=km*vel
            pdot=-3*hn*momentum+dk@(vel*vel)/2-du-np.array([ab*sm,0.,0.])
            kdot=vel@dk
            accel=(pdot-kdot*vel)/km
            hlog=-(sm+4*sr/3)/hn2-np.dot(km,pp*pp)
            wanted=np.r_[pp,accel/hn2-hlog*pp,(-3+ab*pp[0])*sm,-4*sr]
            actual=full_n_rhs(0,st,av,bv,sv,nv)
            err=np.abs(actual-wanted)/np.maximum(1,np.abs(wanted))
            for j in range(8):
                check(f"off_trajectory.{count}.{j}",np.isfinite(err[j]) and err[j]<=fixtures["normalized_tolerance"],
                      actual=float(actual[j]),expected=float(wanted[j]),normalized_error=float(err[j]))
            count+=1
    check("census.off_trajectory",count==len(fixtures["a"])*len(fixtures["b"])*len(fixtures["s"])*len(fixtures["nu"])*len(fixtures["states"]))
    return count

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--out",type=Path,default=HERE/"RESULTS.json")
    args=pa.parse_args()
    fix=json.loads((HERE/"NUMERICAL_FIXTURES_v1.json").read_text())
    mp.mp.dps=fix["precision_digits"]
    sym=symbolic()
    grid=[];omissions=[];masses=[];positivity=[]
    for idx,(aa,bb,ss,nn) in enumerate(itertools.product(fix["a"],fix["b"],fix["s"],fix["nu"])):
        a,b,s,nu=map(val,(aa,bb,ss,nn))
        K0,*_=metric_potential(0,0,0,a,b,s,nu)
        mass=[]
        for i in range(3):
            def pot(t):
                v=[mp.mpf(0)]*3;v[i]=t
                return metric_potential(*v,a,b,s,nu)[1]
            raw=mp.diff(pot,mp.mpf(0),2)/K0[i]*(1+s)
            near(f"vacuum_gradient.{idx}.{i}",mp.diff(pot,mp.mpf(0)),mp.mpf(0))
            want=[(nu*(1+s)+12*a*s)/(1+(1-3*a)*s),mp.mpf(9)/4,mp.mpf(2)][i]
            near(f"mass.{idx}.{i}",raw,want);mass.append(fmt(raw))
        masses.append(dict(id=idx,a=aa,b=bb,s=ss,nu=nn,physical_mass_squared=mass))
        # Independent minimum evaluation against completed-square formula.
        umin=-b*(s*b-1)/(4*mp.sqrt(a)*(1+s))
        fmin=b*(1+s)/2+mp.sqrt(a)*(s*b-1)*umin+2*a*(1+s)*umin**2/b
        bound=b*(3+(2-b)*s)*(1+(2+b)*s)/(8*(1+s))
        near(f"minimum.{idx}",fmin,bound)
        check(f"minimum_positive.{idx}",fmin>0)
        for uu in fix["positivity_u"]:
            u=val(uu)
            ff=b*(1+s)/2+mp.sqrt(a)*(s*b-1)*u+2*a*(1+s)*u*u/b
            near(f"square.{idx}.{uu}",ff,fmin+2*a*(1+s)*(u-umin)**2/b)
            K=metric_potential(u,mp.mpf("0.3"),mp.mpf("0.5"),a,b,s,nu)[0]
            check(f"metric_positive.{idx}.{uu}",all(v>0 for v in K))
        positivity.append(dict(id=idx,u_min=fmt(umin),minimum=fmt(fmin),
                               restoring_coefficient=fmt(2*a/b)))
        for jdx,(xx,yy) in enumerate(fix["xy"]):
            x,y=map(val,(xx,yy));al=mp.sqrt(a)
            Kh,vh,F,D,W,V0,V1=metric_potential(0,x,y,a,b,s,nu)
            H=mp.sqrt(D);vx=-mp.mpf("1.5")*H*x;vy=-2*H*y
            Tb=4*b/(9*D)*vx*vx+b/(3*D)*vy*vy
            rm=2*(1+s)*x*x;rr=2*(1+s)*y*y
            hd=-(1+b)*(x*x+mp.mpf(4)/3*y*y)
            R=6*(2*H*H+hd)
            Wu=mp.diff(lambda uu:metric_potential(uu,x,y,a,b,s,nu)[4],0)
            fr=3*(1+s)*H*H-rm-rr-(1+s)*Tb-2*W
            ray=-2*(1+s)*hd-rm-mp.mpf(4)/3*rr-2*(1+s)*Tb
            ur=-2*Wu+al*s*R-al*rm
            l0=R/2+Tb-2*V0
            tag=f"orbit.{idx}.{jdx}"
            for name,res in [("friedmann",fr),("raychaudhuri",ray),("u",ur)]:
                near(tag+"."+name,res,mp.mpf(0),"1e-60")
            near(tag+".q_constraint",l0,3+(1+b)*x*x+2*b*y*y/3)
            wrong_q=s*(R/2+Tb-2*V1)
            near(tag+".wrong_q_variation",wrong_q,s*(6+(1+b)*x*x+2*b*y*y/3))
            check(tag+".wrong_q_nonzero",(abs(wrong_q)>mp.mpf("1e-50"))==bool(s>0))
            k=a/(1+(1-3*a)*s)
            S2=(1+b)/(1+k)
            gn8pi=(1+k)/(1+s)
            near(tag+".measured_G",H*H,1+gn8pi*S2*(rm+rr)/3)
            grid.append(dict(parameter_id=idx,xy_id=jdx,H_squared=fmt(H*H),
                rho_m=fmt(rm),rho_r=fmt(rr),L0=fmt(l0),S_squared=fmt(S2),
                wrong_fixed_s_q_constraint_addition=fmt(wrong_q),
                full_residuals=[fmt(fr),fmt(ray),fmt(ur)]))
            fr_no=3*(1+s)*H*H-rm-rr-Tb-2*(V0+mp.mpf("1.5")*s)
            wu_no=mp.diff(lambda uu:metric_potential(uu,x,y,a,b,s,nu)[5]
                         +mp.mpf("1.5")*s*mp.exp(4*al*uu),0)
            ur_no=-2*wu_no+al*s*R-al*rm
            near(tag+".omitted_friedmann",fr_no,2*s*b*(x*x+y*y),"1e-60")
            near(tag+".omitted_u",ur_no,2*s*al*b*x*x,"1e-60")
            omissions.append(dict(parameter_id=idx,xy_id=jdx,
                friedmann_without_extra_operators=fmt(fr_no),
                u_without_extra_operators=fmt(ur_no),
                expected_nonzero_metric=bool(s>0 and x*x+y*y>0),
                expected_nonzero_u=bool(s>0 and x!=0)))
    # All cases are checked by full Cartesian census, not only survivors.
    npar=len(fix["a"])*len(fix["b"])*len(fix["s"])*len(fix["nu"])
    check("census.parameter",len(masses)==npar and len(positivity)==npar)
    check("census.orbit",len(grid)==npar*len(fix["xy"]) and len(omissions)==len(grid))
    check("census.parameter_ids",set(r["id"] for r in masses)==set(range(npar)))
    pairs={(i,j) for i in range(npar) for j in range(len(fix["xy"]))}
    check("census.orbit_ids",{(r["parameter_id"],r["xy_id"]) for r in grid}==pairs)
    for i,row in enumerate(omissions):
        check(f"omission_metric_flag.{i}",(abs(mp.mpf(row["friedmann_without_extra_operators"]))>mp.mpf("1e-50"))==row["expected_nonzero_metric"])
        check(f"omission_u_flag.{i}",(abs(mp.mpf(row["u_without_extra_operators"]))>mp.mpf("1e-50"))==row["expected_nonzero_u"])
    null=[];inverse=[]
    cn=mp.mpf(7)/8*(mp.mpf(4)/11)**(mp.mpf(4)/3)
    for i,ki in enumerate(fix["null_k"]):
        k=rat(ki);a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k))
        for mode,b in [("equal",a),("split",k)]:
            row=rational_response(a,b,s)
            check(f"null.{i}.{mode}.k",row["k"]==k)
            check(f"null.{i}.{mode}.eta",row["eta"]==0)
            S2=row["S_squared"]
            check(f"null.{i}.{mode}.speed",S2==((5-3*k)/4 if mode=="equal" else 1))
            pre=Fraction(43,7)*(S2-1)
            post=(val(S2)-1)*(1/cn+val(fix["thermal_N_base"]))
            # Direct radiation-density normalizations, separate from expressions.
            pre_direct=((val(S2)*(mp.mpf(43)/4))-mp.mpf(43)/4)/(mp.mpf(7)/4)
            post_direct=(val(S2)*(1+cn*3)-1)/cn-3
            near(f"thermal.{i}.{mode}.pre",val(pre),pre_direct)
            near(f"thermal.{i}.{mode}.post",post,post_direct)
            null.append(dict(k=str(k),a=str(a),s=str(s),b=str(b),mode=mode,
                response={n:str(v) for n,v in row.items()},S=fmt(mp.sqrt(val(S2))),
                Delta_N_pre=str(pre),Delta_N_post=fmt(post)))
        for st in fix["target_S_squared"]:
            out=inverse_b(k,st)
            b=rat(st)*(1+k)-1
            check(f"inverse.{i}.{st}.value",rat(out["b"])==b)
            check(f"inverse.{i}.{st}.domain",(out["status"]=="admitted")==(0<b<Fraction(1,3)))
            if 0<b<Fraction(1,3):
                check(f"inverse.{i}.{st}.back",(1+b)/(1+k)==rat(st))
            inverse.append(dict(k=str(k),target_S_squared=st,**out))
    check("census.null",len(null)==2*len(fix["null_k"]))
    check("census.inverse",len(inverse)==len(fix["null_k"])*len(fix["target_S_squared"]))
    # Independent case/status oracle on every stored row, including exclusions.
    for i,row in enumerate(inverse):
        bb=rat(row["target_S_squared"])*(1+rat(row["k"]))-1
        check(f"inverse_output.{i}",row["b"]==str(bb) and
              row["status"]==("admitted" if bb>0 and 3*bb<1 else "excluded"))
    ode=[]
    for cfg in fix["ode"]:
        a=cfg.get("a");s=cfg.get("s")
        if "null_k" in cfg:
            k=cfg["null_k"];a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k))
        b,nu=cfg["b"],cfg["nu"];x,y=cfg["x0"],cfg["y0"]
        initial=np.array([0.,x,y,0.,-1.5*x,-2*y,x*x,y*y])
        ns=np.linspace(0,cfg["N_end"],fix["ode_samples"])
        sol=solve_ivp(lambda n,y:full_n_rhs(n,y,a,b,s,nu),(0,cfg["N_end"]),initial,
                      method=fix["ode_solver"],rtol=fix["ode_rtol"],atol=fix["ode_atol"],
                      max_step=fix["ode_max_step"],t_eval=ns)
        check("ode."+cfg["id"]+".success",sol.success,message=sol.message)
        check("ode."+cfg["id"]+".census",sol.y.shape==(8,len(ns)))
        errors=[];samples=[]
        if sol.y.shape==(8,len(ns)):
            for j,n in enumerate(ns):
                xx=x*np.exp(-1.5*n);yy=y*np.exp(-2*n)
                want=np.array([0,xx,yy,0,-1.5*xx,-2*yy,xx*xx,yy*yy])
                err=np.max(np.abs(sol.y[:,j]-want)/np.maximum(1,np.abs(want)))
                check(f"ode.{cfg['id']}.{j}.trajectory",err<fix["ode_tracking_tolerance"],normalized_error=float(err))
                # Evaluate the full field equations at the analytic history.
                rhs=full_n_rhs(n,want,a,b,s,nu)
                deriv=np.array([0,-1.5*xx,-2*yy,0,2.25*xx,4*yy,-3*xx*xx,-4*yy*yy])
                erhs=float(np.max(np.abs(rhs-deriv)/np.maximum(1,np.abs(deriv))))
                check(f"ode.{cfg['id']}.{j}.full_rhs",erhs<2e-8,normalized_error=erhs)
                errors.append(float(err));samples.append(dict(N=float(n),state=sol.y[:,j].tolist()))
        ode.append(dict(id=cfg["id"],a=a,b=b,s=s,nu=nu,success=sol.success,
                        nfev=sol.nfev,njev=sol.njev,max_tracking_error=max(errors) if errors else None,
                        samples=samples))
    check("census.ode",len(ode)==len(fix["ode"]))
    # Validate the stored mass output, independently of the producer-local test.
    for row in masses:
        a,b,s,nu=map(rat,(row["a"],row["b"],row["s"],row["nu"]))
        expected=[(nu*(1+s)+12*a*s)/(1+(1-3*a)*s),Fraction(9,4),Fraction(2)]
        check(f"mass_output.{row['id']}.shape",len(row["physical_mass_squared"])==3)
        for j,want in enumerate(expected):
            near(f"mass_output.{row['id']}.{j}",mp.mpf(row["physical_mass_squared"][j]),val(want))
    additional_general_equation_controls()
    # Ensure named checks themselves do not accidentally alias fixtures.
    check("unique_check_names",len({r["name"] for r in CHECKS})==len(CHECKS))
    result=dict(scope="Conditional new action and exposed diagnostic calibration; no independent empirical test.",
        symbolic=sym,orbit=grid,omissions=omissions,local_masses=masses,positivity=positivity,
        null_families=null,inverse_targets=inverse,ode=ode,
        thermal_constants={"c_nu":fmt(cn),"N_base":fix["thermal_N_base"]},
        checks=CHECKS,counts={"passed":sum(r["passed"] for r in CHECKS),
                             "failed":sum(not r["passed"] for r in CHECKS),"total":len(CHECKS)})
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print("Conditional action: 360 ideal-orbit rows, 72 local Hessians, 72 full off-trajectory equation states, four integrated histories.")
    print("Measured-G normalization and supplied PPN/ideal-species diagnostics are conditional bridges; b=k is calibration, not a prediction.")
    print("TOTAL: PASS="+str(result["counts"]["passed"])+" FAIL="+str(result["counts"]["failed"]))
    return int(result["counts"]["failed"]!=0)

if __name__=="__main__":
    raise SystemExit(main())

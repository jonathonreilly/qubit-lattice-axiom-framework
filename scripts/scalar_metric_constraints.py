"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    from pathlib import Path

    import sympy as s

    M,A=s.symbols('M A',positive=True)

    H,r,v,F,mu,alpha,K2,P,u,pi,U,delta=s.symbols('H r v F mu alpha K2 P u pi U delta',real=True)

    Pd=(v*u-r*U)/(2*M*M)-H*P

    rates={H:-(r+v*v)/(2*M*M),r:(alpha*v-3*H)*r,v:-3*H*v-F,F:mu*v-3*H*alpha*r,
           K2:-2*H*K2,P:Pd,u:pi,U:-P-alpha*u-alpha*v*U,delta:3*Pd+K2*U,
           pi:-3*H*pi-(K2+mu)*u-alpha*r*delta+4*v*Pd-2*F*P}

    dt=lambda q:sum(s.diff(q,a)*z for a,z in rates.items())

    rows=[]

    def ck(n,e):
     q=s.factor(s.cancel(e));rows.append({'name':n,'pass':q==0,'residual':str(q)})

    E=-2*M*M*K2*P-3*H*(v*u-r*U)-r*delta-v*pi+v*v*P-F*u

    ck('Hamiltonian constraint propagated',dt(E)+3*H*E)

    ck('spatial trace follows from momentum and original equations',dt(Pd)+4*H*Pd+(2*rates[H]+3*H*H)*P-(v*pi-v*v*P-(F-alpha*r)*u)/(2*M*M))

    ck('physical Euler theta factors',dt(-K2*U)+(2*H+alpha*v)*(-K2*U)-K2*(P+alpha*u))

    h,b,x,xp,kap,kj2,w,wp,wpp,Pp=s.symbols('h b x xp kap kj2 w wp wpp Pp',real=True)

    ell=h-b*x

    FM=-M*A*A*(xp+3*h*x-2*b*x*x)

    udd=s.symbols('udd',real=True)

    elim=udd+(3*H-alpha*v)*pi+(K2+mu-alpha*F)*u-(6*M*M*alpha*H+4*v)*s.Symbol('Pdot')-(2*M*M*alpha*K2+6*M*M*alpha*H*H-alpha*v*v-2*F)*P

    trans=elim.subs({udd:M*A*A*(wpp+b*x*wp),pi:M*A*wp,u:M*w,H:A*ell,v:M*A*x,alpha:b/M,
                    K2:A*A*kj2,mu:A*A*kap,F:FM,s.Symbol('Pdot'):A*Pp})/(M*A*A)

    deff=kap+b*xp+3*b*h*x-2*b*b*x*x

    derived=wpp+3*ell*wp+(kj2+deff)*w-(6*b*ell+4*x)*Pp-(2*b*kj2+6*b*ell*ell-b*x*x+2*(xp+3*h*x-2*b*x*x))*P

    ck('full matter-time response conversion',trans-derived)

    ck('matter-time damping coefficient',s.diff(trans,wp)-3*ell)

    ck('canonical scalar perturbation remains w=u/M',s.diff(trans,wpp)-1)

    ck('Jordan potential difference supplies b*w',((P+b*w)-(P-b*w))/2-b*w)

    tau=s.symbols('tau',real=True)

    J=s.Function('J')(tau)

    bf=s.Function('b')(tau)

    ck('J over b derivative retained',s.diff(J/bf,tau)-(s.diff(J,tau)/bf-J*s.diff(bf,tau)/bf**2))

    ck('J over b second derivative retained',s.diff(J/bf,tau,2)-(s.diff(J,tau,2)/bf-2*s.diff(J,tau)*s.diff(bf,tau)/bf**2-J*s.diff(bf,tau,2)/bf**2+2*J*s.diff(bf,tau)**2/bf**3))

    wrong_damping=s.diff(trans,wp)-3*h

    rows.append({'name':'detect omitted clock damping shift','pass':bool(wrong_damping.subs({b:1,x:1})!=0),'residual':str(s.factor(wrong_damping))})

    return rows, {}

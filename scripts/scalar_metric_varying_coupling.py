"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import math

    import platform

    from pathlib import Path

    import numpy as np

    import scipy

    from scipy.integrate import solve_ivp

    import sympy as s

    phi,v,r,H,a,u,pi,P,U,delta,k2=s.symbols('phi v r H a u pi P U delta k2',real=True)

    variables=[phi,v,r,H,a,u,pi,P,U,delta]

    beta=s.Rational(45,100)

    gamma=s.Rational(16,100)

    A=s.exp(beta*phi+gamma*phi**2/2)

    b=beta+gamma*phi

    V=s.Rational(1,2)-phi/4+s.Rational(8,100)*phi**2+phi**4/100

    F=s.diff(V,phi)+b*r

    mu=s.diff(V,phi,2)+(gamma+b*b)*r

    pd=(v*u-r*U)/2-H*P

    rates=[v,-3*H*v-F,(b*v-3*H)*r,-(r+v*v)/2,a*H,
           pi,-3*H*pi-(k2/a**2+mu)*u-b*r*delta+4*v*pd-2*F*P,
           pd,-P-b*u-b*v*U,3*pd+(k2/a**2)*U]

    def derivative(expr):
        return sum(s.diff(expr,z)*rate for z,rate in zip(variables,rates))/A

    def jets(expr,order):
        ans=[expr]
        for _ in range(order): ans.append(derivative(ans[-1]))
        return ans

    jj=jets(b*u,4)

    pp=jets(P,3)

    kk=jets(k2/(A*a)**2,2)

    hh=jets((H+b*v)/A,1)

    xx=v/A

    qq=b*xx

    ell=H/A

    LL=gamma*v/(A*b)

    xxp=derivative(xx)

    kappa=mu/A**2

    deff=kappa+b*xxp+3*b*hh[0]*xx-2*qq**2

    theta=[3*ell-2*LL,deff+LL**2-derivative(LL)-3*ell*LL,6*b*b*ell+4*qq,2*b*b,
           6*b*b*ell**2+2*b*xxp+6*hh[0]*qq-5*qq**2]

    truth_jets=[jets(c,2) for c in theta]

    observable_expr=jj+pp+kk+hh

    obs_function=s.lambdify(variables+[k2],observable_expr,'numpy',cse=True)

    truth_function=s.lambdify(variables+[k2],sum(truth_jets,[])+[b,qq,kappa,xx,r/A**2], 'numpy',cse=True)

    rates_function=s.lambdify(variables+[k2],rates,'numpy',cse=True)

    background_function=s.lambdify([phi,v,r,H,a],rates[:5],'numpy',cse=True)

    initial_phi=.2

    initial_v=.45

    initial_r=.5*math.exp(float(beta)*initial_phi+float(gamma)*initial_phi**2/2)

    initial_V=float(V.subs(phi,initial_phi))

    initial_H=math.sqrt((initial_v**2/2+initial_r+initial_V)/3)

    bg0=np.array([initial_phi,initial_v,initial_r,initial_H,1.])

    initial_A=math.exp(float(beta)*initial_phi+float(gamma)*initial_phi**2/2)

    initial_b=float(beta+gamma*initial_phi)

    initial_L=float(gamma)*initial_v/(initial_A*initial_b)

    initial_F=float(F.subs({phi:initial_phi,r:initial_r}))

    epsilon=1e-5

    kvalues=np.array([.5,1.5,3.,5.,8.])

    desired=[(0,1,0,0),(1,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,0)]

    state0=list(bg0)

    for kv,(j,jp,pv,ppv) in zip(kvalues,desired):
        j,jp,pv,ppv=epsilon*np.asarray([j,jp,pv,ppv],float)
        uv=j/initial_b
        piv=initial_A*(jp-initial_L*j)/initial_b
        dp=initial_A*ppv
        vel=(initial_v*uv-2*(dp+initial_H*pv))/initial_r
        dens=(-2*kv*pv-6*initial_H*(dp+initial_H*pv)-initial_v*piv+initial_v**2*pv-initial_F*uv)/initial_r
        state0.extend([uv,piv,pv,vel,dens])

    def original_rhs(tt,yy):
        bg=yy[:5]
        dr=list(np.asarray(background_function(*bg),float))
        for kv,row in zip(kvalues,np.asarray(yy[5:]).reshape(5,5)):
            dr.extend(np.asarray(rates_function(*bg,*row,kv),float)[5:])
        return np.array(dr)

    times=np.linspace(0.,.4,21)

    sol=solve_ivp(original_rhs,(times[0],times[-1]),state0,t_eval=times,method='DOP853',
                  rtol=2e-12,atol=2e-15,max_step=.005)

    checks=[]

    def ck(name,passed,**ev):checks.append({'name':name,'pass':bool(passed),**ev})

    ck('original varying-coupling ODE succeeded',sol.success,message=sol.message)

    rows=[]

    max_theta=max_theta1=max_theta2=max_b=max_q=max_kappa=max_R=max_ham=max_bg=0.

    min_sigma=1.

    min_x=1.

    bs=[]

    for tt, yy in zip(sol.t,sol.y.T):
        bg=yy[:5]
        phiv,vv,rr,hE,av=bg
        matrices=[[],[],[]]
        ys=[[],[],[]]
        for kv,row in zip(kvalues,np.asarray(yy[5:]).reshape(5,5)):
            ob=np.asarray(obs_function(*bg,*row,kv),float)
            j0,j1,j2,j3,j4,p0,p1,p2,p3,k0,k1,k22,h0,h1=ob
            matrices[0].append([-j1,-j0,p1,k0*p0,p0])
            matrices[1].append([-j2,-j1,p2,k1*p0+k0*p1,p1])
            matrices[2].append([-j3,-j2,p3,k22*p0+2*k1*p1+k0*p2,p2])
            ys[0].append(j2+k0*j0)
            ys[1].append(j3+k1*j0+k0*j1)
            ys[2].append(j4+k22*j0+2*k1*j1+k0*j2)
            uv,piv,pv,vel,dens=row
            AA=math.exp(float(beta)*phiv+float(gamma)*phiv**2/2)
            bb=float(beta)+float(gamma)*phiv
            FF=float(s.diff(V,phi).subs(phi,phiv))+bb*rr
            ham=-2*(kv/av**2)*pv-3*hE*(vv*uv-rr*vel)-rr*dens-vv*piv+vv*vv*pv-FF*uv
            max_ham=max(max_ham,abs(ham)/epsilon)
        d0,d1,d2=[np.asarray(m)/epsilon for m in matrices]
        y0,y1,y2=[np.asarray(y)/epsilon for y in ys]
        th0=np.linalg.solve(d0,y0)
        th1=np.linalg.solve(d0,y1-d1@th0)
        th2=np.linalg.solve(d0,y2-d2@th0-2*d1@th1)
        tv=np.asarray(truth_function(*bg,*np.asarray(yy[5:]).reshape(5,5)[0],kvalues[0]),float)
        tj=tv[:15].reshape(5,3)
        true_b,true_q,true_kappa,true_x,true_R=tv[15:]
        for got,truth,which in [(th0,tj[:,0],0),(th1,tj[:,1],1),(th2,tj[:,2],2)]:
            err=float(np.max(np.abs(got-truth)/(1+np.abs(truth))))
            if which==0:max_theta=max(max_theta,err)
            if which==1:max_theta1=max(max_theta1,err)
            if which==2:max_theta2=max(max_theta2,err)
        BB,Bp,Bpp=th0[3]/2,th1[3]/2,th2[3]/2
        Lval=Bp/(2*BB)
        Lp=Bpp/(2*BB)-Bp*Bp/(2*BB*BB)
        qv=h0-(th0[0]+2*Lval)/3
        qp=h1-(th1[0]+2*Lp)/3
        kappav=th0[1]-qp-3*h0*qv+2*qv*qv-2*qv*Lval-Lval*Lval+Lp+3*h0*Lval
        Rv=2*qp-2*h1-2*h0*qv+(2-1/BB)*qv*qv
        bv=math.sqrt(BB)
        max_b=max(max_b,abs(bv-true_b)/(1+abs(true_b)))
        max_q=max(max_q,abs(qv-true_q)/(1+abs(true_q)))
        max_kappa=max(max_kappa,abs(kappav-true_kappa)/(1+abs(true_kappa)))
        max_R=max(max_R,abs(Rv-true_R)/(1+abs(true_R)))
        sig=np.linalg.svd(d0,compute_uv=False)
        min_sigma=min(min_sigma,float(sig[-1]/sig[0]))
        min_x=min(min_x,float(true_x))
        bs.append(float(true_b))
        vpot=float(V.subs(phi,phiv))
        max_bg=max(max_bg,abs(3*hE*hE-vv*vv/2-rr-vpot))
        rows.append({'t_E':float(tt),'background':bg.tolist(),'coefficients':th0.tolist(),
                     'coefficient_first':th1.tolist(),'coefficient_second':th2.tolist(),
                     'truth_coefficient_jets':tj.tolist(),'recovered_b_magnitude':bv,'true_b':float(true_b),
                     'recovered_q':qv,'true_q':float(true_q),'recovered_kappa':kappav,'true_kappa':float(true_kappa),
                     'recovered_R':Rv,'true_R':float(true_R),'smallest_relative_singular_value':float(sig[-1]/sig[0])})

    for name,value in [('coefficient',max_theta),('coefficient first derivative',max_theta1),('coefficient second derivative',max_theta2),
                       ('coupling magnitude',max_b),('speed product',max_q),('fixed-bare-density curvature',max_kappa),('source ratio',max_R)]:
        ck(name+' recovered from registered potential jets',value<2e-8,max_relative_error=value)

    ck('original Hamiltonian propagated',max_ham<2e-9,max_residual_over_epsilon=max_ham)

    ck('original background Friedmann propagated',max_bg<2e-10,max_absolute_residual=max_bg)

    ck('coupling varies on fixture',max(bs)-min(bs)>1e-3,span=max(bs)-min(bs))

    ck('monotonic scalar chart respected',min_x>0,min_x=min_x)

    ck('rank supported at all21sampledepochs',min_sigma>1e-5,min_relative_sigma=min_sigma)

    return checks, {"rows": rows}

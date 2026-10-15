"""Root exact and synthetic controls; no observed data or full matter solution."""
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss


def pointwise_ceiling(relative_lapse, global_ratio, exponent, boundary_z, green, eta):
    """Conditional comparison bound; relative_lapse means N/Nmax."""
    return boundary_z*global_ratio**exponent*relative_lapse**exponent*(1+green/(1-eta))


def controls():
    checks = []
    profiles = []

    def test(name, ok, **info):
        checks.append(dict(name=name, passed=bool(ok), **info))

    def eq(name, lhs, rhs=0):
        delta = s.factor(s.simplify(lhs-rhs))
        test(name, delta == 0, difference=str(delta))

    r = s.symbols('r', positive=True)
    lam, p = s.symbols('lambda p', positive=True)
    N = s.Function('N', positive=True)(r)
    B = s.Function('B', positive=True)(r)
    w = s.Function('w')(r)
    ell1 = s.diff(N, r)/N
    lapell = B*s.diff(ell1, r)+(2*B/r+s.diff(B,r)/2)*ell1
    R3 = -2*s.diff(B,r)/r+2*(1-B)/r**2
    R4 = R3-2*(B*s.diff(N,r,2)+(2*B/r+s.diff(B,r)/2)*s.diff(N,r))/N
    def L(v, power):
        return B*s.diff(v,r,2)+(2*B/r+power*B*ell1+s.diff(B,r)/2)*s.diff(v,r)
    cgen = lam*R3/2+(p-lam)*lapell+(p*(p+1)-lam)*B*ell1**2
    eq('arbitrary-power conjugation', (L(N**p*w,1)+lam*R4*N**p*w/2)/N**p,
       L(w,2*p+1)+cgen*w)
    eq('unique power cancels lapse Laplacian', s.diff(cgen, s.diff(N,r,2)), (p-lam)*B/N)
    C = lam*R3/2+lam**2*B*ell1**2
    eq('reduced potential', cgen.subs(p,lam), C)
    f = s.Function('f', positive=True)(r)
    g = s.Function('g', positive=True)(r)
    bg = 4/(f**2*g**2)
    A = s.diff(f,r)/f
    G = s.diff(g,r)/g
    readout = lam*(2*bg*(A+G)/r+(1-bg)/r**2)+lam**2*bg*A**2
    eq('first-clock-derivative readout', C.subs({N:f,B:bg}).doit(), readout)
    q = s.symbols('q', positive=True)
    eq('clock normalization cancels potential', C.subs(N,q*N).doit(), C)
    eq('clock normalization cancels transformed operator', L(w,2*lam+1).subs(N,q*N).doit(), L(w,2*lam+1))
    zB, nn, mm = s.symbols('zB NminSample Nmin', positive=True)
    eq('normalized transformed threshold', nn**lam*zB/mm**lam, zB*(nn/mm)**lam)
    test('boundary-only transformed threshold fails sign', 1.5>1 and 0.5**(117/49)*1.5<1,
         meaning='Kinematic threshold witness only; not a scalar solution')
    eta, wb = s.symbols('eta wb', positive=True)
    vmax = wb*eta/(1-eta)
    eq('Green supremum bootstrap', vmax, eta*(vmax+wb))
    rr, LL, cmax = s.symbols('rr L Cmax', positive=True)
    eq('regular-ball integral factor', s.integrate(cmax*rr/3,(rr,0,LL)), cmax*LL**2/6)
    lv = s.Rational(117,49); ev = s.Rational(3,20)
    x = (2*lv+1)*ev/3; y=lv*ev/3
    ebar = lv**2*ev**2/(6*(1-x))
    uniform = 1/((1-y)*(1-ebar))
    lower64 = lv*(1-ev/(3*64))*3*(2*ev*64-ev**2-8*ev)/32
    test('rational exponential envelope domain', 0<x<1 and 0<y<1, x=str(x), y=str(y))
    test('uniform Green criterion below one', 0<ebar<1, upper=str(ebar))
    test('uniform scalar ceiling below six-fifths', uniform<s.Rational(6,5), ceiling=str(uniform))
    test('original Green criterion provably above four at n64', lower64>4, lower=str(lower64))
    E,K = s.symbols('epsilon K', positive=True)
    ell=E*(s.cos(K*r)-1)/K
    eq('oscillatory first derivative', s.diff(ell,r), -E*s.sin(K*r))
    eq('oscillatory scalar curvature', R4.subs({B:1,N:s.exp(ell)}).doit(),
       2*E*K*s.cos(K*r)-2*E**2*s.sin(K*r)**2+4*E*s.sin(K*r)/r)
    eq('oscillatory transformed source', C.subs({B:1,N:s.exp(ell)}).doit(), lam**2*E**2*s.sin(K*r)**2)
    theta=s.symbols('theta',real=True)
    eq('positive cosine full-period integral', 2*s.integrate(s.cos(theta),(theta,0,s.pi/2)),2)

    # A manufactured member of the comparison sign class, not the candidate's
    # potential equation: w=1, N=exp(epsilon*(1-r^2)), S=N^lambda*C >= 0.
    # This independently challenges the global lapse threshold in the bound.
    dome_ell=E*(1-r**2)
    dome_N=s.exp(dome_ell)
    dome_C=4*lam**2*E**2*r**2
    eq('manufactured sign-class original PDE',
       (L(dome_N**lam,1)+lam*R4*dome_N**lam/2).subs({B:1,N:dome_N}).doit(),
       dome_N**lam*dome_C)
    de=s.Rational(1,100)
    dx=(2*lv+1)*de
    deta=4*lv**2*de**2/(6*(1-dx))
    test('manufactured sign-class strict omission witness',
         dx<1 and deta<1 and 1+lv*de>1/(1-deta),
         eta_upper=str(deta),z_center_lower=str(1+lv*de),
         scope='Prescribed nonnegative source; not a full candidate or measured body')
    dz=float(s.exp(lv*de)); dr=float(s.exp(de))
    dc=pointwise_ceiling(1.,dr,float(lv),1.,float(deta),float(deta))
    test('manufactured sign-class pointwise implementation',dc>=dz,
         center_z=dz,conservative_ceiling=float(dc))
    test('constant lapse normalization in pointwise implementation',
         pointwise_ceiling(1.,1.,float(lv),3.,0.,0.)==3.)

    lambda_num=float(lv); epsilon=float(ev); k=.1
    a=(1-k)*(1+3*k)/4; nu=.0001; hv=.005
    for n in [1,4,16,64]:
        kap=2*np.pi*n
        ell=lambda rv:epsilon*(np.cos(kap*np.asarray(rv))-1)/kap
        ellp=lambda rv:-epsilon*np.sin(kap*np.asarray(rv))
        ellpp=lambda rv:-epsilon*kap*np.cos(kap*np.asarray(rv))
        lapse=lambda rv:np.exp(ell(rv))
        curvhalf=lambda rv:epsilon*kap*np.cos(kap*np.asarray(rv))-epsilon**2*np.sin(kap*np.asarray(rv))**2+2*epsilon*kap*np.sinc(kap*np.asarray(rv)/np.pi)
        source=lambda rv:lambda_num**2*epsilon**2*np.sin(kap*np.asarray(rv))**2
        def greens(tight):
            def ode(rv, yy):
                na=float(lapse(rv)); mu=na**(2*lambda_num+1)
                return [na*rv**2*max(float(curvhalf(rv)),0), yy[0]/(na*rv**2) if rv else 0,
                        mu*rv**2*float(source(rv)), yy[2]/(mu*rv**2) if rv else 0]
            ends=[0.]+[brentq(lambda rv:float(curvhalf(rv)),j/(2*n),(j+1)/(2*n),xtol=1e-14) for j in range(2*n)]+[1.]
            pieces=[];state=np.zeros(4)
            for left,right in zip(ends[:-1],ends[1:]):
                part=solve_ivp(ode,[left,right],state,method='DOP853',dense_output=True,
                               rtol=2e-12 if tight else 1e-10,atol=2e-14 if tight else 1e-12,
                               max_step=1/((64 if tight else 32)*n))
                pieces.append(part);state=part.y[:,-1]
            class Piecewise:
                success=all(part.success for part in pieces)
                y=state[:,None]
                def sol(self,rv):
                    xx=np.asarray(rv);flat=xx.reshape(-1);out=np.empty((4,len(flat)))
                    idx=np.clip(np.searchsorted(ends,flat,side='right')-1,0,len(pieces)-1)
                    for j,part in enumerate(pieces):
                        hit=idx==j
                        if np.any(hit):out[:,hit]=part.sol(flat[hit])
                    return out.reshape((4,)+xx.shape)
            return Piecewise()
        green=greens(False); fine=greens(True)
        original_eta=lambda_num*float(fine.y[1,-1]); transformed_eta=float(fine.y[3,-1])
        diff=float(np.max(np.abs(green.y[:,-1]-fine.y[:,-1])))
        test(f'n{n}: both Green IVPs complete', green.success and fine.success)
        test(f'n{n}: refined Green agreement', diff<2e-8, max_difference=diff)
        ratio=np.exp(epsilon/(np.pi*n))
        conservative=ratio**(2*lambda_num+1)*lambda_num**2*epsilon**2/6
        cap=ratio**lambda_num/(1-transformed_eta)
        test(f'n{n}: analytic transformed envelope', transformed_eta<=conservative+2e-10 and conservative<1,
             eta=transformed_eta,envelope=conservative)
        test(f'n{n}: uniform rational ceiling', cap<float(uniform)+2e-10,ceiling=cap)
        if n==64:
            test('n64: original criterion inconclusive as proved', original_eta>float(lower64)>1,
                 eta=original_eta,analytic_lower=float(lower64))
        mesh=np.linspace(0,1,max(257,64*n+1))
        def potential(z):
            zz=np.asarray(z);lz=np.log(zz)
            return 6*lambda_num*hv**2*zz**3+hv**2*nu/(1-3*a)*zz**3*(2*lz**2+lz)
        def ode_field(rv,yy):
            zz=lapse(rv)**lambda_num*yy[0]
            if np.any(zz<=0): raise ValueError('positive field chart violated')
            return np.vstack((yy[1],-(2*lambda_num+1)*ellp(rv)*yy[1]-source(rv)*yy[0]+potential(zz)/lapse(rv)**lambda_num))
        def bc(left,right):return np.array([left[1],right[0]-1])
        trial=np.vstack((lapse(mesh)**(-lambda_num),-lambda_num*ellp(mesh)*lapse(mesh)**(-lambda_num)))
        sol=solve_bvp(ode_field,bc,mesh,trial,S=np.array([[0.,0.],[0.,-2.]]),tol=1e-9,max_nodes=120000)
        grid=np.linspace(0,1,max(1025,128*n+1));ww,wp=sol.sol(grid)
        zz=lapse(grid)**lambda_num*ww
        pgrid=fine.y[3,-1]-fine.sol(grid)[3]
        point=pointwise_ceiling(lapse(grid),ratio,lambda_num,1.,pgrid,transformed_eta)
        test(f'n{n}: scalar BVP converged', sol.status==0,status=int(sol.status),nodes=len(sol.x))
        test(f'n{n}: positive scalar chart',np.min(zz)>0,minimum=float(np.min(zz)))
        test(f'n{n}: pointwise scalar ceiling',np.max(zz-point)<2e-8,max_excess=float(np.max(zz-point)))
        test(f'n{n}: global scalar ceiling',np.max(zz)<cap+2e-8,max_z=float(np.max(zz)),ceiling=cap)
        rr=np.linspace(1e-5,1,max(1024,128*n))
        w0,w1=sol.sol(rr);w2=sol.sol(rr,1)[1];nl=lapse(rr)**lambda_num
        z=nl*w0;zp=nl*(w1+lambda_num*ellp(rr)*w0)
        zpp=nl*(w2+2*lambda_num*ellp(rr)*w1+(lambda_num*ellpp(rr)+lambda_num**2*ellp(rr)**2)*w0)
        terms=[zpp,(2/rr+ellp(rr))*zp,lambda_num*curvhalf(rr)*z,-potential(z)]
        residual=float(np.max(np.abs(sum(terms))/(1+sum(np.abs(t) for t in terms))))
        test(f'n{n}: original equation residual',residual<2e-6,relative_residual=residual)
        def flux(order):
            nodes,weights=leggauss(order);left=sol.x[:-1];right=sol.x[1:]
            rr=(left[:,None]+right[:,None])/2+(right-left)[:,None]*nodes/2
            zv=lapse(rr)**lambda_num*sol.sol(rr)[0]
            vals=lapse(rr)*rr**2*(-lambda_num*curvhalf(rr)*zv+potential(zv))
            return float(np.sum((right-left)/2*np.sum(weights*vals,axis=1)))
        f12=flux(12);f24=flux(24)
        surface=float(sol.sol(1)[1]+lambda_num*ellp(1))
        test(f'n{n}: flux quadrature refinement',abs(f12-f24)<1e-8,difference=abs(f12-f24))
        test(f'n{n}: original integrated flux',abs(surface-f24)<1e-8,difference=abs(surface-f24))
        profiles.append({'n':n,'original_eta':original_eta,'transformed_eta':transformed_eta,'conservative_eta':conservative,
                         'ceiling':cap,'max_z':float(np.max(zz)),'r':grid.tolist(),'z':zz.tolist(),'pointwise_ceiling':point.tolist(),
                         'P':pgrid.tolist(),'N':lapse(grid).tolist(),'relative_original_residual':residual,
                         'surface_flux':surface,'integrated_flux':f24,'nodes':len(sol.x)})
    return {'checks':checks,'counts':{'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)},
            'rational_envelope':{'eta':str(ebar),'ceiling':str(uniform),'old_eta_lower_n64':str(lower64)},'profiles':profiles,
            'scope':'Exact comparison identities and synthetic scalar equations in supplied metrics; no physical realization, empirical test or continuum numerical certification.'}

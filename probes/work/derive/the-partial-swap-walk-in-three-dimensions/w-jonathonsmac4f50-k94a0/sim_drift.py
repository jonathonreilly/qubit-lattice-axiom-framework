import sys, numpy as np, time
from sim_lib import *
from scipy.integrate import solve_ivp
NODE=np.array([np.pi/2]*3)
def eig_up(k,eps,order):
    S=symbol(k,eps,order)
    ev,V=np.linalg.eig(S)
    ph=np.angle(ev)
    i=np.argmin(ph)  # eigenphase -theta (theta>0)
    u=V[:,i]/np.linalg.norm(V[:,i])
    return -ph[i],u
def theta(k,eps,order): return eig_up(k,eps,order)[0]
def berry(k,eps,order,h=1e-4):
    Om=np.zeros(3)
    def u_(kk): return eig_up(kk,eps,order)[1]
    for c in range(3):
        a,b=(c+1)%3,(c+2)%3
        ea=np.zeros(3);ea[a]=h;eb=np.zeros(3);eb[b]=h
        u0=u_(k);u1=u_(k+ea);u2=u_(k+ea+eb);u3=u_(k+eb)
        P=(np.vdot(u0,u1)*np.vdot(u1,u2)*np.vdot(u2,u3)*np.vdot(u3,u0))
        Om[c]=-np.angle(P)/h**2
    return Om
def grad_k(f,k,h=1e-5):
    return np.array([(f(k+h*np.eye(3)[a])-f(k-h*np.eye(3)[a]))/(2*h) for a in range(3)])
def predict(m,gdir,k0,eps0,g,T,order,anom=True):
    """central ray (+ optional anomalous velocity) in ticks; clock w=1+g*(gdir.x) ; returns displacement vector at T"""
    m=np.array(m,float);m/=np.linalg.norm(m);gd=np.array(gdir,float);gd/=np.linalg.norm(gd)
    nt=T/(2*eps0)
    q0=k0*m
    def rhs(t,y):
        x=y[:3];q=y[3:]
        w=1+g*(gd@x)
        k=NODE+q
        E=lambda kk: theta(kk,eps0*w,order)
        dEdk=grad_k(E,k)
        dw=1e-5
        dEdx=(theta(k,eps0*(w+dw),order)-theta(k,eps0*(w-dw),order))/(2*dw)*g*gd
        kd=-dEdx
        v=dEdk.copy()
        if anom:
            Om=berry(k,eps0*w,order)
            v=v-np.cross(kd,Om)
        return np.concatenate([v,kd])
    y0=np.concatenate([np.zeros(3),q0])
    sol=solve_ivp(rhs,[0,nt],y0,rtol=1e-8,atol=1e-10)
    return sol.y[:3,-1]
def run_sim(m,gdir,k0,eps0,g,T,order,L=72,sigma=5.0,verbose=False):
    m=np.array(m,float);m/=np.linalg.norm(m);gd=np.array(gdir,float);gd/=np.linalg.norm(gd)
    ctr=np.array([L/2]*3)
    # packet starts so that it is at ctr at T/2 (ray along m)
    x0=ctr-m*T/2
    X=np.stack(np.meshgrid(*[np.arange(L,dtype=float)]*3,indexing='ij'),-1)
    r=X-x0
    q=k0*m
    kk=NODE+q
    th,u=eig_up(kk,eps0,order)
    env=np.exp(-(r**2).sum(-1)/(4*sigma**2))
    phase=np.exp(1j*(X@q))*np.exp(1j*np.pi/2*(X.sum(-1)))   # i^(x+y+z) node shift
    psi=(env*phase)[...,None]*u
    psi/=np.sqrt((np.abs(psi)**2).sum())
    z=(X-ctr)@gd   # clock gradient along gd
    w=1+g*z
    tick=make_tick(w,eps0,order)
    nt=int(round(T/(2*eps0)))
    t=time.time()
    for _ in range(nt): psi=tick(psi)
    dens=(np.abs(psi)**2).sum(-1)
    cen=np.array([(dens*X[...,a]).sum() for a in range(3)])
    edge=dens[:3].sum()+dens[-3:].sum()+dens[:,:3].sum()+dens[:,-3:].sum()+dens[:,:,:3].sum()+dens[:,:,-3:].sum()
    return cen-x0, edge, time.time()-t, nt
if __name__=='__main__':
    m=eval(sys.argv[1]);gd=eval(sys.argv[2]);k0=float(sys.argv[3]);eps0=float(sys.argv[4]);order=sys.argv[5];L=int(sys.argv[6]);T=float(sys.argv[7]) if len(sys.argv)>7 else 30.0
    g=0.004
    res={}
    for sgn in (1,-1):
        d,edge,dt,nt=run_sim(m,gd,k0,eps0,sgn*g,T,order,L=L)
        res[sgn]=d
        print('g sign',sgn,'disp',np.round(d,4),'edge',f'{edge:.1e}','time',round(dt,1),'ticks',nt,flush=True)
    odd=(res[1]-res[-1])/2
    print('odd-in-g displacement',np.round(odd,4))
    for anom in (False,True):
        p=(predict(m,gd,k0,eps0,g,T,order,anom)-predict(m,gd,k0,eps0,-g,T,order,anom))/2
        print('prediction anom=',anom,np.round(p,4))

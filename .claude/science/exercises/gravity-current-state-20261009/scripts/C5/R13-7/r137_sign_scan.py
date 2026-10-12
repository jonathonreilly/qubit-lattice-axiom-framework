"""R13-7: sign of the heavy-electron limit dc_e(inf) = (1/4)<A(q_x) w(q)>, w = (d_y^2+d_z^2+lam^2)/(d_x^2 W^3),
over literal-edge shapes (electron plateau b1,b2; photon plateau c1,c2); lam = 0.  Also checks (H2') analytically
claimed: w convex in q_x wherever d(q_x) = 2 sin(q_x/2) (dense (t, D') grid of the closed-form w''/phi)."""
import sys; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import Law, kgrid1, deriv, U
def inf_const(law,N,lam=0.0):
    q1=kgrid1(N); QX,QY,QZ=np.meshgrid(q1,q1,q1,indexing='ij')
    dx2,dy2,dz2=law.d(QX)**2,law.d(QY)**2,law.d(QZ)**2
    W2=dx2+dy2+dz2+lam**2; W=np.sqrt(W2)
    A=deriv(lambda k: law.S(k)**2,QX,2)/2-1
    return 0.25*np.mean(A*(W2-dx2)/(dx2*W**3))*U
if __name__=='__main__':
    # (H2') closed form: w''/phi = (6-t)/t + y(6-t) + (5/3) t(4-t) y^2, y = 3/(2(t+D'))
    t=np.linspace(1e-4,4,4001)[:,None]; Dp=np.concatenate([[0],np.logspace(-4,2,200)])[None,:]
    y=1.5/(t+Dp); expr=(6-t)/t+y*(6-t)+(5/3)*t*(4-t)*y**2
    # brute-force second derivative check
    q=np.linspace(0.05,np.pi,20001)
    mins=[]
    for D in (0.0,0.01,0.3,3.0,12.0):
        tt=2*(1-np.cos(q)); w=1/(tt*(tt+D)**1.5); wpp=np.gradient(np.gradient(w,q),q)
        mins.append(np.min(wpp[10:-10]))
    if __name__=="__main__": print("(H2') min closed-form w''/phi over grid = %.4e (must be > 0); brute-force min w'' for D'=0,.01,.3,3,12: %s"%(expr.min(),' '.join('%.3e'%x for x in mins)))
    print('heavy-limit dc_e(inf)*U, literal edge, lam=0, N=96')
    rows=[]
    for b1,b2 in [(0.5,1.5),(1.0,2.0),(1.5,2.5),(2.0,3.0),(2.5,3.1),(1.0,3.0),(2.0,2.5),(2.8,3.1),(0.3,0.6)]:
        for c in [(None,None),(0.5,1.0),(b1,b2),(2.5,3.1),(2.8,3.12)]:
            law=Law(b1,b2,0.0,c[0],c[1],1.0)
            v=inf_const(law,96)
            rows.append((b1,b2,c,v))
            print('  e-box (%.1f,%.2f) photon-box %-12s  dc_e(inf)*U = %+9.4f'%(b1,b2,str(c),v),flush=True)
    print('max over scan: %+.4f ; min: %+.4f'%(max(r[3] for r in rows),min(r[3] for r in rows)))

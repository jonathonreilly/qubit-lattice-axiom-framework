# GUIDE-grade: the one-sheet, two-slice-site toy of Lemma KIN for SU(2) and U(1).
# K = class functions of q = Phi_2 Phi_1^-1 (SU(2)); T(bL) = E diag(lam_j(bM)^2 lam_j(bL)^2) E, E = exp(bM x/2).
import numpy as np
Nq=4000
th=(np.arange(Nq)+0.5)*np.pi/Nq; dth=np.pi/Nq
def su2(bM,bL,J=60):
    n=np.arange(1,J+1)                      # n = 2j+1
    S=np.sin(np.outer(n,th))                # chi_j sin(theta) = sin(n theta)
    def lam(b):
        if np.isinf(b): return np.ones(J)
        w=np.exp(b*(np.cos(th)-1.0))
        num=(S*np.sin(th)*w).sum(1)*dth/n   # int sin^2 * chi_j/d_j * w
        return num/num[0]
    E=(2/np.pi)*(S*np.exp(0.5*bM*np.cos(th)))@S.T*dth      # <chi_j, e^{bM cos/2} chi_k>
    kap=lam(bM)**2*lam(bL)**2
    T=E@np.diag(kap)@E
    ev=np.sort(np.linalg.eigvalsh((T+T.T)/2))[::-1]
    return np.log(ev[0]/ev[1]), ev[0]
def u1(bM,bL,J=60):
    n=np.arange(-J,J+1); t=(np.arange(2*Nq)+0.5)*np.pi/Nq; dt=np.pi/Nq
    C=np.exp(1j*np.outer(n,t))
    def lam(b):
        if np.isinf(b): return np.ones(len(n))
        w=np.exp(b*(np.cos(t)-1.0)); num=(np.cos(np.outer(n,t))*w).sum(1)*dt
        return num/num[J]
    E=(C*np.exp(0.5*bM*np.cos(t)))@C.conj().T*dt/(2*np.pi)
    kap=lam(bM)**2*lam(bL)**2
    T=E@np.diag(kap)@E
    ev=np.sort(np.linalg.eigvalsh((T+T.conj().T)/2))[::-1]
    return np.log(ev[0]/ev[1]), ev[0]
for name,f in (("SU(2)",su2),("U(1)",u1)):
    for bM in (0.5,1.0,2.4,4.0,8.0):
        mf,l0=f(bM,np.inf)
        row=["%s bM=%.1f face=%.6f"%(name,bM,mf)]
        mn=1e9; arg=None
        for bL in (0.0,0.5,1.0,2.4,5.0,10.0,20.0,50.0,200.0):
            m,l=f(bM,bL); row.append("bL=%g:%.6f"%(bL,m))
        for bL in np.exp(np.linspace(np.log(0.05),np.log(2000),160)):
            m,l=f(bM,bL)
            if m<mn: mn=m; arg=bL
        row.append("| min over bL in [0.05,2000]: %.6f at bL=%.2f  (min - face = %.2e)"%(mn,arg,mn-mf))
        print("  ".join(row))

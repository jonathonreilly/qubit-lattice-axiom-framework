"""E2: in the one-phase texture, is the triangle angle alpha just the phase of that one element?
Scan phi (phase of the up (1,2) element); report median alpha over realistic-window samples."""
import numpy as np
from math import pi
rng = np.random.default_rng(7)
def run(phi, N=400000):
    def sector():
        return (10**rng.uniform(-4.2,-2.2,N), 10**rng.uniform(-3.0,-1.2,N), 10**rng.uniform(-1.7,-0.6,N), np.ones(N))
    def mk(A,B,C,D,ph):
        M=np.zeros((N,3,3),complex); M[:,0,1]=A*np.exp(1j*ph); M[:,1,0]=A*np.exp(-1j*ph)
        M[:,1,1]=B; M[:,1,2]=C; M[:,2,1]=C; M[:,2,2]=D; return M
    def diag(M):
        w,U=np.linalg.eigh(M); idx=np.argsort(np.abs(w),axis=1)
        return np.abs(np.take_along_axis(w,idx,1)), np.take_along_axis(U,idx[:,None,:],2)
    wu,Uu=diag(mk(*sector(),phi)); wd,Ud=diag(mk(*sector(),0.0))
    V=np.conj(np.transpose(Uu,(0,2,1)))@Ud; ab=np.abs(V)
    win=((ab[:,0,1]>0.15)&(ab[:,0,1]<0.35)&(ab[:,1,2]>0.02)&(ab[:,1,2]<0.08)&(ab[:,0,2]>0.001)&(ab[:,0,2]<0.01)
         &(wu[:,0]/wu[:,1]<0.1)&(wu[:,1]/wu[:,2]<0.2)&(wd[:,0]/wd[:,1]<0.3)&(wd[:,1]/wd[:,2]<0.2))
    V=V[win]
    a=np.angle(-V[:,2,0]*np.conj(V[:,2,2])/(V[:,0,0]*np.conj(V[:,0,2])))
    return win.sum(), np.degrees(np.median(np.abs(a))), np.degrees(np.percentile(np.abs(a),16)), np.degrees(np.percentile(np.abs(a),84))
print("phi_deg  n   median_alpha  [16%,84%]")
for ph in (15,30,45,60,75,90,105,120,135,150,165):
    n,m,lo,hi=run(np.radians(ph)); print("%5d %6d  %8.2f  [%.1f, %.1f]"%(ph,n,m,lo,hi))

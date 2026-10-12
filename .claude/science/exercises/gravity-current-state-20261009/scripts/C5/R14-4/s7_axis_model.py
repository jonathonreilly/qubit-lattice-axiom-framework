# R14-4 s7: the explicit nearest-neighbour axis-only model (the by-product of Lemma V's analysis)
#   H_F = 1/2 sum_x [ E:E + m (tr h)^2 ] + 1/2 sum_x sum_i Phi_i( h(x+e_i) - h(x) ),
#   Phi_z(h) = (h_xx-h_yy)^2/2 + 2 h_xy^2 (and cyclic): the TT part of h relative to axis i.
# PSD, local (range 1), O_h-covariant, no h-E mixing needed.  Prints omega/|k| at small k along axis, face and body
# diagonals: 2 linear TT + exactly flat partners on the axis; 4 and 5 linear branches off-axis.
import numpy as np
def Phi(i,h):
    j,k=(i+1)%3,(i+2)%3; return 0.5*(h[j,j]-h[k,k])**2+2*h[j,k]**2
idx=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
Bs=[]
for (i,j) in idx:
    M=np.zeros((3,3))
    if i==j: M[i,i]=1
    else: M[i,j]=M[j,i]=1/np.sqrt(2)
    Bs.append(M)
def quad(f):
    M=np.zeros((6,6))
    for a in range(6):
        for b in range(6):
            M[a,b]=0.25*(f(Bs[a]+Bs[b])-f(Bs[a]-Bs[b]))
    return M
PH=[quad(lambda h,i=i: Phi(i,h)) for i in range(3)]
TR=quad(lambda h: np.trace(h)**2)
m=1.0
def H(k):
    hh=sum(2*(1-np.cos(k[i]))*PH[i] for i in range(3))+m*TR
    return np.block([[hh,np.zeros((6,6))],[np.zeros((6,6)),np.eye(6)]])
J=np.block([[np.zeros((6,6)),np.eye(6)],[-np.eye(6),np.zeros((6,6))]])
print("min eig of H over random k:",min(np.linalg.eigvalsh(H(np.random.default_rng(0).uniform(-np.pi,np.pi,3))).min() for _ in range(100)))
for name,n in [("axis (0,0,1)",(0,0,1)),("face (1,1,0)",(1,1,0)),("body (1,1,1)",(1,1,1)),("generic (1,2,3)",(1,2,3))]:
    n=np.array(n,float); n/=np.linalg.norm(n)
    for t in (1e-2,1e-3):
        w=np.sort(np.abs(np.linalg.eigvals(1j*J@H(t*n)).real))[::2]
        print("  %-16s |k|=%.0e  omega/|k| = %s   (trace mode omega = %.3f)"%(name,t,np.round(w[w<1]/t,5),w[-1]))
# exactness along the axis at finite k
k=np.array([0,0,1.3]); w=np.sort(np.abs(np.linalg.eigvals(1j*J@H(k)).real))[::2]
print("axis k=1.3: omegas",np.round(w,6)," expected TT omega = sqrt(2(1-cos k)) =",np.round(np.sqrt(2*(1-np.cos(1.3))),6))

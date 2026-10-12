# R14-4 s4: (1) the three rank<=2 families of s2 (A, B, C): PSD? rank over all directions? which polarisation?
#            (2) the margin: with both axis TT stiffnesses = 1 and the axis partners null (VEC = S = 0), the family is
#                c = (1, c2, c3, -2-c2, 1/2-c3, 0).  Over this 2-parameter plane, how large must the third soft
#                stiffness lambda_3(V(k)) be in the worst direction?  (PSD members and all members.)
import numpy as np, itertools
from s3_mixed_models import inv_mats
rng=np.random.default_rng(11)
dirs=[d/np.linalg.norm(d) for d in rng.normal(size=(3000,3))]
dirs+= [np.array(v,float)/np.linalg.norm(v) for v in [(0,0,1),(1,1,0),(1,1,1),(1,2,0),(2,1,3)]]
IM=[inv_mats(n) for n in dirs]
def V(c,i): return sum(ci*M for ci,M in zip(c,IM[i]))
def stats(c):
    mins=[];l3=[];ranks=[]
    for i in range(len(dirs)):
        w=np.linalg.eigvalsh(V(c,i)); mins.append(w[0]); l3.append(np.sort(np.abs(w))[-3]); ranks.append(np.sum(np.abs(w)>1e-9*max(1,np.abs(w).max())))
    return min(mins),max(l3),max(ranks)
fam={'A (c3=-3/2)':[0,0,-1.5,0,0,1.0],'B (c5=2)':[1,-1,0,-1,2,-1],'C (c5=-4)':[1,2,6,-4,-4,-1]}
print("(1) rank<=2 families from s2 (normalised so the nonzero axis TT stiffness is +1):")
for n,c in fam.items():
    c=np.array(c,float); Vz=V(c,len(dirs)-5)
    mn,l3,rk=stats(c)
    print("  %-12s axis diag(T1,S,X,Y,Z)=%s  min eig over %d dirs=%.3e  max rank=%d  max lambda3=%.1e"%(n,np.round(np.diag(Vz),4),len(dirs),mn,rk,l3))
print("(2) margin on the plane TT1=TT2=1, VEC=S=0:  c=(1,c2,c3,-2-c2,1/2-c3,0)")
best_all=(1e9,None); best_psd=(1e9,None); npsd=0
grid=np.linspace(-6,6,81)
sub=list(range(0,len(dirs),6))+list(range(len(dirs)-5,len(dirs)))
for c2 in grid:
    for c3 in grid:
        c=np.array([1,c2,c3,-2-c2,0.5-c3,0.0])
        ws=[np.linalg.eigvalsh(V(c,i)) for i in sub]
        mn=min(w[0] for w in ws); l3=max(np.sort(np.abs(w))[-3] for w in ws)
        if l3<best_all[0]: best_all=(l3,(c2,c3))
        if mn>=-1e-9:
            npsd+=1
            if l3<best_psd[0]: best_psd=(l3,(c2,c3),mn)
print("  grid 81x81 on [-6,6]^2, %d directions: PSD members found = %d"%(len(sub),npsd))
print("  min over ALL members of max_dir lambda_3 = %.4f at (c2,c3)=%s"%best_all)
if best_psd[1] is not None: print("  min over PSD members of max_dir lambda_3 = %.4f at (c2,c3)=%s (min eig %.2e)"%best_psd)
# refine around the PSD optimum with all directions
if best_psd[1] is not None:
    from scipy.optimize import minimize
    def obj(p):
        c=np.array([1,p[0],p[1],-2-p[0],0.5-p[1],0.0]); mn,l3,_=stats(c); return l3+1e3*max(0,-mn)
    r=minimize(obj,best_psd[1],method='Nelder-Mead',options={'xatol':1e-4,'fatol':1e-6,'maxiter':300})
    c=np.array([1,r.x[0],r.x[1],-2-r.x[0],0.5-r.x[1],0.0]); mn,l3,rk=stats(c)
    print("  refined (all %d dirs): (c2,c3)=(%.4f,%.4f) min eig=%.2e  max lambda_3=%.4f  max rank=%d"%(len(dirs),r.x[0],r.x[1],mn,l3,rk))
# the axis-only counterexample F
c=np.array([1,0,0.5,-2,0,0]); mn,l3,rk=stats(c)
print("  F = sum_i k_i^2 Phi_i (c2,c3)=(0,1/2): min eig=%.2e  max lambda_3=%.4f  max rank=%d"%(mn,l3,rk))

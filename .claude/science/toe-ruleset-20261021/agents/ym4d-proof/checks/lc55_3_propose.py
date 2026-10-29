# lc55_3 PROPOSAL generator (floats/numpy). NOT a verdict. Exponential chart U = exp(i(A+v).sigma) on the 2D box (collar),
# stripe A_2 = a(x1 mod 3) s3 with pattern (beta,0,-beta), beta rational. Writes rounded proposals to lc55_3_proposals.txt.
import numpy as np
from fractions import Fraction
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
I2=np.eye(2,dtype=complex)
def ex(X):
    n=np.linalg.norm(X)
    if n<1e-300: return I2.copy()
    H=sum(X[i]*s[i] for i in range(3))/n
    return np.cos(n)*I2+1j*np.sin(n)*H
def insertions(A,h=1e-4):
    D1=[(ex(A+h*np.eye(3)[i])-ex(A-h*np.eye(3)[i]))/(2*h) for i in range(3)]
    D2=[[(ex(A+h*np.eye(3)[i]+h*np.eye(3)[j])-ex(A+h*np.eye(3)[i]-h*np.eye(3)[j])-ex(A-h*np.eye(3)[i]+h*np.eye(3)[j])+ex(A-h*np.eye(3)[i]-h*np.eye(3)[j]))/(4*h*h) for j in range(3)] for i in range(3)]
    return ex(A),D1,D2
def box_exp(n,beta):
    pat=[beta,0.0,-beta]
    bnd=lambda z: z[0] in (0,n) or z[1] in (0,n)
    links=[]
    for x1 in range(n+1):
        for x2 in range(n+1):
            for mu in (1,2):
                y=(x1+(mu==1),x2+(mu==2))
                if y[0]>n or y[1]>n: continue
                if bnd((x1,x2)) and bnd(y): continue
                links.append(((x1,x2),mu))
    idx={l:i for i,l in enumerate(links)}
    cache={}
    def ins(a):
        if a not in cache: cache[a]=insertions(np.array([0,0,a]))
        return cache[a]
    def A_of(l): return pat[l[0][0]%3] if l[1]==2 else 0.0
    D=3*len(idx); H=np.zeros((D,D))
    for x1 in range(n):
        for x2 in range(n):
            fac=[(((x1,x2),1),False),(((x1+1,x2),2),False),(((x1,x2+1),1),True),(((x1,x2),2),True)]
            data=[]
            for (l,inv) in fac:
                E,D1,D2=ins(A_of(l))
                if inv:
                    E=np.linalg.inv(E); D1=[-E@d@E for d in D1]
                    # second derivative of inverse: E^-1 (D_i E^-1 D_j + D_j E^-1 D_i - D2_ij) E^-1 (with E^-1 already)
                    Ei=E; D1o=[(-1)*np.linalg.inv(Ei)@d@np.linalg.inv(Ei) for d in D1]  # unused
                    E0,D1n,D2n=ins(A_of(l)); Einv=np.linalg.inv(E0)
                    D1=[-Einv@d@Einv for d in D1n]
                    D2=[[Einv@(D1n[i]@Einv@D1n[j]+D1n[j]@Einv@D1n[i]-D2n[i][j])@Einv for j in range(3)] for i in range(3)]
                    E=Einv
                data.append((l,E,D1,D2))
            for ka in range(4):
                la=data[ka][0]
                if la not in idx: continue
                for kb in range(4):
                    lb=data[kb][0]
                    if lb not in idx: continue
                    for i in range(3):
                        for j in range(3):
                            M=I2
                            for k in range(4):
                                l,E,D1,D2=data[k]
                                if ka==kb==k: M=M@D2[i][j]
                                elif k==ka: M=M@D1[i]
                                elif k==kb: M=M@D1[j]
                                else: M=M@E
                            H[3*idx[la]+i,3*idx[lb]+j]+=-0.5*np.trace(M).real
    H=(H+H.T)/2
    ev,U=np.linalg.eigh(H)
    return ev[0],U[:,0],links
out=open('lc55_3_proposals.txt','w')
for (num,den) in [(1,5),(1,20)]:
    e,v,links=box_exp(6,num/den)
    v=v/np.max(np.abs(v))
    out.write('EXPBOX beta=%d/%d n=6 float_lowest=%.6e links %s\n'%(num,den,e,' '.join('%d,%d,%d'%(l[0][0],l[0][1],l[1]) for l in links)))
    out.write('EXPVEC %s\n'%(' '.join('%d/%d'%(int(round(x*10**6)),10**6) for x in v)))
    print('beta',num,den,'float lowest',e,flush=True)
out.close()

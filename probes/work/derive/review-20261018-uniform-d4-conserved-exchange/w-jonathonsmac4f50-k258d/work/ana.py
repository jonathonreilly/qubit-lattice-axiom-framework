import sys, itertools, signal
sys.path.insert(0,'.')
import numpy as np
import src
signal.alarm(0)
from src import *

def dihedral_derivs(L2m, tri, m, n):
    """exact d theta_{mn}/d s_{ij} (squared length variable) for interior dihedral at hinge 'tri' between facets opp m,n. returns 5x5 matrix"""
    s = L2m
    G = np.array([[0.5*(s[0,b]+s[0,a]-s[a,b]) for b in range(1,5)] for a in range(1,5)])
    D = np.linalg.inv(G)
    # extended dual gram 5x5
    E = np.zeros((5,5)); E[1:,1:] = D
    E[0,1:] = -D.sum(axis=1); E[1:,0] = E[0,1:]; E[0,0] = D.sum()
    c = -E[m,n]/np.sqrt(E[m,m]*E[n,n])
    out = np.zeros((5,5))
    for i,j in itertools.combinations(range(5),2):
        dG = np.zeros((4,4))
        # G_ab = (s0a+s0b-sab)/2 ; a,b = 1..4
        if i==0:
            a=j-1
            for b in range(4):
                dG[a,b]+=0.5; dG[b,a]+=0.5
            dG[a,a]-=0.5  # diag counted twice: G_aa = s0a -> derivative 1; above gives 0.5+0.5=1, minus extra? fix below
        else:
            a,b=i-1,j-1
            dG[a,b]-=0.5; dG[b,a]-=0.5
        out[i,j]=0
        # handle i==0 properly
        if i==0:
            dG=np.zeros((4,4)); a=j-1
            for b in range(4):
                if b==a: dG[a,a]=1.0
                else: dG[a,b]=0.5; dG[b,a]=0.5
        dD = -D@dG@D
        dE = np.zeros((5,5)); dE[1:,1:]=dD
        dE[0,1:] = -dD.sum(axis=1); dE[1:,0]=dE[0,1:]; dE[0,0]=dD.sum()
        # c = -E_mn / sqrt(E_mm E_nn)
        dc = -dE[m,n]/np.sqrt(E[m,m]*E[n,n]) + 0.5*E[m,n]/np.sqrt(E[m,m]*E[n,n])*(dE[m,m]/E[m,m]+dE[n,n]/E[n,n])
        out[i,j]=out[j,i]=-dc/np.sqrt(1-c*c)   # theta = arccos(c)
    return out

class CA(Complex):
    def _build(self, fd):
        stars, hverts = {}, {}
        for si, s in enumerate(self.simp):
            for tri in itertools.combinations(range(5), 3):
                key, anc = src._key_tri([s[i] for i in tri])
                T = -np.array(anc)
                stars.setdefault(key, []).append((si, T, tri))
                hverts.setdefault(key, [(tuple(np.add(s[i][0], T)), s[i][1]) for i in tri])
        self.terms = []
        for key, st in stars.items():
            hv = hverts[key]
            a_terms=[]
            pairs=[(0,1),(0,2),(1,2)]
            s3=[self.L(hv[i],hv[j])**2 for i,j in pairs]
            A=tri_area(s3)
            # A^2 = (2(ab+bc+ca)-a^2-b^2-c^2)/16 ; dA/ds_a=(b+c-a)/(16A)
            a,b,c=s3
            dAds=[(b+c-a)/(16*A),(a+c-b)/(16*A),(a+b-c)/(16*A)]
            for n_,(i,j) in enumerate(pairs):
                l=np.sqrt(s3[n_]); cc,anc=src._key_pair(hv[i],hv[j]); a_terms.append((self.ekey[cc],np.array(anc,float),dAds[n_]*2*l))
            d_terms=[]
            for si,T,tri in st:
                vs=[(tuple(np.add(v[0],T)),v[1]) for v in self.simp[si]]
                L2m=np.array([[self.L(vs[i],vs[j])**2 for j in range(5)] for i in range(5)])
                m,n=[i for i in range(5) if i not in tri]
                dth=dihedral_derivs(L2m,tri,m,n)
                for i,j in itertools.combinations(range(5),2):
                    l=np.sqrt(L2m[i,j]); cc,anc=src._key_pair(vs[i],vs[j])
                    d_terms.append((self.ekey[cc],np.array(anc,float),-dth[i,j]*2*l))
            pack=lambda tl:(np.array([t[0] for t in tl]),np.array([t[1] for t in tl]),np.array([t[2] for t in tl]))
            self.terms.append((pack(a_terms),pack(d_terms)))
if __name__=="__main__":
    OFF,Sm=d4cone()
    import time;t=time.time()
    C0=Complex(OFF,Sm); print('fd build',time.time()-t); t=time.time()
    C1=CA(OFF,Sm); print('analytic build',time.time()-t, C1.E)
    for k in ([0.3,-0.2,0.5,0.1],[0.01,0.02,-0.01,0.015]):
        k=np.array(k); Qa=C1.Q(k); Qf=C0.Q(k); print(np.abs(Qa-Qf).max(), np.abs(Qa).max())

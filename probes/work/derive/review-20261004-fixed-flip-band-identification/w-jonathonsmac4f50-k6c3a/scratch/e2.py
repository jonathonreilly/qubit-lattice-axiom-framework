import mpmath as mp, itertools, time
mp.mp.dps = 60
TERMS=[(0, 1, (-1, 0, 0), 'y'), (0, 1, (0, 0, 0), 'x'), (0, 3, (0, 0, -1), 'z'), (1, 1, (-1, 0, 0), 'odd'), (1, 3, (1, 0, -1), 'odd'), (3, 1, (0, 0, 1), 'odd'), (0, 0, (1, 0, 0), 'odd'), (0, 2, (-1, 0, 0), 'odd'), (2, 0, (0, 0, 0), 'odd'), (2, 3, (0, -1, 0), 'y'), (2, 3, (0, 0, 0), 'x'), (2, 1, (0, 0, 0), 'z'), (3, 3, (0, -1, 0), 'odd'), (3, 1, (0, 1, 0), 'odd'), (1, 3, (0, 0, 0), 'odd'), (2, 2, (0, 1, 0), 'odd'), (2, 0, (0, -1, 1), 'odd'), (0, 2, (0, 0, -1), 'odd')]
CASES={'i':dict(J=mp.mpf(1),k2=mp.mpf(3)/20,z0=(-2+1j*mp.sqrt(5))/3),
       'ii':dict(J=mp.mpf(5)/2,k2=mp.mpf(45)/44,z0=(7+5j*mp.sqrt(11))/18)}
def Hmat(cs,sgn,x,y,z,kap):
    J=cs['J']; x0=sgn*mp.arg(cs['z0'])
    amp={'x':2,'y':2,'z':2*J,'odd':2*kap}
    H=mp.zeros(4,4)
    for a,b,n,kd in TERMS:
        ph=(n[0]-n[1])*(x0+x)+(n[0]+n[1])*y+n[2]*z
        e=mp.expjpi(ph/mp.pi)
        H[a,b]+=1j*amp[kd]*e
        H[b,a]+=-1j*amp[kd]*mp.conj(e)
    return H
class Node:
    def __init__(s,which,sgn):
        s.cs=CASES[which]; s.sgn=sgn; s.J=s.cs['J']; s.kap=mp.sqrt(s.cs['k2'])
        s.x0=sgn*mp.arg(s.cs['z0'])
        H0=Hmat(s.cs,sgn,0,0,0,s.kap)
        s.H0=H0
        P=mp.eye(4)-H0*H0/(16*s.J**2); Q=mp.eye(4)-P
        for wc in itertools.combinations(range(4),2):
            for uc in itertools.combinations(range(4),2):
                T=mp.zeros(4,4)
                for r in range(4):
                    T[r,0]=P[r,wc[0]];T[r,1]=P[r,wc[1]];T[r,2]=Q[r,uc[0]];T[r,3]=Q[r,uc[1]]
                if abs(mp.det(T))>mp.mpf(10)**-20:
                    s.T=T;s.wc=wc;s.uc=uc;break
            else: continue
            break
        s.P=P
    def blocks(s,H):
        G=s.T.H*H*s.T
        A=G[0:2,0:2];B=G[0:2,2:4];C=G[2:4,2:4]
        return A,B,C
    def num(s,x,y,z,kap):
        H=Hmat(s.cs,s.sgn,x,y,z,kap)
        A,B,C=s.blocks(H)
        detC=(C[0,0]*C[1,1]-C[0,1]*C[1,0])
        adj=mp.matrix([[C[1,1],-C[0,1]],[-C[1,0],C[0,0]]])
        Nm=detC*A-B*adj*B.H
        N0=(Nm[0,0]+Nm[1,1])/2; Nz=(Nm[0,0]-Nm[1,1])/2
        Nx=(Nm[0,1]+Nm[1,0])/2; Ny=1j*(Nm[0,1]-Nm[1,0])/2
        return [mp.re(Nx),mp.re(Ny),mp.re(Nz)],mp.re(N0),mp.re(detC),H,Nm
if __name__=='__main__':
    for w in ('i','ii'):
        for sg in (1,-1):
            nd=Node(w,sg)
            ev=mp.eigh(nd.H0,eigvals_only=True)
            print(w,sg,[mp.nstr(e,8) for e in ev],nd.wc,nd.uc,mp.nstr(abs(mp.det(nd.T)),8))
            Nv,N0,dC,H,Nm=nd.num(0,0,0,nd.kap)
            print(' N at node',[mp.nstr(v,5) for v in Nv],mp.nstr(N0,5),mp.nstr(dC,8))

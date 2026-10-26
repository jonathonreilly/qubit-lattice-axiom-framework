import sys; sys.path.insert(0,'.')
import mpmath as mp
from exact import modes
mp.mp.dps=40
def Fthr(K,m,V):
    # F at E=E_thr(K) with first mode z=-1 exactly; second mode decaying
    E=2*mp.sqrt(m*m+mp.sin(K/2)**2)
    c0,s0=mp.cos(K/2),mp.sin(K/2)
    sx=mp.matrix([[0,1],[1,0]]); B=mp.matrix([[-c0,0],[0,1j*s0]]); Bd=B.H
    p=E**2-2*c0**2; q=E**2-2*s0**2
    a2=-c0**2*s0**2; a1=p*s0**2-c0**2*q; a0=p*q-4*m**2*E**2
    disc=mp.sqrt(a1**2-4*a2*a0)
    xs=[(-a1+disc)/(2*a2),(-a1-disc)/(2*a2)]
    xs.sort(key=lambda x:abs(x+2))
    cols=[]
    for j,x in enumerate(xs):
        if j==0: z=mp.mpf(-1)
        else:
            z1=(x+mp.sqrt(x*x-4))/2; z2=(x-mp.sqrt(x*x-4))/2
            z=z1 if abs(z1)<abs(z2) else z2
        M=E*(E*mp.eye(2)-2*m*sx)-mp.matrix([[c0**2*(x+2),0],[0,-s0**2*(x-2)]])
        a=mp.matrix([-M[0,1],M[0,0]]); a2v=mp.matrix([-M[1,1],M[1,0]])
        if mp.norm(a2v)>mp.norm(a): a=a2v
        c=(B*z+Bd)*a/E
        cols.append((E*mp.eye(2)-2*m*sx-V*mp.eye(2)-Bd*B/E)*a-B*c)
    return mp.det(mp.matrix([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]]))
def Vc(K,m,guess):
    return mp.findroot(lambda V:Fthr(K,m,V).real,guess)
if __name__=="__main__":
    for mv in [mp.mpf(4),mp.mpf('0.8')]:
        s=mp.sqrt(64*mv**4+1); Vc0=(8*mv**2-1-s)/(4*mv)
        ks=[mp.mpf('0.02')*j for j in range(1,6)]
        vals=[]
        g=Vc0
        for k in ks:
            g=Vc(k,mv,g); vals.append(g)
        A=mp.matrix(5,5);b=mp.matrix(5,1)
        for i,k in enumerate(ks):
            for j in range(5): A[i,j]=k**(2*j)
            b[i]=vals[i]
        c=mp.lu_solve(A,b)
        print(mv,'Vc0 closed',mp.nstr(Vc0,15),'fit',mp.nstr(c[0],15),'Vc2 (coeff K^2)',mp.nstr(c[1],12),' Vc"=',mp.nstr(2*c[1],12))

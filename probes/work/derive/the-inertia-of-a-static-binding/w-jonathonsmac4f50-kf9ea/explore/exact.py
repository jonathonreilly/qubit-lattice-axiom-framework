import mpmath as mp
mp.mp.dps=40
def modes(E,K,m):
    c0,s0=mp.cos(K/2),mp.sin(K/2)
    # [E^2-c0^2(x+2)][E^2+s0^2(x-2)]-4m^2E^2=0  quadratic in x
    A=-c0**2*s0**2
    # expand: (E^2-2c0^2 - c0^2 x)(E^2-2s0^2 + s0^2 x)
    p=E**2-2*c0**2; q=E**2-2*s0**2
    # (p - c0^2 x)(q + s0^2 x) = pq + (p s0^2 - c0^2 q)x - c0^2 s0^2 x^2
    a2=-c0**2*s0**2; a1=p*s0**2-c0**2*q; a0=p*q-4*m**2*E**2
    if abs(a2)<mp.mpf(10)**(-30):
        xs=[-a0/a1]
    else:
        disc=mp.sqrt(a1**2-4*a2*a0)
        xs=[(-a1+disc)/(2*a2),(-a1-disc)/(2*a2)]
    out=[]
    B=mp.matrix([[-c0,0],[0,1j*s0]]); Bd=B.H
    sx=mp.matrix([[0,1],[1,0]])
    for x in xs:
        z1=(x+mp.sqrt(x*x-4))/2; z2=(x-mp.sqrt(x*x-4))/2
        z=z1 if abs(z1)<abs(z2) else z2
        M=E*(E*mp.eye(2)-2*m*sx)-mp.matrix([[c0**2*(x+2),0],[0,-s0**2*(x-2)]])
        # null vector
        # rows: M a=0 ; pick a=(M01, -M00) or (−M11, M10) whichever larger
        a=mp.matrix([-M[0,1],M[0,0]])
        a2v=mp.matrix([-M[1,1],M[1,0]])
        if mp.norm(a2v)>mp.norm(a): a=a2v
        c=(B*z+Bd)*a/E
        out.append((z,a,c))
    return out,B,Bd,sx
def F(E,K,m,V):
    ms,B,Bd,sx=modes(E,K,m)
    cols=[]
    for z,a,c in ms:
        v=(E*mp.eye(2)-2*m*sx-V*mp.eye(2)-Bd*B/E)*a-B*c
        cols.append(v)
    return mp.det(mp.matrix([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]]))
def Eroot(K,m,V,guess):
    return mp.findroot(lambda E:F(E,K,m,V),guess)

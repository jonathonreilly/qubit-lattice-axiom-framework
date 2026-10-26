import numpy as np, time
def AmB(r,N):
    h=2*np.pi/N
    k=(np.arange(N)+0.5)*h-np.pi
    # q = r zhat ; evaluate chi(r,0) and chi(0,r)
    sx=np.sin(k); 
    tot_a=0.0; tot_b=0.0
    SX,SY=np.meshgrid(sx,sx,indexing='ij')
    sxy2=SX**2+SY**2
    for kz in k:
        sz=np.sin(kz); szq=np.sin(kz+r)
        e1=np.sqrt(sxy2+sz*sz); e2=np.sqrt(sxy2+szq*szq)
        # chi(r,0): q=0: M=1, E=2e1
        a=4*e1/(r*r+4*e1*e1)
        M=(1+(SX*SX+SY*SY+sz*szq)/(e1*e2))/2
        E=e1+e2
        b=M*2*E/(E*E)
        tot_a+=a.sum(); tot_b+=b.sum()
    vol=(h/(2*np.pi))**3
    return (tot_a-tot_b)*vol/r**2

"""Independent check of the runner's 2-loop beta functions against the standard SM two-loop
expressions (Arason et al. 1992 / Machacek-Vaughn), written here from the literature (GUT-normalised g1),
top Yukawa only, lambda = 0. Difference = runner(loop2)-runner(loop1) vs my 2-loop terms."""
import numpy as np, itertools
import lane_rge_copy as H
PI=np.pi; k=1/(16*PI**2)
def mine2(g1,g2,g3,yt,lam):
    d1=g1**3*k**2*((199/50)*g1**2+(27/10)*g2**2+(44/5)*g3**2-(17/10)*yt**2)
    d2=g2**3*k**2*((9/10)*g1**2+(35/6)*g2**2+12*g3**2-(3/2)*yt**2)
    d3=g3**3*k**2*((11/10)*g1**2+(9/2)*g2**2-26*g3**2-2*yt**2)
    out=[]
    for s1,s2 in itertools.product((+1,-1),(+1,-1)):
        dy=yt*k**2*(-12*yt**4+yt**2*(36*g3**2+(225/16)*g2**2+(393/80)*g1**2)
                    -108*g3**4-(23/4)*g2**4+(1187/600)*g1**4+9*g3**2*g2**2
                    +s1*(19/15)*g3**2*g1**2+s2*(9/20)*g2**2*g1**2+6*lam**2-12*lam*yt**2)
        out.append(((s1,s2),dy))
    return d1,d2,d3,out
for pt in ([0.6,0.5,0.5,0.4,0.0],[0.5,0.62,1.1,0.9,0.0],[0.46,0.65,1.07,0.95,0.0]):
    g1,g2,g3,yt,lam=pt
    b1=np.array(H.beta_full(0.0,pt,n_f=6,loop_order=1)); b2=np.array(H.beta_full(0.0,pt,n_f=6,loop_order=2))
    r=b2-b1
    d1,d2,d3,dys=mine2(*pt)
    print("pt",pt)
    print("  runner 2-loop increments g1,g2,g3:",r[:3]," mine:",[d1,d2,d3])
    print("  runner 2-loop increment yt:",r[3]," mine (sign choices):",[(s,round(v,10)) for s,v in dys])

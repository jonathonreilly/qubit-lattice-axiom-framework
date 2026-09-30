"""Kill check K1: does the lane's own chart operator H(m,delta,q+) have any of the residual symmetries that R1 needs?
(unitary: S, transpositions, S*transposition ; antiunitary: T H* T = H for T in transpositions/identity)"""
import numpy as np, math, itertools
GAMMA=0.5; E1=math.sqrt(8/3); E2=math.sqrt(8)/3
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex)
T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex)
T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex)
def H(m,d,q): return HB+m*T_M+d*T_D+q*T_Q
W=np.ones(3)/math.sqrt(3); S=2*np.outer(W,W)-np.eye(3)
perms={"id":np.eye(3),"(12)":np.array([[0,1,0],[1,0,0],[0,0,1]]),"(13)":np.array([[0,0,1],[0,1,0],[1,0,0]]),"(23)":np.array([[1,0,0],[0,0,1],[0,1,0]])}
for pt,label in (((0.657,0.934,0.715),"data pin (0.657,0.934,0.715)"),((2/3,0.93305,0.7145),"three-identity"),((0.3,0.5,0.9),"generic")):
    h=H(*pt); print(label)
    for nm,P in perms.items():
        for nm2,X in (("",P),("S*",S@P)):
            c=np.linalg.norm(h@X-X@h)
            print(f"   unitary [H,{nm2}{nm}] = {c:.3f}")
        a=np.linalg.norm(P@h.conj()@P-h)
        print(f"   antiunitary  {nm} H* {nm} - H = {a:.3f}")

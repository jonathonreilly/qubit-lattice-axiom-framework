import numpy as np
from scipy.linalg import expm
def spin(j):
    d=int(round(2*j+1)); m=np.arange(j,-j-1,-1)
    Jz=np.diag(m).astype(complex)
    Jp=np.zeros((d,d),complex)
    for k in range(1,d):
        Jp[k-1,k]=np.sqrt(j*(j+1)-m[k]*(m[k]+1))
    Jx=(Jp+Jp.conj().T)/2; Jy=(Jp-Jp.conj().T)/(2j)
    return Jx,Jy,Jz
print("Uniform measure on the 6 quarter-turns (+-pi/2 about x,y,z); operator on spin-j block = (1/6) sum rho_j(g)")
print("j  C2   attacker_lambda=chi/(2j+1)  true eigenvalues (with multiplicity)  mean(eig)")
for j2 in range(1,13):
    j=j2/2; J=spin(j)
    for lift in ([1] if j2%2==0 else [1]):
        M=sum(expm(-1j*s*np.pi/2*Ja) for Ja in J for s in (+1,-1))/6
    ev=np.linalg.eigvalsh((M+M.conj().T)/2)
    chi=np.trace(M).real*6/6/ (2*j+1)
    print(f"{j:3.1f} {j*(j+1):6.2f} {np.trace(M).real/(2*j+1):9.4f}  min={ev.min():8.4f} max={ev.max():8.4f}  eig={np.round(ev,3)}")
# 24-element cubic group uniform (all proper cubic rotations) - class function? not full class function either.

"""K3: (a) record dephasing D(M)=P0 M P0 + P1 M P1 applied to a generic M in the SP23 commutant -> theta13 = 0 (TBM);
(b) data-status arithmetic for s23^2=0.5, delta=270 from the numbers quoted in Ding-Li-Lu-Petcov arXiv:2512.03809 Table 3 (NuFIT-6.0 with SK, NO)
    and the repo-quoted NuFIT-6.1 3 sigma ranges."""
import numpy as np, math
W=np.ones(3)/math.sqrt(3); XI=np.array([2,-1,-1])/math.sqrt(6); ETA=np.array([0,1,-1])/math.sqrt(2)
S=2*np.outer(W,W)-np.eye(3); P23=np.array([[1,0,0],[0,0,1],[0,1,0.]]); R=S@P23
rng=np.random.default_rng(5)
A=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); A=A+A.conj().T
M=(A+R@A@R)/2                                  # generic Hermitian M commuting with S*P23
assert np.allclose(M@R,R@M)
P0=np.outer(W,W); P1=np.eye(3)-P0
D=P0@M@P0+P1@M@P1
w,V=np.linalg.eigh(D)
print("M in SP23 commutant, then record dephasing: commutes with S:",np.allclose(D@S,S@D)," with SP23:",np.allclose(D@R,R@D)," with P23:",np.allclose(D@P23,P23@D))
print("  electron-row |U_e j|^2 of D(M) =",np.round(np.sort(np.abs(V[0])**2),6),"(0 => theta13 = 0)")
# data status (one-sided Gaussian yardstick only; NuFIT profiles are non-Gaussian)
print("\nNuFIT-6.0 with SK, NO (Ding et al. Table 3): s23^2 = 0.470 +0.017 -0.013 ; delta/pi = 1.18 +0.14 -0.23 ; 3sigma s23^2 [0.435,0.585], delta/pi [0.69,2.02]")
print("  s23^2=0.5   : (0.5-0.470)/0.017 = %.1f sigma above best fit; inside 3 sigma: %s"%((0.5-0.470)/0.017, 0.435<=0.5<=0.585))
print("  delta=1.5pi : (1.5-1.18)/0.14  = %.1f sigma above best fit; inside 3 sigma: %s"%((1.5-1.18)/0.14, 0.69<=1.5<=2.02))
print("  delta=+0.5pi (other sign R1 allows): inside 3 sigma: %s  (repo-quoted 6.1 ranges [114,405]/[125,365] deg -> 90 deg outside)"%(0.69<=0.5<=2.02))
print("JUNO 59.1 d s12^2 = 0.3092 +- 0.0087 (quoted in 2512.03809): TM1 0.318 -> %.1f sigma ; TM2 0.341 -> %.1f sigma"%((0.3182-0.3092)/0.0087,(0.341-0.3092)/0.0087))
print("TM1 |U_e1|^2 = 2/3 vs c12^2 c13^2 at (0.3092, 0.0222): %.4f  (old repo comparator 0.684 -> 'NO')"%((1-0.3092)*(1-0.0222)))

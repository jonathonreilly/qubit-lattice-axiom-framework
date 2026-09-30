"""Independent check of the SU(2) control used by T33's R1 (T28 testA): Wilson kernel W=exp(beta cos th) on SU(2) (beta=4 <-> 2N_c pin).
mpmath Bessel functions, own formulas."""
import mpmath as mp
mp.mp.dps=30
def w(beta,n): return (mp.besseli(n-1,beta)-mp.besseli(n+1,beta))/n
def gE2(beta,j2):
    j=mp.mpf(j2)/2; C2=j*(j+1)
    return 2*(-mp.log(w(beta,j2+1)/w(beta,1)))/C2
for j2 in (1,2,3,4):
    b=mp.findroot(lambda x: gE2(x,j2)-1, 4)
    print("j=%.1f  gE2(4)=%.5f  unit point beta=%.4f"%(j2/2,float(gE2(4,j2)),float(b)))
# what beta does the anchor beta_W=16 give? g_E^2(16)
print("gE2 at beta=16 (j=1/2): %.4f -> 4/16 = %.4f"%(float(gE2(16,1)),4/16))

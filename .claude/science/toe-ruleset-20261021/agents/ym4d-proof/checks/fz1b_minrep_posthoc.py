# POST-HOC (run after seeing fz1-B's FAIL).  Criteria file fz1_criteria.md is NOT edited and
# fz1_fwd.py / fz1_out.txt are NOT altered.  This diagnostic asks the question fz1-B should have
# asked: is the MINIMUM over the two exact slot representations still unbounded in k?
from fractions import Fraction as F
def e_R (k,th)      : return th*k + 2*(k-1)            # (R) slot at l=0, witness
def e_Pl(k,th,al)   : return th*(k-1) + (2+al)*(k-1)   # (Pl) slot at l=1, witness
def e_M (k)         : return F(2*(k-1))                # ||x||_M, witness
print("POST-HOC fz1b: min over the two exact representations.  Exponents of L.")
print("the single pre-registered FAIL of fz1-B was theta=1/4, alpha=1/8, k=2 "
      "((Pl)=L^19/8 < (R)=L^20/8, a gap of L^(1/8)).\n")
bad=[]
for th in [F(1,4),F(1,3),F(1,2),F(3,4),F(9,10)]:
    for al in [F(1,8),F(1,4),th]:
        if al>th: continue
        for k in [2,3,5,8,13,40,200]:
            r = min(e_R(k,th), e_Pl(k,th,al)) - e_M(k)
            if r <= 0: bad.append((th,al,k,r))
        k1,k2 = 40,200
        r1 = min(e_R(k1,th), e_Pl(k1,th,al)) - e_M(k1)
        r2 = min(e_R(k2,th), e_Pl(k2,th,al)) - e_M(k2)
        print("theta=%-5s alpha=%-5s   min-ratio exponent: k=40 -> %-7s   k=200 -> %-7s   "
              "growing: %s" % (th,al,r1,r2,r2>r1))
print("\nrows with min-ratio <= 1 (i.e. forward map bounded):", bad if bad else "NONE")
print("\nPOST-HOC CONCLUSION: the minimum over BOTH exact representations has exponent")
print("  min(theta*k, (theta+alpha)*(k-1)) - 0,  which -> infinity for every theta>0, alpha>0.")
print("So fz1-B's single k=2 failure does NOT rescue (FWD-0); fz1-A's verdict is undamaged.")

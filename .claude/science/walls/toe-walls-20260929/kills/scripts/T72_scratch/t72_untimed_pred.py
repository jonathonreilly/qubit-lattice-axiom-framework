import numpy as np
from t72_stag_pairband import W_pair_band
b=1.0;m=1.0;e0=0.0
direct_timed={0.2:0.90324,0.4:0.74827,0.8:0.50430,1.2:0.36884}
direct_untimed={0.2:0.92740,0.4:0.80100,0.8:0.59476,1.2:0.48060}
print("untimed-binding prediction (Hellmann-Feynman): W_untimed = (E0 - <V>) * E''(0),  <V> = lam dE0/dlam")
print(" lam   E0      <V>      E''     W_pred_untimed  W_direct_untimed  err   | W_timed_band W_timed_direct")
for lam in (0.2,0.4,0.8,1.2):
    Wt,E0,d2,_,_,_=W_pair_band(60,lam,b,m,e0,True)
    h=1e-3
    Ep=W_pair_band(60,lam+h,b,m,e0,True)[1]; Em=W_pair_band(60,lam-h,b,m,e0,True)[1]
    V=lam*(Ep-Em)/(2*h)
    Wu=(E0-V)*d2
    print(f"{lam:4.1f} {E0:7.4f} {V:8.4f} {d2:8.5f}  {Wu:10.5f}   {direct_untimed[lam]:10.5f}   {abs(direct_untimed[lam]-Wu)/Wu:6.3f} | {Wt:8.5f} {direct_timed[lam]:8.5f}")

import numpy as np
d=0.6
def kh(w,L,n):
    # trapezoid midpoint grid on (-d,d)
    x=(np.arange(n)+0.5)/n*2*d-d; h=2*d/n
    s=x[None,:]-x[:,None]
    T=(2/w)*np.sin(w*(d-np.abs(s)/2))*h
    ev=np.linalg.eigvalsh(T)
    return (ev**L).sum(), ev
for w in [1,2,3,4,5,6,7,8,9,10,11,12]:
    for L in [3,5]:
        vals=[kh(w,L,n)[0] for n in (200,400,800)]
        ring=(2*np.sin(w*d)/w)**L
        print(w,L,vals,ring)

import numpy as np
from common import dial
sets={
 'up  MZ (attack)':[1.24e-3,0.624,171.7], 'down MZ (attack)':[2.69e-3,0.0535,2.86],
 'up  2GeV/own':[2.16e-3,1.27,162.5], 'down 2GeV/own':[4.67e-3,0.0934,4.18],
 'up  pole-ish':[2.16e-3,1.67,172.7], 'down pole-ish':[4.67e-3,0.0934,4.78],
 'up  1GeV-ish':[2.16e-3*1.3,1.27*1.3,172.7*0.9], 
}
for k,m in sets.items():
    q,r,d=dial(m); print('%-18s Q=%.4f r=%.4f delta=%.4f  scale-free pred 4r/(1+4r)/3=%.4f'%(k,q,r,d,4*r/(1+4*r)/3))

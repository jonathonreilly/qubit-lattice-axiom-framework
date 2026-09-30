import math
P=0.59371
ab=1/(4*math.pi)
# Lepage-Mackenzie (PRD48,2250) plaquette relation, coefficients from memory (label: reading):
# -ln P = (4 pi/3) aV(3.40/a) [1 - 1.185 aV]
lhs=-math.log(P)/(4*math.pi/3)
a=lhs
for _ in range(50): a=lhs/(1-1.185*a)
print('LO aV=%.4f  NLO aV(3.4/a)=%.4f'%(lhs,a))
b0=11.0
for name,a0 in (('LO 0.1246',lhs),('NLO',a)):
    print('anchor',name)
    for n in (0,1,2,4):
        v=ab/P**(n/4)
        lnq=2*math.pi*(1/v-1/a0)/b0
        print('  n=%d alpha=%.4f  q = 3.4/a * %.2f = %.1f/a  (BZ edge pi/a=3.14/a)'%(n,v,math.exp(lnq),3.4*math.exp(lnq)))

import math
MPL=1.220890e19  # GeV, as in repo? check
abare=1/(4*math.pi)
def v(P, n=1, mpl=MPL): return mpl*(7/8)**0.25*(abare/P**(n/4))**16
for P in [0.5934,0.5934379,0.59340+0.0003,0.5937]:
    print(P, v(P), v(P)/v(0.5934)-1)
print('n=2 base:', v(0.5934,2), v(0.5934,2)/v(0.5934))
print('alpha_LM', abare/0.5934**0.25, 'alpha_s(v)', abare/0.5934**0.5, 'alpha/P', abare/0.5934)

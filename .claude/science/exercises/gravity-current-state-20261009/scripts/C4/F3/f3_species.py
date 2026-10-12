# How many light species (or how large a central charge) would a sector at scale M* need to bend the graviton's
# quadratic action at O(1) at k ~ M*?  Free conformal scalar: induced Weyl^2 coefficient 1/(120*16 pi^2) per scalar
# (comparator, standard heat-kernel a2 coefficient), multiplying ln(k^2/mu^2).  Relative to the EH term (M^2/2... use M^2 k^2):
#   rel(k) ~ N * k^2 * ln / (1920 pi^2 M^2)    [one-loop, O(1) tensor factors dropped: suggested]
import math
MPl=1.221e19; MPr=2.435e18
for Ms in (1.5e10,2e9):
    for lab,M in (("nonred",MPl),("red",MPr)):
        for ln in (1.0, 2*math.log(MPl/Ms)):
            N = 1920*math.pi**2*(M/Ms)**2/ln
            print(f"M*={Ms:.1e} {lab:6s} ln={ln:5.1f}: N_species(conformal scalars) for O(1) bending ~ {N:.2e}")

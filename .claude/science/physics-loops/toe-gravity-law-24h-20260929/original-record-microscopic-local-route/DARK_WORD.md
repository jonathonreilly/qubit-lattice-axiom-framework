# Actual cubic positive-grade creation and a dark word

This is an exact source-word discriminator, not a simulation of the full process or an extra measured field/sign record. It uses the original cubic F_a and j_(a,b,sigma), and therefore its Gauss and output meanings are fixed by the supplied law. All displayed field transitions are0 to+/-1, with unit normalized-spin amplitude for every integer S>=1.

Let F=sum_a F_a. The first dressing generator for T=-(F+F^*) is S1=-F+F^*. Outward F_a commute and F_a^2=0. For an original jump at a, [F_c,j_(a,b,sigma)]=0 when c!=a. The grade+1 part of the second transformed-jump coefficient is consequently

    J_(m,+1)^(2)=(1/2)[F,[F,j_m]]=-F_a j_m F_a.       (D1)

The second-order generator of a local ordered implementation can have only W grade0: [F_a,F_c]=[F_a^*,F_c^*]=0, while the remaining inter-gate commutators have grade0. It cannot change(D1). This formula is a coefficient of the actual dressed original jump, not a newly resolved instrument.

On Omega, for one of six fixed birth edges, the first outward hop and the final outward hop choose two distinct other edges. For sigma=+, exchanging these two edges gives the same physical output, with coefficient2; there are choose(5,2)=10 such outputs, so the norm squared is40. For sigma=-, the plus and minus B occupants distinguish the two choices; there are5*4=20 outputs of coefficient1, so the norm squared is20. The plus and minus sets are disjoint, and the unnormalized coherent-edge jump has norm squared60. Thus the total positive-grade creation coefficient per A center in the original scaled dissipator is

    kappa epsilon^2 *6*(40+20)
       =360 kappa epsilon^2,

for either original instrument, although their individual marked output coherences differ.

An actual source word also disproves a tempting stronger absorption inequality. Let a=0, c=e_x+e_y, d=e_x+e_z and b_extra=2e_x+e_z. Starting from Omega, use these internal components of the specified original marks:

1. B_(c,e_y,+): old hop c->e_x and birth c->e_y.
2. B_(d,b_extra,+): old hop d->e_z and birth d->b_extra.
3. The positive-grade component -F_a j_(a,-e_x,+)F_a: old hop a->-e_y, birth a->-e_x, new hop a->-e_z.

The final basis word has one A hole at a, all six B neighbors of a occupied and seven occupied B sites in total. The original bare loss is exactly G=0. Its coefficient is-2 in the full product above; the sparse runner retains all paths, not only this selected sequence, and verifies the resulting coefficient and every intermediate Gauss constraint.

This dark word is not stationary. For the actual rotor fast coefficient H2=C+[F,F^*], take c2=2e_x. Refilling a from e_x and then hopping c2 into e_x gives a target with hole c2. The reverse-order path is blocked, compensation C cannot change the A-hole position, and the exact matrix element is+1. The target has four empty B neighbors and G=8.

Therefore G>=cW and ||H2 psi||<=C||G^(1/2)psi|| are false on the actual physical carrier. This does NOT prove an invariant dark sector, persistent fast propagation, failure of convergence from Omega, or a rate for visiting the displayed internal component. FAST_ONE_HOLE_ABSORPTION.md explicitly exploits the bright output instead of treating the pointwise failure as a no-go.

check_dark_cubic.py uses only sparse integer dictionaries. DARK_CUBIC_RESULTS.json records5,23,100 words after the successive products, exact Gauss checks, coefficients40/20/60, dark loss0 and bright loss8. Executed cost0.020384 CPU seconds,20,054,016 peak RSS bytes. The source-level formula(D1), its relation to a local dressing and its dynamical scope are analytic arguments, not conclusions inferred from this finite control.

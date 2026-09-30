# Exact dense-dark moving-weight discriminator

This is an actual-word obstruction to one proposed multiplier extension. It is not a bare-Omega probability estimate or a no-go for the desired energy bound. A separately recorded small exact control corroborates the geometry; the argument below is the all-m proof.

Use integer coordinates on an even cubic torus L>=16; every displayed coordinate has its unaliased local lift. Orient links A to B. Let

    h=(0,0,0), c=(2,0,0), b=(1,0,0), r=(1,1,0).

At the end there is one A hole at h; every other A has charge+1. All eleven B sites in N(h) union N(c) are occupied, and no others. The shared b has charge+1. Set

 u0=(-1,0,0), u1=(0,1,0), u2=(0,-1,0), u3=(0,0,1), u4=(0,0,-1),
 v0=(3,0,0),  v1=(2,1,0), v2=(2,-1,0), v3=(2,0,1), v4=(2,0,-1).

The five pairs are (u1,v1) at r, (u0,u2) at h, (u3,u4) at h, (v0,v2) at c, and (v3,v4) at c. In each pair the first B has charge+1 and the second charge-1. Its two links carry respectively-1 and+1. The additional h-b link carries-1. Thus total B charge is+1, exactly balancing the vacancy's charge defect. There are eleven unit field links in this baseline configuration.

## Legal preparation and Gauss

From Omega first make m copies of the electric curl on the plaquette

    a=(-2,0,0), d=(-3,1,0), x=(-3,0,0), y=(-2,1,0).

One copy consists of the four legal primitive hops a->x, d->y, x->d, y->a. A occupations and charges return to Omega and the two B sites return empty. The resulting field changes are E_ax=-1, E_dy=-1, E_dx=+1, E_ay=+1. Their divergence is zero at every vertex. After m repetitions these four links carry magnitudes m. None is a baseline pair link.

For each of the five pairs above, perform the actual outward hop from its stated A center to its first B, then the original plus birth on the second B edge. The A center returns to charge+1 and the second B gets charge-1. Finally perform h->b. Every intermediate word obeys the original Gauss law div E=q-1_A. This is also immediate stepwise because every primitive changes its endpoint charges by exactly its link divergence.

At finite integer spin S>=m, every preparation step is legal and has a nonzero normalized shift coefficient; intermediate |E| never exceeds max(m,1). The coherent original edge mark includes the displayed plus branch. Its other sign produces a different charge on that marked B, which is never changed later, so it cannot cancel this component. This proves algebraic nonzero word accessibility, not a lower bound on its amplitude or probability in the continuously evolving microscopic ensemble. A large m requires a long prior primitive word.

Call the resulting physical basis word alpha_m. Now apply the actual two-hop term

    f_(c,b) f_(h,b)*.

The first hop refills h from occupied b and changes E_hb:-1->0. The second moves charge+1 from c into b, changes E_cb:0->-1, and leaves a hole at c. Call this beta_m. Both normalized spin coefficients are exactly one for every S>=1. The complete leading D2 matrix element is

    <beta_m,D2 alpha_m>=1.                                (M1)

Indeed a hole move from h to c can only use [F_c,F_h*]. Their axial stars share only b. The displayed order is the unique path to beta_m. F_c alpha_m=0 since every neighbor of c is occupied, so the reversed order contributes zero. Same-hole terms and diagonal compensation cannot connect distinct hole positions, and all other moving terms have another output hole. Thus(M1) uses the actual compensated operator rather than a chosen path without its competitors.

## Weights, darkness and the failed inequality

Both words have all six neighbors of their hole occupied and exactly eleven occupied B sites within radius three. They are dark and outside the checked sparse projection with cap nine:

    G alpha_m=G beta_m=0,   Pi alpha_m=Pi beta_m=0.           (M2)

For q_mov defined in FIXED_FIELD_MULTIPLIER, all eleven baseline links have A endpoints within distance two of either h or c. The plaquette has two links at A endpoint a, which is distance two from h and four from c; its other A endpoint d is distance four from h and six from c. Hence exactly

    q_mov(alpha_m)=12+2m,     q_mov(beta_m)=12.              (M3)

The global first and second electric sums are the SAME on the two words:11+4m and11+4m². This discriminator is caused solely by moving the sampling center. It is not a demonstration of electric-energy growth on this transition.

For the moving congruence U_mov=sqrt(q_mov)T sqrt(q_mov), the signed permutation O vanishes in every row and column of both dark-bad words. Thus on this two-dimensional compression, U_mov is diagonal with entries a q_mov. The no-event derivative has zero diagonal and off-diagonal magnitude2a delta m, by(M1)-(M3); the original loss is zero there. One normalized coherent superposition of alpha_m,beta_m therefore has expectation

    <L(U_mov)>=2a delta m,      <q_mov Pi>=0.                (M4)

No constant independent of m can satisfy L(U_mov)<=-q_mov Pi+cI on all these physical inputs. Finite spin does not remove this example: the selected H matrix coefficient remains one for S>=m, Delta_S is diagonal, and the compressed O still vanishes on both inputs.

This excludes the tempting direct substitution of a moving local weight into the fixed-field multiplier. It does not exclude a different weighted observable, a conditional source estimate, a cancellation after averaging the actual Omega evolution, or the desired uniform dark first-field residence. No all-state example is promoted to an actual-state lower bound.

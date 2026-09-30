# A source-specific fast one-hole absorption bound

Candidate partial theorem, September30,2026. This is independent of DEFECT_LEMMA. It concerns the actual rotor leading second-order fast coefficient, in a fixed low-GLOBAL-excitation sector. It is not the full compensated microscopic comparison. Every jump below is an original resolved or unnormalized coherent-edge jump; the loss is the same for both instruments. No dark-state projection is a newly supplied observation.

## 1. Exact coefficient and uniform norm

Use an even cubic torus L>=6, integer rotors, the full A/B qutrit carrier with the original Gauss constraint, F=sum_a F_a, and W=sum_a w_a, w_a=1-n_a. The compensating rotor coefficient is C=sum_a F_a^*F_a Q_a, where Q_a is the product of n_c over the18 other A centers at distance2. The first local rotation generator is -F+F^*. Direct BCH calculation gives the actual W-preserving second coefficient

    H=C+[F,F^*]
     =sum_a(F_a F_a^*-F_a^*F_a(1-Q_a))
       +sum_(a!=c,dist(a,c)=2)[F_a,F_c^*].                 (A1)

The finite-spin D_a/[S(S+1)] compensation is not included in(A1): this is its leading rotor fast coefficient on fixed-field vectors. It must not be substituted for the entire finite-spin microscopic dynamics. The fast clock is u=t/epsilon^2, after removing the scalar delta epsilon^-4 W within a fixed W sector.

The incidence bound ||F_a||^2<=12 applies to every charge/occupation/field sector. F_a F_a^* is supported on w_a, while F_a^*F_a commutes with Q_a and 1-Q_a<=sum_(c:dist(a,c)=2)w_c. A cross commutator has norm<=24, is supported on the two-hole-possibility projection w_a vee w_c on BOTH sides, and vanishes for non-neighboring stars. Consequently, as quadratic forms,

    |<psi,H psi>| <=(12+18*12+2*18*24)<psi,W psi>
                   =1092<psi,W psi>.                       (A2)

Since H commutes with W, its restriction to W=1 is bounded by M=1092, independently of volume and fields. This proof uses actual local occupation support, not ||F||=O(volume). H also preserves the total B occupation k.

On W=1 the exact original loss is diagonal:

    G=sum_m j_m^*j_m
      =2*(number of empty B neighbors of the unique A hole),
    0<=G<=12.                                             (A3)

The fast no-event contraction is S(u)=exp[u(-i delta H-kappa G/2)]. Its first absorbing jump has the actual label m and map sqrt(kappa)j_m S(u). In this leading one-hole problem it lands in W=0. This is not a replacement of later microscopic waiting times by a proxy.

## 2. Dark configurations, and six rows with no cancellation

Restrict now to W=1 and global k<=9. For k<=5, G>=2(6-k)I already gives direct absorption. For6<=k<=9 let D=1_(G=0), B=I-D. A dark basis configuration has a hole a whose entire six-site B neighborhood N(a) is occupied. B has G>=2.

Two distinct cubic A stars share at most two B sites. Thus |N(a) union N(a')|>=10 for a!=a', including on the stated L>=6 tori. A B occupancy mask with k<=9 has at most ONE dark A center.

For each of the six axial centers c=a+/-2e_i, the two stars have exactly one common B site b. On a dark input the term F_c F_a^* refills a from b and then moves the occupant of c into b, leaving the hole at c and preserving the B occupancy mask. Its coefficient is +1. The reverse-order term F_a^*F_c is blocked for this same-b path. The rotor shifts and charge transfer define an isometry on this basis domain. The output has at most

    |N(c) intersect N(a)|+(k-6)=k-5<=4

occupied B neighbors at c, so its G eigenvalue is at least4.

Here is the needed absence of destructive interference, including terms not selected above. A hole-moving term in(A1) preserves the B occupancy mask: paths using distinct intermediate B sites cancel between the two orders of [F_c,F_a^*], leaving only shared-same-B paths. Terms that leave the hole center fixed change the B occupancy mask by at most one particle move. A selected axial output therefore cannot be reached from any other dark input:

- If that input has a different hole center from the output, the mask is preserved. The mask has a unique dark center a, and the axial shared site determines the inverse charge/field path uniquely.
- If that input has its hole already at the output center c, one B particle move could lower its number of occupied neighbors from six to at least five. The selected output has at most four, so this case is impossible.

The six output hole centers differ. Different input masks, charges and fields have disjoint or injective selected ranges. Let R project onto their union. For every psi_D in the dark subspace this proves the exact identities/inequality

    ||R H psi_D||^2=6||psi_D||^2,
    ||G^(1/2) H psi_D||^2>=24||psi_D||^2.              (A4)

The projection R is used only in this proof. It is not an additional record readout. The argument remains valid after restricting to Gauss because every contributing original word preserves Gauss.

For arbitrary psi, put x=||G^(1/2)psi|| and y=||G^(1/2)H psi||. Then ||B psi||<=x/sqrt(2) and

    sqrt(24)||D psi||<=y+sqrt(12)M||B psi||
                       <=y+sqrt(6)M x.

Hence ||psi||^2<=y^2/12+(M^2+1)x^2/2. With c0=2/(M^2+1),

    G+H G H >= c0 I.                                  (A5)

This is a two-step absorption inequality. The stronger pointwise inequality G>=cW is false, as the actual dark word in DARK_CUBIC_RESULTS.json demonstrates.

## 3. Elementary uniform decay; explicit constants

No generic unbounded-system decay theorem is imported. Here H and G are bounded on the exact sector with the uniform constants above. Let

    c_delta=min(1,delta^2)c0,
    R0=delta^2 sqrt(12) M^2/2,
    tau=min(1,sqrt(5c_delta)/(8R0)),
    c_U=c_delta tau^3/64,
    a0=min(1/2,kappa c_U/(1+6kappa tau)^2),
    C0=exp(a0/2),  gamma=a0/(2tau)>0.                  (A6)

For U(u)=exp(-i delta H u), write G^(1/2)U(u)psi=a+u b+r(u), with a=G^(1/2)psi, b=-i delta G^(1/2)H psi and ||r(u)||<=R0 u^2||psi||. Inequality(A5) gives ||a||^2+||b||^2>=c_delta||psi||^2. For tau<=1 the scalar Gram matrix of1,u on[0,tau] has minimum eigenvalue at least tau^3/16: its determinant is tau^4/12 and its trace is at most4tau/3. Using ||p+r||^2>=||p||^2/2-||r||^2 and(A6),

    integral_0^tau ||G^(1/2)U(u)psi||^2 du
           >=c_U||psi||^2.                            (A7)

Duhamel gives U-S=(kappa/2) integral U G S. In L2([0,tau]) the Volterra integration norm is at most tau. Since G<=12,

    ||G^(1/2)U(.)psi||_L2
         <=(1+6kappa tau)||G^(1/2)S(.)psi||_L2.

Finally d||S(u)psi||^2/du=-kappa||G^(1/2)S(u)psi||^2. Thus ||S(tau)||^2<=1-a0. Iteration and contraction on the remaining fractional interval prove

    ||S(u)||<=C0 exp(-gamma u),  u>=0.                (A8)

The constants are deliberately crude. In particular their smallness is not a feasible-time claim. They are positive and independent of torus volume, charge assignments and electric fields at fixed delta,kappa. No diagonalization of a large Hilbert space is involved.

## 4. Field-weighted surviving and absorbed outputs

Let Q=1+sum_links|E| on a finite torus. On the sector above, H has integer Q bandwidth<=2, G commutes with Q, and ||H||<=M. The band components H_r, -2<=r<=2, obtained by phase averaging against Q, have norm<=M. Set

    alpha=(1/2)log(1+gamma/(10 C0 delta M))>0.

The bounded conjugated generator defined by these five bands differs from -i delta H-kappa G/2 by at most5delta M(exp(2alpha)-1)=gamma/(2C0). Duhamel with(A8) therefore gives

    ||exp(alpha Q) S(u) exp(-alpha Q)||
                   <=C0 exp(-gamma u/2).              (A9)

The identity is first proved on finite-field vectors by the bounded band-generator power series, then closed on the exponential-weight domain. It is not based on an electric-box approximation retaining(A8); deleting box-edge transitions could spoil the geometric absorption inequality.

Let J be the stack of the ACTUAL original j_m maps, with their labels unchanged. It has norm<=sqrt(12) on W=1 and Q input/output bandwidth<=1. Its three band components imply ||exp(alpha Q_out)J exp(-alpha Q_in)||<=3exp(alpha)sqrt(12). Thus, for each psi with finite exponential field norm,

    integral_0^infinity kappa sum_m
       ||exp(alpha Q_out) j_m S(u)psi||^2 du
     <=108 kappa exp(2alpha) C0^2/gamma
                         ||exp(alpha Q_in)psi||^2.     (A10)

This controls all polynomial electric moments during a surviving fast excursion and in its original marked absorbing output. It is a genuine weighted estimate, not a trace-norm tail inference. It does not identify these excursions with an autonomous component decomposition of the full microscopic process.

## 5. Exact scope and remaining bridge

The assumptions are the supplied rotor/qutrit carrier, original local maps, canonical compensation, cubic geometry, fixed positive delta,kappa, W=1 and GLOBAL N_B<=9. Bare Omega has k=0, but the actual macroscopic process on a large torus creates extensive B occupation. A local sparse configuration is not automatically a state in this global sector. This theorem therefore does not close the thermodynamic microscopic comparison, does not control sectors with many simultaneous holes, and does not justify treating every rare defect as an independent excursion.

Passing from(A1) to the finite-spin fast generator uniformly on the relevant evolving field class is also a separate task. The exact microscopic electric compensation and higher local terms have not been dropped from the main target contract. A full result still needs a many-body local estimate tying defect propagation, original jump/loss coherences and field moments to the actual bare-Omega ensemble. The current result isolates a proved low-excitation mechanism that survives the explicit failure of pointwise absorption, rather than mistaking that failure for a no-go.

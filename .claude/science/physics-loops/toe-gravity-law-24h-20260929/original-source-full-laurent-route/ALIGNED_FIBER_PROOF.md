# An aligned, formally source-invisible dark line at the flat phase

This separate discriminator is conditional mathematics of the supplied rotor. It does not settle the almost-everywhere Laurent observability problem. The periodic adjacency-zero wave is prior art in the checked finite-cluster/late-tail packets. The new ingredient here is its different, literal polarized charge assignment and the resulting annihilation by EVERY original positive-source adjoint. The previously checked Dicke-charge vector instead has a nonzero actual source overlap. These are different vectors in the same large physical sector.

## 1. Physical charge assignment and capacity

Let L>=8 be divisible by four, n=L^3/2 and m=L/2. Work on the exact global W=1, NB=n-1, total-charge-n physical rotor sector. Its number of minus occupations is

    r=(n-2)/2.                                             (1)

Put the unique B vacancy at v=(1,0,0). Give every occupied A site charge +. Define the three-layer B band

    T_B={b in B: (b_y+b_z-m) mod L is -1,0 or 1}.           (2)

Each layer contains L^2/2 B sites, so |T_B|=3L^2/2. Give every B site in T_B charge +. Choose ANY set M of exactly r minus B sites outside T_B and outside v; give every other occupied B site charge +. The capacity is sufficient because

    |B\(T_B union {v})|-r
      =n-3L^2/2-1-(n/2-1)=L^2(L-6)/4>=0.                 (3)

The vacancy v is outside T_B: its y+z layer is zero, while m>=4. Total B charge is (n-1)-2r=1; occupied A charge is n-1. Thus total charge is exactly n. Every hole position below has an integer Gauss flow, since the prescribed divergence sums to zero. No global all-plus occupation state with the wrong physical charge is being substituted.

Use the standard spanning-tree Gauss fiber representation. At zero independent cycle angle every legal unit rotor hop has coefficient one. Charge-dependent tree-flow representatives are included in this representation. The single angle fiber itself is not a normalizable rotor preparation.

## 2. The actual hole wave and every canceled row

For an A hole at h let |h;M,v> denote the physical fiber basis word with the charges just specified. Let

    f(h)=i^(h_x)(-1)^(h_z) 1_((h_y+h_z) mod L=m),
    psi=p^(-1/2) sum_(h in A) f(h)|h;M,v>,
    p=L^2/2.                                               (4)

Because m is even, h_x is even on this plane. Thus all nonzero f(h) are real + or -, and ||psi||=1. Every B neighbor of a supported hole lies in T_B and is occupied with charge +. Consequently G psi=0, and every supported star is aligned plus.

Let K be the ordinary cubic A-to-B incidence matrix, (Kf)(b)=sum_(h~b)f(h). The x-neighbor pair cancels by i+i^(-1)=0 whenever its plane indicator is nonzero. If b_y+b_z=m+1, the contributions h=b-e_y and h=b-e_z cancel because their z parities differ; if the sum is m-1, the corresponding +e_y,+e_z pair cancels. All other cases are zero. Therefore

    Kf=0.                                                  (5)

To use (5) one must reconstruct the ACTUAL canceled Hamiltonian, not assume H=FF*. The previously checked rotor identity is

    P_h H P_h=P_h(F_h F_h* -sum_(a:dist(a,h)=2)F_a*F_a)P_h,
    P_a H P_h=P_a[F_a,F_h*]P_h,  a!=h,                    (6)

with off-diagonal blocks zero unless a and h share B. For each supported h, its periodic graph distance from v is at least m+1>=5. The y/z distances sum to at least m, and its even x coordinate differs from v_x=1 by at least one. Hence every a at distance two from h is at least three from v. Since v is the only empty B site, the first hop F_a in every negative same-hole term in (6) is blocked.

In F_h F_h*, each of the six B donors has charge +. Refilling h leaves that donor as the only empty B neighbor of h, so the return is unique and contributes one. Thus its diagonal contribution is exactly six and does not change the background charges.

For a sharing a B neighbor b with h, b has charge + and A_a has charge +. The order F_a F_h* refills h from b and then empties a into b. It preserves the whole fixed B charge pattern and produces |a;M,v> with coefficient one for each shared b. The reverse order F_h*F_a is blocked, since a is not adjacent to v. All more distant relocation terms have already canceled in (6). There are no other output charge patterns. In particular a supported superposition is mapped by the complete H into the same fixed-B-charge hole-word sector with coefficient K* K f, including rows whose hole is outside the plane.

Equations (5)-(6) therefore give

    H(0)psi=0,       G psi=0.                              (7)

This is an exact invariant dark line for the leading fast no-event generator at the flat phase. The proof never identifies H globally with FF*: away from the declared supported columns that identity is false. The minus B charges outside the band need not be permuted into a symmetric Dicke state; every used donor and recipient in the supported columns has been checked literally.

## 3. Formal source invisibility is exact, and has a different scope

For every original source at h, B_(h,mu)^+=-F_h j_mu F_h adds three occupied B sites and leaves h as its sole A hole. A full six-B output at that h must therefore arise from a three-occupied input star. On the three newly filled sites the charges are sigma, nu, -nu: one is the old A charge sigma and the other two have opposite signs. They can never all be plus, and can never all be minus. This is also the exact aligned kernel of the checked source-frame theorem.

Every nonzero hole component of (4) has all six B neighbors plus. The source adjoint at any different hole location is zero by A-hole orthogonality. Thus, for every center and every resolved sign or original coherent edge label,

    (B_(h,mu)^+(theta))* psi =0                            (8)

for ALL cycle angles theta, using the same constant charge-word section psi. Phases cannot alter this charge obstruction. Equivalently every formal source B_(h,mu)^+ phi is orthogonal to this section, irrespective of the actual or hypothetical input phi. At theta=0, (7) makes that invisible section an exact dark eigenvector. A positive source made from any density therefore has zero quadratic weight in this particular dark line at that fiber.

This is not the previously checked Dicke-charge dark vector. That vector has mixed stars in its charge superposition and a complete original history word has nonzero overlap with it. The existence of a dark fiber by itself consequently says nothing about whether a specified source excites that fiber's particular dark branches.

## 4. Quantifiers that do not follow

The construction refutes an ALL-phase assertion that no aligned dark line exists, and an ALL-phase injectivity claim for the augmented fast-observation stack after adding all formal source adjoints. It does not provide a positive-Haar set of dark fibers, a Laurent null module, or a normalizable invariant rotor state. Equation (8) holds for all phases, but (7) has only been established at theta=0. Away from that phase H(theta) can mix this fixed section into observable or mixed-star states.

The checked generic slab theorem is consistent with this example: the hole wave is plane-confined, so it cannot continue as a plane-confined dark eigenbranch at almost every phase. This proof does not evade that theorem or use its exceptional set as an actual positive-measure preparation. The physical rotor source and its evolution remain the original ones. No nonzero actual Omega weight, source survival tail, finite-spin transfer, continuously forced residence or energy statement follows from (7).

The full remaining problem is still to rule out (or exhibit with actual overlap) an extended invariant dark Laurent module at generic physical cycle phase. The formal source frame and this invisible exceptional branch refine the alternatives but do not decide that problem.

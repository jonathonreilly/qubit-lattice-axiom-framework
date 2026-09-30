# Independent precomparison reconstruction: crowded fast sectors

This derivation is frozen before reading the author proof or code. Exposure consists of the complete author CONTRACT, the parent brief that a filled-B W=2 sector and arbitrarily deep dark islands were claimed, my earlier original-source work, and the already disclosed one-hole/seven-B word and my own low-global-N_B<=9 candidate. No blank-slate claim is made. This is a focused independent check, not formal review or audit. Only this directory may be written.

The actual current-main compensation and finite-rate local-law sources were reread completely at30a9461ee19a49b99fa6628fe942f08e504e8903. They keep the full qutrit matter, normalized spin or separately supplied rotor links, Gauss div E=q-1_A, original resolved or unnormalized coherent-edge births, and actual gated compensation. Procedures remain7146. The original campaign deadline and STOP sentinel apply.

## 1. Exact leading coefficient and loss

Let F=sum_a F_a, T=-F-F^*, W=sum_A w_a, with [W,F]=F. The first rotation generator is S1=-F+F^*. Since [S1,W]=-T and [S1,T]=2[F,F^*], the exact second coefficient is

    H2=C+[F,F^*].                                      (P1)

The local-order ambiguity at second order commutes with W and does not change(P1). Distinct outward F_a commute. Every term of H2 preserves total record number N and W, hence also N_B=N-N_A+W. In the rotor law C=sum_a F_a^*F_a Q_a. For spin, write C_S=sum_a F_a^*F_a Q_a+V_S, with V_S=sum_a(D_a/[S(S+1)])Q_a diagonal. Thus

    H2_S=V_S+K_S,
    K_S=sum_a[F_a F_a^*-F_a^*F_a(1-Q_a)]
          +sum_(a!=c,dist2)[F_a,F_c^*].              (P2)

The complete original resolved and coherent instruments have identical loss. On one empty-A/empty-B edge at field m, its spin loss is2(1-m^2/[S(S+1)]), which lies between2/(S+1) and2. The rotor value is2. Consequently G is diagonal, G<=12W, and in either carrier its kernel consists exactly of configurations in which every A hole has all six B neighbors occupied. No sign is measured to obtain this equality.

## 2. An exact filled-B invariant leading sector

Let P_(r,full) be W=r, N_B=|B|. On this sector F=0, all bare jumps vanish, and the complete compensation C_S=0: every term needs an empty B neighbor. Since H2 preserves W and N_B,

    H2|_(r,full)=F F^*|_(r,full),
    G|_(r,full)=0,                                      (P3)

and this is an invariant self-adjoint sector for the LEADING fast coefficient, in spin as well as rotor. Spin boundaries may suppress individual paths but cannot create a leakage from this occupation sector. In the rotor case, and on suitable finite-spin words, F F^* is nontrivial: refill one hole a from a B neighbor b and then move a different occupied A neighbor c into that b. This moves the hole a->c, permutes charges and updates the two actual link fields.

For fixed r, the matrix is bounded independently of volume even on rotors. An input basis word has at most6r possible refills; each intermediate has one B vacancy and at most6 legal outward hops into it. All matrix weights are nonnegative and at most1. The self-adjoint Schur row-sum estimate gives ||F F^*||<=36r on this sector. Thus for r=2 the no-event propagator is a unitary with norm1 for all fast times. Any strictly positive, background-independent exponential decay bound over all physical W=2 states is false. This is already a finite-volume statement; no unbounded-operator domain is concealed.

Physical charge parity matters. On an even cubic torus |B|=L^3/2 is even. Starting from Omega, N-N_A must be even. Filled B with W=1 has N-N_A=|B|-1 odd and is not in the birth-accessible total-number parity. W=2 has N-N_A=|B|-2 even and is the correct accessible choice. Arbitrary Gauss words cannot be treated as source-accessible without this check.

## 3. Explicit actual birth/hop accessibility

Here is a construction on L divisible by4, L>=8; an existence family is sufficient and is not an assertion for every even period. For each fixed y,z, put p=(y+z) mod2. The A centers a=(4j+p,y,z), j=0,...,L/4-1, partition the B sites in that row into pairs b_-=a-e_x, b_+=a+e_x. All selected pairs are disjoint. At each pair use the actual mark B_(a,b_+,+)=P j_(a,b_+,+)F_a P, choosing the internal old-hop component a->b_-. It leaves a charged+, b_- charged+, b_+ charged-, and uses only initially zero link fields with changes0->-1 and0->+1.

Omit the central pair at a=0. After all other |B|/2-1 births, only b_-= -e_x and b_+=e_x are empty in B. The sites h_-=-2e_x and h_+=2e_x have remained occupied+. Two legal outward hops h_->b_- and h_+->b_+ fill B completely and leave precisely those two A holes. All selected elementary weights are one for every integer S>=1, and Gauss holds after each operation. The record increment is2(|B|/2-1)=|B|-2, as required.

The filled-B word has a nonzero H2 matrix element to the word with h_+ refilled and a hole at0: refill h_+ from e_x, reversing its last field change-1->0, then hop0 into e_x on a previously unused link0->-1. This selected two-hop amplitude is1. On the filled-B sector all contributions to F F^* are nonnegative, so it cannot cancel.

These statements concern INTERNAL components of the actual original maps. No extra field or birth-sign measurement is inserted. For the coherent-edge instrument the same all-plus component is included with positive coefficient. The product of original B maps can have many other components; existence of this component is not a normalized probability estimate.

The same word is algebraically accessible in the TRUE finite-spin microscopic instrument, not only in a proxy. At fixed finite L,S,epsilon, expand each no-event waiting propagator before an original j mark to first order in its own waiting time. On P the first nonzero j coefficient is the actual outward F term; W and C preserve A occupation and cannot substitute. After the last birth, expand the final no-event propagator to second order to produce the two A holes. Its only lowest-degree contribution to W=2 is two outward T hops. All such terms have the same overall phase and nonnegative spin matrix elements, and the chosen path has nonzero coefficient. Therefore the multitime analytic output kernel is not identically zero. This proves nonzero accessibility for some sufficiently short positive waiting intervals at fixed resources. It gives NO useful lower bound uniform in epsilon, volume or a prescribed macroscopic time, and no conditional observation of the internal word.

## 4. Finite islands and an explicit long dark prefix

The filled sector is enough to disprove an all-background gap. A stronger local statement can be reconstructed without assuming a finite-particle kinetic model. From ||F_a||<=6, the terms of(P2) give the quadratic-form estimate

    |<psi,K_S psi>|<=(36+18*36+2*18*72)<psi,W psi>
                    =3276<psi,W psi>.                (P4)

Indeed F_a F_a^* is supported on w_a; 1-Q_a<=sum_(c:dist2)w_c; and each cross commutator has norm<=72 and is supported on w_a vee w_c on both sides. Thus ||K_S||_(W=r)<=M_r=3276r, uniformly in spin and volume. The sharper incidence norm is unnecessary here.

Take a basis word with initial A-hole set Z of size r, and suppose all B sites within graph distance2q+3 of Z are occupied. The other B sites may be empty. Each cross term moves a hole by at most two and preserves the B occupancy mask: different intermediate-B paths commute and cancel, leaving only shared-same-B paths. Same-center F_a F_a^* is diagonal if all B neighbors of the hole are filled. A term F_c^*F_c(1-Q_c) with c occupied can act only within distance2 of a hole, and it vanishes if all six B neighbors of c are filled. Induction therefore shows that every word of at most q K insertions keeps the B mask fixed, moves each hole by at most2q from Z, and is killed by G. This is a zero-pattern statement, valid for finite spin even if some paths vanish at the spin boundary.

For spin, remove the diagonal V_S exactly. Its interaction-picture K_S(t) has the same configuration zero pattern and the same norm bound M_r; V_S also commutes with G. Thus the same dark-prefix statement holds for arbitrary ordered products K_S(t_n)...K_S(t_1), not merely powers of a constant rotor matrix.

Let U(u) be the full unitary generated by delta(V_S+K_S), and S(u) the no-event contraction including -kappa G/2. The bounded interaction-picture Dyson series and the dark prefix imply

    ||G U(u)psi||<=12r R_q(delta M_r u),
    R_q(x)=sum_(n>q) x^n/n!,

for a normalized initial word psi. Duhamel between the unitary and contractive propagators then gives

    ||S(u)psi||>=1-6kappa r u R_q(delta M_r u).        (P5)

This is an explicit survival-amplitude lower bound; when positive it may be squared for a no-event probability. For x<q+2,

    R_q(x)<= [x^(q+1)/(q+1)!]/[1-x/(q+2)].

For example u=(q+1)/(2e delta M_r) makes this tail at most2^(-q-1)/(1-1/(2e)). Thus an increasing filled island can produce increasing fast residence times with survival approaching one, with no assertion about its initial statistical weight. There is no norm-Bochner issue: after removing the diagonal, finite-volume K_S(t) is strongly continuous, bounded and acts strongly on vectors; in the rotor leading law V=0 and K itself is bounded on W=r.

A finite, algebraically accessible r=2 island is obtained by the same disjoint B-pair construction in a finite box of rows and x-blocks, omitting the central pair and filling it by the two final hops. The pair box can contain any prescribed buffer around h_+ and h_-. Its source fields are again0,+/-1. Finite canonical graphs/tori are chosen large enough to contain the box without aliasing. This supplies the relevant parity and source word for the island, but still does not price the word's probability from Omega.

## 5. Limits relevant to the real target

The leading dark subspace is NOT generally invariant under the true microscopic Hamiltonian. In a filled-B state F^* can refill a hole and leave a B vacancy, so T=-F-F^* leaves the sector immediately. Higher dressed jumps can also act: the first correction includes -jF^* on a filled-B input and can remove two holes when a suitable shared B edge becomes vacant. Such contributions have physical order one after the original epsilon^-1 jump scaling, even though the bare leading loss vanishes on the fast clock. No permanent microscopic darkness follows from(P3).

The finite-island obstruction rejects a BACKGROUND-INDEPENDENT absorption hypothesis, not the actual volume-uniform local limit from bare Omega. A source-weighted argument could still suppress the large crowded islands and their field action. The checked O(epsilon^2) hole density and count expectation do not by themselves provide that weight, control clustered B occupations, or establish microscopic field uniform integrability. These are the exact high-fanout limits to check against the author proof.

## Control price and independence freeze

Before author exposure, run one standard-library sparse integer control at<=30CPU seconds/150MB, one thread. It constructs the L8 full-B source word, a finite dense island, local Gauss checks, the selected unit-weight matrix element and two exact Krylov insertions in an interior where(P2) reduces to the filled-B walk. It stores only a fixed reference field/charge background and sparse local deviations, not a full torus Hilbert basis. Its output corroborates source words and a finite prefix, not the all-q proof or actual ensemble probabilities. Code, output, source identities and this PRE will be hashed before asking for the author packet.

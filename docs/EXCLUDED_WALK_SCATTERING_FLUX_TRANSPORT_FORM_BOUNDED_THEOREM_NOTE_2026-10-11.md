---
claim_id: excluded_walk_scattering_flux_transport_form_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For the supplied antisymmetric Weyl pair with singlet exclusion, derive the paired stationary probability-flux cross section, normalized finite-beam transfer and the full central canonical-current quadratic form; verify the rank-one scattering algebra in Lean."
upstream_dependencies:
  - excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
runner: scripts/excluded_walk_scattering_flux_transport_form_2026_10_11.py
---

# Probability flux and energy-current transport form in the supplied excluded walk

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent audit has not occurred.

The target is to derive, in the supplied walk's stated normalization, a paired
stationary cross section with a nonzero threshold limit and an exact positive
scattering-flux form whose complete three-component energy-current tensor is
calculated. The normalizable finite-beam experiment is a separate construction.
The exact algebra used in those constructions has a scoped Lean certificate.

The [parent low-energy theorem](EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md) supplies the symbol and contact
normalization, regular central shell, threshold expansion, canonical energy
placement and quantitative Cook comparison. It is provisional source content
on the stacked parent branch, independently checked for its stated scope.
The present dependency closure includes that complete parent delta: review
and land the parent first, or review the cumulative delta from frozen main
`a13caa4885f547c8d206265b031ba7649e539fd9`. No rejected branch is a premise.

At K=0 the paired cross section tends to `1/(4pi I0^2)`. A normalized corner
beam has other-corner probability `(7/64)|s-1|^2`; its finite-preparation
version is positive of order lambda^2. For real bounded angular observables,
`Q_mu(f)=4pi rho^2 Var_nu(f)/|G|^2=||S* f S-f||^2/pi`. The full
canonical-current tensor is order lambda^8 with unnormalized phase-space
measure, and order lambda^6 after that measure is normalized. The contact
ellipsoid gives its exact rank: the number of nonzero components of kappa.
These coefficients do not yet define a microscopic collision frequency.

**Imports and proof obligations.** The walk, continuous generator clock,
antisymmetric pair sector, contact exclusion and selected energy placement
are explicit model premises from the parent contract. The regular stationary
lattice resolvent expansion is imported from the primary source with checked
hypotheses in the flux proof below. The K=0 threshold computation is proved
here. General central threshold/Cook inputs are proved in the parent source
and inherit its conditions. The flux disintegration, full tensor, rank and
coercivity are proved here. No observed target value or fitted parameter is
used. The registered units, kinetic-form-isotropy and realized-state primitives
are not classified as missing premises; this theorem uses no new primitive.
Its supplied dynamics and its state preparations remain explicit assumptions.

**Boundary.** The regular shell has `0<E<=1/8, |K|<=E/4` with nonzero G.
Small-parameter statements take the fixed compact central scaling specified
below. Far radius is taken at fixed regular shell; no joint radius/energy
remainder is asserted. The canonical scalar multiplier in the form is the
asymptotic current; the finite-time placement correction is kept distinct.
The next unproved physical bridge is a justified encounter process preserving
or controllably reducing phase information. It is not a lemma used below.

**Primary:** [finite controls](../scripts/excluded_walk_scattering_flux_transport_form_2026_10_11.py).
The canonical cache is `logs/runner-cache/excluded_walk_scattering_flux_transport_form_2026_10_11.txt`.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Supplied-model stationary flux, finite beam and transport-form theorems with explicit analytical premises."
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: null
target_blocker_text: "Connect the excluded walk's unitary scattering to a normalized microscopic transport object."
source_of_blocker_text: frontier_question
artifact_role: theorem
next_trace_action: "Derive encounter and phase-memory dynamics before using the form in a many-body collision law."
```

## Probability flux and normalized beams

The supplied three-dimensional two-record unitary has the singlet contact
removed in its antisymmetric sector. Lengths and times below are the supplied
lattice and generator units. The publication review record below supersedes
the author-stage review status in the preserved research evidence.

The strongest result is a stationary probability-flux cross section with an
explicit incident normalization. For the antisymmetric paired incident state
defined below, at K=0,

    sigma_pair(E,q_in)=2pi rho(0,E)/[v_in |G(0,E+i0)|^2],
    lim_(E->0+) sigma_pair=1/(4pi I0^2)>0,
    I0=integral_(T^3) dq/[(2pi)^3 4|sin q|^2].                (F1)

All eight outgoing corners are included. A weak angular lattice-flux measure
is proved below, including its exact normalization and the parity interference
that prevents a pointwise incoherent sum. Thus the small eigenphase of S does
not, by itself, mean a small cross section in lattice-area units.

A separate exactly normalized finite-beam construction gives an outgoing
probability into the other seven corners of

    P_other=(7/64)|s-1|^2                                  (F2)

on a fixed regular shell. Energy and K envelopes make it a normalizable
two-record state. Under the named scaled Cook regularity input, it also gives
an actual finite-time excluded-unitary experiment with P_other of order
lambda^2 and a positive explicit leading coefficient. This probability is
not (and need not equal) the squared norm of the full scattered difference.

### 1. Exact sources, reading and dependency limits

The following table records frozen research-source identities. The parent
publication contains the threshold, canonical-current and finite-preparation
arguments; its evidence directory preserves their original source bytes.
The source map in this milestone binds the additional flux/form inputs.

| Frozen input | SHA-256 | Actual role |
| --- | --- | --- |
| `EXCLUDED_WALK_TRANSPORT_PROBE.md` | `8bc423b2d5adf368f4ae09a2bb87730517be243a050b4289dad3a0b217f09526` | Model, central channel map, stationary S convention. Its general scaled G coefficient and order-seven derivatives are inputs only to the explicitly marked central-scaling and finite-time extensions. |
| `EXCLUDED_WALK_COOK_BRIDGE_DRAFT.md` | `2c54b891deeb43a19c5f41de5059aadac7fc8d672dfb68e0b8aa575d27eb3fc7` | C1-C7 and direct-integral preparation/tails for the optional finite-time beam. |
| `EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md` | `79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe` | Identifies the distinct energy-current observable. Its canonical correction is not used as a probability current. |
| `EXCLUDED_WALK_COHERENT_PACKET_DRAFT.md` | `b4ae921cc065fb2f38c1caee5aca3a1cf69bac317a6f6f0f537becd393b6cd38` | Reused direct-integral normalization and Cook scaling convention. The coherent-current coefficient is not a premise of this flux derivation. |

These sources were read in full in the preceding work. Their reuse is author
composition, not independent evidence for the author's threshold proof. The
K=0 resolvent, low-energy G limit, local probability current, parity structure,
flux normalization and paired incident normalization are derived explicitly
here, without the high-order threshold derivative input.

The matched repository source is M6 at frozen main
`a13caa4885f547c8d206265b031ba7649e539fd9`:
`docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
SHA `e0536f80a25feb0b368c10a0016a9d09b07b5bd06827751c30029d2eb1d70065`.
Its complete 226 lines were reread from `git show`; an exact copy is
`flux_bridge/M6_frozen.md`. T2 contains the rank-one resolvent and a formally
normalized shell transition expression. Its Premises explicitly supplies a
Fermi-golden-rule transition rate at definition level. It does not prove the
incident-flux, spatial far-field or plane-versus-normalized-beam bridge here.
The common conditional outgoing shell weight is prior art, not new in this
note. M3/M9 and their exact paths/hashes retain the earlier complete coverage
record in `excluded_walk_probe/identity_manifest.json`; their no-current
conservation conclusions do not supply this flux normalization.

Three broader frozen-main regex searches and their full raw hits are saved in
`flux_bridge/repo_search_0.log` through `repo_search_2.log`, with commands and
counts in `repo_search_manifest.json`. They returned 146, 231 and 551 hits.
This was a targeted matched-source review, not a read of every unrelated hit:
ice transfer cross sections, thermal Sommerfeld imports, classical capturing
bodies, raw historical prompts and unrelated matrix references are context-only.
No global novelty claim follows from those searches. No new open-PR inventory
or repository status audit was performed for this bounded derivation.

The new primary mathematical source is W. Shaban and B. Vainberg,
[*Radiation Conditions for the Difference Schrödinger Operators*](https://arxiv.org/pdf/1812.06390).
The Fourier convention/setup, Theorem 1, Lemma 2, Theorem 4, its amplitude
formula (13), and the asymptotic argument through (21) were read; formula (13)
was also checked on rendered PDF page 8. The import is the regular strictly
convex scalar lattice resolvent expansion. At K=0 the exact scalar reduction
below has paper energy 6-E^2 in (2,6), finite-support source, nonzero group
velocity and positive curvature. The central matrix extension below repeats
its coarea/stationary-phase argument with those hypotheses checked, rather
than applying a scalar theorem to a matrix without justification.
Local PDF SHA: `95cd35e4045482e4c7885e598be980cd2e75d426cdbe0d1880fa5bcd02103ffa`.
The paper's remaining nonconvex, uniqueness and perturbed-operator arguments
were not needed or claimed as fully read. No continuum Dirac
flux-across-surfaces theorem is imported for this lattice.

### 2. Hilbert-space and incident-normalization conventions

Use the ordered-coordinate embedding with relative coordinate x=x1-x2 in
Z^3 and normalized Fourier measure dq/(2pi)^3. A local total-momentum chart
has k1=K/2+q, k2=K/2-q. Its Jacobian is one; no half-volume factor enters.
In that embedding the physical antisymmetric fiber consists of spinor fields

    psi(-x)=-Swap psi(x),   ||psi||^2=sum_x ||psi(x)||^2.       (F3)

For x!=0, passing to one representative of each orbit {x,-x} multiplies its
amplitude by sqrt(2), so the norm on unordered configurations is the same.
In particular a full oriented angular flux integral is not divided by two
again. A detector on the unoriented axis identifies n and -n and adds their
two equal densities on a representative hemisphere.

Let c be the normalized singlet, both as a spin vector and as the contact
vector delta_(x,0)c. The generator and compression are

    H0(K,q)=sigma_1 dot sin(K/2+q)+sigma_2 dot sin(K/2-q),
    C=|c><c|, P=I-C, H=PH0P.                              (F4)

The restriction of H to P is the physical excluded unitary. On the full fiber
it also has a decoupled zero vector c, which is not an incident state. Write
R0(z)=(H0-z)^(-1), G(z)=<c,R0(z)c>, rho=Im G(E+i0)/pi.

The quantity called probability current below is the continuity current of
the squared norm of this supplied unitary. It is a different observable from
the canonical energy current. At K=0 the latter vanishes, whereas outgoing
relative-coordinate probability flux need not vanish. No framework-level
measurement or record-selection law is inferred from this Hilbert-space use.

### 3. A local source identity fixes the total outgoing flux

For a nearest-neighbor Bloch generator write

    (H0 psi)(x)=sum_a [T_a psi(x+e_a)+T_a^* psi(x-e_a)],
    T_a=(sin(K_a/2)/2)(sigma_(1,a)+sigma_(2,a))
                   -(i cos(K_a/2)/2)(sigma_(1,a)-sigma_(2,a)).

Its oriented outward bond current is

    j_a(x;psi)=-2 Im[psi(x)^* T_a psi(x+e_a)].             (F5)

Direct differentiation of ||psi(x)||^2 under i dot psi=H0 psi gives
dot rho_x=-sum_a[j_a(x)-j_a(x-e_a)]. For a stationary inhomogeneous field
(H0-E)psi=f the same algebra gives

    div j(x)=-2 Im[psi(x)^* f(x)].                        (F6)

This identity is local and requires no asymptotic scattering assumption.
For the outgoing boundary field R_E(x)=(R0(E+i0)c)(x), it implies

    div j(x;R_E)=2 Im G(E+i0) delta_(x,0),
    total outward flux through every finite enclosing boundary
                           =2 Im G=2pi rho.             (F7)

Boundary currents are summed with their oriented signs. Pointwise boundary
values and the homogeneous equation away from zero follow either from the
K=0 scalar reduction below or from smooth regular-shell coarea subtraction.
There is no infinity-limit exchange in (F7): any enclosing finite region
satisfies it after taking the pointwise resolvent boundary value.

At z=E+i eta the exact precursor is
div j=2 Im G(z) delta_0-2 eta ||R0(z)c(x)||^2. This also fixes the sign of
(F7) and is tested exactly on a finite periodic lattice in the helper.

If psi_in is any generalized free solution at E with contact amplitude
a=<c,psi_in>, the hard-core stationary field is

    psi=psi_in+psi_sc,
    psi_sc=-R_E a/G,
    <c,psi>=0,   P(H0-E)P psi=0.                         (F8)

Thus its scattered field alone has total outward flux

    Flux_sc=2pi rho |a|^2/|G|^2.                         (F9)

This is obtained from an actual stationary field and continuity, not by
calling an S-matrix element a collision rate. The full field has zero net
flux through an enclosing surface: its contact source is orthogonal to its
contact-free value. The interference between incident and scattered fields
therefore cancels (F9), as required by conservation. Ignoring that interference
and treating the full squared scattered difference as a probability would
be incorrect.

### 4. K=0: exact scalar reduction and eight-corner parity

At K=0, let t_a=sigma_(1,a)c. The four vectors c,t1,t2,t3 are orthonormal.
The matrices A_a=sigma_(1,a)-sigma_(2,a) obey

    A_a c=2t_a,   A_a t_b=2 delta_ab c.

Consequently H0^2 c=4|sin q|^2 c, and exactly

    R0(z)c(q)=[z+2 sigma_1 dot sin q]c/[4|sin q|^2-z^2].  (F10)

The mixed zero-energy spin directions carry no contact weight at K=0.
They are not omitted positive-energy channels.

Put

    L_z(x)=integral e^(iq.x)/[4|sin q|^2-z^2] dq/(2pi)^3.

The denominator is pi-periodic in each q coordinate. Hence L_z(x)=0 unless
all x_a are even, and

    L_z(2m)=integral e^(ip.m)/[6-2 sum_a cos p_a-z^2] dp/(2pi)^3,
    R0(z)c(x)=z L_z(x)c
                 -i sum_a [L_z(x+e_a)-L_z(x-e_a)]t_a.     (F11)

The first expression is the standard nearest-neighbor scalar lattice
resolvent at z^2, with the supplied spacing change explicit. It also proves
the exact parity selection: all-even x carry only c; exactly-one-odd x
carry only the corresponding t_a; two or three odd coordinates give zero.
This holds before taking any low-energy or large-distance limit.

For 0<E<=1/8, each of the eight open ++ shells is C0+Sigma_E, where C0 is a
corner in {0,pi}^3 and

    Sigma_E={p near 0: 4 sum_a sin^2 p_a=E^2}.

The Hessian of its defining function is 8 diag(cos 2p_a)>0 on the entire
small enclosed region. Thus it is strictly convex with a smooth Gauss map.
Let p_E(n) be its unique point whose outward group velocity points along
n, let v_E(n)=|grad(2|sin p|)| there, and let k_E(n)>0 be its Gaussian
curvature in physical relative q coordinates. Finally set
s_hat_E=sin p_E/|sin p_E|.

The outgoing far field, with r=|x| and n=x/r, is

    R_E(x)=sum_C0 e^(i(C0+p_E(n)).x)
           (1+sigma_1 dot D_C0 s_hat_E)c
                         /[4pi r v_E(n) sqrt(k_E(n))]+O_E(r^-2), (F12)

where D_C0=diag(cos C0_a). Equivalently its leading term is

    2 e^(ip_E(n).x)/[pi r v_E sqrt(k_E)]
          [1_(x even)c+sum_a 1_(parity(x)=e_a) s_hat_(E,a)t_a].

The second expression agrees with the exact parity rule. It is not the
pointwise sum of eight intensities.

Since p_E=(E/2)n+O(E^3), v_E=2+O(E^2), k_E=4/E^2+O(1), each individual
cone has leading low-energy amplitude

    E(1+sigma_1 dot D_C0 n)c/[16pi r].                   (F13)

This verifies the proposed coefficient and spin factor. Its exact phase is
e^(ip_E(n).x). Replacing that phase by e^(iEr/2) requires controlling
E^3 r; it is not a uniform fixed-E far-field formula as r tends to infinity.
No jointly uniform r,E remainder is asserted here.

### 5. Stationary-phase normalization and the compact central extension

The coefficient in (F12) can be reconstructed from the Fourier integral.
Near a simple positive shell, retain its matrix spectral projector Pi(q).
Coarea writes the singular part using Pi(q)c/|grad E(q)|. The boundary
identity (t-i0)^(-1)=PV(1/t)+i pi delta(t), followed by stationary phase
on a smooth strictly convex surface, selects the outgoing critical point.
The two-dimensional surface Hessian is negative definite there. Its factor
(2pi/r)e^(-i pi/2)/sqrt(k) and the outgoing normal integral 2pi i, divided
by (2pi)^3, give precisely

    e^(iq(n).x) Pi(q(n))c/[2pi r v(n) sqrt(k(n))].          (F14)

The opposite normal stationary point cancels between PV and delta terms.
Away from the shell the matrix inverse is smooth and repeated integration
by parts gives rapid decay. This is the coarea/PV argument of the primary
source with our Fourier convention and outgoing sign restored explicitly.
At K=0, Pi_(++)c=(1+sigma_1 dot D_C0 s_hat_E)c/2, giving (F12).

The same argument is available on any compact scaled central domain
K=lambda kappa,E=lambda e with e>=e_min>0 and |kappa|<=e/4. For sufficiently
small lambda only ++ is open. In one corner write q=C0+lambda y. The
scaled energy tends in C^m, for every fixed m, to

    e_0(y)=|y+kappa/2|+|y-kappa/2|.

On its level e, both one-particle lengths are at least (e-|kappa|)/2>0.
Its surface is the ellipsoid

    y^T B^(-1)y=1, B=[D I+kappa kappa^T]/4,
    D=e^2-|kappa|^2>0.                                  (F15)

It has uniformly positive curvature on the compact parameter set. The
lattice shell is a small C^2 perturbation there and hence remains strictly
convex, with a uniformly nonsingular Gauss map in scaled coordinates. This
checks the needed geometry; no global convexity at arbitrary energy is used.

All eight lattice shells are identical translates: changing C0 applies
the same coordinate signs to both sine vectors. Their energy, group velocity,
curvature and singlet weight are identical. Their spin projectors need not
be replaced by one projector. With q(n)=C0+p_(K,E)(n), define

    w(n)=||Pi_C0(n)c||^2
       =[1-n1(n) dot n2(n)]/4,
    n1=sin(K/2+p)/|sin(K/2+p)|,
    n2=sin(K/2-p)/|sin(K/2-p)|.

Then the full outgoing field is

    R_E(x)=e^(ip_(K,E)(n).x)/[2pi r v(n) sqrt(k(n))]
                       sum_C0 e^(iC0.x) Pi_C0(n)c+O_(K,E)(r^-2). (F16)

At fixed small (K,E), all remainders and their one-lattice-step versions
are uniform in n. This suffices for the flux limit. Uniformity when r and
lambda tend to their limits together is not used or claimed.

### 6. A defined angular lattice-flux measure, including interference

Choose a smooth radial cutoff chi with chi=1 for radius<=1 and chi=0 for
radius>=2. For a smooth real angular test function a(n), define

    Flux_R[a;psi]=sum_(x,b) a(x/|x|)
         [chi(|x|/R)-chi(|x+e_b|/R)] j_b(x;psi).          (F17)

The angular value at x=0 is irrelevant because the bracket is zero there.
This is a smoothed outward bond-flux functional on an annulus, not a count
of hypothetical collisions. For a=1, summation by parts and (F7) give
Flux_R[1;R_E]=2pi rho for every sufficiently large R.

For general a insert (F16). The phase of a neighbor obeys
p(n').(x+e_b)=p(n).x+p_b(n)+O_(K,E)(r^-1), because derivatives of p along
the shell are orthogonal to n. In the leading current, products of corners
C0 and C1 carry exp(i(C1-C0).x). Averaging over a 2-by-2-by-2 parity cell
annihilates every cross term with C0!=C1. The slowly varying coefficients
produce only O_(K,E)(R^-1) error in (F17). This is a Riemann-sum statement
with eight parity cosets, not an assumption of incoherent preparation.

For a diagonal term, the band Hellmann-Feynman identity gives

    (Pi_C0 c)^* partial_(q_b)H0 (Pi_C0 c)=v_b ||Pi_C0 c||^2.

It follows that the limiting angular outward flux density of R_E is

    lim_(R->infinity) Flux_R[a;R_E]
       =integral_(S^2) a(n) F_(K,E)(n) dOmega,
    F_(K,E)(n)=2w(n)/[pi^2 v(n) k(n)].                   (F18)

The local bond-current remainder is O_(K,E)(r^-3); multiplying the cutoff
difference O(R^-1) and summing O(R^3) annular sites proves its O(R^-1)
contribution. Standard Riemann sums on each parity sublattice then prove
the limit. In particular (F18) is positive for a>=0.

The total normalization checks independently through the Gauss map:
dOmega=k dSigma on one corner shell, and

    rho=8/(2pi)^3 integral_(one shell) w dSigma/v,
    integral F_(K,E) dOmega=2pi rho.                     (F19)

At K=0, w=1/2 and F=1/(pi^2 v_E k_E). One can also compute the averaged
current directly from (F12): only the all-even and the corresponding
one-odd site contribute to each bond direction. The parity average of
their singlet-triplet currents is n/[pi^2 r^2 v_E k_E]. This reproduces
(F18) while preserving exact zeros on the other site classes.

### 7. Paired incident flux and a stationary cross section

Fix a regular incoming ++ momentum q_in=C_in+p_in. Let u be a unit spin
vector in its one-dimensional band, with c^*u=sqrt(w_in) by phase choice.
The antisymmetric generalized incident field is

    psi_in(x)=[e^(iq_in.x)u-e^(-iq_in.x)Swap u]/sqrt(2).   (F20)

It has mean squared norm per relative lattice site equal to one, since the
cross term averages to zero on large boxes for q_in away from a corner.
At K=0 its two spin components are orthogonal and its density is identically
one. Because Swap c=-c,

    a=<c,psi_in>=sqrt(2w_in).                            (F21)

The two ordered travelling components have densities 1/2 and opposite
group velocities of magnitude v_in. Define the paired incident flux density
as the sum of their incoming flux magnitudes through their respective
transverse planes: j_in=v_in/2+v_in/2=v_in. Equivalently, on the unordered
configuration space this counts one incoming pair flux, using (F3).
The net vector current of the two opposed components is not that incident
flux; using the net zero vector as a denominator would be meaningless.

Define the stationary paired-beam cross section to be the outward flux of
the scattered field alone divided by this j_in. Equations (F9),(F18),(F21)
then prove

    d sigma_pair/dOmega
       =4 w_in w(n)/[pi^2 v_in v(n) k(n) |G|^2],
    sigma_pair=4pi rho w_in/[v_in |G|^2].                 (F22)

This is an explicitly defined relative-coordinate probability-flux cross
section, with area in the supplied lattice units. It includes every outgoing
corner through the coarse angular flux. Resolving individual outgoing corners
in Fourier space assigns one eighth of that flux to each corner, with its
own projector. No spatial pointwise corner incoherence is assumed.

A single unit-density ordered travelling component would have contact
intensity w_in and the same speed, producing half of (F22) in the formal
rank-one comparison. That component is not itself an antisymmetric state.
Nor does this comparison assert a distinguishable-particle hard-core theorem:
removing all distinguishable contact spin states would be a different model.

The wave (F20) is generalized and is not a normalized angular delta state.
It is used solely to define an incident flux density. The normalizable beam
result in Section 10 supplies a different, explicitly probability-normalized
experiment; this note does not assert an unproved plane-beam limiting theorem
equating the two experiments.

### 8. The K=0 low-energy limit is self-contained

Equation (F10) gives G(0,z)=z J(z), with
J(z)=integral [4|sin q|^2-z^2]^(-1)dq/(2pi)^3. The finite positive number
I0=J(0) is integrable because its eight singularities are inverse squares
in three dimensions. Here is a direct boundary-value estimate:

    J(E+i0)=I0+O(E),
    G(0,E+i0)=E I0+O(E^2).                              (F23)

Near each corner use p=sin q and its smooth Jacobian. Outside |p|<=2E,
the difference of denominators is bounded by a constant times E^2/|p|^4;
its three-dimensional integral is O(E). Inside |p|<=2E, rescale p=E y.
Both the zero-energy integral and the boundary-value integral have overall
factor E. The latter has a fixed simple radial pole at |y|=1/2; subtracting
the smooth radial numerator at that pole bounds its principal value, and
the delta term is also uniformly bounded. Smooth cutoffs can be inserted
between the two regions. The remainder outside fixed corner charts is
O(E^2). This proves (F23) without a numerical principal-value extrapolation.

The same change of variables gives exactly, for 0<E<2,

    rho(0,E)=E^2/(16pi^3) integral_(S^2)
                 product_a(1-E^2 n_a^2/4)^(-1/2) dOmega
             =E^2/(4pi^2)+O(E^4).                       (F24)

At K=0 the incoming w_in=1/2, v_in=2+O(E^2), uniformly in direction and
corner. Equations (F22)-(F24) prove (F1), and also

    d sigma_pair/dOmega=1/(16pi^2 I0^2)+O(E),
    sigma_pair=1/(4pi I0^2)+O(E),
    s-1=-i E/(2pi I0)+O(E^2).                           (F25)

Thus the cross section has a finite nonzero threshold limit while the
scattering eigenphase tends to zero. These are different normalizations.
The eight-cone and antisymmetric factors are already included. There is
no additional multiplication by eight or division by two.

For explicit rough bounds, I0>=1/12 since 4|sin q|^2<=12. Folding to the
cube [-pi/2,pi/2]^3, using |sin x|>=2|x|/pi, and enclosing that cube in a
ball gives I0<=sqrt(3)pi/8. Hence the positive limit in (F1) lies between
16/(3pi^3) and 36/pi. No fitted numerical value of I0 is needed.

### 9. Central scaled cross sections and their inherited input

This section additionally uses the frozen threshold coefficient

    G(lambda kappa,lambda e+i0)=lambda A(kappa,e)+O(lambda^2),
    rho=lambda^2 D/(4pi^2)+O(lambda^4),
    A=e integral [(e^2-|kappa odot cos q|^2)
           / (4|sin q|^2(e^2-(kappa dot v0(q))^2))] dq/(2pi)^3,
    v0_a(q)=sin q_a cos q_a/|sin q|.                     (F26)

Its positivity and uniform remainder are named inputs from that source,
not independently certified by this flux derivation. For K=0 they reduce
to the independently calculated (F23)-(F24).

The limiting outgoing geometry can be computed directly from (F15). Put
gamma(n)=D+(kappa dot n)^2. The point with outward normal n and its speed,
contact weight and scaled Gaussian curvature are

    y(n)=[D n+(kappa dot n)kappa]/[2sqrt(gamma)],
    v_lim(n)=2sqrt(gamma)/e,
    w_lim(n)=gamma/(2e^2),
    k_lim(n)=4 gamma^2/(D^2 e^2).                        (F27)

For the curvature, the implicit ellipsoid formula gives k=(n^T B n)^2/det B;
det B=D^2 e^2/64. The two one-particle lengths have product e^2 D/(4gamma),
which proves the displayed contact weight and speed. The actual lattice
quantities differ by O(lambda^2) after this scaling; its curvature is
lambda^-2[k_lim+O(lambda^2)]. Consequently

    F_(lambda kappa,lambda e)(n)
       =lambda^2 D^2 e/[8pi^2 gamma(n)^(3/2)]+O(lambda^4),
    d sigma_pair/dOmega
       =D^2 sqrt(gamma(n_in))
                    /[16pi^2 A^2 gamma(n)^(3/2)]+O(lambda),
    sigma_pair=D sqrt(gamma(n_in))/[4pi e A^2]+O(lambda).   (F28)

Here n_in is the incoming relative group-velocity direction, not necessarily
the radial momentum direction. The elementary identity
integral_(S^2) gamma^(-3/2)dOmega=4pi/(D e) checks both total normalizations.
All statements are uniform on the selected compact central parameter set,
including incoming and outgoing directions, once lambda is sufficiently
small. The angular flux uses the large-radius limit first. No joint
far-field/threshold error estimate is hidden in (F28).

### 10. A normalized finite-beam analogue with actual probabilities

On a regular shell let v=Zc/sqrt(rho), so S=I+(s-1)|v><v|. Let Q_j select
one of the eight corner components. Exchange maps q to -q within the same
corner, so Q_j preserves the antisymmetric shell space. The eight contact
masses are exactly equal, giving

    ||Q_j v||^2=1/8,
    chi_j=sqrt(8) Q_j v, ||chi_j||=1,
    v=(1/sqrt(8))sum_j chi_j.                            (F29)

These are unit angular states distributed across a whole corner shell, not
directional delta states. The exact outgoing shell state is

    S chi_j=[(7+s)/8]chi_j+sum_(k!=j)[(s-1)/8]chi_k.       (F30)

Thus each other corner has probability |s-1|^2/64, their total is (F2),
and the same-corner probability is 1-7|s-1|^2/64. Their sum is exactly one.

More generally, a normalized angular beam chi with support A and an angular
detector B disjoint from A satisfies

    ||Q_B S chi||^2=|s-1|^2 |<v,chi>|^2 ||Q_B v||^2.       (F31)

All sets must be exchange invariant, or the corresponding detector must be
defined on unordered channels. If chi=Q_A v/sqrt(nu(A)), the probability in
a disjoint set B is |s-1|^2 nu(A)nu(B), and in A's complement it is
|s-1|^2 nu(A)[1-nu(A)]. Smooth angular windows give the
same formula with their actual normalization and contact overlap. A shrinking
angular cap has shrinking contact overlap; it does not become a unit delta
direction. Inside A, interference with the incident amplitude must be kept.
The pure contact vector v has S v=s v and exactly zero angular-probability
redistribution, despite ||(S-I)v||^2=|s-1|^2.

For a fully normalizable packet choose smooth compact alpha(kappa),f(e) in
the same strict central domain, normalized by
integral |alpha|^2 d^3kappa/(2pi)^3=integral |f|^2de=1, and set

    Psi_lambda(K,E)=lambda^-2 alpha(K/lambda) f(E/lambda) chi_j(K,E). (F32)

Its squared amplitude lambda^-4 exactly cancels the measure factors
lambda^3 and lambda. It is smooth for each positive lambda after inverse
coarea restriction; its bump support stays inside the regular corner charts.
The outgoing other-corner probability is exactly the weighted integral of
(F2). Under (F26) it becomes

    P_other^asym=lambda^2 C_beam+O(lambda^3),
    C_beam=(7pi^2/16) integral |alpha|^2|f|^2
                    [D/(4pi^2)]^2/A^2 d^3kappa/(2pi)^3 de>0. (F33)

This is a norm-squared transition probability for one prepared packet.
Its O(lambda^2) behavior differs from the O(1) flux cross section of the
generalized incident field. Neither supplies an event frequency or gas
collision rate, and no fixed beam-area identification equating them is assumed.

There is also an optional finite-time realization, using the frozen Cook
source and the threshold source's uniform scaled derivatives through order
seven. The contact profiles of (F32) and its outgoing packet are

    b_c^in(K,E)=lambda^-1 alpha(kappa) B^in(lambda,kappa,e),
    B^in=f sqrt(r_lambda)/sqrt(8), B^out=s B^in,
    b_h^b=E b_c^b, r_lambda=rho/lambda^2.                 (F34)

Define L_(j,r)^b by the L2_(kappa) norm, weighted by |alpha|^2, of the
L1_e norm of partial_e^r(e^j B^b), j=0,1, and let bar L be their supremum
over the compact scaled family. These constants are finite by the named
order-seven threshold input and smooth envelopes. Then

    ||A_r^b||_(L2_K)=lambda^(3/2-r) L_(0,r)^b,
    ||D_r^b||_(L2_K)<=lambda^(3/2-r)
                            [sqrt(6)L_(0,r)^b+lambda L_(1,r)^b]. (F35)

Put D_star=sqrt(6)(bar L_(0,7)^in+bar L_(0,7)^out)
+lambda_0(bar L_(1,7)^in+bar L_(1,7)^out). At T=lambda^(-3/2), prepare

    Eta_-=P exp(iTH0)Psi_lambda/||P exp(iTH0)Psi_lambda||,
    Eta_+=exp(-2iTH)Eta_-.

The one global normalization is legitimate for sufficiently small lambda,
since removed mass p<= [bar L_(0,7)^in]^2 lambda^10. Cook gives

    ||Eta_+-exp(-iTH0)S Psi_lambda||
       <= (D_star/6)lambda^(7/2)+sqrt(2)bar L_(0,7)^in lambda^5. (F36)

Let Q_other be the free positive-band projector onto the other seven corner
windows on the actual packet support. Its expectation on Eta in P is the
compression P Q_other P; Q_other need not preserve P. Since its norm is one,
the difference between its outgoing probability and (F33) is at most twice
the right side of (F36). Its initial leakage after the projection is at most
2p=O(lambda^10). Thus the actual finite-time probability, and also its change
from the prepared initial probability, has the same positive leading
lambda^2 C_beam as (F33). Global projection reweights K; this norm estimate
already includes that change and assumes no fiberwise renormalization.

### 11. Evidence, failed shortcuts and remaining obligations

The complete helper `flux_bridge/flux_controls.py` and its full exit-0 log
`flux_bridge/flux_controls.log` were read. Source SHA-256:
`9803c454d4cc7610e0056ef47d389891cecb1680b2dc666c92d6d9ed36476a36`;
log SHA-256: `cea70a1a1fc9bf42b9ae087ab525cbb0f0a934fb872964e2375faab01b5edfb1`.
Exact Gaussian-rational calculations verify all 64 local source/absorption
identities on a 4^3 torus, its finite-box outward-flux identity, all parity
zeros, paired incident density and contact factors, and a normalized
eight-channel example with other-corner probability 7/80 and total probability
one. The floating controls construct original tensor-product spin projectors
on actual lattice shells, sum their eight coherent parity fields, and compute
the bond currents. Across 24 shell cases they agree with the proposed parity-
averaged current within relative error 3.92e-16 and approach the limiting
ellipsoid density. A separate one-dimensional angular quadrature checks its
total normalization. Floating quadrature is not interval certified. None of
these finite checks proves stationary phase or a uniform PV estimate.

Failed or insufficient shortcuts are preserved:

- Adding eight intensities at each lattice site misses exact parity zeros.
  Only the defined weak annular flux averages the interference terms away.
- The candidate e^(iEr/2) phase is not valid at fixed E for arbitrarily large
  r; the lattice phase p_E(n).x is retained.
- A unit directional delta is not an L2 shell state; (F20) is explicitly a
  generalized flux-density reference, while (F29)-(F32) are normalized beams.
- The net vector current of an antisymmetric paired incident field is not
  its total incoming flux density. Ordered and unordered normalization factors
  cannot be silently interchanged.
- ||(S-I)chi||^2 is not generally a detector probability. The disjoint-output
  construction (F31) removes incident/scattered interference only where the
  incident state is actually zero.
- A continuum flux-across-surfaces theorem was not applied to this lattice.
  The stationary flux functional is defined and proved directly here.

The K=0 stationary result has a supplied-model proof above. A separate
source-bound research check reconstructed the incident/quotient normalization,
matrix stationary-phase extension and parity-averaged flux limit. Its complete
report and exact evidence identities are in the publication review record.
The general central asymptotics inherit the frozen threshold coefficient
and remainder; the finite-time normalized beam additionally inherits its
order-seven derivative estimate. These are named provisional dependencies,
not consequences of the finite helper. No common simultaneous large-radius/
low-energy error bound or beam-width-to-plane-wave cross-section limit has
been proved. The latter would be a useful further bridge, not a condition
silently assumed in the stated separate experiments. No physical collision
clock, many-body closure, Boltzmann equation, relaxation rate, adopted law,
or universal current loss follows from this note.

The historical author receipt `flux_bridge/identity_manifest.json` preserves
its exact input identities, reading scope and PDF-tool setup failures. Those
operational failures did not replace any mathematical check. The original
PDF remains external; its primary-source URL and digest are recorded above.

## Scattering-flux transport form

This continuation uses the probability-flux normalization proved above.
The supplied walk, singlet exclusion, antisymmetric sector, lattice units and
canonical energy placement remain premises. The defined quadratic form is
an exact mathematical object; an encounter process and a closed many-body
evolution remain further research targets.

The exact result, in the conventions defined below, is

    Q_mu(f)=4pi rho^2 Var_nu(f)/|G|^2
           =(1/pi)||S^* f S-f||_op^2.                    (T1)

Here mu is the unnormalized full-shell phase-space measure and nu=w mu/rho
is the normalized contact probability measure. The leading three-component
canonical-current form has an order-lambda^8 expansion, calculated below.
Its rank is the number of nonzero components of kappa. Dividing the form by
the total phase-space mass changes its order to lambda^6. These statements
refer to different normalizations, not to competing physical rates.

### 1. Exact contract, sources and prior-art coverage

Target: derive the scattering-flux quadratic form from the actual paired
incident normalization; prove its positivity, coercivity and coherent-norm
identity; calculate its full energy-current tensor on a compact central
scaling domain. The new obligation is the measure-normalized transport form
and its tensor, rather than another one-component scattering-phase estimate.
The proof route is flux disintegration, exact rank-one algebra, then the
fourth moments of the limiting contact ellipsoid. Separate finite controls
within this author run use weighted matrix algebra and direct polynomial
integration, followed by actual lattice-shell quadrature. They do not confer
independent-review status.

The following source identities refer to the frozen research evidence; the
publication source map records its repository locations.

| Source | SHA-256 | Exact role |
| --- | --- | --- |
| `EXCLUDED_WALK_FLUX_BRIDGE_PROBE.md` | `35cfa3095d1abaaeef0e6b77296b42a218615b23f680ee312576adbf924dfc17` | F3-F9 and F18-F22: outgoing source flux, eight-corner measure, and paired incident convention. F26 supplies the named central G expansion; F29-F31 distinguish normalized coherent beam probabilities. No bytes changed. |
| `ROOT_EXCLUDED_WALK_FLUX_REVIEW.md` | `8fbc4a36dc351460bfc151a4bb3c40ea569f437057e2b72da47540c508608214` | Entire independent selective review read; reports complete frozen flux-note coverage and no requested repair. Its reviewed scope and limits remain attached. It is not a review of the present transport derivation. |
| `EXCLUDED_WALK_TRANSPORT_PROBE.md` | `8bc423b2d5adf368f4ae09a2bb87730517be243a050b4289dad3a0b217f09526` | Supplied walk, regular central channels, stationary S, contact threshold coefficient and G expansion. The general central expansion remains an inherited analytical input. |
| `EXCLUDED_WALK_COHERENT_PACKET_DRAFT.md` | `b4ae921cc065fb2f38c1caee5aca3a1cf69bac317a6f6f0f537becd393b6cd38` | Entire note reread. P9-P16 supply the fixed coarea convention and limiting contact distribution; the scalar moment is rederived and extended to all cross moments here. P3 and the asymptotic paragraph after P22 identify the canonical-current observable. Its finite-time Cook theorem is not used. |
| `EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md` | `79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe` | Previously fully read and independently reconstructed identity J=P g P+F for the stated placement; asymptotic current mapping only. |

The first threshold source and both new derivations are this author's work;
reusing their proofs is not an independent check of them. The parent evidence
holds their source-bound checks. A new separate reconstruction of this form's
normalization, off-diagonal moments and tensor rank is recorded below.

The repository comparison remains the identified local main snapshot
`a13caa4885f547c8d206265b031ba7649e539fd9`. Three new statement searches,
commands and all eleven raw hits are saved under `flux_transport_form/`.
All eleven hit lines were read. The only matched walk source is the previously
fully read M6 note
`docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
SHA `e0536f80a25feb0b368c10a0016a9d09b07b5bd06827751c30029d2eb1d70065`.
Its rank-one/contact angular weight is prior art. It supplies an FGR-rate
convention and does not derive this incident-flux form or current tensor.
Other hits concern plane-chain cross sections, cq-channel covariance, winding
covariance, or ice-estimator covariance and are context-only at the returned
scope. Their complete unrelated proofs were not read for this task. No global
novelty or refreshed open-PR inventory is claimed.

No new literature theorem is used. The primary lattice stationary-phase
source and its checked hypotheses remain in the unchanged flux note. The
historical author receipt records the a13caa comparison, exact identities
and reading limits. The publication adds no new imported literature theorem.

### 2. Shell space, measures, spin and paired incidence

Fix 0<E<=1/8 and |K|<=E/4 on a regular positive shell for which G is nonzero.
The supplied free fiber is

    H0(K,q)=sigma_1 dot sin(K/2+q)+sigma_2 dot sin(K/2-q).

Only the ++ band is open. Its eight corner components together form Sigma.
Write v_g(q)=|grad_q E_(++)(K,q)|, Pi(q) for its rank-one spin projector, and

    dmu(q)=dSigma(q)/[(2pi)^3 v_g(q)],
    w(q)=<c,Pi(q)c>,   rho=integral_Sigma w dmu,
    M=mu(Sigma),      dnu=w dmu/rho.                      (T2)

Thus mu is finite but not normalized, while nu is a probability measure.
The regular central geometry gives 1/4<=w<=1/2. The constant spin vector c
is the normalized singlet. G=<c,(H0-E-i0)^(-1)c> has Im G=pi rho>0.

The fiber norm uses the entire relative q torus, restricted by exchange
antisymmetry. Scalar observables f below are real and exchange even,
f(-q)=f(q), so multiplication preserves that physical subspace. All eight
corners and both antipodal points are already present in (T2). If instead
one works on exchange orbits, the measure is the pushforward of the full
mu, namely twice its restriction to a representative half-shell. This and
the corresponding norm isometry preserve every formula below. No further
factor of two or eight is inserted.

A paired generalized incident field at a in Sigma has mean full-relative-
space density one, speed v_g(a), and contact intensity 2w(a). Its two opposed
components each have density one half. Its defined incoming flux is the sum
of their incoming magnitudes, v_g(a), not their net vector current. The
outgoing resolvent source has angular flux 2pi w(b)dmu(b). This is the
spectral/coarea disintegration of the weak spatial flux in F18-F19; the
projector weight w retains the spin dependence. Therefore the paired
cross-section measure and its speed multiple are exactly

    d sigma_pair(a,b)=4pi w(a)w(b)dmu(b)/[v_g(a)|G|^2],
    k(a,db):=v_g(a)d sigma_pair(a,b)
             =c_G w(a)w(b)dmu(b), c_G=4pi/|G|^2.         (T3)

The input factor 2w(a) is essential. A formal unit-density ordered component
would give half this coefficient, but it is not the antisymmetric incident
state of the frozen flux result. Using that alternative normalization without
changing all later constants is an error.

Equation (T3) defines a scattering-flux kernel. Its total weight at a is

    ell(a)=c_G rho w(a),   k(a,db)=ell(a)dnu(b).           (T4)

This disintegration is not a count of actual encounters per unit time. The
coherent scattering operator does not discard the incident amplitude or its
interference. In particular, k is not inferred to be its repeated-collision
Markov transition law.

### 3. Exact variance identity, boundedness and coercivity

For real exchange-even f in L2(mu), define

    Q_mu(f,h)=(1/2)integral dmu(a) k(a,db)
                                [f(b)-f(a)][h(b)-h(a)],
    Q_mu(f)=Q_mu(f,f).                                   (T5)

Symmetry holds because dmu(a)k(a,db) is invariant under exchanging a and b.
Expanding the square and using integral w dmu=rho proves

    Q_mu(f,h)=c_G rho^2 Cov_nu(f,h),
    Q_mu(f)=c_G rho^2 Var_nu(f).                         (T6)

All integrals exist for L2(mu) because w is bounded and mu is finite. This
also proves positivity without a dynamical or incoherence hypothesis.

Let w_- be a positive lower bound for w and w_+ an upper bound. Define

    dist_mu(f,constants)^2=min_b integral |f-b|^2 dmu.

Since variance minimizes the corresponding squared distance, comparison
of the measures w mu and mu gives the two-sided estimate

    c_G rho w_- dist_mu(f,constants)^2
       <=Q_mu(f)<=c_G rho w_+ dist_mu(f,constants)^2.      (T7)

For the upper bound, evaluate the weighted minimization at the mu mean;
for the lower bound use w>=w_- before minimizing. Thus the nullspace is
exactly the constants, up to mu-null sets, and the form is coercive on their
L2(mu) orthogonal complement. It is a bounded quadratic form, represented by

    (A_mu f)(a)=c_G rho w(a)[f(a)-integral f dnu],
    0<=A_mu, ||A_mu||<=c_G rho w_+.                      (T8)

Indeed its L2(mu) inner product with h equals (T5). The weighted mean is
not generally the mu mean; substituting one for the other in (T8) would
break this identity. All bounds restrict correctly to exchange-even functions.

Here coercivity is a statement about a mathematical form and its normed
space. It does not assert exponential decay under the actual unitary walk.
A Markov evolution built using -A_mu would be an additional construction,
requiring a specified physical encounter process and loss of coherence before
it could represent collisions in a many-body system. Neither is derived.

### 4. Exact relation to coherent shell-current change

In the actual shell Hilbert space let

    v=Zc/sqrt(rho), S=I+(s-1)|v><v|, s=conj(G)/G.

The probability measure induced by v is precisely nu. For bounded real
exchange-even f, put m=integral f dnu and W=(f-m)v. Then W is orthogonal
to v, and direct expansion of S^* f S gives

    D_f:=S^* f S-f
       =(s-1)|W><v|+(conj(s)-1)|v><W|.                  (T9)

The diagonal term cancels using |s|=1. If W is nonzero, this is a two-by-two
off-diagonal Hermitian block on span(v,W); otherwise it is zero. Therefore

    ||D_f||_op^2=|s-1|^2 Var_nu(f),
    Tr(D_f D_h)=2|s-1|^2 Cov_nu(f,h),
    |s-1|^2=4pi^2 rho^2/|G|^2.                         (T10)

Combining (T6) and (T10) proves (T1) and its polarized form

    Q_mu(f,h)=(1/(2pi))Tr(D_f D_h).                     (T11)

The trace exists because these differences have finite rank, regardless of
the infinite dimension of the angular shell. The operator norm equals the
largest absolute coherent expectation change over unit vectors, not the
change of every vector. The form is its square divided by pi.

Dark coherent channels are retained exactly: S psi=psi whenever
<v,psi>=0, so their expectation of every bounded f is unchanged. Also S v=s v,
so v itself has unchanged angular probability and unchanged f expectation.
When Q_mu(f)>0, W/||W|| is an explicit normalized dark preparation.
These states give zero current change despite the positive form. A finite-beam transfer
probability additionally depends on its overlap with v and the detector;
it is not Q_mu(f), and the flux note's formula for disjoint detectors retains
that dependence. Positivity of (T6) is not universal unitary dissipation.

### 5. Central scaling and the three relevant measures

Take (kappa,e) in any compact set with 0<e_min<=e<=e_max and
|kappa|<=e/4, and set K=lambda kappa,E=lambda e. Choose lambda sufficiently
small for the regular-shell hypotheses. Write

    D=e^2-|kappa|^2, B=[D I+kappa kappa^T]/4,
    rho=lambda^2[r0+O(lambda^2)], r0=D/(4pi^2),
    G=lambda[A(kappa,e)+O(lambda)],                     (T12)

uniformly on that compact set. The named threshold input supplies

    A=e integral [(e^2-|kappa odot cos q|^2)
        /(4|sin q|^2(e^2-(kappa dot v0(q))^2))]dq/(2pi)^3,
    v0_i(q)=sin(q_i)cos(q_i)/|sin q|,
    (D/e)I0<=A<=e I0,
    I0=integral dq/[(2pi)^3 4|sin q|^2]>0.               (T13)

No new PV proof is asserted here. Only this order-zero expansion is needed;
the high-order threshold derivatives and Cook estimates are not used.

The limiting contact law can be reconstructed directly. On one cone put
p=kappa/2+y. The shell is |p|+|kappa-p|=e, with contact weight
w0=D/[8|p||kappa-p|]. For k=|kappa|>0, prolate coordinates with
u=(|p|+|kappa-p|)/k, t=(|p|-|kappa-p|)/k and azimuth phi have volume
Jacobian k^3(u^2-t^2)/8. Multiplication by w0 and delta(e-ku) leaves
D dt dphi/16. Integrating, restoring (2pi)^-3 and all eight cones, yields
r0=D/(4pi^2). After normalization, t is uniform on [-1,1] and phi on
[0,2pi]. Equivalently,

    y=L n, n uniform on S^2, L=B^(1/2),                 (T14)

with equal weight at each corner. The k=0 statement is its regular spherical
limit. This reproduces P13-P15 of the frozen packet source without treating
its scalar variance as an assumption for the new cross moments.

For later normalization the unweighted phase-space mass is also needed.
On this parametrization, 1/w0=2(e^2-k^2 t^2)/D. Consequently

    M=lambda^2[M0+O(lambda^2)],
    M0=r0 integral (1/w0)dnu0
       =(e^2-|kappa|^2/3)/(2pi^2).                     (T15)

The measure and shell geometry are smooth in lambda^2 in scaled coordinates,
so these order-two corrections are uniform. The spectral gap bound (T7) in
L2(mu) does not vanish merely because M does. Indeed

    c_G rho=D/[pi A^2]+O(lambda),
    15/(16pi I0^2)<=D/(pi A^2)<=16/(15pi I0^2).           (T16)

After decreasing lambda uniformly if necessary, (T7) thus implies the
explicit sufficiently-small-lambda bounds

    15/(128pi I0^2) dist_mu(f,constants)^2
         <=Q_mu(f)<=16/(15pi I0^2) dist_mu(f,constants)^2. (T17)

Here we used w_-=1/4,w_+=1/2 and a factor-two allowance in (T16).
The same constants hold if both Q and the squared L2 distance are divided
by M. They do not give a physical decay frequency.

Keep the measures separate:

- mu is the unnormalized phase-space measure, of mass M=O(lambda^2).
- bar mu=mu/M is normalized phase space. Its associated form with the same
  outgoing kernel is Q_bar_mu=Q_mu/M.
- nu=w mu/rho is normalized contact probability. The bare contact variance
  Var_nu(f) is Q_mu(f)/(c_G rho^2), not Q_mu itself.

In particular, normalizing the outer measure silently removes a factor
lambda^2. Replacing only the outer mu by nu while retaining (T3) generally
breaks detailed balance under a/b exchange and changes the variance identity
(T6). The resulting difference-product integral is still a symmetric bilinear
form in f,h, but it has different weights.

### 6. Energy-current tensor from full fourth moments

For the specified canonical energy placement the current is

    J_i=P g_i P+F_i,  g_i(K,q)=sin K_i cos(2q_i),
    F_i=-|partial_(K_i)(H0c)><H0c|-|H0c><partial_(K_i)(H0c)|.
                                                               (T18)

The bounded finite-rank F_i has vanishing free asymptotic expectation on
the regular packets with the integrable spectral profiles specified in the
canonical/packet sources. Wave-operator convergence transfers that statement
to scattering states. Thus g_i is the asymptotic canonical-current multiplier.
This section computes its angular form. It does not apply (T5) to the full
finite-time operator F_i, which is not a scalar angular multiplier.

On a corner q=C+lambda y, subtract the shell-constant sin(lambda kappa_i):

    g_i-sin(lambda kappa_i)
         =lambda^3 gamma_i(y)+O(lambda^5),
    gamma_i(y)=-2 kappa_i y_i^2.                         (T19)

The expansion is uniform in the scaled shell coordinates. Constants vanish
from every covariance. If C_ij denotes Cov_nu0(gamma_i,gamma_j), then

    Cov_nu(g_i,g_j)=lambda^6 C_ij+O(lambda^8).            (T20)

For n uniform on S^2,
E(n_alpha n_beta)=delta_(alpha,beta)/3 and its fourth moment is the sum
of the three pairings divided by 15. Using y=Ln and LL^T=B gives

    E(y_i^2)=B_ii/3,
    E(y_i^2 y_j^2)=[B_ii B_jj+2 B_ij^2]/15,
    C_ij=(8/45)kappa_i kappa_j[3B_ij^2-B_ii B_jj]
        =(kappa_i kappa_j/90)
          [3(D delta_ij+kappa_i kappa_j)^2
                   -(D+kappa_i^2)(D+kappa_j^2)].        (T21)

For i=j this reduces to kappa_i^2(D+kappa_i^2)^2/45, agreeing with
P15-P16 after squaring its one-component standard deviation. Off-diagonal
entries generally do not vanish; treating the three squares y_i^2 as
independent would give an incorrect tensor.

Define the transport tensor T_ij(lambda,kappa,e)=Q_mu(g_i,g_j). Equations
(T6),(T12),(T20) give the explicit result

    T_ij=lambda^8 T0_ij+O(lambda^9),
    T0_ij=[D^2/(4pi^3 A^2)] C_ij
         =[D^2 kappa_i kappa_j/(360pi^3 A^2)]
           [3(D delta_ij+kappa_i kappa_j)^2
                     -(D+kappa_i^2)(D+kappa_j^2)].       (T22)

The error is uniform in matrix norm on the selected compact central set.
The order-nine remainder comes from the inherited O(lambda) correction to
G/lambda; the angular covariance itself has the stronger order-eight error.
For a real current direction z,

    Q_mu(z dot g)=z^T T z,
    ||S^*(z dot g)S-z dot g||_op^2=pi z^T T z.           (T23)

For a single component with kappa_i nonzero, the coherent packet's leading
signed coefficient has magnitude
c_i=|kappa_i|(D+kappa_i^2)D/(6pi sqrt(5) A). Accordingly
T0_ii=c_i^2/pi. This checks the normalization against the earlier coherent
construction, but is not its independent review. At finite lambda that
specific v plus/minus i u preparation attains |Im s| times the standard
deviation; the operator optimum uses |s-1|. Only their leading small-phase
coefficients coincide.

The measure comparison is now explicit:

    Q_mu(g_i,g_j)=O(lambda^8),
    Q_bar_mu(g_i,g_j)=lambda^6 T0_ij/M0+O(lambda^7),
    Cov_nu(g_i,g_j)=lambda^6 C_ij+O(lambda^8).            (T24)

Energy E and total momentum K are constants on each fixed shell and have
zero form. The current is an angular observable and can have positive form
without either conserved quantity changing.

### 7. Tensor rank, null directions and explicit bounds

Let I={i:kappa_i!=0}, let a_i=kappa_i z_i and A_z=diag(a_1,a_2,a_3).
The quadratic form of the covariance tensor is

    z^T C z=(8/15)||L A_z L-[Tr(L A_z L)/3]I_3||_F^2.    (T25)

This follows either from the fourth moments above or from the uniform-sphere
variance of a quadratic form. Hence it vanishes exactly when

    A_z=t B^(-1), B^(-1)=(4/D)[I_3-kappa kappa^T/e^2]     (T26)

for some real t. If I is a proper subset, an inactive diagonal entry of A_z
is zero whereas the corresponding entry of B^(-1) is positive; therefore
t=0. If I is all three coordinates, a nonzero off-diagonal entry of B^(-1)
again forces t=0. Thus, for every kappa,

    ker C={z:kappa_i z_i=0 for each i}, rank C=|I|.       (T27)

As a useful nondegenerate example, when kappa=b(1,1,1) with b!=0,
substitution in (T21) gives eigenvalue b^6/15 along (1,1,1) and the
double eigenvalue b^2 D(D+2b^2)/30 on its orthogonal complement. The third
direction is weak for small b but positive; replacing the contact ellipsoid
by an exactly spherical law would incorrectly erase this contribution.

At kappa=0 all entries are zero. The same rank holds for T0 because its
scalar factor in (T22) is positive. At actual K=lambda kappa, each inactive
current component g_i is exactly zero. On a compact set with a fixed active
pattern bounded away from kappa_i=0, the active finite-lambda tensor retains
rank |I| for sufficiently small lambda, by (T20) and positivity below.
There is no uniform rank-three coercivity across coordinate planes.

A quantitative lower bound avoids relying only on a rank calculation. For
nonempty I put

    eta_I=1-[sum_(i in I) (B^(-1)_ii)^2]/||B^(-1)||_F^2>0.

The strict inequality follows from an unused positive diagonal term when I
is proper, or from off-diagonal terms when I is all three. For any diagonal
A_z supported on I, Cauchy-Schwarz gives

    dist_F(A_z,span(B^(-1)))^2>=eta_I sum_i a_i^2.

Since ||L^(-1)||^2=4/D, conjugating the traceless minimization in (T25)
gives the lower bound; ||L||^2=e^2/4 gives the upper bound:

    (D^2 eta_I/30)sum_i kappa_i^2 z_i^2
       <=z^T C z<=(e^4/30)sum_i kappa_i^2 z_i^2.         (T28)

These explicit bounds, multiplied by D^2/(4pi^3 A^2), bound T0. They also
supply uniform active-subspace coercivity on any of the compact sets just
described. Constants and a sufficiently small lambda range can be chosen
from their positive minima and the finite uniform remainder in (T20).
No numerical largest validity range is certified here.

In particular, K=0 has positive paired probability-flux cross section but
zero canonical energy current, and hence a zero current tensor. If kappa
has one or two zero components, the corresponding exact current directions
remain null. Coherent dark preparations remain stationary under S even when
all three current directions give a positive tensor. These are separate,
compatible facts about the observable, measure and prepared state.

### 8. Controls, scope and next check

The separate helper `flux_transport_form/transport_controls.py` and complete
log `flux_transport_form/transport_controls.log` are author evidence. Its
first family uses a genuinely nonuniform unnormalized eight-atom measure,
with different mu and nu, and exact Gaussian-rational S matrices. It verifies
the variance identity, squared operator norm, Hilbert-Schmidt polarization,
coercivity on the chosen fixture and exact dark/pure-contact zero-change controls. Multiplying by
pi makes all tested coefficients rational without substituting a decimal pi.
The finite atoms are exchange-orbit quadrature analogues, not a claim that
the actual eight corner masses differ.

The second family directly integrates polynomials on the unit sphere using
exact monomial moments, rather than inserting the tensor formula. Five
rational ellipsoid geometries have ranks 0,1,2,3,3 as their active components
predict; exact principal-minor tests check the proposed upper and lower
quadratic bounds. The last family evaluates the actual sine-dispersion
coarea moments, retaining all eight corners, in nine shell cases at two
quadrature resolutions. It checks mass, contact density and the full current
covariance against the limiting formulas. This floating calculation is not
interval certified and does not prove the analytic uniform remainders.
The method overlaps this author's earlier radial-shell controls; it is
separate finite evidence, not an independent scientific review.

The complete 228-line helper and 18-line exit-0 log were read. Their SHA-256
identities are `befeb5d995039a55031ce697e1098370ebed1c3a846657ef3cc1cd1d01830d23`
and `aeaec385f509e049b7175c8b7987219ab2e77781b193fa0a352d9dd08a9c44d4`,
respectively. Exact identities, execution status, source coverage and tooling
failures are recorded in `flux_transport_form/receipt.json`. The note and controls do not
recompute G by a numerical PV fit. The general central expansion remains
the named analytical dependency; the abstract identities T3-T11 hold on
any regular supplied shell satisfying their explicit conditions.

Insufficient routes retained: replacing the paired incident state by an
ordered component loses a factor of two; normalizing mu silently changes a
lambda power; discarding cross covariances can change rank; and treating the
positive form as a statewise unitary current loss conflicts with its exact
dark and phase-only controls. These are normalization/interpretation checks,
not a universal no-go claim about future kinetic constructions.

The normalization, coherent-norm identity, full tensor and coercivity/rank
proof have received the separate source-bound check recorded below. A useful
next target is a derived encounter process with controlled phase information,
which could connect this form to a closed collision equation. That target is
outside the theorem proved here; the construction does not settle it.

## Review record and scoped formal verification

The component proofs were read completely and independently reconstructed
before publication. `ROOT_EXCLUDED_WALK_FLUX_REVIEW.md` binds the 628-line
flux source, its nonparallel-spinor and nonuniform-channel checks, and the
selected primary stationary-phase source passages. The 468-line form source
has the separate `ROOT_EXCLUDED_WALK_TRANSPORT_FORM_REVIEW.md`, including
three-channel matrix calculations, a fourteen-point sphere design and exact
rank/coercivity checks. Those are selective independent research checks,
not an applied audit verdict. Their exact sources, full outputs and receipts
are preserved in this milestone's evidence directory.

The complete 202-line `formalization/excluded_walk_rank_one/RankOneScattering.lean`
proves the universal Hilbert-space rank-one unitarity, observable difference,
coherent expectation and normalized disjoint-cap transfer identities.
`formalization/excluded_walk_rank_one/README.md` maps its hypotheses and the
pinned Lean/Mathlib environment. Normal compilation succeeded; the printed
axiom reports contain only propext, Classical.choice and Quot.sound. Three
positive scalar boundary witnesses compile and six deliberately false identities
reject at mathematical goals. The certificate supplies the stated algebra;
it does not formalize the lattice flux, analytic threshold or Cook arguments.
The operator-norm and tensor proofs here retain their separate analytic checks.

The primary contains both complete author control programs, so its finite
checks have no hidden helper-runner dependency. They cover exact finite-torus
continuity and parity, finite-channel scattering, weighted forms, spherical
moments and actual lattice-shell quadrature. Floating quadrature is not
interval certified. Source mutations and their full intended-failure logs,
canonical execution output and composition identities are recorded in
`.claude/science/physics-loops/toe-scattering-flux-20261011/DELIVERY_CHECKS.md`.
Formal compilation is a separately reproducible proof artifact, not a success
claim inferred by the Python primary. Historical failed Lean development and
control-harness attempts are preserved without treating them as certificates.

No earlier scientific statement is replaced. Publication changes to the frozen
arguments are confined to metadata, source-location explanation, headings and
review-status prose; the composition map lists the exact edits. The complete
stacked premise and its inherited scope must remain in the reviewed landing
unit. No audit-owned state, physical axiom, editable prompt or repo-wide claim
registry is changed. This is conditional-support original mathematics awaiting
independent audit under its explicit premises.

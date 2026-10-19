# Native finite-size selection: fusion energy and kinetic stability

Type: bounded_theorem (author derivation, independent review pending).
Status: conditional-support. Target remains open outside the quantified window.
This is direct work requested after the fixed campaign deadline, not an extension
of that campaign. No new interaction, oscillator, qubit or physical primitive is
introduced. Every coefficient below belongs to the supplied Hamiltonian

    H=-J sum ZZ_z-J lambda(sum XX_x+sum YY_y), J>0,

on an even transverse torus and periodic height L=10. Weak coupling, this
Hamiltonian and slab geometry remain premises. The observation-facing question
is whether it supplies persistent finite objects; no empirical dataset or
observed particle size has been inserted or tested.

## Exact target and result

Distinguish energetic size selection from absence of capture in an isolated
unitary collision. Let q count bad COLUMN PLAQUETTES, not physical qubits or
particle number. Let E_q denote the lowest excitation energy in the native
low-energy spectral cluster continuing the wall-free, q-defect, all-positive-
plane sector. Its use is justified only where these clusters are separated.

Under the previously derived finite-order, Q-relative normal-form bounds,
there are constants C,C' independent of q,R such that, for admissible neutral
q>0, sufficiently large R relative to q, and sufficiently weak lambda,

    E_(2q)-2 E_q <= -8 J b lambda^6
                    +4 C J q lambda^8+C' J R² lambda^M,
    b=3L/8192 >0.                                           (1)

The normal-form hypotheses and the spectral separation conditions are stated
below; (1) is not being extrapolated beyond them. For every FIXED admissible q,
the right side is negative for sufficiently small lambda. More generally it
is negative along q lambda² ->0, q/R ->0 and R²lambda^(M-6)->0. This is a
constructive fusion-energy inequality, not proof that collisions actually
capture or that every size is unstable at any fixed coupling. It leaves open
size selection with q of order lambda^-2 or larger, a different regime, and
kinematic/metastable protection. The original Hamiltonian has not yet supplied
a preferred finite size.

## Inputs and provenance

The exact sixth-order operators are derived in
[SIX_LAYER_NEUTRAL_POLE_PROOF.md](SIX_LAYER_NEUTRAL_POLE_PROOF.md), section1:
its diagonal connected-word calculation is per longitudinal layer and is
independent of height once wraps are longer than six. Here L10 excludes the
L6 winding term at that order. Thus the wall-free energy relative to flat is

    J[(L/64) q lambda^4 +(2a q+2b p(S))lambda^6],
    a=25L/18432, b=3L/8192,                                (2)

where p(S) is the edge perimeter of the bad-plaquette set S. The finite-order
reduction, coefficient-relative bound |D_j|<=C_j Q, wall exclusion and final
absolute tail C J R²lambda^M are provisional checked inputs from
[ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md),
section 'Low-energy embedding for any fixed polynomial size'. Its explicitly
GLOBAL Q-relative inequality, rather than a fixed-Q4 norm extrapolation, is
needed for the growing-q statement. Both files are inherited at commit
98416789caa714eac194a99c88f41aaa95459212. No independent review of the new
uniform-q composition has completed; failure of that premise invalidates that
extension, while leaving the finite geometric identity intact.

Even-order parity and the absence of winding below order10 give, on Q=q,

    ||H_q-e_flat-J[(L/64)q lambda4+(2a q+2b p)lambda6]||
       <= C J q lambda8 + C' J R²lambda^M.                 (3)

Here H_q is the matched finite-order block, not H with Q arbitrarily declared
exactly conserved. All diagonal shape corrections and quantum hopping are
included in the bound. For fixed truncation order its constants are independent
of q and R. The first winding hopping is order10 and cannot supply an omitted
order-six quantum pressure. Arbitrary fixed lambda, all-volume convergence of
the expansion and strong-coupling energetics are not assumed.

## Reflection gluing lemma: arbitrary shapes, not a rectangle ansatz

Every finite realizable S has even parity in each occupied row and column.
Its finite inverse column mask has parity

    nu(S)=sum_(x,y in S) x*y mod2.

Neutral positive Z-plane charge means nu(S)=0. Finite syndromes with even row
and column sums have a finite inverse: the discrete double antiderivative
modulo2. Uniform positive X/Y plane superpositions then realize each such
neutral syndrome in the physical one-qubit Hilbert space.

Let h=max{x:(x,y) in S} and reflect a copy by x ->2h+1-x. The two sets are
disjoint, occupy opposite sides of the cut h+1/2, and have the same boundary
column y-coordinates. Set T=S union reflected(S), and let c be the number of
points in the rightmost column of S. Column parity gives c even and c>=2.
Exactly c new nearest-neighbor bad-bad edges cross the cut. Therefore

    |T|=2|S|,   p(T)=2p(S)-2c <=2p(S)-4.                 (4)

All row and column parities remain even. Reflection preserves nu(S), since
sum y is even modulo2 by the row condition; hence nu(T)=0. T has a valid finite
inverse column mask. This step accommodates holes, separated pieces and
irregular shapes. It does not violate a hard-core rule: no physical site gets
an extra qubit, and the inverse mask is simply another Pauli column-flip state.

Let p_q be the minimum perimeter among admissible neutral q-defect sets. A
minimum exists because perimeter is a positive integer and an admissible set
is supplied. A representative can be compressed: occupied coordinate gaps
larger than one can be replaced by 2 or3 of the same parity. This preserves
nearest-neighbor incidence and nu, and gives span O(q). Thus a sufficiently
large torus with R>12q contains S and T without wrap contact. Applying (4) to
a minimizing S gives p_(2q)<=2p_q-4.

The min-max bounds from (3) give

    E_q=J[(L/64)q lambda4+(2a q+2b p_q)lambda6]
           + r_q,  |r_q|<=C J q lambda8 + O(JR²lambda^M).

The terms proportional to q cancel in E_(2q)-2E_q. Using (4) yields (1).
Quantum relaxation was not discarded: the LOWER bound for E_q and UPPER bound
for E_(2q) use the full operator error in (3). This avoids comparing a joined
trial against two unrelaxed product states and mistaking that for a bound
between optimized energies.

## Growing size and microscopic spectral meaning

For fixed q and R~lambda^-p, choose M>6+2p. For a growing q~lambda^-alpha,
0<alpha<2, choose p>alpha and M>6+2p. More generally use the three little-o
conditions following (1). Then q lambda6=o(lambda4), so the widths of the
relevant nearby Q-clusters are smaller than their order-lambda4 spacing.
The global Q-relative lower bound excludes much higher Q, and q lambda4=o(1)
keeps the target energies below the order-J wall threshold. The absolute tail
is smaller than the fusion margin. Weyl/min-max transfer therefore identifies
the stated actual-H energy clusters under the inherited bounds.

This is a limit statement about defect count. It is not a measured radius,
a uniform fixed-lambda thermodynamic theorem, or a derivation of the scale
lambda^-2 as an optimum. That scale marks where the present error estimate
can stop deciding the sign. A future stable-size calculation must resolve
that regime rather than relabel the error boundary as the answer.

## Larger explicit witnesses and higher-order checks

A separate complete order-eight calculation already independently checked in
[final_pending/neutral-aggregate-review.md](final_pending/neutral-aggregate-review.md)
uses motifs at columns (4i,3j),(4i+1,3j). Every finite coarse subset A has
q=4|A| and perimeter12|A|, and its full D8 interaction is

    -J (9L/32768) lambda8 * edges(A).

Only straight-three plaquette operators bridge neighboring motifs, twice per
coarse edge; no retained support meets three motifs. An m-by-m occupied coarse
square has binding -Jv lambda8(2m²-2m). This trial-family identity supports
aggregation but by itself did not compare optimized sizes. Equation(1) is the
stronger new comparison and uses the earlier order-six boundary energy.

For a compact 2m-by-2m filled bad square with even m, q=4m², neutral inverse
parity is m² mod2=0. The elementary bound p>=4sqrt(q) is attained, so p_q=8m.
Joining two into a 4m-by-2m rectangle saves perimeter4m and energy
8Jbm lambda6 at leading order. Full D8 invariants, including repulsive ones,
are later by lambda² at each fixed m. Their existence has been included in
(3); it is not a license to discard them at large q or lambda near one.

## Energy conservation can prevent capture without selecting a size

The already derived two-neutral-feature threshold and tetramer band differ
by Jv lambda8. Their respective kinetic widths begin at orders lambda12 and
lambda16. In the sufficiently weak regime the bands are disjoint. Exact
spectral projectors commute with H: a state prepared in the exact incoming
energy window cannot evolve into the lower isolated tetramer window under
H alone. An initially separated but unfiltered packet needs its initial
bound-band overlap estimated; zero capture is not asserted for that arbitrary
preparation. Emission, a third body, other channels, finite density and an
external environment require a separate energy/matrix-element analysis.

There is also an unfiltered quantitative version using the already constructed
native dilute two-feature states. Let W be the physical finite-occupation
isometry of [NATIVE_DILUTE_FIELD_PROOF.md](NATIVE_DILUTE_FIELD_PROOF.md), with
its matched actual ground. Choose two normalized smooth momentum envelopes
supported at |q|<=K lambda², R~lambda^-14 and final normal-form order M80.
Its checked intertwining error is J[lambda4/R+R²lambda80]=O(Jlambda18),
while the two-particle kinetic energy above 2epsilon_N(0) is O(Jlambda16).
Thus the normalized PHYSICAL initial state Psi=W psi obeys

    ||(H-E_g-2epsilon_N(0))Psi|| <= C J lambda16.

No exact bound-band removal has been applied to Psi. Let P_lower project onto
energies at most E_g+2epsilon_N(0)-c Jlambda8 for fixed c>0; choose c smaller
than v for the tetramer family. By the spectral theorem,

    ||P_lower Psi||² <= C² lambda32/(c²lambda16)
                     = O(lambda16).

Because P_lower commutes with the exact H, the same bound holds for
P_lower exp(-itH)Psi at EVERY physical time t. The argument uses only the
initial residual estimate, so it does not extend a finite-time effective
Hamiltonian approximation to infinite time. The existing dilute-packet
preparation and fixed slab remain explicit conditions. Additional particles,
an environment or another energetically allowed outgoing channel are not
covered. The bound supplies no preferred size, capture rate or cosmological
initial-state selection.

This provides a real native protection mechanism for isolated collisions.
It protects preparation-dependent excitations; it does not minimize E_q/q or
select one feature size. Likewise exact plane charges can protect charged
sectors, but the neutral fusion construction preserves all plane characters.
A growth rate or lifetime is not deduced from the energetic inequality.

## Checks, prior art and next decisive calculation

Root checked 2047 nonempty even-parity column masks on a 3-by-4 test domain,
including disconnected and irregular syndromes. Every reflected union passed
exact Q doubling, perimeter saving, row/column parity and finite-inverse checks.
Contact counts were2 (1364 cases) or4 (683 cases). This finite control checks
the constructive lemma; its arbitrary-size proof is (4), not extrapolation.
The scalar aggregation reviewer checked all512 subsets of a3-by-3 coarse
array before its later usage-limit failure. New full fusion-energy and
uniform-q transfer review remains pending because reviewers hit usage limits.

Landed search at origin/main847eb8a25bbeafd3228a56c503ef3e6030410234 found
no matching finite-feature aggregation statement using finite-size/aggregation/
self-limiting/coarsening variants. PR9763 at182edbe560964d5edfc40740e535c27030a80a81
was read: it joins odd-height arrays and tests dark readout, a different claim.
PR9820 is the immediate tetramer premise, not a stable-size result. This is a
bounded search, not a claim of exhaustive literature novelty. Grid perimeter
optimization is established prior art: [Bollobas and Leader, 1991](https://digitalcommons.memphis.edu/facpubs/4558/).
The reflection construction and native energy comparison are written out here;
no novelty is claimed for the general surface-energy/coalescence idea.

Next decisive target: compute optimized quantum energy versus q where q lambda²
is order one, with controlled errors, and separately identify an energetically
allowed native capture/emission channel. A turnover in E_q/q would support
energetic finite-size selection; a suppressed capture channel alone would
support kinetic persistence. Neither is supplied as an assumption.

## No-Go Discipline Gate: partial narrowing, not a universal no-go

N1: Five distinct mechanisms were examined: arbitrary shape relaxation (gluing
lemma); quantum kinetic pressure (full operator bound); local occupancy exclusion
(disjoint syndrome plus physical inverse); exact plane charges (neutral fusion
preserves them); and energy-conserving capture (disjoint spectral windows).
The fifth actually supplies kinetic protection, so the broad claim that H
cannot stop aggregation is rejected. Mesoscopic q lambda²=O(1), strong coupling
and other excitations remain untested. No retained-authority rejection of those
routes is claimed, and a universal five-route no-go packet is NOT certified.

N2: Supplied H, weak regime and physical spectral interpretation are explicit.
The growing-q interpretation depends on the GLOBAL Q-relative bound; it is not
an independent wall. No count of independent obstructions is asserted.

N3: 'background' means the specified flat column syndrome in the inherited
normal form. 'canonical' concerns the matched finite-order frame. Neither
supplies a hidden state-selection or universal measurement bridge. All other
conditions are stated above.

N4: PR9763 is a nonmatching joining/readout result and is not used as evidence
against size selection. The tetramer and Q-relative notes supply coefficients
and bounds only; none is cited as a prior universal aggregation no-go.

N5: Per-site occupancy, finite-pattern geometry and block energy are tested.
Individual physical-mode lifetime and the full fixed-lambda lattice are not
resolved. The runner prints these resolution limits explicitly.

N6: The approved scale-reference, kinetic-form and realized-state primitives
were checked in the registry and source notes. No conversion of units or
pointwise state specialization determines an energy optimum or capture rate.
No new primitive is requested or asserted necessary.

N7: Strongest counter-route: an optimizing feature whose defect number grows
at least as fast as lambda^-2 can lie outside the error-controlled comparison;
quantum mixing or higher-order interface structure there could select a size.
Even inside the energy comparison, exact energy conservation can inhibit capture.
These are live mechanisms, so only (1) in its stated domain is proposed.

N8: Prior native joining, weak-coupling common-metric and finite-source limits
were checked for scope. Their restrictions do not close this target. The
counter-route stays explicit; independent review and full packet certification
remain pending. Overall disposition: author-supported partial narrowing, no
universal no-go and no formal audit verdict.

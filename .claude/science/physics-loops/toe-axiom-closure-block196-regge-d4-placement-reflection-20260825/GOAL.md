# Goal

Block 196 tests the first physically typed Regge-D4 carrier chain.  It must
pass representation, chain-map, faithfulness, and action/Riesz gates before
any L24 source contraction or TT response may be read.

## Known exploratory inputs, not target discoveries

Route preflight has already exposed six facts which this campaign must
independently reproduce rather than present as blind discoveries:

1. the 15 positive Regge directions are closed under coordinate permutations,
   but time reflection needs 22 directions and the full 24-frame proper-
   spatial orbit modulo edge reversal needs 40;
2. a raw-column-identity `15 x 10` one-cell Ward prefilter has exact linear
   rank `798=rank_aug` in 800 unknowns, permutation covariance fixes the two
   remaining coefficients to `sqrt(2)/12`, and one common rank-ten minor is
   `i/1024` at D1 and `-(sqrt(3)-i)/2048` at H1;
3. that prefilter is not yet a physical chain map because the D4 gauge columns
   are link centered while Regge gauge columns are vertex displacements; and
4. at `z_t=-1`, raw-link and vertex-vector time-reflection representations
   force any equivariant globally invertible single-cover gauge leg to rank at
   most three; and
5. a temporal-only double cover is not closed under the 24 proper-spatial
   frames: for the half-turn `diag(-1,-1,1,1)` at `z_x=z_y=-1`, the raw-link
   representation is `I_4` while the vertex representation has a two-plus,
   two-minus split, forcing an equivariant temporal-only `C` to rank at most
   two.  The minimal group-closed live target is therefore the full four-axis
   half-lattice placement grading; and
6. the literal Block-77 raw `Gamma_D` and Regge `G_R` have only even placement
   grades, whereas column `mu` of `G_R C` has singleton grade `u_mu`.  A
   one-coset 800-coefficient `M` is therefore ill typed.  The smallest
   symmetry-unbiased literal-raw ansatz has all four singleton grades on every
   tensor slot, or four decoupled 800-variable systems.  The other twelve
   parity grades have zero target and would add only unselected homogeneous
   sectors.

## Target gate

Let

`K=Q(i,sqrt(2),sqrt(3))`

and work over the minimal group-closed placement extension

`R=K[z_x,z_x^-1,...,z_t,z_t^-1,u_x,u_x^-1,...,u_t,u_t^-1]`

modulo `u_mu^2=z_mu^-1` for all four axes.

It has the 16 placement-parity grades over the coarse Laurent ring.  Signed
spatial frames act by the corresponding permutations and inversions of the
`u_mu`; time reflection sends `u_t` to `u_t^-1`.  These are formal ring
automorphisms, and their exact composition and involution laws are target
gates.  The grading must descend to one base-torus physical map: sheet labels
may not become new species, observables, responses, or selectable sectors.

The gauge-placement leg is fixed before the solve by the Block-77 physical-
center chart,

`C(u)=diag(u_x,u_y,u_z,u_t)`.

It is not a fitted target.  Seek the single response-blind tensor leg `M`
satisfying

`M(z,u) Gamma_D(z) = G_R(z) C(u)`

such that:

1. the frozen `C` maps the four link-centered D4 gauge columns to the
   vertex-based Regge gauge carrier, has `C(1,+,+,+,+)=I_4`, rank four on
   every sheet, and exact proper-spatial/time-reflection covariance;
2. `M` maps all ten D4 tensor components into the appropriate Regge edge
   carrier, obeys the coefficientwise Ward identity, and has generic rank ten;
3. the construction closes first on the 22-edge time-reflection union and then
   on the 40-edge full proper-spatial induced carrier/orientation bundle;
4. all shared orientations agree with their Laurent placement translations,
   rather than being duplicated as independent fitted rows; and
5. normalization and equivalence are fixed without reading any action inverse,
   Riesz dual, TT response, D1/H1 sensitivity, or held-out outcome.

The only allowed coefficient ansatz is fixed explicitly.  For a positive base
row `d in {0,1}^4 \ {0}` and any of the ten Frobenius tensor slots `A`, require

`M[d,A] = sum_(g=0)^3 u_g sum_(s<=d) c[d,A,g,s] z^s`,

where each component of `s` is zero or one.  This is exactly 3200 coefficients
and splits coefficientwise into four 800-variable systems
`M^(g) Gamma_D=G_R E_gg`.  Signed frame inversions preserve the singleton set
because `u_g^-1=z_g u_g`.  No other placement grade is allowed.
The 22- and 40-edge rows are induced from these 15 base rows by the frozen
group/anchor action and are never separately fitted.  At the all-plus zero-
momentum sheet, `M` is normalized to the standard Regge edge-versus-Frobenius-
metric map.  No fallback support, second graded carrier, altered orbit, or
larger range is allowed.  The constant-support mixed-monomial failure is a
known control, not a new target.

The 40-edge carrier is frozen mechanically: apply each Block-77 proper-cubic
rotation embedded as `diag(R_3,1)` to every positive base direction; identify
an unoriented image with its negative by choosing the representative whose
first nonzero component is positive; and, on reversal, attach the unreversed
image direction as the anchor offset.  That offset supplies the Laurent phase.
No alternative canonicalization or independently fitted reflected row is
allowed.  The existing Block-48 constructor remains the independent 22-edge
time-reflection control.

The declared faithfulness census is every fourth-root torus point
`z_mu in {1,-1,i,-i}` on all 16 choices
`u_mu=+-sqrt(z_mu^-1)`: 4096 exact labelled `(z,u)` points.  Require
`rank C=4` and rank ten for the 15-, 22-, and 40-edge `M` maps throughout,
including every spatial and temporal Nyquist stratum.  Generic symbolic rank
alone is not enough.

If and only if the carrier, group-law, coefficientwise Ward, uniqueness, and
faithfulness gates all pass, open the frozen Regge and D4 quadratic forms.
Require the Regge form to descend to the D4 gauge quotient and match the
frozen D4 action up to one response-independent normalization or a proved
gauge-exact equivalence.  Require a positive, reflection-covariant, unique
Riesz dual on that quotient.  PR #7327 is a method template only and supplies
no premise.  Indefiniteness, action mismatch, or multiple positive duals is a
failure before response.

Only after all of those gates pass may D1/H1 be opened and the ten-slot L24
source be composed; all held-out response points remain sealed until that
first response gate is packaged.

The campaign stops before action/Riesz/response if the half-lattice carrier is
not reflection equivariant, if the one frozen support is empty or rank
deficient, if the 22/40-edge gluing is inconsistent, or if more than one
normalized physical solution direction survives.  A failed group law,
nontrivial unremoved cocycle, placement-coset nonclosure, or failure of
sheet-independent descent is also an immediate stop.  A failure is narrow: it
does not close larger doubled carriers, a different placement complex, or full
OS/GNS/CAR reconstruction.  Any such failure pivots the portfolio immediately
to an explicit reflection-positive OS/CAR history reconstruction rather than
another coefficient scan.

No axiom amendment, obligation retirement, retained status, or TOE percentage
movement is preregistered.

## Outcome

T1 passed and T2 failed exactly.  Each singleton-grade system has rank
`798` versus augmented rank `799`; `28/60` direction-grade blocks are
inconsistent, with first witness `d=1100,g=0` at `40/41`.  The mixed-edge
corner argument proves that no entrywise regular Laurent `M` of any finite
support solves the same frozen raw-symbol equation.  The registered stop fired
before 22/40 target induction, torus rank census, action, Riesz, response, or
held-outs.  No axiom, obligation, or TOE percentage moves.  The automatic
OS/GNS/CAR pivot is now rank one.

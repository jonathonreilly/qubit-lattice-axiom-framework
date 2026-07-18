# Physical Cycle-269 full two-particle fixed-seam interface — Cycle 305

Date: 2026-07-17
Authority: none
Audit: unset

## Decisive question

Can one fixed-Wilson physical M2 code carry the complete two-particle logical
sector of the six-mode Cycle-219 coin—not only the twelve perpendicular pairs,
but also the three antipodal pairs—and support an exact input-slice coin
comparator, Cycle-230 contact, and collision-safe stream/catch-up on one common
linear encoder?

## Constructive result

Yes, as a bounded reference-relative interface at one supplied body-cell
address.

The logical pair basis consists of all fifteen unordered pairs `a<b` of the
six direction modes.  The twelve perpendicular pairs are direct internal
octahedron edges.  Each of the three antipodal pairs is created by a bounded
two-edge intracell path through one perpendicular intermediate mode.

All columns are defined relative to the supplied fixed +++ Wilson reference
vacuum.

For every pair `p`, let `P_(x,p,0)|Omega_+++>` be its intracell state and
`P_(x,p,1)|Omega_+++>` its state after the complete outer-edge FSWAP and
collision-safe auxiliary catch-up.  The common encoder is one 30-column E_x,

    E_x = sum_(p=0)^14 sum_(t=0)^1
          P_(x,p,t)|Omega_+++><x,p,t|.

All 30 auxiliary tag patterns are distinct.  Therefore
`E_x^dagger E_x=I_30` exactly, and arbitrary coherent amplitudes across both
proper-cubic pair orbits and both stream slices are encoded by one linear map.

## The antipodal columns

An opposite pair has four possible two-edge paths, one through each
perpendicular intermediate direction.  The runner reduced every path modulo
the complete fixed +++ Wilson, all-`B=+1` stabilizer tableau.  At training
sizes `L=3,4,5` and held L=6, all four antipodal paths for all three pairs:

- produce exactly the two requested endpoint occupations;
- have bounded face support 2, 4, 6, or 8 M2; and
- are the same physical reference-vacuum ray with relative phase zero.

Thus the chosen smallest-label intermediate used by the executable is only
a representative gauge.  It is not a physical preferred route or ordering.
All four antipodal paths were explicitly checked; compatibility is not inferred
from their labels.

## Exact exterior-square coin

For the Cycle-219 six-mode coin `C`, the complete logical two-particle action
is `wedge^2(C)`, with matrix entries

    [wedge^2(C)]_(ij,ab) = C_(i,a) C_(j,b) - C_(i,b) C_(j,a),

for `i<j` and `a<b`.  This is the fermionic exterior square, including all
mixing between the twelve perpendicular and three antipodal pairs.

For beta `-0.2,-0.3,-0.4` and held beta `-0.35`, the runner checked:

- exact action on 24 generic decomposable wedges per beta;
- unitarity residual below `2.7e-15`;
- `det(wedge^2 C)=det(C)^5`; and
- `tr(wedge^2 C)=((tr C)^2-tr(C^2))/2`.

Only the `t=0` slice has both particles colocated at the supplied body cell.
The `t=1` columns have particles in distinct cells, so applying an onsite
two-particle coin there would not be the actual Cycle-230 volume law.  The
earned unitary comparator completion is therefore

    K_seam |p,0> = sum_q [wedge^2(C)]_(q,p) |q,0>,
    K_seam |p,1> = |p,1>.

Equivalently, it is `blockdiag(wedge^2(C),I_15)` in slice-major order.  The
bounded physical fixed-seam comparator is the local matrix-unit polynomial
described below and satisfies

    E_x K_seam = K_physical,seam E_x.

This imports the Cycle-219 coin coefficient matrix.  It does not turn its
wrapped eigenphases into physical energy or derive a new two-particle mass.
It does not claim a physical coin on the separated slice and is not a recurrent
volume update.

## Local physical matrix-unit polynomial

The shell touches twelve auxiliary tag vertices: the six body ports and their
six outer neighbors.  Let `Pi_j` be the projector onto the twelve-bit tag
pattern of column `j`, and let

    Q_ij = P_i P_j^dagger,
    M_ij = Q_ij Pi_j.

The executable checked all 900 `M_ij`, all 27,000 matching triple products,
adjoints, representative action, tag flips, and projector transport.  It found
zero failures in

    M_ij M_jk = M_ik,
    M_ij^dagger = M_ji,
    Q_ij Pi_j = Pi_i Q_ij.

Every transition and every projector generator commutes with the local
`B_v Z_port(v)` constraints, elementary face-code checks, and fixed Wilsons.
The coefficient matrix has 210 nonzero terms at beta `-0.3`.  The explicit
local matrix-unit polynomial acts by `K_seam` on the 30
selected tag sectors and as identity on the other 4,066 patterns of the twelve
active tags.

This establishes a bounded physical operator algebraically.  Primitive gate
synthesis remains open; no short native gate sequence is supplied.

## Contact, stream, and the one-step fixed-seam comparator

Every input-slice pair has both particles in the supplied body cell, including
the antipodal pairs, while every output-slice pair has its particles in two
distinct neighboring cells.  The existing Cycle-230 physical contact product
therefore restricts to

    D_coarse = I_15 tensor diag(exp(i g),1),  g=0.37,

and obeys

    E_x D_coarse = D_physical E_x.

The complete outer-edge FSWAP layer plus simultaneous collision-safe catch-up
restricts to `S_coarse=I_15 tensor X_2` and obeys

    E_x S_coarse = S_physical E_x.

The declared one-step comparison uses the actual Cycle-230 order: first the
input-slice `wedge^2` coin comparator, then the complete stream and auxiliary
catch-up, then contact:

    E_x (D_coarse S_coarse K_seam)
      = (D_physical S_physical K_physical,seam) E_x.

Contact commutes with the comparator because it is scalar on the complete
input pair sector.  Stream does not commute with either contact or the
slice-selective coin comparator.  The stream/coin norm is
`1.999998711280099`, the stream/contact norm is `0.36789306705608243`, and the
contact/coin residual is zero.  The displayed order cannot be exchanged.
Compiler substeps are not called physical time.

On the earned `t=0` one-step input domain, the stream sends the two particles
to different cells, so the subsequent Cycle-230 contact is identity.  The
nontrivial `exp(i g)` branch of `D_coarse` appears only when the unitary seam
completion is entered from `t=1` and streamed back to the colocated slice; that
reverse branch is a comparator control, not a claimed recurrent law.  The
actual next onsite volume coin would act independently at the separated cells
and generally leave this 30-column fixed seam.  That recurrent volume
interface is not constructed or claimed here.

The executable makes this scope numerical: deleting post-stream contact on
the forward `t=0` domain has residual zero, while the artificial reverse-slice
completion has residual `1.4248437218933756`.

Across every body cell at `L=3,4,5,6`, the individual stream, contact, coin,
inverse/unitarity, arbitrary coherent-state, and composed-update residuals
were zero up to a maximum floating residual of `4.440892098500626e-16` for
state normalization and `3.518561999592328e-15` for unitarity.

## Proper-cubic covariance

The pair basis carries the signed-wedge representation.  A frame maps
`e_a wedge e_b` to the sorted target pair with the exchange sign required by
the ordering reversal.  This is the CAR wedge sign, not a separately selected
column phase.

For every one of 27 `L=3` body cells under all 24 proper-cubic frames, the
runner transformed both face representatives and port tags.  All 19,440
joint column tests had:

- the exact signed-wedge phase on both slices;
- zero common-slice phase mismatch;
- zero tag-permutation failure; and
- an invariant unique reference tableau.

The twelve perpendicular and three antipodal addresses form the expected two
proper-cubic orbits.  All 576 signed-wedge group products have residual zero,
and both `wedge^2(C)` and the slice-selective comparator have covariance
residual zero.  All 27 L=3 translations, or 810 joint column tests, also pass
exactly.

## Support, overhead, and leakage

The all-anchor relative-state and matrix-unit-shell sweep at `L=3,4,5` and
held L=6 gives:

- 30, 34, 38, or 42 face M2 in the full interface union;
- twelve auxiliary port M2;
- total bounded support 42, 46, 50, or at most fifty-four M2;
- maximum representative support 16, 17, 18, or 19 M2; and
- fixed installed overhead of twenty-one M2 per cell: fifteen face plus six
  auxiliary port M2.

Every size includes all twelve perpendicular and three antipodal pairs at
every anchor.  Held `L=6` tests 216 encoders and 6,480 physical columns.  Exact
Gram, occupation, local-check, Wilson, and port-constraint leakage counts are
all zero.

The 42--54-M2 census is not the union support of the complete lattice update.
The complete stream/catch-up and contact products remain extensive products of
bounded local factors.  Cycle 305 only supplies their exact restriction to
`im(E_x)` plus the bounded fixed-seam matrix-unit comparator.

## Deletion and lawful-domain controls

The following independent deletions are detected:

- deleting catch-up leaves zero streamed states in the code;
- retaining only one stream factor leaves zero states in the code and violates
  the port constraint;
- retaining only one factor of an antipodal two-edge path never creates the
  requested opposite pair;
- deleting all three antipodal columns leaves perpendicular-sector coin
  leakage of operator norm `0.9428090415820635`;
- deleting one nonzero coin matrix-unit coefficient gives unitarity residual
  `0.4673119189904857`;
- deleting the active contact-pair phase changes the column by
  `|exp(i g)-1|=0.36789306705608243`; and
- deleting one stream-slice column gives closure residual one.

The perpendicular-only leakage is especially important: the complete
`wedge^2(C)` action genuinely uses the three antipodal columns.  Their need is
computed from the coin, not inferred from representation labels.

Lawful domain controls reject coincident, reversed, and out-of-range pair
labels; a spurious intermediate on a perpendicular pair; invalid antipodal
intermediates; out-of-range bodies; malformed or nonfinite coin matrices; and
periodic `L=2`.

## Supplied-structure inventory

Supplied are:

1. the global fixed +++ Wilson, all-`B=+1` reference vacuum;
2. one body-cell address and the six direction labels;
3. the Cycle-269 `A/B/FSWAP` dictionary and local framing repair;
4. six zero-initialized collision-safe auxiliary port M2 per cell;
5. the Cycle-219 six-mode coin `C`;
6. the Cycle-230 real contact coupling `g=0.37`;
7. the Cycle-230 one-step fixed-seam coin-then-stream-then-contact comparator
   order; and
8. one chosen antipodal path representative gauge, whose physical ray was
   proved path independent.

Derived here are the complete 15-pair/two-slice isometry, the three antipodal
rays, exact exterior-square input action, slice-selective comparator completion,
900-element matrix-unit basis, physical contact and stream restrictions,
one-step composed intertwiner, signed-wedge covariance, support, inverse,
leakage, deletion, and held-size controls.

No global Jordan-Wigner ordering, nonlocal parity service, copied tag, or
host-side direction control is used by the physical operators on the declared
code space.

## Exact boundary

This is the full two-particle logical sector at one supplied position.  It is
not a full-Fock compiler.  Absolute vacuum preparation remains open.  Coherent
position remains open, as does bounded preparation of arbitrary `E_x`
amplitudes across a volume-growing collection of body cells.  Primitive gate
synthesis remains open, along with overlapping simultaneous shells, larger
even sectors, odd parity, and the actual recurrent onsite volume coin after
the particles separate.

The result is not physical energy, a generator element is not a rate, and it
supplies no gravity/source semantics.  It makes no Record claim or Born-law
claim.  There is no no-go claim and no axiom pressure.

## Dependency-ledger effect

- `C_ref`: unchanged and explicit; the fixed +++ Wilson reference vacuum and
  body anchor remain supplied imports.
- `C_local`: narrowed to reference preparation, coherent position, primitive
  synthesis, multishell overlap, and the recurrent separated-particle volume
  interface; the one-step fixed-position two-particle seam is constructive.
- `C_int`: narrowed materially at one step; exact Cycle-230 contact shares one
  code with the full input `wedge^2(C)` comparator and stream/catch-up.
- `C_wrap`: unchanged because compiler schedule and slice order are not
  physical time.
- `C_num` and `C_source`: unchanged by this interface.

The highest-value next seam is coherence across multiple body positions or an
overlap-safe composition of simultaneous two-particle shells, while separately
seeking a native primitive synthesis of the bounded matrix-unit polynomial.

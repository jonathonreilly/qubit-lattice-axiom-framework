# Preflight Witnesses

No Block19 target runner, cache, or target mutation has been executed. These
are analytical design witnesses and falsifiers that the independent
implementations must rederive after the preregistration commit.

## Exact local dilation witness

For a fixed profile `r`, the blank input and six marked outputs are mutually
orthogonal. Equation (1) in `GOAL.md` gives

```text
K_0^dag K_0 = P_rec + (1-delta h)P_blank,
sum_f K_f^dag K_f = delta h P_blank.
```

Their sum is the identity. The Stinespring image of `|bottom>|0>` has squared
norm `(1-delta h)+delta h sum_f p_f=1` and is orthogonal to every locked
`|g>|0>`. A direct sum of two-plane rotations supplies an exact finite
unitary. This establishes an existence design only; it does not classify the
allowed function `h`.

## Generator witness

On diagonal pointer states, one collision changes a blank profile by

```text
delta sum_f h(r)p_f(r)[F(r^f)-F(r)].
```

There is no remainder in the local classical probability kernel. Products at
overlapping sites have cross terms starting at `delta^2`, so every finite
ordering has the same first-order generator. Standard finite-dimensional
product convergence must be proved in the runner from an explicit norm bound,
not cited as a label.

## Selection witness

If only positivity, boundedness, range one, translation covariance, proper
cubic covariance, QND controls, and the fixed `p_f` are imposed, multiplying
all six amplitudes at profile `r` by `sqrt(h(r))` preserves every listed
property. Cubic covariance requires only `h(gr)=h(r)`. It does not visibly
require a profile-independent constant.

The count-only controls

```text
H_0(n)=alpha,
H_1(n)=alpha(1+n/6)
```

are positive, bounded, and covariant. Their ratio is not constant. The runner
must determine whether some frozen microscopic condition omitted from this
preflight removes one member; if none does, the positive selector target
fails and the narrower lift-plus-underselection terminal becomes eligible.

## Raw-weight factorization witness

The displayed product coupling in `GOAL.md` has no profile lookup and no
normalizing denominator. Every matching-neighbor projector multiplies the
amplitude by `sqrt(2)`, hence multiplies its squared jump intensity by `2`.
The six raw intensities are proportional to `w_f=2^m_f`, and their sum is
proportional to `Z`. Conditionalizing on a jump recovers `p_f=w_f/Z`.

Inside the minimal matching-only product form, one probability doubling per
match forces the gain magnitude `sqrt(2)`. A common base amplitude supplies
only global scale. This is an anticipated positive conditional theorem.

The label-blind factor with gain `b` is the mandatory robustness attack. It is
also a fixed, table-free product of commuting range-one QND controls and is
proper-cubic invariant. It multiplies every mark intensity at a profile by
`b^(2n)`, so it cancels from `p` but not from the occurrence hazard. Unless an
additional frozen physical condition excludes it, `b!=1` defeats full-family
uniqueness while leaving the minimal matching-only theorem intact.

## Profile-census witness

Each neighbor slot is blank or one of six labels, giving `117,649` profiles.
The full proper-cubic orbit census was independently found in Block18, but it
is held out as a cross-check rather than inserted into the primary. The
classification must rotate both slots and labels. A rotation of slots alone
is a hostile mutation.

The count-only subfamily has seven positive values `H(0),...,H(6)` and hence
six independent dimensionless ratios after quotienting one global scale. The
full orbit family is expected to be much larger; exact orbit count and
projective dimension are target outputs.

## Strict-`M_2` and fresh-bath scope

The orthogonal pointer carrier makes QND label controls possible. It is an
enlarged readable Record carrier, not a proof that the six nonorthogonal
`rho_f` matrices can be perfectly distinguished and preserved as strict
one-qubit states. The Block11 no-information-without-disturbance boundary is
therefore preserved, not evaded by rhetoric.

Fresh ancillas, their vacuum preparation, and the collision scaling are
declared downstream inputs. The block asks what generator family they induce;
it does not attribute the bath, reset, or absolute cadence to the axioms.

## Principal risks

1. Generic dilation existence may be mistaken for physical selection.
2. Normalizing `p_f` may silently normalize away the target scalar `h`.
3. A profile-controlled coupling norm may be forbidden in prose but still
   present in the unitary.
4. Finite collision ordering may be mistaken for a physical scheduler.
5. QND control on orthogonal labels may be misreported as strict-`M_2` QND.
6. Fresh-ancilla reset may be hidden as autonomous dynamics.
7. One collision may be called a complete history without a scaling limit.
8. Phases irrelevant to the classical generator may be counted as distinct
   occurrence laws.
9. A common global coupling scale may be counted as physical nonuniqueness.
10. An underselection result may be broadened to all microscopic dynamics or
    used to propose an axiom amendment.

## Hard falsifiers

- missing no-jump Kraus mass or failed CP/TP completeness;
- nonorthogonal output labels called perfectly readable;
- any change to a recorded target or neighboring Record control;
- fixed direction labels that do not rotate with the profile;
- an ancilla preloaded with the realized mark;
- a hidden profile-dependent scheduler outside the displayed coupling norm;
- only one constructed `h` with no uniqueness classification;
- a raw-weight selector called robust without executing the label-blind gain;
- two `h` functions related by one global positive constant;
- a finite scan order called an absolute or framework clock;
- a product formula with an unbounded or unproved remainder;
- inheritance of Block18 infinite dynamics without exact generator equality;
- a global next-event chain on infinitely blank `Z^3`;
- a strict-`M_2`, compound-event, gravity-source, or full-TOE upgrade; or
- an axiom change inferred from the frozen collision family.

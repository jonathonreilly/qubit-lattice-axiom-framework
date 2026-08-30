# Goal

Source/Eta Block 19 executes the post-Block18 panel's `4-1` choice: one
bounded microscopic QND repeated-interaction classification. The target is not
to exhibit another possible occurrence law. It is to determine whether a
fixed local quantum collision architecture derives one Record generator ray
up to a common time scale, or whether the dimensionless hazard freedom found
in Block 18 survives inside the microscopic coupling norm.

No Block19 target runner, cache, or mutation may execute before this packet is
committed.

## Exact target contract

| field | frozen contract |
|---|---|
| Positive target | `MICROSCOPIC-QND-DILATION-DERIVES-PERMANENT-RECORD-JOINT-INTENSITY-UP-TO-GLOBAL-TIME-SCALE` |
| State carrier | At every site, an orthogonal seven-state pointer `H_R=span{|bottom>,|f>:f in D}`, `D={+-e_1,+-e_2,+-e_3}`. The classical label `f` decodes the Block18 density-matrix content `rho_f`; the enlarged orthogonal pointer is not identified with strict one-qubit `M_2(C)`. |
| Condition carrier | The six nearest-neighbor Record pointers, read only through their commuting label projectors. A recorded condition is unchanged by the interaction. |
| Mark law | The frozen Block18 kernel `p_f(R)=2^(m_f(R))/Z(R)`, where `m_f` counts neighboring label `f` and `Z=sum_g 2^(m_g)`. This is a supplied conditional law, not axiom content. |
| Microscopic family | One fresh seven-state ancilla per candidate collision, initialized in `|0>`, one vacuum-to-single-mark controlled rotation, QND neighbor controls, append-only target write, identity lock on already recorded targets, range one, translation covariance, and proper-cubic covariance. No postselection. |
| Classification variable | The squared vacuum-to-mark coupling norm `h(R)=sum_f |a_f(R)|^2` on a blank target. Relative squared amplitudes must equal `p_f(R)`. Phases may vary covariantly but do not alter the classical jump generator. |
| Selection gate | Classify every admissible `h` inside the frozen family modulo multiplying all profiles by one positive constant. One generator ray closes the positive target. Two positive, bounded, covariant nonproportional rays with a local Record-order discriminator close only the narrow underselection terminal. |
| Required dynamics bridge | Exact CP/TP collision instrument and explicit unitary extension; QND neighbor preservation; pointer orthogonality/readability; target permanence; first-order finite-volume generator; order-independent continuous-time limit; equality to the corresponding Block18 classical generator; local-infinite process inherited only after that equality is proved. |
| Forbidden imports | A profile-dependent attempt rate called a mark probability; a supplied scheduler or absolute clock called derived; nonorthogonal strict-`M_2` contents called perfectly QND-readable; a target table hidden in an ancilla; one chosen dilation presented as uniqueness; environment resets or weak-coupling scaling attributed to the minimal axioms; compound events; source/gravity claims. |
| Outcomes that do not close | Generic Stinespring existence, one CPTP instrument, CP/TP without a scaling limit, a constant-hazard construction without classification, a discrete scan order called physical time, or two couplings differing only by one global constant. |

## Local pointer instrument

For a fixed neighbor profile `r`, write

```text
w_f(r)=2^(m_f(r)),      Z(r)=sum_g w_g(r),
p_f(r)=w_f(r)/Z(r).
```

Let `0<delta<=1/h_max`, and let `h(r)>0` be a bounded coupling-norm function.
On a blank target define exact Kraus operators

```text
K_f(r,delta)=sqrt(delta h(r) p_f(r)) |f><bottom|,
K_0(r,delta)=P_rec + sqrt(1-delta h(r)) |bottom><bottom|,
P_rec=sum_f |f><f|.                                      (1)
```

They obey

```text
K_0^dagger K_0 + sum_f K_f^dagger K_f = I.              (2)
```

The neighbor profile enters through mutually orthogonal commuting control
projectors, so (1) combines into one controlled instrument. Already recorded
targets are fixed by `K_0` and annihilated by every `K_f`. Neighbor controls
are not changed. The six written targets are orthogonal and perfectly
readable.

An explicit Stinespring isometry sends

```text
|bottom>|0> -> sqrt(1-delta h(r)) |bottom>|0>
               + sum_f sqrt(delta h(r)p_f(r)) |f>|f>,
|g>|0>      -> |g>|0>.
```

The two displayed subspaces have equal finite dimension and the isometry must
be extended by explicit profile-controlled two-plane rotations to a unitary,
not merely cited as generic Stinespring existence. The runner may represent
the square roots by exact radicands; every norm and orthogonality identity must
be exact.

The one-collision classical kernel is

```text
P(r:bottom -> f)=delta h(r)p_f(r),
P(r:bottom -> bottom)=1-delta h(r).                       (3)
```

Thus its local first-order generator has joint intensity

```text
q_f(r)=h(r)p_f(r),       lambda(r)=sum_f q_f(r)=h(r).      (4)
```

The mark completeness relation fixes the relative amplitudes. Whether the
declared microscopic constraints also fix `h(r)` is the target question.

## Table-free factorized pincer

The full classification is attacked from a smaller positive family rather
than only by arbitrary profile controls. Let `P_(y,f)` be the orthogonal
projector that says neighbor `y` carries label `f`, and define the raw
vacuum-to-mark coupling

```text
J_(x,f) = g |f><bottom|_x
            product_(y nearest x) [I+(sqrt(2)-1)P_(y,f)]. (5)
```

The neighbor factors commute. On a profile with `m_f` matching neighbors,
the amplitude is `g(sqrt(2))^(m_f)`, so

```text
q_f(r)=|g|^2 2^(m_f(r)),
h_raw(r)=|g|^2 Z(r),
q_f/h_raw=p_f.                                             (6)
```

This is a table-free microscopic lift of the Block18 kernel: the denominator
`Z` appears only when conditioning on the occurrence of some mark. Within the
frozen **minimal matching-gain subfamily**—one common base coupling, one
identical factor per matching neighbor, no label-blind occupancy factor, and
no additional common profile gate—the probability ratio `2` fixes the gain
magnitude to `sqrt(2)`, and (6) is unique modulo `|g|^2` and irrelevant
covariant phases. The runner must prove this classification rather than print
the formula.

That conditional positive selector is not allowed to masquerade as robustness.
The same frozen block must test the nearest symmetry-allowed extension

```text
J_(x,f)^(b) = J_(x,f)
              product_(y nearest x)
                [I+(b-1)P_y^recorded],                   (7)
```

where `b>0` is common to all labels and
`P_y^recorded=sum_g P_(y,g)`. It leaves `p_f` unchanged but gives

```text
h_b(r)=|g|^2 b^(2n(r)) Z(r).                              (8)
```

If (7) obeys the same full-family locality, covariance, QND, carrier, ancilla,
and scaling premises, then the minimal result is only a conditional
subtheorem: symmetry and QND consistency do not forbid a dimensionless
label-blind gain. The primary and independent checker must report both the
minimal factorized classification and the robustness verdict.

## Finite-volume and continuous-time bridge

On a finite torus, couple one fresh ancilla to each site. The simultaneous
finite-volume unitary or any product ordering of the local collision maps may
differ at order `delta^2` because neighboring candidate maps overlap. The
runner must prove that every declared ordering has the same first-order map

```text
T_delta = I + delta sum_x L_x + O(delta^2),               (9)
```

with a volume-local bound, and that `(T_(t/N))^N` converges on the diagonal
pointer algebra to the continuous-time pure-Record semigroup generated by
(4). A finite scan order is a regulator, not a physical scheduler. The limit
must be translation/proper-cubic covariant.

Once (4) is derived exactly, the finite-history and local-infinite Harris
existence theorem of Block 18 may be inherited for the two executed bounded
hazards by exact generator identity. This block must not claim a global next
event on `Z^3`, a common finite completion time, or an absolute clock.

## Uniqueness classification

Let the proper cubic group act simultaneously on the six neighbor slots and
six Record labels. The frozen family permits a positive bounded control norm
`h(r)` precisely when it is constant on the resulting profile orbits. The
primary must derive the orbit count rather than quote Block18. It must then
classify:

1. the full orbit-invariant family;
2. the smaller count-only family `h(r)=H(n(r))`, `n=0,...,6`; and
3. the quotient of each family by one common positive scale.

The anticipated hostile witness pair, to be rederived rather than assumed,
is

```text
h_0(r)=alpha,
h_1(r)=alpha(1+n(r)/6).                                  (10)
```

If both are realized by the same carrier, ancilla type, QND rule, event arity,
scaling, and initial-law contract, their `n=0` versus `n=6` Record-order odds
must be recomputed. A nonconstant ratio proves that QND dilation existence did
not select the coupling norm. The permitted terminal is then only

```text
QND-REPEATED-INTERACTION-LIFTS-EXIST-HAZARD-NORM-UNDERSELECTED.
```

This statement is restricted to the frozen orthogonal-pointer collision
family. It does not rule out an action-selected coupling, an autonomous bath,
a strict-`M_2` construction, a compound instrument, or another microscopic
architecture, and it cannot authorize an axiom edit.

## Relation to the direction/corner law

Block 09's phrase “directions compare qubits; cells weigh corners” supplies a
positive normalized fourteen-outcome conditional law and Block 10 supplies a
joint condition carrier. Those results materially help with relative mark
probabilities. They do not fix the scalar `h=sum_f q_f` in (4), and Block 11
shows that unchanged perfect readout of noncommuting strict-`M_2` inputs is a
separate microscopic obstacle. Block19 therefore uses orthogonal Record
pointers and tests only the occurrence-norm selection seam. It does not replay
the Block09/10 probability construction or broaden their strict-`M_2` scope.

## Required test battery

The primary runner must:

1. generate the six directions and `24` proper cubic rotations;
2. exhaust all `7^6` ordered profiles, derive kernel normalization and
   covariance, and independently compute the profile-orbit census;
3. construct (1)--(3) exactly for every profile and both hostile hazards;
4. verify CP/TP, explicit isometry/unitary-block completion, orthogonal
   readability, neighbor QND preservation, target append, and locked-sector
   identity;
5. derive (4), including the no-jump coefficient, without inserting the
   expected generator as a test oracle;
6. prove the finite-volume first-order product formula and continuous-time
   diagonal-sector convergence, with schedule differences only at
   `O(delta^2)`;
7. classify full orbit-invariant and count-only coupling norms modulo global
   scaling;
8. derive the raw-weight product coupling (5), prove its uniqueness inside the
   minimal matching-gain subfamily, and execute the label-blind extension (7);
9. reconstruct the local `1/2` versus `2/3` Record-order discriminator if two
   nonproportional lifts survive;
10. bind the exact Block18 generator/Harris inheritance and repeat its local,
   not global, scope;
11. reject hostile mutations and print substantive `per_element:`,
    `per_site:`, `per_mode:`, `per_block:`, and `lattice_wide:` lines, ending
    in `TOTAL: PASS=n FAIL=n` with stdout below `6000` bytes.

The independent checker must reconstruct the classification without importing
the primary. A negative/underselection terminal additionally requires the
full N1--N8 No-Go Discipline sidecar.

## Stop rule

Run this one frozen collision family to a result without widening its carrier,
ancilla, support, or premise set mid-block.

- One generator ray modulo scale in the full frozen family: ship the positive
  selector terminal. Uniqueness only after forbidding (7) earns a conditional
  minimal-factorized subtheorem, not full selection.
- Two dimensionlessly inequivalent admissible lifts: ship only the narrow
  hazard-norm underselection terminal and pivot to the action/transfer
  uniqueness audit.
- Failure of CP/TP, QND permanence, locality, or the controlled limit: stop at
  the first exact construction gate; do not infer microscopic impossibility.

No outcome changes formal TOE percentages, audit status, or axiom text in this
author-side block.

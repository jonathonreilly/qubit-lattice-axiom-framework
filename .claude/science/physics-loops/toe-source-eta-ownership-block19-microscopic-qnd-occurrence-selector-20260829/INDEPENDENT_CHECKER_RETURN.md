# Independent Checker Return

## Disposition

The strengthened independent checker completed with:

```text
TOTAL: PASS=63 FAIL=0
```

It independently reconstructs the corrected Block19 relation-factor
collision family and supports the following bounded result only:

> Within the frozen orthogonal-pointer, fresh-ancilla, range-one
> relation-factor grammar, the supplied conditional kernel forces
> `kappa=(a/b)^2=2`, while `beta=b^2` remains a dimensionless coordinate of
> the induced diagonal pure-Record generator modulo one common positive rate
> scale.

The matching-only `beta=1` member remains a positive realization of the
supplied conditional kernel. The surviving `beta` coordinate prevents a
one-ray classification of the complete corrected pair-factor grammar under
the stated equivalence relation.

## Independence statement

The checker was constructed and executed without opening, importing, or
executing the Block19 primary runner. Its profile group, rotations, orbit
census, relation-factor coefficients, collision algebra, weak generator,
classification, races, bounds, and limits were reconstructed in the
independent source rather than copied from another implementation. Anticipated
orbit counts, race fractions, and rate bounds were not used as comparison
oracles:

- signed coordinate axes are generated from the spatial dimension;
- the proper-cubic group is generated from signed permutations with positive
  determinant and checked for identity, closure, and inverses;
- Burnside fixed-point counting and direct canonical-orbit enumeration are
  independent cross-checks;
- race fractions are calculated from independently constructed profiles and
  exact `Fraction` hazards;
- hazard extrema are calculated once over all ordered profiles and again over
  independently generated count vectors; and
- exact CP/TP is checked over every profile by rational normalization and the
  formal `sin^2(theta)=1-cos^2(theta)` identity. Floating-point trigonometry is
  retained only as a regression.

At the start of the work, the worktree was verified at correction commit
`809a64b74d7e61e81829d7696f3d9a1394afa554`. During execution, the shared
worktree HEAD moved externally to `97b0b6d14f7ce45a7ea520142953e3e5f657b361`
and an untracked primary-named runner appeared. That file was not opened,
hashed, imported, or executed. The checker resolves all scientific support by
explicit Git object reads from the correction commit, so the external HEAD
movement does not enter its evidence.

## Source and provenance hashes

Independent checker:

- path:
  `scripts/independent_admissibility_d4_pair_factor_qnd_occurrence_selector_2026_08_29.py`
- Git blob:
  `4ad0b583920260c2ff9a167a7547fb367338111d`
- SHA-256:
  `94bf5a898ede4c3e0b79768cf107e39acd4cd838e7b606f7b8ba8dddc4644008`

Correction provenance:

- correction commit:
  `809a64b74d7e61e81829d7696f3d9a1394afa554`
- declared and actual single parent:
  `3d35ec50807305c682abee677e799359cb262830`
- corrected six-file support-manifest SHA-256:
  `ca825aa1f3cd2574630bf468bb201f05b07712a3f69cf82b743825018d5b927b`

The support manifest covers `APPROACH_REGISTRY.md`, `GOAL.md`,
`INDEPENDENT_PREREG_ATTACK.md`, `PANEL_RETURN.md`,
`PREFLIGHT_SUPPORT_CORRECTION.md`, and `PREFLIGHT_WITNESSES.md` at the
correction commit. The manifest digest is formed from each path, Git blob,
content SHA-256, and byte length.

Block18 parent-commit anchors:

| anchor | Git blob |
|---|---|
| claim-status certificate | `f25a9c59eef1c4c7ebc7d6e88f918b130332b402` |
| source runner | `52510c844be2bb8fdd6f31e5680b772cf90335e9` |
| independent source runner | `33c368171daeb2871c3c0b1be55d502ce2471eb1` |
| source cache | `0105bfc6cd2af8e8e80c85a305c0228764c1ace1` |
| independent cache | `ed08d6d8275460bcd6106a9bd010ae76b5711652` |

Their combined manifest SHA-256 is
`9337503f11c6e6356250c9827c0bbeb73308cb7e7dd6277a44b1767c11bd4108`.
These anchors establish provenance and method availability only; no Block18
runner output was imported as a Block19 numerical oracle.

## Checker defects found and corrected before the final run

The first complete execution honestly returned `PASS=54 FAIL=2`. Both
failures were defects in the independent checker, not discrepancies in the
corrected physics contract:

1. The first label-only hostile test expected a rate-covariance failure.
   Because the count-based rate formula has an accidental independent label
   relabeling symmetry, that expectation was false. The corrected test rejects
   label-only motion because it differs from the stipulated simultaneous
   geometric action on slots and labels; it does not claim a nonexistent rate
   asymmetry.
2. The first ordered-product test compared a sweep remainder divided by
   `delta` with an unrelated telescoping-bound scale. It was replaced by the
   correct mesh test: the uniform remainder divided by `delta` decreases under
   successive halving, while direct alternating-order two-site sweeps converge
   to an independently uniformized continuous-time semigroup.

Before the final run, the checker was also strengthened as follows:

- a literal direction tuple was replaced by generated signed coordinate axes;
- exact rational/formal Kraus completeness was added over every profile;
- fresh-vacuum target lock and the nonvacuum reverse channel were tested in
  the explicit 49-dimensional target-ancilla space;
- finite generators were tested for conservation, append-only transitions,
  and permanence;
- growing finite-volume lower rate sums were used to reject a global
  next-event chain on infinitely blank data; and
- provenance-role declarations were replaced by correction-commit and
  Block18 Git-object checks with source-manifest hashes.

The strengthened rerun produced `PASS=63 FAIL=0`.

## Exact stdout

```text
BLOCK19 independent relation-factor QND collision certificate
group: PASS rotations=24 profiles=117649 orbits=5075 burnside_sum=121800
orbit_sizes: PASS 1:3,3:6,4:4,6:34,8:21,12:244,24:4763 outer_projective_dim=5074 count_projective_dim=6
collision: PASS star_rank=2 spectrum=(+sqrt(h),-sqrt(h),0x5) cp_error=2.22e-16
weak_generator: PASS max_rate_errors_delta,half=(5.503e+01,2.797e+01) sine_remainder_ratio<=0.333318
classification: PASS kappa=2 beta_dimension=1 modulo_global_g2
same_Z_race: PASS n=(2,3) Z=(9,9) beta=1->1/2,beta=2->2/3
hostile_old_fixture: PASS odds=beta=1->2/3,beta=2->128/129
order_mutation: PASS leading_coefficients=beta=1:+0.166666666667,beta=1/2:-0.416666666667 first_order=0
ordered_limit: PASS varying_sweeps_to_exp errors_at_N128=beta=1:3.747e-04,beta=2:5.396e-04
local_Harris: PASS h_over_alpha=[1,736] clan_coefficient_over_alpha=5152 tail_m=35 tail=4.54e-11
hostile_mutations: PASS linear_delta,nonvacuum_lock,complete_state_QND,slot_only,label_only,beta_clock,old_fixture,first_order_order,global_next_event
per_element: PASS profiles=117649 marks=6 exact_channel/kernel/covariance checked
per_site: PASS blank write/no-write, recorded lock, pointer-projector QND, range-one append-only generator checked
per_mode: PASS marks=6 profile_orbits=5075 pair-factor_beta_dimension=1 outer_control_demoted
per_block: PASS finite_sites=27 arbitrary-permutation remainder and varying-order weak limit checked
lattice_wide: PASS local classical Harris construction only; proposal=736 backward_clan_tail finite; no global next-event or quantum-unitary claim
provenance_objects: PASS correction=809a64b74d7e parent=3d35ec508073 support_sha256=ca825aa1f3cd2574 block18_sha256=9337503f11c6e635 block18_blobs=claim:f25a9c59eef1,source:52510c844be2,independent_source:33c368171dae,cache:0105bfc6cd2a,independent_cache:ed08d6d82754
provenance: PASS Block02=writer-precedent-only Block11=strict-M2-boundary-preserved Block18=pure-Record/Harris-method-only; bath/reset/scaling/cadence imported
scope: PASS orthogonal-pointer fresh-ancilla range-one diagonal-generator classification only; no clock/action/gravity/axiom/audit/TOE upgrade
TOTAL: PASS=63 FAIL=0
```

The executed stdout is below 6,000 bytes and contains substantive
`per_element:`, `per_site:`, `per_mode:`, `per_block:`, and `lattice_wide:`
resolution lines.

## Scope and non-upgrades

The independent result licenses only:

1. an exact local fresh-vacuum QND collision realizing the supplied
   conditional mark kernel;
2. the first-order diagonal pure-Record generator and its finite-volume
   arbitrary-order weak limit;
3. finite and local-infinite classical process membership for the executed
   pair under the imported fresh-ancilla protocol; and
4. a one-dimensional `beta` underselection statement inside the corrected
   positive-real pair-factor grammar modulo one global rate scale.

It does not establish or change any of the following:

- derivation of the supplied factor-of-two conditional kernel;
- uniqueness or nonuniqueness of the full coherent quantum instrument;
- complete-state neighbor identity or an ancilla-independent Hamiltonian
  target lock;
- a strict `M_2(C)` encoder or nondemolition readout;
- autonomous-bath dynamics, a reusable environment, or a physical clock;
- compound-event, correlated, non-Markov, action, or transfer selection;
- a global infinite-lattice collision unitary, global next-event chain, or
  common finite completion time;
- a gravity source or gravity-dynamics closure; or
- any axiom, audit status, obligation, governance, or TOE-percentage change.

The seven-state orthogonal pointer, single-target event arity, fresh vacuum
ancillas, reset/disposal, collision cadence, and weak scaling remain explicit
family imports. Block02 supplies a writer precedent only; Block11's strict
`M_2(C)` boundary remains intact; Block18 supplies the pure-Record target and
Harris method only.

Finally, this independent return is evidence for the corrected classification,
not by itself the release artifact for a negative terminal. Under the current
No-Go Discipline, any shipped underselection claim still requires an N1--N8
checklist landing in the PR and the primary runner's substantive five-line N5
execution certificate landing in its cached stdout.

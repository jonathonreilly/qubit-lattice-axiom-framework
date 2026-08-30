# Independent Checker Return

## Evidence binding

The corrected frozen execution packet is commit `5dd5f77522`. The following
SHA-256 values were recomputed from the files in the shared worktree after both
caches were frozen:

| role | artifact | SHA-256 |
|---|---|---|
| primary runner | `scripts/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py` | `c1f7e00b8f42111d677fc5e53ced6f6a25a4871325671270f3984670d5f7b799` |
| primary cache | `logs/runner-cache/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt` | `31653b583ee0cc3c6b3aabccacbddd59227627a692932e4161f23bf09c04ca44` |
| independent runner | `scripts/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py` | `de91d8a726d44bd16536753d8fe7789eec1ac87915f4c3d3de40b926964e8d8f` |
| independent cache | `logs/runner-cache/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt` | `2f2120b0106bac4123f69daad63915df4c1bc494a6739c41acfa79a66e854265` |

Each cache records the same runner hash shown above, `exit_code: 0`, empty
stderr, and `status: ok`. The primary reports `TOTAL: PASS=12 FAIL=0`; the
independent checker reports `TOTAL: PASS=17 FAIL=0`. Both reject all `18/18`
named hostile mutations and return exactly

```text
PURE-RECORD-HARRIS-PROCESSES-EXIST-DIMENSIONLESS-GENERATOR-UNDERSELECTED
```

The independent runner was reconstructed without importing or inspecting the
primary source. This packaging comparison used the two frozen stdout caches
and recomputed artifact hashes; it did not use primary implementation details
to revise the independent result.

## Exact agreement

| gate | primary result | independent result | comparison |
|---|---|---|---|
| proper-cubic data | `6` signed directions and `24` determinant-`+1` rotations | `6` directions and `24` rotations | exact agreement |
| supported Record states | spectra `113/512,399/512` | spectra `113/512,399/512`, determinant `45087/262144` | exact agreement; independent adds the determinant |
| mark-kernel census | `117649` profiles under all `24` rotations | `117649` profiles, `2823576` profile/rotation pairs | exact agreement |
| mark law | blank probabilities all `1/6`; one matching neighbor gives `2/7` versus five `1/7` entries | full exact normalization/covariance census; the seed rows recover `1/6` and `2/7` | exact agreement |
| finite process | conservative exact `Lambda_3` rows, permanence, absorption, jump cap `27` | same properties and cap `27` | exact agreement |
| ordered histories | conservative pure-birth DAG normalization | same normalization, `5/5` invalid histories rejected, sample density `125/74088 exp(-961/42)` | exact agreement; independent adds a rational fixture |
| dimensionless discriminator | finite and local Record-order odds `1/2,2/3` | finite and local Record-order odds `1/2,2/3`; initial local-set rates `8 alpha,9 alpha` | exact agreement; no absolute clock is used |
| formation/covariance | positive baseline, equivariance, local Harris construction | `P(blank at t)<=exp(-alpha t)`, asymmetric-initial-law control, equivariant local sample map | exact agreement |
| event arity | all six directions give bounded one-site order `3` and sole compound order `1` | six explicit direction rows give orders `(3,1)` | exact agreement |
| corrected support | `L>=6` row pairs `(1/6,2/7)` and `(1/6,1/3)`; `L=3,4,5` wraps reproduced | the same six `L=6` rows and exact small-torus controls | exact agreement |
| lumpability scope | unequal future-cell rows; compensation and constant/coarser quotient exits retained | unequal single-entry rows; compensating-target falsifier retained | exact agreement |
| periodic incidence | all-`L>=3` rank theorem; regressions `26,63,124` | same theorem and regressions `26,63,124` | exact agreement |
| source/debit | one/three birth totals with debits `-1,-3` | birth totals `(1,3)` and debits `(-1,-3)` | exact agreement |
| rhetoric certificate | five substantive N5 lines, with physical modes absent | five substantive lines; `per_mode` honestly says checked and not executed | exact semantic agreement |

## Independent differences that do not alter the terminal

- The primary uses one shared-field Harris regression with a `22`-site,
  radius-`2` clan. The independent checker extends both time and volume axes:
  its two rational-time queries have clans `(38, radius 2)` and
  `(170, radius 4)`, process `148896` finite marked points, and stabilize the
  fixed/periodic cylinders by even volumes `L=10` and `L=14`.
- Both use `14 alpha T=1` and the same factorial-tail argument at
  `m=4,8,12`. The primary observation set has size `2`, producing bounds
  `5/48,1/17920,13/2874009600`; the independent observation set has size `3`,
  producing exactly `3/2` times those bounds:
  `5/32,3/35840,13/1916006400`. This is the required `|A|` multiplicity, not
  a disagreement.
- The independent census additionally resolves `5075` proper-cubic profile
  orbits, orbit-size distribution
  `{1:3,3:6,4:4,6:34,8:21,12:244,24:4763}`, `923` distinct probability rows,
  and `721` uniform profiles. The primary does not print those auxiliary
  counts.
- The primary prints an auxiliary compound fixture with sole-direct
  coefficient `5/42` and general direct-sum control `5/28`. The independent
  checker uses a different positive compound coefficient internally and
  certifies the same terminal-bearing rule: the linear coefficient equals the
  sum of every direct entry, while the `kappa/6` formula requires a sole
  direct transition. The arbitrary fixture values need not coincide.
- The primary groups its proof into `12` gates; the independent checker prints
  `17` gates because each of the six seed directions is a separate row. Pass
  counts therefore are not compared as if they were scientific observables.

No terminal-bearing discrepancy remains.

## Bounded return

The jointly supported result is only:

> Within the invariant seven-state, six-mark sector, conditional on the
> supplied conditional mark kernel and the declared bounded local one-site
> Markov/process ansatz, two complete finite/local-infinite processes obey the
> same premises but have different local first-Record order probabilities,
> `1/2` and `2/3`. They are therefore inequivalent modulo one common positive
> rescaling, so this premise set underselects these two hazard laws.

This is an existence-plus-underselection theorem inside the frozen model
sector. It is not a no-occurrence theorem, a claim about every lawful process,
or a physical selection result.

The following exits remain explicitly live:

- a microscopic QND repeated-interaction dilation that derives a unique
  occurrence law;
- an action, detailed-balance, DLR, OS-reconstruction, or other proved
  same-premise selector;
- the common full-`M_2(C)` extension and arbitrary full-domain initial laws;
- compound, correlated, non-Markov, or other event-arity laws, including the
  Block16 three-Record atom;
- a different successfully lumpable process or quotient, including maps that
  discard or compensate the tested future cell; and
- an explicit gravity-source decoder using a local reservoir incidence,
  source/debit, open flux, neutral pair, signed content, or worldline
  transition.

The local Harris result supplies no global next-event chain, global
nonexplosion claim, or common finite completion time. The incidence result is
only about raw cumulative Record occupancy on a connected periodic carrier;
it is not a gravity no-go. No axiom update, audit verdict, formal TOE
obligation retirement, or TOE-percentage movement follows from this return.

The sibling `NO_GO_DISCIPLINE_CHECKLIST.md` remains the controlling N1--N8
release artifact; this independent return does not substitute for its final
post-execution status or for independent audit.

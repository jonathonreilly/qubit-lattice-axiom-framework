# Source-exposed carrier-interface check

Date: 2026-11-09. Scope: complete research source check, after the independent derivation was frozen. This is neither an audit nor a formal landing review, and it supplies no retained status.

## Exact sources and actual review mode

The following two files were read completely with numbered lines, without truncated output, from `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/carrier_interface/`:

| Source | Complete coverage | SHA256 |
|---|---|---|
| `RESULT.md` | Lines 1–355 | `ad12e660846dc8d1ccfa679f9842a7a37a8af1935293dd81cbafa6ac8a65901e` |
| `ASSUMPTIONS.md` | Lines 1–41 | `9e06e542c393f386680c3f28d3929265c83aa74d1ee1507cea176b93ec173bc5` |

Source checkout HEAD: `95a40545b05ba3039a83819cf41158d049e2596a`; pinned `origin/main`: `bf92a1d763030836ed55631d5d7a7ef3b288f284`. The five governing source files named in `CHECKPOINT.md` were rehashed and remain unchanged, including the axiom memo SHA256 `301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`. Their prior complete readings were reused.

Actual mode: source-exposed hand verification of every argument in these two files, against the previously derived checks and fresh adversarial examples. No numerical job, test runner, Lean check, implementation execution, extra agent, or external source was used. Runtime model/effort and cross-family separation remain unattested. This check is not a new independent derivation and does not alter the original independence claim. The referenced original proof, search artifacts, and negative-claim checklist were not read. Their preservation, search history, and citation attribution are not authenticated here; the mathematics used in the reviewed source is self-contained.

The original files remain frozen:

- `INDEPENDENT.md`: `9ae83aa0dcc5b9fd4cf926526f2201ce0b72a56c1533eb0e341f3122ae8fb7a5`.
- `CHECKPOINT.md`: `e1af91795b530263420b4483a43875f6d25d0dbac80359cb3efaa61d3752f54f`.

Only this `SOURCE_CHECK.md` is written by this task. No source correction, prompt edit, commit, push, or audit action is performed.

## Findings requiring a bounded source correction

### F1. The displayed POVM trace sum need not equal the Hilbert dimension

`RESULT.md:281–285` supposes a density-matrix representation of the `K` copied inputs. The inequality `1=tr(rho_a E_a)<=tr(E_a)` is correct: `I-rho_a` is positive, and `tr((I-rho_a)E_a)=tr(E_a^(1/2)(I-rho_a)E_a^(1/2))>=0`. Commutation is not required.

However, the subsequent displayed equality `sum_a tr(E_a)=d` is not established if the POVM retains all `M` fine labels with `M>K`. The sum runs over the `K` copied-symbol effects, which are only a subset of the POVM elements. Those effects sum to at most the identity.

Exact counterexample to the displayed equality: choose `K=2`, `M=d=3`, states `rho_0=|0><0|`, `rho_1=|1><1|`, and the three-outcome basis POVM `E_b=|b><b|`. Every required copied probability is `tr(rho_a E_b)=delta_(a,b)`, including zero probabilities for the unused third outcome, yet `sum_(a=0)^1 tr(E_a)=2`, whereas `d=3`.

The corrected line is

`K <= sum_(a=0)^(K-1) tr(E_a) <= d`.

Alternatively the source could explicitly define a `K`-outcome coarse-grained POVM, but the inequality handles the general statement directly. The conclusion `d>=K` is valid and unchanged. This is a proof-line correction, not a failure of the capacity comparison, a new physical premise, or an obstruction to quantum sectors generally.

### F2. “No extra visible records” must be relative to the selected target pattern

`RESULT.md:174–181` first lists the six mandatory detector seed records and an unqualified requirement of “no extra visible records,” then gives the fine pattern as the seed and the coarse pattern as the seed plus the fine record. The later cases make the intended rule clear, but the initial requirement can be read as a stage-independent exclusion of every record beyond the six seeds.

Under that literal implementation, the coarse center at `R1` fails the global no-extra-records test precisely because its required fine predecessor is visible, so the second birth never becomes enabled. That reading conflicts with the explicit coarse case and the termination proof.

Make equality with the complete target-specific pattern explicit: the fine content branch requires exactly the six seed records; the coarse branch requires exactly those six records plus the prescribed fine record; no other visible records are allowed in the corresponding branch. Header/frame/valid-value checks precede this choice, and every unmatched case falls back. This is the reading used in the independent derivation and in the remainder of the source. The correction removes a formal-definition ambiguity without changing the intended law or adding an assumption.

## Complete argument check

| Source region | Checked content and disposition |
|---|---|
| `RESULT.md:11–50` | The common-history-kernel condition is stronger than label omission. Integrating the common apparatus law and successive source-independent kernels gives the required history channel. Fixed context includes placement/orientation. Continuous variables use kernel integration. Adaptive controls and failures are covered only under the stated common-kernel premises. No joint dynamics is attributed to Admissibility alone. Valid. |
| `RESULT.md:52–105` | Total probability gives effects in `[0,1]^C`, complement/event addition, affine responses, and equality of observable histories for equal complete carrier laws. The signed-difference proof gives total-variation contraction and the equal-prior guessing bound; an available positive-support indicator attains it. The perfect-discrimination statement is about the two laws under discussion, not an unrestricted multi-preparation joint measurement. The restricted-effect and preparation-mixture qualifications are sound. The postselection example has TV `1/2`, complete-trial optimum `3/4`, and acceptance probability `1/2` under both sources. Valid. |
| `RESULT.md:107–133` | The apparatus XOR counterexample has equal carrier/apparatus marginals and different conditional apparatus laws. The restricted single-bit example has identical individual-bit statistics and is separated by parity or a joint read. Its single-test restriction is explicit and is not assigned to the native detector. The relay and clock warnings identify missing hypotheses, rather than inferring isolation from distance. Valid. |
| `RESULT.md:135–173` | Program base decoding is bijective, including zero digits. `Q>=2^K>=K` and `Q>=M`, so every carrier and output scalar belongs to the stated finite alphabet. Negative headers and labels are distinct from data. The eight detector coordinates have L1 diameter at most five; the external label is at least seventeen away. Spatial copies and the supplied readout code are explicit. Valid. |
| `RESULT.md:174–204` | Subject to F2's target-specific pattern clarification, the content kernel depends only on the punctured neighborhood and occupancy suppresses only the rate. Unique typed headers fix one frame, so only its two output coordinates can ever be enabled over all of `Z^3`. Exactly one rate-one birth is enabled at each of the first two prefixes, and none at the last. Independent exponential waits give almost-sure completion and mean two. The claim is limited to the prepared-prefix domain; no arbitrary-environment robustness is inferred. Valid under the clarified definition. |
| `RESULT.md:206–223` | Every old seed record leaves a mandatory hole at its own center. The occupied fine site sees its seed at `R1` and an extra coarse record at `R2`, hence the stated deterministic/fallback support cases. The occupied coarse site sees its seed plus fine predecessor. The label sees no other record. In fallback, `0<=l<=k` gives `0<p<1`, and every code atom has mass at least `1/(2|A_code|)`. Recorded zero remains present. Fixed context and no relay birth give the claimed label-independent detector law conditional on the carrier. Valid. |
| `RESULT.md:225–260` | Fine/coarse output-only equivalence is correctly separated from reading the retained input carrier. No timestamp readout is supplied. The exact `g`-fiber TV formula and its no-opposite-sign cancellation condition are correct, including zero differences and constant programs. A common independent timing factor changes no TV. Every subset indicator uses only labels zero and one, hence is available for every fixed `M>=2`. The two-symbol testing calculations are correct. Valid. |
| `RESULT.md:262–294` | Copying uses `T>=K`, available point preparations, and `M>=K`; arbitrary fixed menus are not silently enlarged. The law parameters vary with `K`, while the layout remains fixed. The paired-label example has `K` copied carrier states and indistinguishable label pairs, so the carrier is not merely the external label renamed. The optional density/POVM test is separate from native dynamics and uses a fixed apparatus. Its dimension conclusion is valid after F1's trace inequality correction. |
| `RESULT.md:296–327` | The full simplex uses the already chosen point preparations plus the optional mixture protocol. Random subset weights are nonnegative, normalize by product expansion, and give marginal inclusion probability `e(a)`. Random-map weights similarly realize each normalized menu with at most the fixed `M` fine labels. A three-outcome refinement of `e,f,1-e-f` needs the stated `M>=3`; `M>=max(K,3)` permits it and copying under one fixed rule. The program record is retained, so equality of selected coarse responses is not promoted to equality of full histories. Valid. |
| `RESULT.md:329–355` | The conclusions remain bounded and conditional; no global classicality, physical quantum impossibility, Bell result, continuum result, or new axiom is claimed. The finite TV argument is proved in the source rather than imported from the cited literature. Citation/search provenance itself was not independently checked. |
| `ASSUMPTIONS.md:1–41` | The ledger correctly separates governing structure, initial conditions, detector code, dynamics, isolation/readout scope, optional mixtures, and the quantum comparison. The full-simplex statement is read with the explicit selected point-preparation menu in `RESULT.md:262–299`; it is not asserted for an arbitrary previously fixed menu. The fixed-`M` refinement limits and absence of timing readout are explicit. No additional load-bearing scientific premise appears here. |

## Source-check result

The substantive mathematical conclusions agree with the frozen independent derivation. The checked revision has one incorrect displayed equality and one target-pattern ambiguity, as recorded above. Both admit the narrow corrections specified; neither changes the stated conditional capacity result or requires an axiom change. No other mathematical error or hidden physical identification was found in the two files under this complete source-exposed review.

This report concerns only the exact hashes above. A corrected source requires a separately identified delta check; this report does not silently certify a moving replacement. The supervisor owns integration and any later formal review.

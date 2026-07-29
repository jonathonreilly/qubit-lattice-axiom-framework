# Cycle-317 Born-forcing surface input contracts (Cycle-729 grounding)

This is a bounded extraction from exactly:

- `scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py`
  (abbreviated **R** below); and
- `docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md`
  (abbreviated **N** below).

No Cycle-719, Cycle-722, Cycle-725, or Cycle-729 file was read. References to their requested style or conclusion below come only from the task statement. “Public” means a module-level name without a leading underscore; the runner defines no `__all__` and does not declare a stable library API.

## 1. Runner surface

### 1.1 Public constants and state

| name | source | exact value/type and shape | role / external status |
|---|---:|---|---|
| `ROOT` | R29 | `pathlib.Path`, `Path(__file__).resolve().parents[1]` | Internally derived repository root. |
| `NOTE` | R35–38 | `pathlib.Path`, the Cycle-317 note below `ROOT` | Frozen note target; not a parameter. |
| `TOL` | R39 | `float`, `5.0e-11` | Frozen executable tolerance. |
| `POINTER_DIMENSION` | R40 | `int`, `8` | Frozen maximum number of fine labels and logical pointer dimension. |
| `POINTER_M2` | R41 | `int`, `3` | Frozen three-bit/M2 pointer capacity, since `2^3=8`. |
| `PASS` | R42 | mutable `int`, initially `0` | Certificate counter, reset by `main`; not science input. |
| `FAIL` | R43 | mutable `int`, initially `0` | Certificate counter, reset by `main`; not science input. |
| `I2` | R45 | complex `np.ndarray`, shape `(2,2)`, identity | Frozen seam-qubit basis operator. |
| `X` | R46 | complex `np.ndarray`, shape `(2,2)`, Pauli X | Frozen seam-qubit basis operator. |
| `Y` | R47 | complex `np.ndarray`, shape `(2,2)`, Pauli Y | Frozen seam-qubit basis operator. |
| `Z` | R48 | complex `np.ndarray`, shape `(2,2)`, Pauli Z | Frozen seam-qubit basis operator. |

`PASS` and `FAIL` are uppercase module state, not immutable constants.

### 1.2 Public record type

`@dataclass(frozen=True) class PhysicalFixture` is declared at R126–138 with this exact field contract:

```python
length: int
code: object
encoder: object
basis_rows: tuple
occurrence: dict
exchange: np.ndarray
full_encoding: np.ndarray
two_ray_encoding: np.ndarray
contact: np.ndarray
physical_contact: np.ndarray
constraint: np.ndarray
```

For runner-created certificate fixtures, `two_ray_encoding` is `(510,2)` and `contact` is `(2,2)`: the former follows from R154 and the explicit 510-row checks at R195, and the latter from its use throughout the two-ray algebra. `full_encoding` is 510-row and the note calls it a rank-127 seam closure (N121–138). `physical_contact` and `constraint` must act on those 510 rows. The allowed sources do not state a separate exact shape for `exchange`, nor more specific Python classes for `code` or `encoder`; the annotations really are only `np.ndarray`/`object`.

The dataclass is frozen only against field reassignment. NumPy arrays stored in it are not thereby made immutable. Constructing an arbitrary instance is syntactically possible, but no fixture-boundary validator establishes all Cycle-311 invariants.

### 1.3 All public functions: exact signatures, inputs, and returns

#### Infrastructure and constructors

| line | exact signature | accepted input contract | exact return |
|---:|---|---|---|
| R51 | `check(label: str, condition: bool, detail: object = "") -> None` | Diagnostic label, truth value, arbitrary detail. | `None`; increments `PASS` or `FAIL` and prints one diagnostic line (R52–58). |
| R61 | `normalized(path: Path) -> str` | A readable UTF-8 path. | Lower-cased, whitespace-collapsed `str` after removing `*`, backticks, and `>` (R62–65). |
| R68 | `note_contract() -> None` | No parameter; reads frozen `NOTE`. | `None`; emits one certificate check (or missing-note failure), R69–110. |
| R113 | `basis(dimension: int, index: int) -> np.ndarray` | Integer dimension and valid NumPy index. There is no explicit validation. | Complex basis vector, shape `(dimension,)`, R114–116. |
| R119 | `projector_bloch(vector: np.ndarray) -> np.ndarray` | Converted to float; must have exact shape `(3,)` and norm within `1e-10` of one (R120–122). | Complex `(2,2)` Bloch projector `(I+n·sigma)/2`, R123. |
| R141 | `physical_fixture(length: int) -> PhysicalFixture` | Integer passed to the imported Cycle-311 code builder. | The 11-field `PhysicalFixture` above (R142–174), with pair `(0,1)`, slices `(0,1)`, imported `COUPLING`, contact, encodings, and constraint selected internally. |
| R177 | `physical_subcode_controls() -> dict[int, PhysicalFixture]` | No parameter. | Exactly a dictionary keyed by `3` and `6`, each value from `physical_fixture`; also emits two checks (R178–245). |

`basis` is not used elsewhere in this runner. `physical_fixture(length)` is parameterized only by lattice length: it does **not** accept a fixture, contact, pair, seam slice, coupling, effect, coefficient, or weight.

#### Dilation/effect utilities

| line | exact signature | accepted input contract | exact return |
|---:|---|---|---|
| R248 | `stack_isometry(kraus: tuple[np.ndarray, ...]) -> np.ndarray` | Tuple length `1..8`; every element exact shape `(2,2)` (R249–252). Completeness/isometry is not validated here. | Complex stacked array shape `(16,2)`, zero-padded to eight blocks (R253–257). |
| R260 | `derived_effects(isometry: np.ndarray, groups: tuple[tuple[int, ...], ...]) -> tuple[np.ndarray, ...]` | `isometry.shape == (16,2)`; all pointer indices across groups must be unique and in `0..7` (R263–269). Empty groups and incomplete coverage are not rejected. | Tuple of length `len(groups)`; each item is a `(2,2)` compressed effect, the sum of `K_i†K_i` for that group (R270–280). |
| R283 | `physical_isometry(two_ray_encoding: np.ndarray, kraus: tuple[np.ndarray, ...]) -> np.ndarray` | Intended `two_ray_encoding` shape `(n,2)` and `(2,2)` Kraus blocks. This helper performs no shape/count validation (R286–290). | With `k<=8`, shape `(8n,2)` after zero padding; certificate `n=510`, hence `(4080,2)`. If called with `k>8`, it does not reject and stacks `k` blocks, shape `(kn,2)`. |
| R293 | `menu_metrics(effects: tuple[np.ndarray, ...]) -> dict[str, float]` | Nonempty tuple of matrices compatible with Hermitian eigensolving and summation against `(2,2)` `I2`; no explicit validator. | Exactly three float keys: `normalization`, `minimum_eigenvalue`, `maximum_eigenvalue` (R294–301). |
| R358 | `nonlinear_binary_weight(effect: np.ndarray) -> float` | Matrix compatible with `(2,2)` `sigma0 @ effect`; intended qubit effect. | Python `float`, `v^3/(v^3+(1-v)^3)`, with internally frozen `sigma0=(I+0.5Z)/2` (R359–361). |

`derived_effects` accepts pointer grouping, i.e. supplied menu context, but not numerical Born weights. `nonlinear_binary_weight` evaluates one hard-coded counterfunctional; it is not a configurable weight-law port.

#### Parameterized compiler helpers

| line | exact signature | accepted input contract | exact return |
|---:|---|---|---|
| R409 | `split_projector_isometry(projector: np.ndarray, splits: tuple[float, ...], contact: np.ndarray) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]` | `splits` must be nonnegative and sum to one within `1e-10` (R414–415); the resulting `len(splits)+1` `(2,2)` blocks must pass `stack_isometry`, so executable capacity is at most seven splits. Intended `projector` and `contact` are `(2,2)`, rank-one-projective/unitary respectively, but this function does not validate those properties itself. | `(V, groups)`: `V` shape `(16,2)`; `groups` has `len(splits)+1` singleton tuples `(0,),...`, R416–419. |
| R422 | `merge_isometry(weighted_projectors: tuple[tuple[float, np.ndarray], ...], contact: np.ndarray) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]` | One to four `(float, ndarray)` components (R426–427); weights nonnegative and total at most one within tolerance (R428–430); each projector exact `(2,2)`, idempotent and Hermitian within `TOL` (R434–440). Despite the error text, rank one is not explicitly checked: rank-zero and rank-two projectors pass those three tests. Intended contact is unitary `(2,2)`, but is not validated. Four components with a remainder attempt nine blocks and are rejected downstream; the four-component certificate case totals one and uses eight. | `(V, groups)`: `V` shape `(16,2)`; group 0 merges all plus indices, followed by one singleton per minus index and, if total `<1-1e-12`, a final coin singleton (R431–452). |

The `splits` and component `weight` values are apparatus coefficients. They are not the numerical grade `w(E)` and not observed frequencies.

#### Certificate stages

There is one executable certificate entry point, `main()` (R866; invoked at R902–903). The seven directly callable stage entry points it orchestrates are `note_contract`, `physical_subcode_controls`, `contact_trine_controls`, `binary_and_ternary_threshold_controls`, `mixed_projective_forcing_basis_controls`, `physical_locality_and_covariance_controls`, and `deletion_domain_and_semantic_controls`. Together with `main`'s final check (R879–890), they account for the advertised 15 checks. Their contracts are:

| line | exact signature | parameter and return shape |
|---:|---|---|
| R304 | `contact_trine_controls(fixture: PhysicalFixture) -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...]]` | Takes a fixture whose used fields are `(2,2)` `contact` and `(n,2)` `two_ray_encoding`. Returns `(kraus,effects)`, each an exact length-3 tuple of `(2,2)` arrays (R307–355). Directions and `sqrt(2/3)` are internal/frozen. |
| R364 | `binary_and_ternary_threshold_controls(trine_effects: tuple[np.ndarray, ...]) -> None` | Takes the trine-effect tuple; certificate binding is exactly the three `(2,2)` effects returned above. No explicit length/shape validator. Returns `None` after one check (R367–406). RNG seed `317`, 12 binary tests, coin Kraus blocks, nonlinear functional, and target sums are internal/frozen. |
| R455 | `mixed_projective_forcing_basis_controls(fixture: PhysicalFixture) -> tuple[tuple[np.ndarray, ...], dict[str, object]]` | Takes the same fixture contract. Returns an exact length-8 tuple `retained_kraus` of `(2,2)` arrays from the final held four-component axis presentation, plus `forcing_data` (R636–648). All test directions, split/component coefficients, arbitrary-effect eigenvalues, and held `sigma` are internal/frozen. |
| R651 | `physical_locality_and_covariance_controls(fixtures: dict[int, PhysicalFixture], route_kraus: dict[str, tuple[np.ndarray, ...]]) -> None` | Takes a fixture map (iterates every entry and later requires key `3`) and a route map whose values are tuples of intended `(2,2)` Kraus blocks; route-name strings have no semantics in the body. Returns `None` after locality and all-frame checks (R655–802). |
| R805 | `deletion_domain_and_semantic_controls(fixture: PhysicalFixture, forcing_kraus: tuple[np.ndarray, ...]) -> None` | Uses `fixture.contact` and a Kraus tuple. Certificate binding is the exact length-8 tuple returned by the mixed-projective stage; it deletes index 3 by replacement with a `(2,2)` zero (R809–814). Returns `None` after deletion, unlawful-domain, and note-firewall checks (R815–863). |
| R866 | `main() -> int` | No parameter. Hard-wires all stage bindings: fixtures `[3]`, trine outputs, mixed-projective outputs, and two named route tuples (R869–890). Prints data/summary/result and returns `0` iff `FAIL==0`, otherwise `1` (R891–899). |

`forcing_data` has the exact runner-created shape below (R505–515, R547–554, R636–648):

| key | exact value shape |
|---|---|
| `ray` | length-4 tuple of `(2,2)` arrays |
| `axis` | length-3 list of dicts with `left_mass: float`; `left_fine,right_fine: int`; and `left_half_I,right_half_I,presentation_equality,left_normalization,right_normalization: float` |
| `representations` | length-3 list of dicts with `eigenvalues: tuple[float,float]`, `fine_labels: int`, and `effect_residual,complement_residual,normalization: float` |
| `forcing_sufficiency` | dict with five boolean keys `same_direction_splits`, `coin_refinements`, `projective_complements`, `four_component_axis_identity`, `every_qubit_effect_at_most_three_components`, plus `maximum_fine_labels: int` |

### 1.4 What an external caller can actually supply

| supplied category | callable ports | exact distinction |
|---|---|---|
| Fixture/code realization | `contact_trine_controls(fixture)`, `mixed_projective_forcing_basis_controls(fixture)`, `physical_locality_and_covariance_controls(fixtures,...)`, `deletion_domain_and_semantic_controls(fixture,...)` | A caller can pass `PhysicalFixture` objects, but only the runner-built objects have the checked Cycle-311 binding. An arbitrary fixture is new supplied structure, not certified by its type. |
| Length | `physical_fixture(length)` | Only an integer enters. `main` freezes the tested lengths to `3,6`, and downstream code contains 510-row assumptions. |
| Bloch direction | `projector_bloch(vector)` | One supplied float-convertible unit three-vector can become a `(2,2)` projector. Certificate trine/axis/effect directions are not parameters; they are frozen literals. |
| Apparatus Kraus blocks | `stack_isometry`, `physical_isometry`, locality `route_kraus`, deletion `forcing_kraus` | A caller can supply tuples of `(2,2)` operators. This supplies an apparatus/program, not a Born law. |
| Contact | `split_projector_isometry(...,contact)`, `merge_isometry(...,contact)`; indirectly fixture fields | A direct `(2,2)` contact is accepted by the helpers but not validated as the actual Cycle-230 contact. The certificate binds the internally constructed `fixture.contact`. |
| Split/component coefficients | `split_projector_isometry(...,splits,...)`, `merge_isometry(weighted_projectors,...)` | These are lawful nonnegative apparatus coefficients under the bounds above. They are not effect grades or frequencies. |
| Coarse menu grouping | `derived_effects(isometry,groups)` | A caller can supply disjoint pointer-index groups. This selects a coarse presentation/context. |
| Effects | `menu_metrics(effects)`, `nonlinear_binary_weight(effect)`, `binary_and_ternary_threshold_controls(trine_effects)` | Effects can be supplied directly to diagnostics. Doing so bypasses the runner's “derived by pointer compression” provenance unless each is exactly bound to `derived_effects` output. |
| Numerical Born weights / density matrix / census | **none** | No signature accepts a general `w`, `sigma`, eligibility declaration, occurrence/member, Record corpus, count vector, frequency, epoch, or calibration. The only `sigma0`, nonlinear map, and held Born `sigma` are literals inside R358–361 and R602–606. |

Thus external data can lawfully supply **fixtures, effects, apparatus coefficients, split/component weights, Kraus operators, contacts, and pointer groups** at helper boundaries. In the shipped certificate, `main` supplies none of them externally: it constructs fixtures and wires internal outputs/literals. Most importantly, “component weights” in `merge_isometry` are not a port for Born outcome weights.

## 2. Note claims, exact scope, and inventories

The note has `Authority: none`, `Audit: unset`, and “Constitutional effect: none” (N7–11). It says the cycle changes no axiom/foundation/registry/policy surface (N19–20). Accordingly, the following are bounded construction and conditional-theorem claims, not an audited universal law.

### 2.1 Derived/constructed inventory

The note's exact “Constructed without a numerical grade” inventory is (N424–433):

> - one accepted physical-M2 two-ray matter subcode;
> - one actual contact-dependent three-outcome Naimark isometry;
> - positive normalized effects derived from pointer compression;
> - one bounded `X1^(8)` dilation compiler;
> - exact ray split, coin, complement, merge, and refinement identities;
> - a forcing-complete finite proof basis for the qubit effect algebra;
> - bounded support, local constraint preservation, held `L=6`, deletions, and all-frame covariance.

The fixed trine effects are derived from Kraus blocks: `K_k=sqrt(2/3)P_k U_g` and `E_k=K_k†K_k=U_g†(2P_k/3)U_g`, with `sum E_k=I` (N43–54). The note emphasizes:

> “The effects are obtained from the dilation; they are not entered as a menu of matrices after the fact.” (N56–57)

The construction is one actual ternary menu, not universal G2 (N196–197), and the bounded compiler contains the complete finite proof basis, not the whole arbitrary-finite X1 presentation family (N89–117, N324–338).

### 2.2 Exact conditional theorem and boundary

The theorem is exactly (N437–448):

> If all compiled `X1^(8)` menus are eligible and normalized by one numerical map that is a function of the compressed effect alone, then the PR-5479 T3 elimination forces one Born trace form on the two-ray effect algebra.
>
> `physical dilation`
> `  -> derived effect/refinement family`
> `  -> [supplied effect functionality + eligibility + weight normalization]`
> `  -> unique trace-form numerical representation on this qubit effect algebra.`

The note's earlier boundary is equally explicit:

> “It does **not** derive the weight functional, effect functionality across programs, eligibility, normalization of weights, occurrence, an actual member, or a Record.” (N105–108)

> “A held Born trace functional passes every compiled normalization, refinement, merge, and same-effect identity; that is a consistency check, not selection of the Born rule.” (N108–110)

For equal compressed effects, “Effect functionality identifies the numerical value of the two physical presentations,” but this “is a hypothesis, not a consequence of unitary dilation” (N296–298). Compatibility is checked only “after a trace functional is supplied” (N340–351).

### 2.3 Still-open inventory

The exact open inventory is (N450–467):

> - selection or derivation of the numerical weight functional;
> - eligibility and weight normalization across the compiled family;
> - same-effect-across-program identification as a physical law rather than a
>   mathematical grading hypothesis;
> - a single fixed autonomous programmable unitary generating the continuous
>   projector/weight family;
> - the literal arbitrary-finite X1 family in one bounded shot;
> - G1 and G2 on every effect/menu of a general finite physical region;
> - physical occurrence and one actual local member;
> - lawful Record formation, typing, protection, permanence, readable fibre, and continuation capacity;
> - repeated-process extension, causal/boundary ordering, and global additivity;
> - frequency or component-mean calibration; and
> - empirical identification of the trace weights with observed relative frequencies.

The semantic boundary is:

> “Pointer labels are not Records. Dephasing is not occurrence. Conditional Born weights are not frequencies. The theorem does not choose an actual member, and a selected member alone would not derive the numerical law.” (N469–471)

Contact dependence does not change that: deleting contact changes the labeled trine effects but leaves normalization, so the instrument is not an occurrence detector (N56–68).

### 2.4 Supplied-structure inventory

The note's supplied items and their non-derivations are (N475–491):

| supplied item | use here | not derived here |
|---|---|---|
| Cycle-311 fixed-Wilson reference and role-constrained M64 seam | accepted physical code | preparation/genesis of the reference and seam-role coherence |
| one body cell and pair label `(0,1)` | declares the two-ray fixture | unique origin or pair selection |
| Cycle-230 `g=0.37` and one contact application | actual relative contact phase | coupling selection or occurrence of the interaction |
| equatorial trine directions | fixed ternary instrument coefficients | why nature selects the trine |
| continuous projectors and component weights | parametric `X1^(8)` compiler inputs | autonomous generation or selection |
| split rows and coarse pointer grouping | refinement/merge presentation | physical law selecting the menu context |
| three blank pointer M2 and their computational basis | eight fine labels | blank preparation, readout, or actual outcome |
| bounded Cycle-311 dense matrix-unit grammar | physical Kraus-block expansion | one-/two-M2 primitive sequence for every new coefficient block |
| ordinary complex-Hilbert dilation rule | turns Kraus blocks into an isometry | selection of a numerical grade |
| effect functionality across different programs | load-bearing PR-5479 premise | physical identification/noncontextuality law |
| eligibility and normalization of numerical weights | load-bearing PR-5479 premise | Born law, occurrence, or frequency |
| trace functional in one held consistency check | verifies compiled identities | unique selection or empirical calibration |
| numerical tolerances | executable regression gates | physical thresholds |

The fine block explicitly uses a “supplied weight `lambda_i`, direction `n_i`, and split fraction `r`” (N234–239). Continuous directions, split weights, the compiled-menu choice, and application of its coefficient block “remain supplied” (N389–396). The note then states that supplied continuous directions and weights are coefficient data and that no exact universal autonomous program register is constructed (N493–496).

The strongest compact inventory statement is:

> “succeeds as `X1^(8)`; coefficients, eligibility, effect functionality, and weights remain supplied” (N563–566).

This is the exact Cycle-317 support for the task's Cycle-719 warning that weights remain supplied.

## 3. Meaning of “bounded ternary Born-forcing menu”

“Bounded” has three simultaneous restrictions:

1. One logical two-ray/qubit effect algebra embedded in the accepted seam code,
   tested at `L=3` and held `L=6` (N119–151).
2. Three pointer M2, hence at most eight simultaneous fine labels,
   `X1^(8)` (N70–80). A ninth label is rejected only for this one-shot
   architecture; sequential/recurrent arbitrary-finite realization is open
   (N112–117, N411–420).
3. The family is only the finite load-bearing PR-5479 T3 basis: projective
   complements, coin refinements, three-way same-ray splitting, up-to-four
   component merges/axis cancellation, and all-qubit-effect presentations
   (N70–98, N322–338). It is neither G2 nor literal arbitrary-finite X1.

“Ternary” first means the fixed physical contact trine with three derived
effects. It supplies a physical counterexample to binary-only sufficiency: the
held nonlinear binary functional normalizes on complements but sums to `4/7`
on the quarter coin and `1/3` on the contact trine, rather than one
(N199–228). This rejects that particular non-Born family under ternary
normalization; it does not select a replacement law.

“Born-forcing” means a conditional representation theorem, not dynamical or
empirical selection:

- constructed premises: physical dilations, compressed effects, and exact
  split/refinement/merge/same-effect operator identities;
- supplied premises: one numerical map, effect functionality across different
  programs, eligibility of every compiled menu, and normalization of that map
  on each menu;
- forced conclusion: there exists one density matrix `sigma` such that
  `w(E)=Tr(sigma E)` on the complete two-ray effect algebra (N98–110);
- not forced: which `sigma`/weight functional nature selects, why the
  apparatus coefficients/menu are selected, occurrence, an actual member,
  Records, global additivity, frequencies, or calibration.

There are therefore two distinct senses of “feeding”:

1. **Feed the apparatus/compiler:** provide a legal projector, split row,
   component coefficients, contact, Kraus blocks, and/or pointer grouping to
   the helper ports in §1.4. The derived effects then follow by compression.
2. **Feed the conditional forcing premises:** provide one same-effect
   functional grade, certify eligibility of the whole compiled family, and
   certify menu normalization. The current runner has no callable port for
   this feed; these remain hypotheses in the note.

Supplying empirical counts, pointer labels, an arbitrary effect list, or
component coefficients alone does not feed the second sense.

## 4. Synthesis for a Cycle-729 epoch-census spec

Assume the requested Cycles-722/725 style means: byte-pin every source artifact,
perform zero fitting/refitting, and declare every projection, basis, ordering,
normalization, and missing-data convention. That style is task-supplied, not
independently extracted here.

### 4.1 Concrete entry-point bindings

| Cycle-317 port | lawful Cycle-729 binding | status / new supply |
|---|---|---|
| `physical_fixture(length)` | Bind a declared integer length. For exact Cycle-317 replay bind `3` or `6`; do not infer/refit it from census values. | **Pinned rerun + exact binding** at `3,6`. Any other length is **NEW SUPPLIED DATA** and is outside the certified downstream 510-row contract. |
| `projector_bloch(vector)` | A byte-pinned census projection may emit exactly one ordered real unit vector `(x,y,z)` under a declared frame/sign/normalization convention. | **NEW SUPPLIED DATA** unless the vector is exactly one of the frozen runner literals. Passing it supplies an apparatus direction; it does not derive why that menu is selected. |
| `stack_isometry(kraus)` | Bind `1..8` exact complex `(2,2)` arrays, including declared complex serialization and basis order. | Exact re-binding to returned Cycle-317 Kraus is replay. Any census-derived block is **NEW SUPPLIED DATA / supplied apparatus coefficients**. No refit. |
| `derived_effects(isometry,groups)` | Bind an exact `(16,2)` logical isometry and disjoint ordered pointer-index groups in `0..7`. | Compression is a deterministic pinned rerun. Any new `groups` value is **NEW SUPPLIED DATA / menu-context selection**. Directly supplied effects must not be called derived. |
| `physical_isometry(F,kraus)` | Bind `F` exactly to a pinned `(510,2)` runner-created `two_ray_encoding` and Kraus exactly to a named compiled route. | **Pinned rerun + exact binding.** Any external `F` or Kraus is **NEW SUPPLIED DATA** and requires its own physical/code certificate. |
| `menu_metrics(effects)` | Bind only to byte-identical `derived_effects` output, or label an external `(2,2)` effect tuple explicitly as supplied. | Metric calculation is deterministic. External effects are **NEW SUPPLIED DATA** and lose dilation provenance until exactly rebound. |
| `nonlinear_binary_weight(effect)` | Bind an exact `(2,2)` effect; the counterfunctional stays the frozen internal formula. | Diagnostic replay only. It cannot accept a census-selected law. |
| `split_projector_isometry(P,splits,U)` | Projection may supply exact `(2,2)` `P`, a declared finite nonnegative tuple summing to one, and exact `(2,2)` contact. | If all three are rebound to Cycle-317 literals/fixture contact, deterministic replay. Otherwise each changed direction, fraction, or contact is **NEW SUPPLIED DATA**. Fractions are apparatus coefficients, not Born weights. |
| `merge_isometry(weighted_projectors,U)` | Projection may supply one to four exact `(lambda_i,P_i)` pairs satisfying the lawful domain, plus exact contact. | Deterministic compilation after binding. Every new `lambda_i`, `P_i`, component order, or contact is **NEW SUPPLIED DATA**. `lambda_i` is not `w(E_i)`. |
| `contact_trine_controls(fixture)` | Bind exactly to `physical_subcode_controls()[3]`. | **Pinned rerun + exact binding.** It accepts no epoch values, effects, directions, weights, or refit. An external fixture is **NEW SUPPLIED DATA**. |
| `binary_and_ternary_threshold_controls(trine_effects)` | Bind exactly to the length-3 effect tuple returned by the preceding stage. | **Pinned rerun + exact binding.** Census effects would be **NEW SUPPLIED DATA** and would not automatically satisfy the exact target. |
| `mixed_projective_forcing_basis_controls(fixture)` | Bind exactly to the same `[3]` fixture. | **Pinned rerun + exact binding.** Its directions, eigenvalues, splits, component coefficients, and held `sigma` cannot be supplied through this signature and remain frozen diagnostics. |
| `physical_locality_and_covariance_controls(fixtures,route_kraus)` | Bind fixtures exactly to the `{3,6}` return and routes exactly to `{"contact_trine": trine_kraus, "X1_8_axis_merge": forcing_kraus}`. | **Pinned rerun + exact binding.** New fixtures/routes/Kraus are **NEW SUPPLIED DATA** and need independent locality/covariance interpretation. |
| `deletion_domain_and_semantic_controls(fixture,forcing_kraus)` | Bind `[3]` fixture and exact retained length-8 Kraus tuple. | **Pinned rerun + exact binding.** New branch data or altered ordering is **NEW SUPPLIED DATA**. |
| `check`, `normalized` | Administrative values/path only. | Not a physics feed. Changing the note text or tolerance contract is not census evidence. |
| `main()` and zero-parameter stages | No epoch input exists. Byte-pin runner/note and replay exact internal wiring. | **Pinned rerun only**; proves Cycle-317 regressions, not a Cycle-729 census connection. |

`basis(dimension,index)` can encode a declared pointer/basis label, but it is
unused by the certificate and adds no scientific binding by itself.

### 4.2 What an epoch census would still have to add

The current surface has no receiver for an epoch identifier, event/member
census, Record rows, counts, exposure, missingness, frequency, effect-to-bin
map, eligibility mask, normalized grade, `sigma`, or general weight law.
Consequently a Cycle-729 spec needs an adapter outside this runner, with every
one of the following marked as supplied unless separately derived:

1. **NEW SUPPLIED DATA:** byte identities/hashes and byte ranges for every
   census artifact, plus epoch boundary and row-order conventions.
2. **NEW SUPPLIED DATA:** the exact projection from census fields to a
   Cycle-317 object: fixture ID, route, pointer group, effect, projector
   direction, or apparatus coefficient. Declare units, frame, signs, complex
   basis/order, degeneracy, missing rows, and normalization. Zero refit means
   no coefficient may be estimated or tuned on the held epoch.
3. **NEW SUPPLIED DATA:** an exact provenance binding showing that any claimed
   effect equals `derived_effects(V,groups)` for a byte-pinned `V` and declared
   groups. Otherwise the effect is supplied, not derived.
4. **NEW SUPPLIED DATA / hypothesis unless proved:** which compiled menus are
   eligible and why all required `X1^(8)` menus, not merely observed ones, fall
   under one rule.
5. **NEW SUPPLIED DATA / hypothesis unless proved:** same compressed effects
   across different programs receive the same numerical value (effect
   functionality).
6. **NEW SUPPLIED DATA / hypothesis unless proved:** the normalized numerical
   map `w(E)` itself. Census counts do not become `w` without an occurrence,
   Record, sampling/exposure, and calibration bridge.
7. **NEW SUPPLIED DATA:** any component/split coefficients not byte-identical
   to runner literals. These remain selected apparatus/program coefficients;
   the Born-forcing theorem does not choose them.
8. **NEW SUPPLIED DATA / open physics:** occurrence/member selection, lawful
   Record typing, repeated-process/global additivity, and frequency or
   empirical calibration. The note explicitly keeps all four open.

No existing leg may estimate `sigma`, choose coefficients, select a Born
functional, normalize census counts into one, or infer eligibility. A
zero-refit projection may report a predeclared number, but that number remains
supplied until the missing physical/statistical bridge is certified.

### 4.3 Required firewall

Use a firewall analogous in form to the note's `C_source` warning at N532:

> **`C_grade/census` firewall:** epoch rows, projected effects, apparatus
> component/split coefficients, pointer occupancies, normalized counts, and
> exact fixture bindings are not thereby an effect-functional numerical grade,
> an eligibility law, a selected density matrix, a Born-law selection,
> occurrence, Records, global additivity, frequencies, or empirical
> calibration.

In particular:

- do not identify apparatus coefficients `lambda_i`/`r` with outcome weights;
- do not identify pointer labels or occupancies with occurrences or Records;
- do not call normalized census counts conditional Born weights;
- do not call a trace-form consistency rerun selection of `sigma` or the Born
  rule;
- do not promote exact byte binding or zero refit into physical derivation;
- do not claim G2, arbitrary-finite X1, a selected weight law, actual outcome,
  Record, permanence, global additivity, frequency, or calibration
  (the note's own prohibition, N749–751).

The honest Cycle-729 result available without new supplied science is:
“the byte-pinned epoch specification exactly replays and binds to the
Cycle-317 bounded physical effect surface; conditional on separately supplied
effect functionality, eligibility, and normalized weights, the finite
`X1^(8)` identities force trace form on the two-ray algebra.” It is not a Born
law selection.

## COMPLETENESS

- All 11 uppercase module bindings are inventoried, including mutable
  `PASS`/`FAIL`.
- The public `PhysicalFixture` record and all 20 public functions are listed
  with definition lines, exact annotations/signatures, input constraints, and
  return shapes.
- The executable certificate entry point, its seven callable stages, and every
  helper-level fixture/effect/coefficient/weight port are distinguished.
- The note's constructed, conditional, open, and supplied inventories and its
  effect-functionality/eligibility/coefficient/weight boundaries are quoted at
  their exact source lines.
- “Bounded ternary Born-forcing” is separated into physical compilation,
  supplied forcing premises, forced trace representation, and prohibited
  selection/frequency claims.
- Every Cycle-729 binding is marked either pinned rerun/exact binding or
  **NEW SUPPLIED DATA**, and the required grade/census firewall is explicit.
- No claim from an unread Cycle-719/722/725/729 artifact is attributed to those
  artifacts; their only use is the style/boundary requested in the task.

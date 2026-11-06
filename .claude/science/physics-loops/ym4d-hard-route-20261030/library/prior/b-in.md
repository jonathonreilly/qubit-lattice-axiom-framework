# Prior work: B-in

Reading digest at `993762321`; research text, not an audit. No proof or status grant.
Paths are relative to `.claude/science/physics-loops/ym4d-hard-route-20261030/`.
`I`, `II`, `III` denote the complete account; `SA` its outline, upstream `31a47c543775`.
Source locators: I = `/tmp/sa_ca_I.tex`; SA = `/tmp/sa_ym4.tex`. II/III references below are attributed to the existing cited inventory.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Tadeusz Balaban for his inputs.
“PROVED” reports the source/index label with its premises, not our verification.

## 1. Target and statement sites

- **B-in:** on every positive-level cell of the sealing core `D₂\B_S`, the real pair `(U₂,J(U₂))` obeys every defining analytic-space inequality, derived entries included, at most `F w c r_a(n)/64`. Here `F≥φ_flat`, `w,c≥1`, and `n` is the current level or a finer birth index. Cube clauses use the base's gauges. The bound is independent of age `h−n`, exclusions, blocks and strata. `A′=0`.
- Our full formulation is `library/ca-claude.md:78`; its exclusion of raw cells is at `:80`; the additional **S-B** scope assertion is at `:82`: all positive-level cells in the collar's one-bond read neighbourhood and all whole index-zero cubes meeting it lie in `D₂\B_S`. This is an input, not a proved placement theorem.
- Our other statement/use sites: `library/ca-claude.md:10`, `:15`, `:18`, `:84`, `:90`, `:94`, `:96`, `:110`, `:186`, `:212`, `:222`, `:224`; `library/ca-f.md:18`, `:27`, `:180`, `:190`. `library/ca-claude-r1.md:8` replaces only Proposition F and Result input 2, leaving input 1 untouched.
- Their exact base assertion is I:138438–138450, inside `4.27:prf-room-dissolving` (I:138348, **PROVED**). Its conclusion (b), I:138383–138386, already states the cellwise `θ/64` specialisation. The proof invokes an own-level sealing bound; it does not establish that bound there.
- Their other explicit use is I:136724–136733 and I:136754–136756, `4.27:prf-ambient-inclusion` (I:136490, **INCOMPLETE**). It adds three `1/64` increments and uses one base gauge per whole frozen cube. I:138361–138367 names the sealing construction and its objects without providing the missing quantitative theorem; I:138472–138482 describes its claimed dependency order.
- The full-index rows are `library/sa-index/ca-full/index.tsv:510`, `:516`; only the former is in `library/sa-index/ca-full/leaves.tsv:39`. Thus absence from the leaf list does **not** supply the unnumbered base input. No separately labelled sealing/base theorem was found in either TSV.
- The outline does not state this exact B-in. Its stored birth-space/transport discussion is SA:17433–17459, indexed at `library/sa-index/chunk-16.md:52`–61; `library/sa-index/obligations.md:912`–915. Those are sketched permanent-domain/transport assertions, not this seed estimate.

## 2. Existing results to reuse

| Source and declared standing | What it supplies; missing part |
|---|---|
| `library/ca-claude.md:39`–74, Lemma A; FINISH row 382 reports the lost check's ADVANCE | Actual splice rows/data identify `U₂=V₀` on stratum bonds. Pinned plaquettes are `<ε₀<0.04α₀₀`; `A′=0`. Side plaquettes and whole-cube reads remain. |
| I:92401–92435, 92515–92537, `4.22:lem-current-localisation`, **PROVED**; I:91761 `lem-law-site`, **PROVED** | Defines `B₂`, U₂ and its criticality/localisation; identifies common blocks off the graded layer. Does not bound every full current or admit every U₂ side plaquette. Index: `library/sa-index/ca-full/index.tsv:338`, `:340`. |
| I:142592–142812, `4.27:lem-real-point-collar`, **PROVED**; `library/sa-index/ca-full/index.tsv:524` | On its own date's admitted real minimizer, proves pinned curvature, current `≤0.48r₃(0)` and index-zero cubes, conditional on (a)–(g). Input (d) already assumes its positive-level real bound. Matching that minimizer and its full cube data to the spliced U₂ is missing. |
| I:142618–142659, same lemma, inputs (e)–(g) | Current formula, axial cube estimate and last coupling caps give the current/cubes **once all stencil/cube plaquettes are small**. These are retained inputs, not a proof of side-plaquette admission. |
| I:141509, `4.27:lem-level-zero-ratios`, **PROVED**; `library/sa-index/ca-full/index.tsv:521`; `library/ca-claude.md:90` | Converts the stronger B-in level-one radius to `<3×10⁻⁴α₀₀`. Does not supply curvature for U₂. |
| `library/ca-claude.md:84`–96, Lemma B | Conditional current and cube conclusions from B-in **and S-B**. Do not redo its algebra as a proof of the premise. |
| `library/arr.md:692`–736, seed comparison; `:843`–954, full-stencil seed/layer criterion; `library/crca.md:166`–231 | Gives conditional routes from an admitted matching seed, or small whole-cube curvature plus actual-layer bounds, to CA. No unconditional matching seed. |
| `library/arr.md:752`–783 | Empty/aligned-trace collar is a vacuous special case. It supplies no nonempty core bound. |
| `library/ca-claude.md:151`–162, Lemma E; `library/ca-f.md:86`, `:110`, `:149` | Zone-distance bound, segment current and cancelled weighted-layer response address the **increments**. They do not bound the base U₂. |

The account's positivity, frozen-room and heredity results do not create a seed bound: see I:132608 `lem-factor-positivity` (**PROVED**; index `:494`), and the inventory `library/prior/ca-claude.md:27`–36. The room-dissolving proof itself explicitly imports B-in.

## 3. Earlier attempts and their first missing steps

- `library/arr.md:558`–579: transfer regular real admission; no matched U₂ boundary data, regular ancestor or whole-cube admission.
- `library/arr.md:581`–614: criticality/projected-current localisation; `GQ*=0` erases a possibly large constraint-current component. It does not bound full J₂.
- `library/arr.md:616`–633: real estimates plus holomorphy; no uniform complex-domain inclusion follows.
- `library/arr.md:677`–750: prepared geometry/exact nesting; missing equality of actual splice rows, their data and an admitted ancestor. Lemma A later fixes the stratum rows only (`library/ca-claude.md:74`).
- `library/arr.md:752`–783: torus transport; empty trace does not identify a nonempty-collar seed, while same-trace transport still needs an admitted reference.
- `library/arr.md:785`–841: LSC integral/source control; total mass/moments do not give every-fibre datum suprema.
- `library/ca-claude.md:96`: compare U₂ to `U(B″_k,V″)`; still needs a quantitative comparison for the two constrained problems, including every side plaquette on the required cubes.
- `library/ca-claude.md:139`–149: cut decay alone leaves `√k exp(−δ Ř_k)` unbounded in cutoff depth. Lemma E repairs the layer version, not the independent seed comparison theorem.
- `library/ca-f.md:14`, `:29`–52: old step F cuts a datum without a norm bound (D1), and reads a full-layer source identity at partial segments (D2). Its replacement does not attack B-in. Row 382's check is rerunning; the lost verdict is only recorded in `FINISH.md:446`.
- The lost first digest has no recoverable proof: `FINISH.md:447` records only “partly covered”, with side-plaquette/full-read scope, age-uniform core bound and S-B remaining.

## 4. Consumers and weakest needs

| Consumer | Weakest identified sufficient input |
|---|---|
| Lemma B(i),(ii), `library/ca-claude.md:84`–92 | Actual U₂ side plaquettes on every current stencil at the collar bounded by `0.04α₀₀`; pinned ones are already supplied by Lemma A. Full analytic-space `1/64` bounds are stronger than needed here. |
| Lemma B(iii), `library/ca-claude.md:94` | Same bound on **every plaquette of every whole required index-zero cube**, plus retained axial-gauge inputs/caps. A statement only at collar vertices is insufficient. |
| Proposition C, `library/ca-claude.md:98`–123; base in F at `:186` | Seed curvature/current/cube conclusions above, with actual layer bounds. C consumes B-in through Lemma B; F uses the resulting small base. |
| Corrected F and CA assembly, `library/ca-f.md:155`, `:174`, `:178`–190, `:200`; `library/ca-claude-r1.md:8` | Inherits Lemmas A/B/C unchanged; needs no new global B-in assertion. Layer inputs N1/N3/G-sep stay separate. |
| Ambient inclusion, I:136724–136756 | Room for base plus actual increments at current/finer birth thresholds, derived entries and whole frozen cubes with one gauge. Its displayed argument uses `1/64+3/64`; a replacement must preserve the required final margin. Collar-only level-one curvature does not serve it. |
| Dissolving room/spend table, I:138348–138484 | All consumed entries at `θ/64`, age-independent and on its cells/cubes; three increment shares then give `θ/16`. A relaxed constant would require changing that table and its downstream uses. |

**Weakening:** the full-read side-plaquette statement serves all *our CA seed* consumers and avoids proving the full age-uniform B-in/S-B package. It is not shown sufficient for both account consumers. No weaker replacement serving **all** the listed consumers is established.

## 5. Overlap and search boundary

- CA already belongs to `ca-claude`: `library/open-registry.md:13`, `:548`; `library/open-core.md:99`; FINISH row 347 (`FINISH.md:411`). The base subproblem must stay with that owner, not become a duplicate CA lane.
- ARR/CRCA and rows 319/353 (`FINISH.md:383`, `:417`) cover the earlier seed/consumer attempts. Rows 382/383/386/387 (`FINISH.md:446`, `:447`, `:450`, `:451`) cover the lost check, lost digests, repaired layers and this reading task.
- `library/open-registry.md:139` assigns no owner to B99b-T314; H-STAGE is `stage-claude` at `:272`. These are ca-f inputs, distinct from B-in.
- `library/chain-ca.md:177`, `library/port/p5-induction.md:778`, `library/port/p6-correlation.md:4500`, `library/port/p10-stability.md:770`, `library/port-map.md:58`, `:92` carry ambient inclusion unresolved; none supplies the base.
- The unrelated boundary-activity input also called B-in (`library/nl1-L-draft.md:473`; `library/td-draft.md:328`) is not this lemma.
- Whole-folder tracked searches covered the symbols, account labels, CMP 119 (2.10)–(2.14), CMP 122b (1.50)–(1.55), CMP 109 (1.8), CMP 99b (3.35), and their paper names. Both full-account TSVs and outline chunks/obligations were searched with neighbouring rows. Navigation log: `/tmp/ym-prior-387/b-in-search.txt`. Earlier broader CA inventory: `library/prior/ca-claude.md:23`–69. No new proof lane was opened.

partly covered: pinned seed, splice identity, conditional current/cube algebra and layer estimates exist; actual side-plaquette bounds on all required stencils/whole cubes remain, and the full age-uniform core bound and S-B are unsupplied.

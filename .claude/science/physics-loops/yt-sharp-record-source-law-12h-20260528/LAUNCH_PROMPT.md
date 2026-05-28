Run a 12-hour `physics-loop` campaign on the Y_T frontier-physics theorem route.

Repository:

```text
/private/tmp/yt-primitive-physical-source-theorem-20260526
```

Branch / delivery:

```text
physics-loop/yt-primitive-physical-source-theorem-20260526
existing PR: #1980
```

Do not open new PRs. Work on this branch only. Commit coherent results, push
the branch, and update PR #1980 when a meaningful block closes. Keep all loop
state under:

```text
.claude/science/physics-loops/yt-sharp-record-source-law-12h-20260528/
```

Use the `physics-loop` skill. This is a constructive frontier-theorem
campaign, not another broad inventory/no-go sweep. Spend the full 12-hour
budget unless a genuine global tooling failure prevents safe progress.

Objective:

```text
Derive the Y_T sharp-record physical source law from the qubit/Cl(3)/Z^3
substrate:

local signed qubit records + ideal sharp projective measurement + Cl(3)/Z^3
same-surface action/source constraints
  -> physical top source lives in the nontrivial C3 block P_nt, not P_0
  -> the relative radial/source factor is lambda_top = 1/sqrt(2)
  -> V_top = (A/sqrt(2)) B_x
```

The theorem must not use:

- `H_unit`;
- old Ward authority;
- `yt_ward_identity`;
- `y_t_bare`;
- PDG/top/W/Z observed targets;
- alpha_LM, plaquette/u0, Planck, alpha_s;
- fitted selectors;
- target-value insertion.

Constructive success requires all of:

```yaml
selects_nontrivial_block: true
excludes_P0_without_target_matching: true
derives_lambda_top: 1/sqrt(2)
uses_H_unit_or_Ward: false
uses_observed_targets: false
accepted_same_surface_source_law: true
status: exact-support|proposed_retained
```

Preferred constructive attack surfaces:

1. Sharp-record/qubit measurement theorem:
   derive the neutral one-Higgs source factor `1/sqrt(2)` from ideal
   two-outcome projective record geometry, signed records, and local
   record-preserving interventions.

2. Action-first source theorem:
   derive the unique degree-one same-surface local action tangent compatible
   with qubit records, chirality, gauge locality, and top/W same-source
   comparability.

3. C3/chirality selection theorem:
   derive why a physical massive top response must live in the faithful real
   nontrivial C3 block `P_nt`, excluding the singlet `P_0` by law rather than
   target matching.

4. Feynman-Hellmann/LSZ physical response theorem:
   derive the same-source top/W radial ratio from pole residue normalization,
   if and only if the required strict backend/projector/source fields are
   accepted on the same surface.

5. Variational/fixed-point theorem:
   derive the coefficient by a real physical principle such as
   minimum-disturbance, sharp-record stability, or boundary regularity. Do not
   merely rename a normalization convention as a physical law.

Required exercises inside the loop pack:

- assumptions/imports audit;
- no-go ledger scoped only to constructive theorem attempts;
- first-principles "Elon" reduction of the theorem to irreducible physical
  drivers;
- simulated physicist panel only when choosing between constructive routes;
- targeted literature/math search only if it can directly inform the theorem;
- trace gate for every artifact: what blocker does it move?

Stop wasting cycles on:

- top-only Hilbert-Schmidt/Fisher/unit-norm/homogeneous normalization
  variants already pruned;
- W-normalized ratio restatements that leave `lambda_top` free;
- local C3 coefficient-flow templates that do not supply a physical
  basepoint/readout law;
- hidden-repo scans unless a specific artifact path is named by a theorem.

If full positive closure is not achieved, leave the narrowest honest result:

```text
exact-support / bounded-support / no-go
```

and identify the single next theorem or strict observable packet needed. Do
not claim retained or proposed-retained unless the constructive success
criteria above are all met.

Verification:

- run any new theorem runner(s);
- run the current full closure stack:

```text
python3 scripts/frontier_yt_full_closure_stack_and_strict_pole_response_contract.py
```

- run `python3 -m py_compile` on new scripts;
- run `git diff --check`;
- update loop `STATE.yaml`, `CLAIM_STATUS_CERTIFICATE.md`, `TRACE_GATE.md`,
  `HANDOFF.md`, and PR #1980 body after meaningful closure or at the campaign
  end.

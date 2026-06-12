# Handoff

Branch: `physics-loop/koide-first-order-converse-scope-20260612`

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3715

Target row:
`koide_first_order_selector_is_the_chiral_lr_coupling_not_a_symmetry_narrow_note_2026-06-05`

## What changed

- The note no longer states the broad shorthand `C3-equivariance iff commutes-with-Gamma_chi`.
- The allowed statement is now restricted to the native circulant generation-mass family.
- The companion runner now proves a non-converse guard: there are non-circulant operators commuting with
  `Gamma_chi` that do not commute with `C`.
- The note explicitly states that this PR does not supply a retained `AC_phi_lambda` physical-coupling bridge.

## Verification

```text
python3 scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py
10 PASS, 0 FAIL
```

```text
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py --force --concurrency 1 --push-mode none --allow-non-main
ok 1
```

## Remaining blocker

The retained bridge from `AC_phi_lambda` to the physical `M(b) tensor sigma_+` coupling and the physical
`r`-weighting is still open. This branch is scoped to the false-converse repair.

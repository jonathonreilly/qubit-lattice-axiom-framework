# SU(2) u0 One-Plaquette Bracket Loop Pack

Branch: `codex/su2-u0-one-plaquette-bracket-20260618`
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4383

Goal: source-side audit unlock for the `g_2(v)` bounded interval row by
replacing the purely literature-only `u_0(SU(2)) in [0.96,0.98]` interval with
a framework-native finite one-plaquette Wilson/Haar support point at
`beta_W = 16`.

Artifacts:

- `docs/SU2_WEAK_U0_ONE_PLAQUETTE_WILSON_BRACKET_BOUNDED_SUPPORT_NOTE_2026-06-18.md`
- `scripts/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.py`
- `docs/G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`
- `scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`

Claim boundary:

- proves the exact finite one-plaquette identity
  `<P>_1plaq(beta) = I_2(beta)/I_1(beta)`;
- verifies `u_0,1plaq(16) in [0.9761,0.9762] subset [0.96,0.98]`;
- does not claim the full four-dimensional nonperturbative `SU(2)` lattice
  vacuum plaquette;
- does not audit, retag, or land any status.

Verification:

- `python3 scripts/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.py`
  -> `PASS=17 FAIL=0`
- `python3 scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`
  -> `PASS=39 FAIL=0`
- runner caches refreshed for both scripts

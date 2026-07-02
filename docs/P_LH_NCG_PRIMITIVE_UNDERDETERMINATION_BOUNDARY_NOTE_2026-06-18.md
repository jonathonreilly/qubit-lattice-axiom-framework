# P-LH NCG Primitive Underdetermination Boundary

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded negative boundary / route-pruning support
**Status:** bounded support only
**Source runner:** [`scripts/frontier_p_lh_ncg_primitive_underdetermination_2026_06_18.py`](../scripts/frontier_p_lh_ncg_primitive_underdetermination_2026_06_18.py)
**Runner cache:** [`logs/runner-cache/frontier_p_lh_ncg_primitive_underdetermination_2026_06_18.txt`](../logs/runner-cache/frontier_p_lh_ncg_primitive_underdetermination_2026_06_18.txt)

## Scope

This note is a no-new-axioms boundary for the parent trace target
`PRIMITIVE_P_LH_CONTENT_PROPOSAL_NOTE_2026-05-10_pPlh.md`.
The latest audit asks for a source artifact deriving or explicitly registering
the order-one condition, KO-dim-6 real structure, and finite algebra from the
physical `Cl(3)/Z^3` baseline. This note does not register those structures.
It instead records the negative source-side fact visible on the current
minimal axiom surface:

```text
Lattice + Quantum + Record do not determine the NCG finite algebra,
order-one condition, or KO-dim-6 real structure used by the P-LH route.
```

The result is bounded support for keeping the P-LH content row open unless a
separate derivation or explicit primitive approval is supplied. Independent
audit owns any verdict or dependency registration.

## No-go Discipline Gate

- **N1 Alternative routes:** the runner tests finite-algebra selection,
  KO-dim-6 real-structure selection, and order-one selection on the same finite
  Pauli block. It does not test every possible SM LH/RH route.
- **N2 Wall independence:** the three witnessed walls are independent missing
  choices: finite algebra, antiunitary sign, and finite Dirac/opposite-action
  data. Supplying one does not supply the other two.
- **N3 Hidden-wall scan:** load-bearing inputs are only the current
  `Lattice + Quantum + Record` baseline and explicit finite Pauli matrices. No
  particle content, gauge group, spectral triple, or NCG primitive is imported.
- **N4 Residual matching:** the residual matches the parent blocker: derive or
  explicitly register the order-one condition, KO-dim-6 real structure, and
  finite algebra from the physical `Cl(3)/Z^3` baseline.
- **N5 Rhetoric audit:** the claim is not that P-LH is false and not that NCG
  cannot be used. It only says the current baseline does not determine the NCG
  packet without an added derivation or approved primitive input.
- **N6 Partial closure paths:** retained derivation of the NCG packet, explicit
  primitive approval, or a different SM LH/RH content route can still close the
  parent.
- **N7 Steelman:** a future bridge could show that dynamics, a readout context,
  or a larger retained finite sector selects the NCG data. This note grants
  that possibility and tests only the no-new-axioms finite Pauli route.
- **N8 Cross-cycle echo:** the note does not turn a missing primitive into a
  bounded status. It records a route-pruning boundary and leaves admission,
  audit status, and retained dependency movement to the governed lanes.

## Baseline Used

The current public framework axiom memo is
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md). Its Quantum
axiom supplies one qubit per site, equivalently one-site operator algebra
`M_2(C)` / `Cl(3,0)`. It explicitly does not supply particle content, gauge
group, species identification, or physical observable bridge.

The runner uses only that finite Pauli representation boundary:

- `rho_+ : gamma_i -> sigma_i`;
- `rho_- : gamma_i -> -sigma_i`;
- `Cl^+(3)` bivectors are identical in `rho_+` and `rho_-`;
- the chirality volume element has opposite signs on `rho_+` and `rho_-`.

## Three Underdetermination Witnesses

### 1. Finite algebra

The same `rho_+ direct-sum rho_-` Hilbert block admits both:

- an SM-like action where `Cl^+(3)` acts only on the left/chiral block and the
  right block carries only scalars;
- a Pati-Salam-like action where `Cl^+(3)` acts on both chiral blocks.

Both are compatible with the local `Cl(3)` Pauli representation as algebraic
actions. Choosing the SM-like action is therefore an extra algebra-Hilbert
pairing choice, not a consequence of the one-site `Cl(3)` baseline.

The color summand `M_3(C)` is even more visibly absent from the one-site
qubit algebra: a faithful fundamental color factor requires an added
three-dimensional multiplicity. The four-dimensional `rho_+ direct-sum rho_-`
test block is not divisible by three, so the current local baseline does not
contain the nontrivial `M_3(C)` finite-algebra factor.

### 2. KO-dim-6 real structure

On the same finite block, there are at least two antiunitary involution
choices with `J^2 = +1`:

- `J = K`, which commutes with chirality;
- `J = S K`, where `S` swaps the two chirality blocks, which anticommutes
  with chirality.

The KO-dim-6 sign used by the P-LH route is the second choice. The baseline
does not select it over the first.

### 3. Order-one condition

The order-one condition is also not forced by the baseline. With `D = 0`, the
order-one double commutator is vacuously zero for both SM-like and
Pati-Salam-like finite actions. With an off-diagonal mixing `D`, the verdict
depends on the separately chosen finite algebra and opposite-action data.
Thus the order-one test is a spectral-triple structure imposed on top of the
baseline, not a theorem of `Cl(3)/Z^3` alone.

## Consequence For The P-LH Parent

This note partially answers the audit blocker by pruning the no-new-axioms
derivation route for the NCG primitive packet on the tested current baseline.
It does not derive SM LH/RH content, does not approve any substrate primitive,
and does not import the Connes-Chamseddine package into the framework.

The remaining ways to close the parent route are therefore explicit:

1. derive the finite algebra, order-one condition, and KO-dim-6 real structure
   from another retained framework-native bridge not used here; or
2. explicitly approve/register the needed NCG structures as primitives; or
3. find a different route to the SM LH/RH content problem that avoids these
   NCG imports.

## Firewalls

- No new axiom or primitive premise is introduced.
- No audit ledger, queue, or effective-status file is changed.
- This note is not a framework-derived SM LH/RH content theorem.
- This note is not an approval of order-one, KO-dim-6, or
  `C + Cl^+(3) + M_3(C)` as framework primitives.
- The boundary is scoped to the finite Pauli-representation and current
  minimal-axiom baseline checked by the runner.

## Verification

Run:

```bash
python3 scripts/frontier_p_lh_ncg_primitive_underdetermination_2026_06_18.py
```

The expected result is `FAIL=0`.

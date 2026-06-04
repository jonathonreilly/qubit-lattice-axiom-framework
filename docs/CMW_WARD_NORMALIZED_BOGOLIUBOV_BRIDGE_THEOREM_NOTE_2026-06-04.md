# CMW Ward-Normalized Bogoliubov Bridge Theorem

**Date:** 2026-06-04
**Type:** positive_theorem
**Claim type:** positive_theorem (exact finite-volume support theorem under W1-W4 hypotheses)
**Status authority:** independent audit lane only.
**Runner:** `scripts/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.py`

## Artifact Chain

- [`scripts/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.py`](../scripts/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.py)
- [`logs/runner-cache/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.txt`](../logs/runner-cache/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.txt)
- [`outputs/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.json`](../outputs/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.json)

## Purpose

This note supplies the bridge missing from the low-dimensional CMW
sublattice row: the finite-volume implication from a divergent lattice IR sum
to vanishing continuous-symmetry order parameter, after the order operator and
charge mode are Ward/commutator normalized with constants independent of the
box size.

This is not a new axiom and not a textbook import. The external
Mermin-Wagner/Hohenberg/Bogoliubov literature remains parallel context. The
load-bearing statement below is a finite-volume inequality on the framework
`Z^d` Fourier boxes.

## Setup

Let `Lambda_L = (Z/LZ)^d`, `V = L^d`, and

```text
E_k = 2 sum_mu (1 - cos k_mu),        k_mu = 2 pi n_mu / L.
```

Let `H_L` be a finite-volume Hermitian Hamiltonian with Gibbs state
`rho_beta`, `beta > 0`. Suppose there are finite-volume Fourier operators
`A_k` and `Q_k`, and a real order parameter `m_L`, satisfying constants
`c_W, C_A, C_H > 0` independent of `L`:

```text
W1. Ward/commutator lower bound:
    |<[Q_k, A_-k]>_beta| >= c_W V |m_L|     for every k != 0.

W2. Susceptibility/onsite anticommutator bound:
    (1/V^2) sum_{k != 0} <{A_k, A_k^dagger}>_beta <= C_A.

W3. Local double-commutator bound:
    <[[Q_k, H_L], Q_k^dagger]>_beta <= C_H V E_k.

W4. Finite Gibbs-state Bogoliubov inequality:
    |<[Q_k, A_-k]>_beta|^2
      <= (beta/2) <{A_k, A_k^dagger}>_beta
                    <[[Q_k,H_L],Q_k^dagger]>_beta.
```

The volume factors above match the unnormalized Fourier convention
`A_k = sum_x e^{ikx} A_x` and `Q_k = sum_x e^{ikx} q_x`. With a normalized
Fourier convention the same theorem is obtained by absorbing the corresponding
power of `V` into `c_W`, `C_A`, and `C_H`; the only invariant requirement is
that these constants do not grow with `L`.

## Theorem

Define

```text
I_d(L) = (1/V) sum_{k != 0} 1/E_k.
```

Under W1-W4,

```text
|m_L|^2 <= (beta C_A C_H) / (2 c_W^2 I_d(L)).                 (1)
```

Consequently, if `I_d(L) -> infinity` along the thermodynamic sequence, then
`m_L -> 0`.

For the framework lattice dispersion:

- `d = 1`: `I_1(L)` diverges linearly;
- `d = 2`: `I_2(L)` diverges logarithmically;
- `d >= 3`: the infrared integral is finite at the origin.

Therefore any one- or two-dimensional framework sublattice whose local
Hamiltonian/order pair satisfies W1-W4 has no finite-temperature
continuous-symmetry order parameter in the thermodynamic limit.

## Proof

For each nonzero `k`, combine W1, W3, and W4:

```text
c_W^2 V^2 |m_L|^2
  <= (beta/2) <{A_k,A_k^dagger}>_beta C_H V E_k.
```

Rearrange:

```text
<{A_k,A_k^dagger}>_beta / V
  >= (2 c_W^2 |m_L|^2) / (beta C_H E_k).
```

Average over nonzero momenta and use W2:

```text
C_A
  >= (1/V^2) sum_{k != 0} <{A_k,A_k^dagger}>_beta
  >= (2 c_W^2 |m_L|^2 / beta C_H) I_d(L).
```

This gives (1). If `I_d(L)` diverges, the right-hand side forces
`|m_L| -> 0`.

The dimension threshold for `I_d` is the lattice IR-sum threshold already
checked in
[`AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md)
and
[`MERMIN_WAGNER_BOGOLIUBOV_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](MERMIN_WAGNER_BOGOLIUBOV_TEXTBOOK_IMPORT_NOTE_2026-05-18.md).

## Boundary

This bridge proves the implication once W1-W4 are supplied. It does not prove
that every Hamiltonian with an abstract continuous symmetry automatically has
the required local order operator, Ward lower bound, finite susceptibility, and
local double-commutator constant. Downstream notes must carry those hypotheses
explicitly or supply a separate operator-construction theorem.

The bridge does not use observed values, fitted selectors, or a new framework
axiom.

## Verification

Run:

```bash
python3 scripts/cmw_ward_normalized_bogoliubov_bridge_2026_06_04.py
```

Expected summary:

```text
SUMMARY: CMW WARD BRIDGE PASS=17 FAIL=0
```

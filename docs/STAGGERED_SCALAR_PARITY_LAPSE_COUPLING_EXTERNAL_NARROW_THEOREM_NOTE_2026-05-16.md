# Staggered Scalar Parity / Lapse Coupling Algebra Certificate

**Date:** 2026-05-16; scope repair 2026-05-26
**Claim type:** bounded_theorem
**Runner:** `scripts/frontier_staggered_scalar_parity_lapse_coupling_external_narrow.py`
**Status:** bounded algebraic certificate for the stated staggered operator
forms. This is not a literature-correctness theorem and not a derivation from
the framework axioms.

## Purpose

The earlier row tried to identify the parity and lapse forms as externally
authoritative staggered scalar couplings. Audit correctly found that the
packet did not provide the load-bearing external source text or a bridge
proving that identification.

This repair keeps only the algebra the runner verifies. The result is useful
as an operator-form certificate:

- if a staggered sign `epsilon(x) = (-1)^{sum_i x_i}` is used;
- if the parity diagonal, identity diagonal, and lapse symmetrization below
  are the forms under comparison;
- then their exact finite-site identities and distinctions follow.

No external literature authority is load-bearing in this repaired row.

## Definitions

For a finite regular lattice site `x = (x_1, ..., x_d)`, define

```text
epsilon(x) = (-1)^{x_1 + ... + x_d}.
```

For real mass `m`, real scalar profile `Phi(x)`, and Hermitian flat
Hamiltonian `H_flat`, compare three operator forms:

```text
(P)  H_diag_parity(x)  = (m + Phi(x)) * epsilon(x)
(I)  H_diag_identity(x)= m * epsilon(x) + Phi(x)
(L)  H_lapse           = sqrt(N) * H_flat * sqrt(N),
     N(x)              = 1 + Phi(x) / m
```

The lapse form is evaluated where `N(x) >= 0`, so `sqrt(N)` is real diagonal.

## Bounded Claim

The runner verifies these exact algebraic facts with rational arithmetic on
small finite lattices:

1. `epsilon(x)` takes values in `{+1, -1}` and alternates on nearest-neighbor
   sites.
2. `(m + Phi(x)) * epsilon(x)` matches hand-computed parity diagonal values.
3. If `H_flat` is Hermitian and `sqrt(N)` is real diagonal, then
   `sqrt(N) H_flat sqrt(N)` is Hermitian.
4. The parity and identity diagonals differ by
   `Phi(x) * (epsilon(x) - 1)`, hence agree on even sites and differ by
   `-2 Phi(x)` on odd sites.
5. With constant positive `Phi`, the parity diagonal alternates exactly by
   `epsilon`, while the identity diagonal does not.
6. At `Phi(x)=0`, the lapse form reduces exactly to `H_flat`.
7. On odd sites, well/hill ordering under `(P)` is opposite the ordering under
   `(I)` in the tested rational profile; on even sites, the parity ordering is
   the direct sign of `Phi`.

These are finite algebraic identities for the stated definitions.

## Boundary

This row does not claim:

- that `(P)` or `(L)` is the unique or externally correct scalar coupling;
- that any external paper is verified by this packet;
- derivation of these forms from the baseline framework axioms;
- closure of the staggered-Dirac realization gate;
- irregular-graph directional-observable closure;
- trajectory-sign closure;
- continuum-limit or full-GR consequences;
- any new axiom or audit verdict.

Downstream notes may use this row only as a bounded algebraic comparison of
the three displayed operator forms. If a downstream result needs the stronger
claim that `(P)` or `(L)` is forced by external staggered-fermion theory or by
the repo's framework primitives, that stronger bridge must be supplied
elsewhere.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_staggered_scalar_parity_lapse_coupling_external_narrow.py
```

Expected result:

```text
PASS=26 FAIL=0
```

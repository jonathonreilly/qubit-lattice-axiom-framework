# Factor Split Does Not Force a Koide Carrier-Value Bridge

**Date:** 2026-06-02
**Claim type:** no_go
**Review provenance:** source theorem candidate; post-landing review decides the
ledger grade. This note introduces no axiom, primitive, Tier-A admission, matter
attachment rule, or charged-lepton Koide derivation.
**Primary runner:** `scripts/frontier_koide_factor_split_bridge_no_go.py`
(SCORECARD PASS=17)

## Claim

The product-factor algebra alone does not force the Koide carrier-side `Z_2`
choice on the site factor `C^2` to equal the value-side `Z_2` choice on the
generation factor `C^3`.

In the scoped product model

```text
generation value factor C^3  tensor  site carrier pair C^2 tensor C^2,
```

the runner verifies:

1. value-side circulant generation operators commute with the finite
   `C_3` complex-structure orientation on `C^3`;
2. carrier-side hard-core and Jordan-Wigner fermion ladders differ only in the
   cross-site exchange sign on the site pair;
3. value-axis operators on `C^3` commute with carrier-axis operators on
   `C^2 tensor C^2`;
4. both mixed sign sectors are nonempty, so the product algebra permits
   `value=+1, carrier=-1` and `value=-1, carrier=+1`;
5. neither equality nor sign-reversed equality between the two axes follows
   from the product algebra.

Therefore a `C^2`-to-`C^3` bridge is not a consequence of factorization,
commutation, or the shared finite carrier space. A bridge can still be supplied
by a later source theorem or an explicitly approved admission, but it is an
extra welding link, not something this product algebra derives.

## Boundary

This note does not claim:

- the carrier is closed;
- the value bit is derived;
- the statistics bit is derived;
- a future bridge is impossible;
- the two factors are physically unrelated in the final theory.

It only rules out one route: deriving the carrier-value bridge from the bare
factor split and commuting tensor-factor algebra.

## Computation

The runner checks four finite linear-algebra blocks.

First, a generic real antisymmetric generation operator `D` gives Hermitian
`H = iD`, and any value operator acting on `C^3` commutes with any carrier
operator acting on `C^2 tensor C^2` after tensor embedding.

Second, the circulant generation mass algebra commutes with
`Jcs = (C - C^2)/sqrt(3)` for a deterministic grid of real and complex
coefficients. This keeps the orientation datum on the value side.

Third, the single-site ladder `sigma_+` is nilpotent in both hard-core and
fermion readings, while native cross-site ladders commute and Jordan-Wigner
ladders anticommute. The discriminator is a carrier-side exchange sign.

Fourth, the value involution and carrier exchange involution have all four joint
sign sectors nonempty on the product space. That explicit mixed-sector witness
is enough to reject a forced equality relation.

## No-Go Discipline Gate

**Gate result:** PASS for the scoped product-factor no-go only.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Direct equality route | Identify the value involution with the carrier exchange involution on the product space. | Their tensor embeddings are different matrices and both mixed sign sectors are nonempty. | ATTEMPTED |
| Sign-reversed equality route | Identify the value involution with minus the carrier exchange involution. | The opposite mixed sectors are also nonempty, so sign reversal is not forced either. | ATTEMPTED |
| Commutation route | Use tensor-factor commutation to force a shared bit. | Commutation gives simultaneous diagonalization, not equality; the joint spectrum contains all four sign combinations. | ATTEMPTED |
| Value-internal route | Use the circulant value algebra to select the carrier exchange sign. | Circulant value operators commute with `Jcs` on `C^3` and never mention the site exchange sign. | ATTEMPTED |
| Carrier-internal route | Use single-site `sigma_+` data to identify the value orientation. | Single-site data is blind to the cross-site exchange sign and has no generation index. | ATTEMPTED |
| Future welding theorem | Supply an independent relation equating the two signs. | Out of scope and left open; this would be an additional theorem or approved admission, not a consequence of factorization alone. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The collapsed wall set has one wall: the factor split does not impose equality
between the value-side and carrier-side signs. The equality, sign-reversal,
commutation, value-internal, and carrier-internal routes are separate tests of
that one wall, not independent admissions.

### N3 - Hidden-Wall Scan

Phrase scan result: no load-bearing step uses "we assume", "by construction",
"as is standard", "the framework provides", "bridge context", "naturally",
"obviously", or "canonical" as proof support. The note tests a finite product
algebra and leaves any physical welding theorem open.

### N4 - Residual Matching

The residual attacked here is only:

```text
factor split + commuting tensor factors -> carrier-value bridge.
```

It is not the residual of deriving the value bit, deriving CAR statistics,
deriving matter attachment, or deriving `Q = 2/3`. Those remain separate lanes.

### N5 - Rhetoric Audit

"Does not force" is scoped to the product-factor algebra. "Extra welding link"
means an additional theorem or approved admission would be needed to equate the
two signs; it does not mean the bridge is false.

### N6 - Partial-Closure Path Scan

Open paths remain: a source theorem equating the record-side sign with the
generation orientation, a matter-attachment theorem that couples the factors, or
an explicit owner-approved admission. None is called a new axiom here.

### N7 - Steelman

A hostile reviewer can argue that the final physical carrier may carry one
reality structure that acts on both the site and generation factors, so the two
signs should be identified by the physical interpretation rather than by bare
tensor algebra. That is a live route. It supplies exactly the extra welding link
this note says is missing from the product-factor route alone.

### N8 - Cross-Cycle Echo

The recurring failure mode is to verify a factor-local statement and then
promote it into a global carrier closure. This note avoids that echo by keeping
the claim at the factor-local no-go boundary and by leaving both the factor-local
lanes and the possible re-merge theorem open.

## Command

```bash
python3 scripts/frontier_koide_factor_split_bridge_no_go.py
```

Expected output: `SCORECARD: PASS=17 FAIL=0`.

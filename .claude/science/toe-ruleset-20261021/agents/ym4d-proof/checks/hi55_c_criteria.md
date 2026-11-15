# hi55_c — lattice free comparator under Wilson flow (criteria, written before the script; INFORMATIONAL)

Owner: HINT55.md (model claude-opus-5-5). Written 2026-10-28 after HINT55 PRE-STATED, before `hi55_c_latfree.py`
exists. Not load-bearing for any PROVEN claim: it illustrates HINT55 §2.6 (the free lattice Maxwell field, flowed by the
lattice heat flow, has the screening sign at flow times τ ≳ 1 in lattice units). Plain Python, Fractions; rigorous
rational enclosures.

Object. For the noncompact lattice Maxwell field (one colour, unit coupling, any gauge), the plaquette field strength
F̂_μν = p̂_μÂ_ν − p̂_νÂ_μ flows as e^{−τp̂²} (p̂_μ = 2 sin(p_μ/2)), its summed trace is 6 (hi55_a A2 with p → p̂), so
⟨E_lat(τ)⟩ = (3/2)·B(4τ)⁴ with B(x) := e^{−x}I_0(x) = ∫_{−π}^{π}e^{−x(1−cos p)}dp/(2π). Define the dimensionless
F_lat(τ) := τ²B(4τ)⁴ (so τ²⟨E_lat(τ)⟩ = (3/2)F_lat(τ)); its continuum (τ → ∞) value is 1/(64π²), so that
τ²⟨E_lat⟩ → 3/(128π²), the continuum value of hi55_a A4. (Edited for wording before the script existed.)

Enclosure. I_0(x) = Σ_k (x/2)^{2k}/(k!)², summed to K terms with the tail bounded by 2·(last term) once the term ratio is
≤ 1/2; e^{−x} enclosed by 1/(upper and lower partial sums of e^x with the same tail rule); π² enclosed by
[9.8696044010, 9.8696044011] (from π ∈ [3.14159265358, 3.14159265359]).

**C1 (screening sign, τ ≥ 1).** F_lat strictly decreasing along τ ∈ {1, 2, 4, 8, 16, 32, 64}: each upper enclosure at the
larger τ is below the lower enclosure at the smaller τ. PASS iff all six comparisons hold.
**C2 (designed contrast, lattice regime).** F_lat strictly increasing along τ ∈ {1/32, 1/16, 1/8}. PASS iff both hold
(the C1 gate can fail; the lattice-scale regime is not in the continuum comparator class).
**C3 (approach to the continuum constant).** For τ ∈ {32, 64}: 64π²F_lat(τ) − 1 ∈ [1/(16τ), 1/(4τ)] (consistent with the
expansion 1 + 1/(8τ) + O(τ^{−2}); window pre-registered as a factor 2 either side). PASS iff both enclosures lie inside.

Verdict: informational PASS/FAIL per item; recorded in HINT55 §8 with no load-bearing use.

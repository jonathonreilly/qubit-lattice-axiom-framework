# Generalized entropy bookkeeping: boundary of the former GSL claim

**Date:** 2026-05-01; source correction 2026-10-21.
**Type:** bounded_theorem (only the stated conditional algebra; no physical entropy theorem)
**Source scope:** conditional entropy balance, not a derivation of the GSL.
**Status authority:** independent audit lane only; no audit verdict is set here.
**Runner:** `scripts/axiom_first_gsl_check.py`

## Withdrawn inference

The previous proof added an area increase to a claimed nonnegative matter
entropy change. In a generalized entropy, the matter term is the **exterior**
entropy S_out. It can decrease when matter crosses the horizon. Evolution
of the exterior alone was not shown to be a unital channel on a fixed
Hilbert space. A finite-dimensional unital-channel entropy inequality does
not establish that missing premise. A Gibbs/KMS equilibrium condition alone
also does not imply relaxation or monotone entropy under arbitrary dynamics.

Thus the old composition did not prove the GSL. Its evaporation corollary
used decreasing area and lies outside its classical area-increase argument.
The generic appeal to quantum energy inequalities did not supply a
semiclassical proof. The information bound and information-paradox
corollaries are withdrawn with that inference. This is a correction to the
argument, not a claim that the GSL itself is false.

The original source is recoverable at commit
`f24d17d97d372df977476e4a69674577f31af575`. The filename remains for stable
references. Historical upstream citations below confer no current retained
status in this source.

## Surviving conditional calculation

In units hbar=c=k_B=1, supply G>0 and the area-entropy relation:

```
S_gen = A/(4G) + S_out,
Delta S_gen = Delta A/(4G) + Delta S_out.
```

For an idealized absorption with no other exterior entropy change, write
`Delta S_out=-S_in`. Then the desired inequality is precisely

```
Delta A/(4G) >= S_in.
```

It is an additional condition, not a consequence of `Delta A>=0` alone.
For a supplied Schwarzschild mass change M->M+E the area formula gives
`Delta S_BH=8 pi G M E + 4 pi G E^2`. This is algebra under supplied
geometry; deriving physically permitted S_in and the actual process is
separate work. The runner displays both satisfying and violating numerical
assignments. A violating assignment tests the inference, not the physical
realizability of a GSL violation.

For evaporation, the required balance is `Delta S_out>=-Delta S_BH`.
Assigning radiation entropy to satisfy it is not a derivation of radiation
entropy. No Hawking spectrum or semiclassical GSL proof is supplied here.

## Verification and open obligations

The runner checks the area formula, the balance identity, an exterior-entropy
loss example and controls on both sides of the required threshold. It does
not label a hardcoded entropy increase a theorem test.

A physical GSL derivation would need an applicable horizon/state framework,
a defined exterior entropy (including regularization where required), and
an argument that controls its change together with the gravitational term.
Those hypotheses and dynamics are not discharged by this packet. Neither a
Bekenstein bound nor a GSL proof may be obtained by circularly citing the
other note in this pair.

## Citations

- A_min: [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
- Block 01 KMS: [`AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md)
- Block 02 Hawking: [`AXIOM_FIRST_HAWKING_TEMPERATURE_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_HAWKING_TEMPERATURE_THEOREM_NOTE_2026-05-01.md)
- Block 05 First law: [`AXIOM_FIRST_FIRST_LAW_BH_MECHANICS_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_FIRST_LAW_BH_MECHANICS_THEOREM_NOTE_2026-05-01.md)
- historical BH 1/4: [`BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md`](BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md)
- historical framework GR: [`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md)
- historical external references (not a proof of the withdrawn composition):
  Hawking (1971) *Phys. Rev. Lett.* 26, 1344 (area theorem);
  Penrose (1965) *Phys. Rev. Lett.* 14, 57;
  Bekenstein (1973) *Phys. Rev. D* 7, 2333 (GSL proposal);
  Ford-Roman (1995) *Phys. Rev. D* 51, 4277 (quantum energy bounds).

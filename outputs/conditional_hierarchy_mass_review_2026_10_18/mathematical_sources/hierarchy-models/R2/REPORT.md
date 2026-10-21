# Complete exercise argument with controlling corrections

Original source: `.claude/science/exercises/hierarchy-wall-20261018/R2/REPORT.md`; exact SHA-256 `26d66bcf8e6af4b8eebfe4735e15a7919819be7957acc0bd51c7cebde839adbb`.

**Controlling scope:** Periodic XOR finite-support statements retain periodic hypotheses. The uniform-background finite-support classification {1,2,4,8,infinity} is historical/unverified here: the report layer argument does not supply its complete lower-bound proof. Finite SAT and path-sum results do not establish all-size minimality or universal detuning effects. Chamon codes and perturbation classes are supplied comparators.

**Source-use boundary:** The complete argument below is preserved for inspection, including its original qualifications and counterexamples. Its old verdict labels, claims of completed reviews, operational history and numerical outputs are historical provenance only. Terminal physical exclusions and claims stronger than the controlling scope are deferred, not active conclusions. The canonical conditional exercise note and its correction register control. This attachment is not a separately promoted scientific claim and is not a fresh replay of its exploratory computations.

---

I read the four refresher files in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`, `PRIMITIVE_REGISTRY_CHECK.md`, `SCALE_REFERENCE_PRIMITIVE_NOTE.md` and `derivation_obligations.json`. The JSON has no hierarchy entries, only the three AC/theta obligations. I also read the wall, the HIER-1 and HIER-3 reports on the PR #9783 branch, and main's 2026-10-17 note on the Chamon stabilizer rule.

## Plain answer

**Short answer:** for a vacuum scale such as v, no, unless a whole number for the size of a finite region is supplied. For other kinds of small number, partly yes.

- **What works.** A fixed nearest-neighbour rule can set a large whole number by itself: the smallest move it allows can involve 18 to 62 sites. Then a tunnelling amplitude of 1e-15 needs a perturbation of only ε/J ≈ 0.14–0.6.
- **What fails.** In every case found, the two end states differ in energy already at second order. So the tiny amplitude only sets how slowly a heavy local object moves. It is not a small gap or a vev.
- **Vacuum scales.** A finite move can never connect two symmetry-related vacua. So a tiny vacuum splitting needs a finite region size L, and the axioms do not supply one.

The other tools in my tradition contribute no route:
- **Kondo and transmutation** are already covered by HIER-1(b) and HIER-3.
- **Order by disorder** gives energies of order ε²/J. That is the detuning measured below, not a source of small numbers.
- **Lieb–Schultz–Mattis** (suggested; template from Po–Watanabe–Jian–Zaletel 2017): under the soldered rotation action each qubit carries a projective representation of the cubic group, so a symmetric vacuum with a unique gapped ground state is excluded. That protects exact zeros. It does not make small nonzero numbers.

**Prior art on main.** There are no hits for tunnelling splitting, order by disorder, Kondo, Lieb–Schultz–Mattis or a minimal-flip classification. The "code distance" hit is unrelated. Already mapped:
- the Chamon rule as the unique soldered rule, with log₂ degeneracy 4L (10-17 note);
- ring exchange at orders 4–6 in the cubic-ice notes;
- E3, "first breaking at order n ≥ 15", listed as an open escape in HIER-1.

## Route 1: the rule itself sets the tunnelling order

**Declared model, not axiom content.**
- A one-bit support rule: a set of allowed 7-site star patterns, closed under the 24 proper rotations, acting trivially or with the sign twist (bit flip for rotations whose axis permutation is odd).
- A penalty J for each violated star, plus a field ε ΣX.
- If two valid configurations differ on a minimal flip S of n sites, the leading amplitude is t = C_n εⁿ/Jⁿ⁻¹.

**Results.**

- **Lemma 1 (proved).** From a uniform background, the minimal finite flip is 1, 2, 4, 8 or ∞ sites.
  - Proof: take the site of S that maximises a generic positive linear function. Its in-S neighbours lie inside one corner triple.
  - Single site, domino, 2×2 square and 2×2×2 cube realise the four finite values. A layer argument gives the lower bounds.
- **Lemma 2 (proved, elementary).** Take two periodic configurations c and g·c, with g a lattice symmetry, possibly with a bit flip. If they differ on only a finite set, they are equal. Reason: their XOR is periodic, so finite support means it is zero. A finite flip therefore never links distinct symmetry-related vacua.
- **Exact SAT search (checked).** Over all rules, all period-2 backgrounds, and layered backgrounds of period 3 and 4:
  - Minimal flips of 12, 18 and 22 sites exist, stable from a 5³ to a 6³ box.
  - The Néel background gives 62, stable in 6³, 7³ and 8³ boxes. The 117 found in the 5³ box was a box artefact.
  - Requiring every neighbour condition to allow some centre value (a distribution exists at every site): 18 is stable to 7³. The 5³ maximum of 56 was not stability-checked. Twist-action values (up to 32) were not stability-checked.
  - **So locality does not cap the order.** E3's "n ≥ 15" can be set by the rule alone.

**Exact sum over all n! flip orders (checked):**

| n | C_n^(1/n) | ε/J giving t = 1e-15 J | second-order detuning D2 |
|---|---|---|---|
| 8 | 1.16 | 0.011 | +52 ε²/J |
| 12 | 0.93 | 0.060 | +7.6 ε²/J |
| 18 | 1.02 | 0.143 | +12.4 ε²/J |
| 22 | 0.95 | 0.219 | −9.5 ε²/J |

- There is no factorial enhancement: the energies of the intermediate states grow as the flip proceeds and cancel the n! count. So t/J ≈ (ε/J)ⁿ.
- Extrapolating to n = 62 gives ε/J ≈ 0.57 (suggested, not computed).

**Number it would fix.** A splitting t/J = C_n(ε/J)ⁿ, but only if the two end states were exactly degenerate. They are not: D2 is nonzero in all four cases (checked; the generic case is suggested). So t is an off-resonant mixing, or the bandwidth of a heavy local object. With Lemma 2, no vacuum degeneracy is ever split at finite order. ε and the choice of rule are also unsupplied.

**Strongest objection.** The small number is a heavy object's kinetic scale, not a light mass or vev. At ε/J ~ 0.5, perturbation theory is not reliable.

**Kill condition.** The route dies if no rule has a defect with two symmetry-related internal states that are joined only by a flip of ≥ 15 sites with no valid intermediate state. Such a pair would have D2 = 0 by symmetry and a splitting of about εⁿ; the comparator is tunnel splittings in molecular magnets. Even if such a pair exists, it gives a defect-level scale, not v.

**Cheapest next test.** A SAT search for such symmetric defect pairs (base ⊕ T versus g·(base ⊕ T), g a point-group element), then the same path-sum code. About an hour.

## Route 2: the soldered branch (Chamon) needs a finite region size L

- **Object.** The Chamon rule plus a one-site perturbation. The code space first splits at order d(L), the minimum weight of a nontrivial logical operator.
- **Checked.** d(4) = 4 exactly (search complete to weight 6). d(6) ≥ 5. The code has k = 16 and 24 logical qubits, i.e. 4L, matching main's note.
- **Proved.** From the syndrome polynomial, a two-fracton pair hops at first order: X_r moves {r±y} to {r±z}. Main's note proves an isolated fracton never moves. So the soldered class has no large order fixed by the rule. On Z³ the splitting is exactly zero.
- **Number.** δ/J ~ (ε/J)^{d(L)}, with d ≈ L (Bravyi–Leemhuis–Terhal; comparator). 1e-15 needs L ≈ 15 at ε/J = 0.1, or L ≈ 30 at ε/J = 0.3.
- **Why it is not supplied.** L is not in the axioms. Taking the cosmic size, L ~ 1e61, gives e^(−1e61), and that scale would drift in time.
- **Strongest objection.** It needs a frozen region of 15–50 sites, which is an extra integer. And a code-space splitting is not a vev.
- **Kill condition.** No axiom-level quantity fixes a coherent region of that size.
- **Cheapest test.** Exact d(6) and d(8), plus a check of whether a region bounded by permanent records (main has the record-bounded ring-model note) behaves like a box of fixed distance.

## Named extra numbers

For a vacuum hierarchy from tunnelling, the integer extent L is unavoidable in the classes tested. This is proved for finite flips between periodic vacua; that the endpoints are detuned is checked in four cases and suggested in general. The perturbation strength ε and the rule's identity are also unsupplied. E3 survives only for scales of defects or heavy objects.

Everything was run with `capped.sh`, one process at a time, peak memory 170 MB. Nothing is left running, and no file outside my folder was edited.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/R2/tests/`:
- `PREREG.txt`
- `t1_minflip.py`, `t1b_boxstab.py`, `t1c_neel.py`, `t1e_faithful18.py`
- `t2_pathsum.py`, `t3_chamon_distance.py`
- `*.out`, one log per run
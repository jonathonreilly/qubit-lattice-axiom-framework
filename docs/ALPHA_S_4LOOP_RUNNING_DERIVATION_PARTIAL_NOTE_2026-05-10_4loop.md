# Alpha_s Four-Order Running — Formal-Algebra and Physical-Input Accounting Note

**Date:** 2026-05-10; boundary repaired 2026-07-16
**Type:** bounded_theorem
**Source-note proposal disclaimer:** this note proposes an accounting boundary,
not an audit verdict or a physical running theorem.
**Primary runner:**
[`scripts/cl3_alpha_s_4loop_running_derivation_2026_05_10_4loop.py`](../scripts/cl3_alpha_s_4loop_running_derivation_2026_05_10_4loop.py)
**Cached output:**
[`logs/runner-cache/cl3_alpha_s_4loop_running_derivation_2026_05_10_4loop.txt`](../logs/runner-cache/cl3_alpha_s_4loop_running_derivation_2026_05_10_4loop.txt)

## 1. Repair and question

This row accounts for the four-order running input used by the broader direct
Wilson-loop lane. Earlier wording incorrectly promoted the first two physical
coefficient templates to framework-derived or retained content merely because
their values can be evaluated from supplied symbols. That conflated two
different layers:

1. a QFT layer that supplies a beta-function calculation, coefficient
   templates, a physical gauge/coupling identification, and the interpretation
   of `n_f`; and
2. a formal layer that substitutes exact values into already-defined
   polynomials and forms induced nonnegative variables in an already-defined
   vector field.

The direct formal supplier is
[`ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md`](ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md).
Despite its historical filename, that row now proves only the second layer. It
does not derive a QCD beta function, loop universality, scheme independence,
active-flavour selection, or physical running.

## 2. Explicitly imported physical/QFT layer

A physical four-order running calculation would need, at minimum:

- a physical gauge theory and colour-carrier identification;
- a physical coupling and scale variable;
- the QFT diagrammatic or renormalization argument that produces each
  coefficient template;
- an interpretation and scale-dependent selection rule for `n_f`;
- a renormalization scheme for scheme-dependent higher coefficients;
- threshold matching and boundary data before a physical running value can be
  produced.

None of these inputs follows from defining `C_A=3`, `C_F=4/3`, `T_F=1/2`, or
from evaluating an affine polynomial. They remain explicit inputs or open
bridges in this accounting row.

For orientation only, if one separately supplies the familiar first two
coefficient templates,

```text
b0(n_f) = (11/3) C_A - (4/3) T_F n_f,

b1(n_f) = (34/3) C_A^2
          - 4 C_F T_F n_f
          - (20/3) C_A T_F n_f,
```

then the formal supplier proves their exact specialization at the explicitly
defined packet `C_A=3`, `C_F=4/3`, `T_F=1/2`. The word "supplies" is
load-bearing: neither polynomial is derived here as a physical/QFT law.

## 3. Per-order accounting

| Order | Formal content available from the direct supplier | Physical/QFT content not supplied by that theorem |
|---|---|---|
| **L1 (`b0`)** | Exact simplification `11-2n/3`, values, slope, root, sign window, and induced-variable chain-rule algebra for a defined vector field | Origin of the template as a physical one-loop coefficient; colour/coupling identification; physical meaning and selection of `n_f`; physical running |
| **L2 (`b1`)** | Exact simplification `102-38n/3`, values, slope, root, sign window, and induced-variable chain-rule algebra for a defined vector field | Origin of the template as a physical two-loop coefficient; any universality or scheme-independence theorem; colour/coupling identification; physical meaning and selection of `n_f`; physical running |
| **L3 (`b2`)** | No coefficient template or formal higher-order theorem is supplied by the direct supplier | A specified scheme and the corresponding QFT coefficient calculation remain imported/open |
| **L4 (`b3`)** | No coefficient template or formal higher-order theorem is supplied by the direct supplier | A specified scheme and the corresponding QFT coefficient calculation remain imported/open |

The first two rows are therefore `formal_defined_template_only`, not retained
physical coefficients. The latter two are `physical_coefficient_import_open`.
This repair makes no fractional "import count reduction": the QFT origin and
physical interpretation of L1/L2 remain load-bearing even though the
downstream arithmetic is exact.

## 4. Bounded theorem

**Theorem (formal-algebra/physical-input separation).** Given the explicitly
defined coefficient polynomials and vector field in the direct supplier:

1. the exact substitutions
   `b0(n)=11-2n/3` and `b1(n)=102-38n/3` follow;
2. the exact listed rational evaluations follow;
3. along any real formal trajectory of the defined `g` vector field, the
   induced nonnegative variables `alpha=g^2/(4 pi)` and
   `a=alpha/(4 pi)` have the stated rates by the chain rule; and
4. none of these algebraic implications supplies the QFT origin of the
   templates or the physical semantics enumerated in section 2.

The proof of items 1–3 is the direct supplier's exact `Fraction`/SymPy
certificate. Item 4 is a typed input boundary: the formal packet contains no
field for QFT origin, physical colour, active-flavour selection, scheme
independence, threshold placement, or physical coupling/running.

This is a bounded accounting theorem. It is not a claim that the missing QFT
or physical bridges are impossible to derive. No global no-go is asserted for
L1–L4, and this note does not treat an absent current supplier as an
impossibility proof.

## 5. Exact formal checks, not physical comparators

The direct supplier proves, as formal polynomial evaluations,

```text
b0(6)=7,       b0(5)=23/3,
b1(6)=26,      b1(5)=116/3,
b1(4)=154/3,   b1(3)=64.
```

These values are not presented as framework predictions or experimental
matches. The arguments `3,4,5,6` are rational inputs to the defined
polynomials; this row does not infer that a physical threshold realizes any
one of them.

No observed `alpha_s(M_Z)`, quark mass, threshold, Sommer scale, or fitted
matching coefficient is used by the proof.

## 6. Audit-readable proposed scope

```yaml
proposed_claim_type: bounded_theorem
proposed_claim_scope: |
  Exact accounting separation for a supplied two-coefficient polynomial
  vector field. The direct supplier proves formal substitutions, rational
  evaluations, slopes, roots, sign windows, and two induced-variable
  identities. It supplies no physical QCD beta-function origin, loop
  universality, scheme independence, physical colour/coupling bridge,
  active-flavour interpretation or selector, thresholds, or physical running.
  L1 and L2 are formal_defined_template_only; L3 and L4 remain
  physical_coefficient_import_open. No no-go and no audit verdict is proposed.

per_order_accounting:
  L1_b0:
    accounting_class: formal_defined_template_only
    exact_polynomial: "11 - 2*n/3"
    formal_outputs:
      - defined_b0_polynomial
      - exact_rational_evaluations
      - exact_slopes_roots_signs
      - defined_induced_variable_identities
    physical_requirements:
      - one_loop_qft_calculation
      - qft_coefficient_origin
      - physical_colour_carrier
      - physical_coupling_identification
      - physical_nf_interpretation
      - scale_dependent_nf_selector
      - physical_scale_variable
      - threshold_matching
      - boundary_data
    physical_origin: explicit_input_or_open_bridge
  L2_b1:
    accounting_class: formal_defined_template_only
    exact_polynomial: "102 - 38*n/3"
    formal_outputs:
      - defined_b1_polynomial
      - exact_rational_evaluations
      - exact_slopes_roots_signs
      - defined_induced_variable_identities
    physical_requirements:
      - two_loop_qft_calculation
      - qft_coefficient_origin
      - scheme_independence_theorem
      - physical_colour_carrier
      - physical_coupling_identification
      - physical_nf_interpretation
      - scale_dependent_nf_selector
      - physical_scale_variable
      - threshold_matching
      - boundary_data
    physical_origin: explicit_input_or_open_bridge
  L3_b2:
    accounting_class: physical_coefficient_import_open
    formal_template_in_direct_supplier: absent
    formal_outputs: []
    physical_requirements:
      - three_loop_qft_calculation
      - qft_coefficient_origin
      - renormalization_scheme
      - physical_colour_carrier
      - physical_coupling_identification
      - physical_nf_interpretation
      - scale_dependent_nf_selector
      - physical_scale_variable
      - threshold_matching
      - boundary_data
  L4_b3:
    accounting_class: physical_coefficient_import_open
    formal_template_in_direct_supplier: absent
    formal_outputs: []
    physical_requirements:
      - four_loop_qft_calculation
      - qft_coefficient_origin
      - renormalization_scheme
      - physical_colour_carrier
      - physical_coupling_identification
      - physical_nf_interpretation
      - scale_dependent_nf_selector
      - physical_scale_variable
      - threshold_matching
      - boundary_data

declared_one_hop_deps:
  - alpha_s_universal_two_loop_beta_kernel_theorem_note_2026-06-18

forbidden_promotions:
  - formal_polynomial_to_physical_qcd_beta_function
  - defined_n_to_active_flavour_selector
  - exact_coordinate_identity_to_physical_running
  - absent_current_supplier_to_global_no_go
```

## 7. Verification

Run:

```bash
python3 scripts/cl3_alpha_s_4loop_running_derivation_2026_05_10_4loop.py
```

The runner imports the direct supplier's executable formal certificate,
rechecks the exact identities, computes the missing physical-input sets, and
guards the consumer note against reintroducing the historical promotion
phrases. It does not apply an audit verdict.

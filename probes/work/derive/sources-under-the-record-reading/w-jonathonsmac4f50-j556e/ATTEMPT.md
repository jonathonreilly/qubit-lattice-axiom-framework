# sources-under-the-record-reading, attempt 3 of 4: records-only fits the axioms; formation must reprice the record, locally; an executed discriminator

Worker `w-jonathonsmac4f50-j556e` (`claude-opus-5-5`), unit `J-derive-sources-under-the-record-reading:a3`.

**Provenance.**
- a1 and a2 left nothing on `ai/probes`.
- The task names blocks 53–55; block 56 (PR #8573) supplies the box, the exact strong-field law and the ledger `Σ m_x φ_x`.
- Two later blocks of the same campaign are relevant. Both are by my model family, unrefereed, and not named in the task:
  - block 58 (PR #8579) already holds the exact kept-ledger condition for a formation event (T1), and "a monopole from nothing"
    under records only (T4);
  - block 67 (PR #8598) holds the curvature-member version.
- Both blocks explicitly leave open whether an unrecorded amplitude sources anything. This attempt:
  - re-derives the parts of (b) it needs;
  - adds the weak-field formula, the average over arbitrary odds, and an exact **locality** identity;
  - does (a), (c) and (d).
- I read the axioms memo in full this session.
- The parked statistical postulate is not assumed, adopted or raised. The discriminator names its conditions on formation.

## 1. What is claimed

**Setting (block 56).**
- The simplest bond energy is `F = (2/γ)Σ(φ_x − φ_y)²`, with walls held at the ambient rate `φ = 1`.
- Bodies at rest have bare energies `m_x`, and the exact law is `((1 − A) + (γ/12)M)φ = 0` inside.
- The ledger is `L = Σ m_x φ_x`, and `g = (1 − A)⁻¹` with the walls held.

> **(a) Records only.**
> - A packet that has formed no record sources nothing. It is pulled with block 54's force `−e∇u` and pulls nothing back.
> - With records at rest (the Record axiom's permanence), the packet's momentum changes and nothing else does. The pair does not
>   conserve momentum: the records' field acts as an external field that never feels the packet.
> - The ledger `⟨H_w⟩ + F[records]` is then kept, but only trivially: `H_w` is static, so `⟨H_w⟩` is conserved, and `F` does not
>   depend on the packet.
> - If records move (the owner's reading of 2026-09-20), the field changes in time. The packet's energy then changes at
>   `Σ_x e_x du_x/dt` (block 55 T1), and no source term balances it. So the ledger drifts at `Σ e_packet du/dt` (block 55 T2(b)
>   with `s` the records' source).
> - At formation the field acquires a monopole from nothing (block 58 T4).
>
> **(b) The formation event.** An amplitude at rest (weights `ρ`, bare energy `E`, ledger `L`) is replaced by one record at `y`.
> - **Exact:** the ledger is kept iff the record's bare energy is `m' = L/(1 − (γ/12) g_yy L)`, which requires
>   `L < 12/(γ g_yy)` (block 58 T1).
> - **Weak field:** `L = E − (γ/12)E²⟨ρ, gρ⟩ + O(γ²)`. A record keeping the bare energy loses `(γ/12)E²(g_yy − ⟨ρ, gρ⟩) > 0` of
>   ledger. That is the field's self-energy change, exactly in terms of the potential of `1 − average` (`g_yy → G₀(0) = 1.5164`
>   on `Z³`).
> - **On average, with no rule for where the record forms:** over any odds `p`, the required mean excess is
>   `(γ/12)E²(Σ_y p_y g_yy − ⟨ρ, gρ⟩)`.
>   - On `Z³` this is `≥ 0` for **every** odds: there `g_yy = G₀(0)` for every `y`, and `g_xy ≤ G₀(0)` by Cauchy–Schwarz. A
>     formation event must on average make the record heavier.
>   - In a box it can have either sign. Example: weight 99/100 at the centre and 1/100 at a corner, with odds at that corner.
> - **Locality (exact, new):** for an amplitude symmetric about the formation site, in a box symmetric about it, the record energy
>   that keeps the ledger is **independent of the walls**. It is `1188/1091` for the uniform 7-site star at `γ = 1`, in both the 5³
>   and 7³ boxes; the centre-heavy star and `γ = 7/3` behave the same way, and lopsided weights break it.
>
> **(c) An executed discriminator.** It uses only the test body's formed records.
> - A test packet of block 54's walk passes an **unrecorded** source lobe.
> - Under **(a)** the rates stay ambient, so the test body's transverse centre follows the free walk.
> - Under **(c)** (mean-field amplitude sourcing) it shifts toward the lobe: by `1.06, 2.17` sites at `γE = 1, 2` after `t = 36`.
>   The mirror placement gives `−2.00`.
> - The discriminator needs four conditions, named and not assumed:
>   1. the test body forms records along its path whose mean transverse position follows its amplitude's centre (for example, odds
>      proportional to `|χ|²` or to `|χ|²φ`, which differ at `O(γ)`);
>   2. the source forms no record during the passage;
>   3. the field is static during the passage;
>   4. the test body is light (its own sourcing is negligible).
>
> **(d) The axioms, sentence by sentence** (a reading, not a proof). Records-only is compatible with every sentence of the Record
> and Qualification axioms. Amplitude sourcing is compatible only if the amplitude counts as part of the state or of a law's
> supplied condition (table in §2, step 6).

## 2. The steps

1. **PROVED + CHECKED (B1): (b) exact, and at weak field.**
   - One body at `y` (Sherman–Morrison on the rank-one `M`): `φ_y = 1/(1 + (γ/12) g_yy m')`, so the ledger is
     `m'/(1 + (γ/12) g_yy m')` (block 56 T3). Setting it equal to `L` gives `m'`.
   - Weak field: `φ = 1 + δ` with `δ = −(γ/12) g M(1 + δ)` (Neumann series), so `L = E − (γ/12)⟨m, g m⟩ + O(γ²)`.
   - Checked exactly on held-wall boxes 5³ and 7³, for the 7-site star with `E = γ = 1`: the ledger identity, `m' > E`, and at the
     centre and an arm.
   - Checked on the 5³ box with an exact solve at `γ = 10⁻⁶`: the first-order coefficients `−⟨ρ, gρ⟩/12` and
     `−(g_yy − ⟨ρ, gρ⟩)/12`, to `10⁻⁵`.
2. **PROVED + CHECKED (B2): the average over odds.**
   - `g` is positive definite. For `p = ρ`: `⟨ρ, gρ⟩ ≤ Σ_y ρ_y g_yy`, since `g_xy ≤ (g_xx + g_yy)/2`.
   - On `Z³`, `g_yy = G₀(0)` for all `y`, and `|g_xy| ≤ G₀(0)`. So `Σ_y p_y G₀(0) − ⟨ρ, gρ⟩ ≥ 0` for every `p` and `ρ`.
   - Checked exactly on the 7³ box: the star, and the centre-and-corner counterexample `g_corner = 1.11341 < 1.34676`. Also a
     sample of Cauchy–Schwarz inequalities, compared as squares.
3. **PROVED + CHECKED (B3): locality.**
   - Let `H = g_box − g_{Z³}` be the walls' correction. It is discrete-harmonic in each argument inside the box. By the mean-value
     property at the star's centre, `avg_arms H(·, arm) = H(·, c)`.
   - If the box is symmetric about `c` and the charges are symmetric, `H` acts on them as the constant `H(c,c)·J`.
   - A constant shift of `g` over the support changes `1/L` and `(γ/12) g_cc` by the same amount (Sherman–Morrison on `J`). So
     `1/m' = 1/L − (γ/12) g_cc` does not change.
   - Checked exactly in two boxes, at two couplings, for two symmetric weightings. The lopsided control differs:
     `1.0823595` against `1.0822232`.
4. **PROVED (from blocks 54 and 55, both same family and unrefereed): (a).**
   - The force `−e∇u` acts on the packet, and records do not respond to it (records only).
   - `d⟨H_w⟩/dt = Σ e du/dt` along any motion (block 55 T1).
   - The ledger's rate is `Σ(e − s) du/dt` (block 55 T2(b)), with `s = 0` on the packet.
5. **NUMERIC (C1): (c).** Block 54's walk on a 48×24×4 torus. The field comes from `u − Au = −(γ/6)(e − ē)`, solved by FFT, with
   a Gaussian lobe of width 1.5 placed 5 sites off the path. The packet has `k = 0.6` along `x` and width 2; it is evolved with
   `expm_multiply`.
   - The transverse centre is compared with the ambient run, and the shift grows about linearly in `γE`.
   - The observable is the centre of the test body's records, under conditions 1–4.
6. **Argued: (d)**, from the memo read in full.

   | sentence | records only (a) | amplitude sources (c) |
   |---|---|---|
   | "Records form." | fits | fits |
   | "When present, a record locks exactly one admissible local possibility." | the source is a locked, local datum | the source is an unlocked density |
   | "A site never carries more than one record; records are permanent." | permanent sources: a static field between events, a monopole at each event | fits |
   | "Only records are readable. … A site with no record cannot be read." | clocks, and so other bodies' records, depend on records only | an unrecorded site changes readable records of other bodies: read indirectly (step 5 is such a reading) |
   | "A state is a configuration of records." | the field is a function of the state | the field depends on amplitudes, which are not in the state |
   | "A law … at every state where the condition holds … gives exactly one answer." | one field per record configuration | many fields per record configuration, unless the amplitude is part of the condition |
   | "Further physical structure requires a retained derivation or bridge …" | a supplied reading | a supplied reading |

## 3. Where this stops

- **(a)'s price is structural.** Under records only, an unrecorded body is pulled and does not pull. Action and reaction fail until
  it forms records, and every formation event creates a monopole (block 58 T4). Whether that is acceptable is the owner's call.
- **(b)** is exact on boxes and at weak field, for bodies at rest. Moving amplitudes and the curvature member (block 67) are not
  treated here.
- **(c)**'s discriminator is conditional on formation conditions 1–4. It is a proposal for an experiment in the executed sense,
  not a derivation.
- **(d)** is a reading of the sentences, not a theorem.

## 4. What would finish it

1. The owner's decision between records-only and amplitude sourcing. The (d) table favours records-only on the memo's wording.
2. Under records only, a law for how the field follows a formation event: it is static here, and block 57's delay is one
   candidate. Also, where the momentum goes when an unrecorded body is pulled.
3. The locality identity for general amplitudes. The lopsided control shows it needs the symmetry; its size without symmetry is
   the dipole jump of block 58 T3.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/sources-under-the-record-reading/w-jonathonsmac4f50-j556e/check.py
```

- It has 4 lines: B1–B3 exact (sympy rationals on held-wall boxes) and C1 labelled NUMERIC (numpy/scipy).
- It runs in about 20 seconds.

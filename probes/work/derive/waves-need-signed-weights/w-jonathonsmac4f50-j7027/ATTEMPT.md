# waves-need-signed-weights, attempt 1 of 5 — Wielandt is not needed

Worker `w-jonathonsmac4f50-j7027` (`claude-opus-5`), unit `J-derive-waves-need-signed-weights:a1`.

**Provenance.** Four prior attempts exist. Three (`j62b1`, `jafb3`, `j841b`) are the same model
family, machine and running worker as this one, and `j841b` is **mine**, finished earlier in this
same session. The fourth (`w-macbookpro90c72-jf9e6`) is from another machine. I re-run none of
their routes. My own `a3` (issue #8535) flagged that **Wielandt's equality case is ASSUMED in every
treatment of (a) so far** — scalar, one-level and many-level — which makes the classification half
of (a) conditional lane-wide, and listed as its item 1: *re-prove it at this scope or replace it*.
This attempt replaces it.

## 1. What is claimed

> **Theorem.** Let `C` be nonnegative irreducible with `ρ(C) = 1`, and `B` complex with `|B| ≤ C`
> entrywise. If `Bx = λx` with `x ≠ 0` and `|λ| = 1`, then `|B| = C` **entrywise**.
>
> **Proof.** Entrywise, `|x| = |λ||x| = |Bx| ≤ |B||x| ≤ C|x|`, so `C|x| ≥ ρ(C)|x|` with `|x| ≥ 0`,
> `|x| ≠ 0`. By the lemma below, `C|x| = |x|` and `|x| > 0`. Then every inequality in the chain is
> an equality, so `(C − |B|)|x| = 0` with `C − |B| ≥ 0` and `|x| > 0`, forcing `C − |B| = 0`. ∎
>
> **Lemma.** `C` nonnegative irreducible, spectral radius `ρ`; `y ≥ 0`, `y ≠ 0`, `Cy ≥ ρy`. Then
> `Cy = ρy` and `y > 0`.
> **Proof.** Perron–Frobenius gives a strictly positive **left** eigenvector `v`, `vᵀC = ρvᵀ`.
> Then `vᵀ(Cy − ρy) = 0` while `Cy − ρy ≥ 0` and `v > 0`, so `Cy − ρy = 0`. Positivity of `y`
> follows from `(I + C)^{n−1}y > 0`. ∎

For nonnegative weights, `|B_{mn}| = C_{mn}` says `|Σ_y w(y)_{mn}e^{−iky}| = Σ_y w(y)_{mn}`, which
on an **open set** of `k` holds only if that entry has a single displacement. **That is condition
(i), and the only import left is ordinary Perron–Frobenius — not its equality case.**

## 2. The steps

1. **Q1.** Statement of what (a) uses: only the entrywise half of Wielandt's conclusion.
2. **PROVED + CHECKED (`Q2`).** The sub-eigenvector lemma. Checked on three gain-one companions
   (diffusive one-level, two-level chain, two-component one-level): `ρ(C(0)) = 1` and the left
   `1`-eigenvector has all entries of one sign.
3. **PROVED + CHECKED (`Q3`).** The squeeze, with three examples on both sides of condition (i):
   - *rigid transport* (two-component, two-level): `|C(k)| = C(0)` entrywise — (i) holds, and this
     rule is unimodular at every `k`;
   - *single-site but mixing*: `|C(k)| = C(0)` entrywise **also** — (i) holds, yet every branch is
     strictly inside the circle. So **(i) is necessary and not sufficient**, and this is precisely
     where condition (ii) does its work — the same point my `a3` made from the other direction;
   - *two displacements in one entry* (the diffusive rule): `|C(k)| ≠ C(0)` — (i) fails, so by the
     theorem no branch can be unimodular.
4. **CHECKED (`Q4`).** Irreducibility is a **real** side condition, not automatic: a two-level rule
   whose deepest weight vanishes has a **reducible** companion. Such a rule is really of smaller
   depth, so the honest statement is "`J` is the true depth, and then irreducibility of the
   companion reduces to irreducibility of `A`" — which is the hypothesis `j62b1` already makes. For
   one level the companion **is** `A`, checked both ways.
5. **`Q5`.** What remains assumed: Perron–Frobenius only.

## 3. Where this stops

- **Condition (ii) is untouched.** This attempt proves (i) and gives no argument at all for the
  phase/diagonal-conjugation half. That is deliberate — the open-set statement rests on (i) alone
  — but anyone wanting the full classification (the exact characterization of the exceptional
  family, with the `Q^d` velocity) still needs (ii), and for that Wielandt or a substitute is
  still required.
- **Perron–Frobenius is assumed.** Its existence half only (positive left eigenvector, and
  `(I+C)^{n−1} > 0` under irreducibility). That is a much more standard import than the equality
  case, but it is an import.
- **Reducible rules are handled by a remark, not a proof.** "Drop the empty level and re-apply" is
  correct for the specific failure I exhibit (deepest weight zero), but a general reducible `A`
  needs the class-by-class bookkeeping that `j62b1` also lists as unwritten.
- **The checks are `d = 1` and small.** The proof uses neither, so this limits the evidence, not
  the statement.

## 4. What would finish it

1. Condition (ii) by a direct argument, which would make the exceptional family an exact
   characterization without importing Wielandt anywhere.
2. The reducible bookkeeping, now that the irreducible case needs only Perron–Frobenius.
3. An outside-family referee. Four of the five attempts on this problem, including this one, are
   the same family; and this one's failure mode would be a misapplied standard theorem.

## 5. Running it

```
python3 probes/work/derive/waves-need-signed-weights/w-jonathonsmac4f50-j7027/check.py
```

Standard library plus `sympy`; 12 checks, exact symbolic and rational arithmetic.

# Lean replay receipt for row 1432

[Ring.lean](Ring.lean) was checked from the pinned row-1425 data on the Mac mini. Run the following commands from this directory.

```sh
~/.elan/bin/lean --version
/usr/bin/time -lp /usr/bin/nice -n 10 ~/.elan/bin/lean -j1 -M1600 Ring.lean
```

```text
Lean (version 4.36.0, arm64-apple-darwin24.6.0, commit 611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9, Release)
SHA-256 46c69bc41998fabbbc8d5ec514b2089b78b04db910a1b58f66a29361c1478642  Ring.lean
exit=0
```

The full run started at 2026-11-23T03:31:00+00:00, used 1285.84 seconds wall time, and reached 1,444,233,216 bytes (1377.3 MiB) maximum resident set size. It checked 584 named theorems. The trusted computation is Lean 4.36.0's kernel with the bundled `Init` and its natural-number primitives. Arithmetic proofs use `decide` or definitional equality. The cover and summary proofs assemble those results. The source contains no external imports, compiled decision procedure, native-decision axiom or proof placeholders. Transcription and witness generation may be untrusted. Their identification with the signed Haar integral is the Stage 2 obligation in the [row report](../../library/gap-rg-ring-lean-replay-astra62.md).

## Witnesses and scope

The original witness directory was `/Volumes/SANDISK SSD/Mac Storage/Developer/lean-fixtures/row1425-witness/ym4d-row1425.a4IgI8Ax/`. The signed source streams are `groups42.txt` (1,897 rows) and `vacuum28.txt` (96 rows). A reverse comparison matched all keys and coefficients. `evaluate42.log`, `vac-eval28.log`, `circle.log`, `conditional.log`, `quotient.log` and `sphere.log` give the comparison targets. The exact scalar, derivative, circle and per-cell inputs are included in the Lean file. Running it requires only the declared toolchain.

The 512 marked and 128 ordinary coupling cells share endpoints and cover the full band. Both conditional dimensions use four coupling cells and 2,048 angle cells. The final checker verifies all 2,048 fine-cell containments in a consecutive cover of 271 intervals. It checks all eight dimension-and-coupling tables on every full covering interval. The histogram checker keeps exact rational coefficients and rounds its cell sums once at the end. The two deliberately false quotient acceptances were also run as separate Lean inputs. They returned exit 1 at the false proposition, as expected. The delivered theorems give the resulting wrong intervals as well as the rejection. The additional one-row histogram sign corruption changes the leading numerator from 15655 to 50215 on the same denominator.

## Input fingerprints

| File | SHA-256 |
|---|---|
| `recouple.py` | `24871875f00a545a52660662a8cc75476b30a92429da055005defdc8054225f3` |
| `evaluate.py` | `32339f9828f50c18300da401100b221002d4d06599105abee0ae7f665399f629` |
| `circle_tail.py` | `6addda58fde4959796a094bf35f72846a142e771c2359e2e8145c1df3ed6a715` |
| `conditional_ring.py` | `ee8b9170915b56fe005d2782e23881db0fa34b6f703130730a61a2294fcea812` |
| `quotient.py` | `458b2a7728e5ad4e3819c8bd5babc5380fe19160a2414234e71222b2683c9b74` |
| `groups42.txt` | `a74838223d2f9e5fec4fdb648cbd7b0cdfb4d2619bfaf26497d719b4a8939acb` |
| `vacuum28.txt` | `ae66db958f3c42062d7707e2bb90d07634d0829a7e1dcceb6503ab1634e9fdae` |
| `evaluate42.log` | `bfb7c1b4eb1e0c7272a4b57ada74fdf179c2047d206dc457408cb49d8f907978` |
| `vac-eval28.log` | `1215203180055ba5b2ff79020dfe6a6a253de9a4fc775c699f80e0fb6d2f812a` |
| `circle.log` | `df9ed33e099cbea79f2492d631bd80b831e760037bdca1865cee544daa4048bb` |
| `conditional.log` | `a13d7afdcf331c889f93e94aef0b4c2dbbe85e06a6e0567da7fd5877b0d557a5` |
| `quotient.log` | `2146f0fad13947bdd40dc7db000eae0157ca8fb4270bdcb5262ccf0265a30886` |
| `sphere.log` | `24cdf54ac86a5946e6781c3e09c7651d91208e3ebd24eba585dc4efaa8a11c63` |

## Run measurements

The first command of the session was the requested version probe. The shell returned in 0.13 seconds including the plan and scratch-directory setup. The version process had no separate RSS or elapsed-time measurement. The timed repeat and every invocation that checked a Lean source file follow. The macOS `/usr/bin/time -lp` field is maximum resident set size in bytes. Full stdout, timing and source-hash logs for each run are in `/tmp/sa-gap-rg-ring-lean-replay-astra62.2nayX0/`, named `<run>.out`, `<run>.time` and `<run>.json`.

| Run | Exit | Wall seconds | Peak RSS bytes | Scope |
|---|---:|---:|---:|---|
| version | 0 | 0.21 | 50,708,480 | Timed repeat of the initial version probe. |
| quotient | 0 | 0.64 | 421,822,464 | Initial quotient, Cauchy fractions, sphere addition and negative controls. |
| histogram | 0 | 2.21 | 609,681,408 | Signed histograms and the degree-16 coefficient. |
| axiomtrace | 1 | 0.56 | 421,756,928 | Diagnostic identified the signed Boolean comparison. A diagnostic name lookup failed. The delivered comparison uses decidable integer equality. |
| singlecell | 0 | 4.47 | 804,700,160 | One full marked polynomial at the first cell. |
| fourcells | 0 | 11.11 | 1,402,929,152 | Four marked cells, including exact Taylor endpoint checks. |
| corecircle | 0 | 1153.14 | 1,434,796,032 | All 640 histogram cells and both circles before the conditional part was appended. |
| conditionaltrial | 0 | 34.09 | 988,282,880 | Original single-cell recurrence on eight angles across both dimensions, including the input tables. |
| rejectvac | 1 | 0.56 | 422,035,456 | Deliberately false acceptance of a unit vacuum. |
| rejectmark | 1 | 0.50 | 421,789,696 | Deliberately false acceptance of the reversed marked sign. |
| extrema | 0 | 6.24 | 942,358,528 | Attained decimal endpoints, the band for b and a one-row histogram sign corruption. |
| condinputs | 0 | 2.25 | 677,543,936 | Conditional Taylor and derivative input tables in isolation. |
| spantrial | 0 | 11.41 | 678,690,816 | Eight certified wider angle intervals, including containment of every constituent fine cell. |
| final | -15 | 65.87 | 1,517,453,312 | Integrated trial. The combined convolution proof hit the 1,400 MB Lean limit. Stopped with SIGTERM after the diagnostic. |
| circleblocks | 0 | 7.13 | 551,862,272 | Rechecked the circle calculation using seven consecutive blocks per radius. |
| verified | 0 | 1285.84 | 1,444,233,216 | Fresh run of the entire delivered source. |

## Deliberate failures

The scratch trials asserted acceptance of each corrupted input. Lean gave the following diagnostics.

```text
/tmp/sa-gap-rg-ring-lean-replay-astra62.2nayX0/WrongSign.lean:144:79: error: Tactic `decide` proved that the proposition
  fourTable markedTotal.neg vacuumTotal 5047 = some expectedFour
is false
```

```text
/tmp/sa-gap-rg-ring-lean-replay-astra62.2nayX0/WrongVacuum.lean:144:77: error: Tactic `decide` proved that the proposition
  fourTable markedTotal { lo := 10 ^ 15, hi := 10 ^ 15 } 5047 = some expectedFour
is false
```

## Final axiom output, verbatim

```text
'Ring1425.even_tails' does not depend on any axioms
'Ring1425.total_enclosures' does not depend on any axioms
'Ring1425.four_dimensional_division' does not depend on any axioms
'Ring1425.reject_reversed_mark' does not depend on any axioms
'Ring1425.reject_omitted_vacuum' does not depend on any axioms
'Ring1425.five_dimensional_division' does not depend on any axioms
'Ring1425.sphere_leading_sum' does not depend on any axioms
'Ring1425.scalar_tail_ratio' does not depend on any axioms
'Ring1425.histogram_inventory' does not depend on any axioms
'Ring1425.histogram_leading_sum' does not depend on any axioms
'Ring1425.monomial_denominators' does not depend on any axioms
'Ring1425.vacuum_uses_four_spins' does not depend on any axioms
'Ring1425.circle_lambda_inputs' does not depend on any axioms
'Ring1425.circle_spin_sums' does not depend on any axioms
'Ring1425.marked_alpha_0_6' does not depend on any axioms
'Ring1425.marked_alpha_7_13' does not depend on any axioms
'Ring1425.marked_alpha_14_20' does not depend on any axioms
'Ring1425.marked_alpha_21_27' does not depend on any axioms
'Ring1425.marked_alpha_28_34' does not depend on any axioms
'Ring1425.marked_alpha_35_41' does not depend on any axioms
'Ring1425.marked_alpha_42_48' does not depend on any axioms
'Ring1425.vacuum_alpha_0_6' does not depend on any axioms
'Ring1425.vacuum_alpha_7_13' does not depend on any axioms
'Ring1425.vacuum_alpha_14_20' does not depend on any axioms
'Ring1425.vacuum_alpha_21_27' does not depend on any axioms
'Ring1425.vacuum_alpha_28_34' does not depend on any axioms
'Ring1425.vacuum_alpha_35_41' does not depend on any axioms
'Ring1425.vacuum_alpha_42_48' does not depend on any axioms
'Ring1425.circle_convolutions' does not depend on any axioms
'Ring1425.circle_bound_values' does not depend on any axioms
'Ring1425.marked_cells_0_1' does not depend on any axioms
'Ring1425.marked_cells_2_3' does not depend on any axioms
'Ring1425.marked_cells_4_5' does not depend on any axioms
'Ring1425.marked_cells_6_7' does not depend on any axioms
'Ring1425.marked_cells_8_9' does not depend on any axioms
'Ring1425.marked_cells_10_11' does not depend on any axioms
'Ring1425.marked_cells_12_13' does not depend on any axioms
'Ring1425.marked_cells_14_15' does not depend on any axioms
'Ring1425.marked_cells_16_17' does not depend on any axioms
'Ring1425.marked_cells_18_19' does not depend on any axioms
'Ring1425.marked_cells_20_21' does not depend on any axioms
'Ring1425.marked_cells_22_23' does not depend on any axioms
'Ring1425.marked_cells_24_25' does not depend on any axioms
'Ring1425.marked_cells_26_27' does not depend on any axioms
'Ring1425.marked_cells_28_29' does not depend on any axioms
'Ring1425.marked_cells_30_31' does not depend on any axioms
'Ring1425.marked_cells_32_33' does not depend on any axioms
'Ring1425.marked_cells_34_35' does not depend on any axioms
'Ring1425.marked_cells_36_37' does not depend on any axioms
'Ring1425.marked_cells_38_39' does not depend on any axioms
'Ring1425.marked_cells_40_41' does not depend on any axioms
'Ring1425.marked_cells_42_43' does not depend on any axioms
'Ring1425.marked_cells_44_45' does not depend on any axioms
'Ring1425.marked_cells_46_47' does not depend on any axioms
'Ring1425.marked_cells_48_49' does not depend on any axioms
'Ring1425.marked_cells_50_51' does not depend on any axioms
'Ring1425.marked_cells_52_53' does not depend on any axioms
'Ring1425.marked_cells_54_55' does not depend on any axioms
'Ring1425.marked_cells_56_57' does not depend on any axioms
'Ring1425.marked_cells_58_59' does not depend on any axioms
'Ring1425.marked_cells_60_61' does not depend on any axioms
'Ring1425.marked_cells_62_63' does not depend on any axioms
'Ring1425.marked_cells_64_65' does not depend on any axioms
'Ring1425.marked_cells_66_67' does not depend on any axioms
'Ring1425.marked_cells_68_69' does not depend on any axioms
'Ring1425.marked_cells_70_71' does not depend on any axioms
'Ring1425.marked_cells_72_73' does not depend on any axioms
'Ring1425.marked_cells_74_75' does not depend on any axioms
'Ring1425.marked_cells_76_77' does not depend on any axioms
'Ring1425.marked_cells_78_79' does not depend on any axioms
'Ring1425.marked_cells_80_81' does not depend on any axioms
'Ring1425.marked_cells_82_83' does not depend on any axioms
'Ring1425.marked_cells_84_85' does not depend on any axioms
'Ring1425.marked_cells_86_87' does not depend on any axioms
'Ring1425.marked_cells_88_89' does not depend on any axioms
'Ring1425.marked_cells_90_91' does not depend on any axioms
'Ring1425.marked_cells_92_93' does not depend on any axioms
'Ring1425.marked_cells_94_95' does not depend on any axioms
'Ring1425.marked_cells_96_97' does not depend on any axioms
'Ring1425.marked_cells_98_99' does not depend on any axioms
'Ring1425.marked_cells_100_101' does not depend on any axioms
'Ring1425.marked_cells_102_103' does not depend on any axioms
'Ring1425.marked_cells_104_105' does not depend on any axioms
'Ring1425.marked_cells_106_107' does not depend on any axioms
'Ring1425.marked_cells_108_109' does not depend on any axioms
'Ring1425.marked_cells_110_111' does not depend on any axioms
'Ring1425.marked_cells_112_113' does not depend on any axioms
'Ring1425.marked_cells_114_115' does not depend on any axioms
'Ring1425.marked_cells_116_117' does not depend on any axioms
'Ring1425.marked_cells_118_119' does not depend on any axioms
'Ring1425.marked_cells_120_121' does not depend on any axioms
'Ring1425.marked_cells_122_123' does not depend on any axioms
'Ring1425.marked_cells_124_125' does not depend on any axioms
'Ring1425.marked_cells_126_127' does not depend on any axioms
'Ring1425.marked_cells_128_129' does not depend on any axioms
'Ring1425.marked_cells_130_131' does not depend on any axioms
'Ring1425.marked_cells_132_133' does not depend on any axioms
'Ring1425.marked_cells_134_135' does not depend on any axioms
'Ring1425.marked_cells_136_137' does not depend on any axioms
'Ring1425.marked_cells_138_139' does not depend on any axioms
'Ring1425.marked_cells_140_141' does not depend on any axioms
'Ring1425.marked_cells_142_143' does not depend on any axioms
'Ring1425.marked_cells_144_145' does not depend on any axioms
'Ring1425.marked_cells_146_147' does not depend on any axioms
'Ring1425.marked_cells_148_149' does not depend on any axioms
'Ring1425.marked_cells_150_151' does not depend on any axioms
'Ring1425.marked_cells_152_153' does not depend on any axioms
'Ring1425.marked_cells_154_155' does not depend on any axioms
'Ring1425.marked_cells_156_157' does not depend on any axioms
'Ring1425.marked_cells_158_159' does not depend on any axioms
'Ring1425.marked_cells_160_161' does not depend on any axioms
'Ring1425.marked_cells_162_163' does not depend on any axioms
'Ring1425.marked_cells_164_165' does not depend on any axioms
'Ring1425.marked_cells_166_167' does not depend on any axioms
'Ring1425.marked_cells_168_169' does not depend on any axioms
'Ring1425.marked_cells_170_171' does not depend on any axioms
'Ring1425.marked_cells_172_173' does not depend on any axioms
'Ring1425.marked_cells_174_175' does not depend on any axioms
'Ring1425.marked_cells_176_177' does not depend on any axioms
'Ring1425.marked_cells_178_179' does not depend on any axioms
'Ring1425.marked_cells_180_181' does not depend on any axioms
'Ring1425.marked_cells_182_183' does not depend on any axioms
'Ring1425.marked_cells_184_185' does not depend on any axioms
'Ring1425.marked_cells_186_187' does not depend on any axioms
'Ring1425.marked_cells_188_189' does not depend on any axioms
'Ring1425.marked_cells_190_191' does not depend on any axioms
'Ring1425.marked_cells_192_193' does not depend on any axioms
'Ring1425.marked_cells_194_195' does not depend on any axioms
'Ring1425.marked_cells_196_197' does not depend on any axioms
'Ring1425.marked_cells_198_199' does not depend on any axioms
'Ring1425.marked_cells_200_201' does not depend on any axioms
'Ring1425.marked_cells_202_203' does not depend on any axioms
'Ring1425.marked_cells_204_205' does not depend on any axioms
'Ring1425.marked_cells_206_207' does not depend on any axioms
'Ring1425.marked_cells_208_209' does not depend on any axioms
'Ring1425.marked_cells_210_211' does not depend on any axioms
'Ring1425.marked_cells_212_213' does not depend on any axioms
'Ring1425.marked_cells_214_215' does not depend on any axioms
'Ring1425.marked_cells_216_217' does not depend on any axioms
'Ring1425.marked_cells_218_219' does not depend on any axioms
'Ring1425.marked_cells_220_221' does not depend on any axioms
'Ring1425.marked_cells_222_223' does not depend on any axioms
'Ring1425.marked_cells_224_225' does not depend on any axioms
'Ring1425.marked_cells_226_227' does not depend on any axioms
'Ring1425.marked_cells_228_229' does not depend on any axioms
'Ring1425.marked_cells_230_231' does not depend on any axioms
'Ring1425.marked_cells_232_233' does not depend on any axioms
'Ring1425.marked_cells_234_235' does not depend on any axioms
'Ring1425.marked_cells_236_237' does not depend on any axioms
'Ring1425.marked_cells_238_239' does not depend on any axioms
'Ring1425.marked_cells_240_241' does not depend on any axioms
'Ring1425.marked_cells_242_243' does not depend on any axioms
'Ring1425.marked_cells_244_245' does not depend on any axioms
'Ring1425.marked_cells_246_247' does not depend on any axioms
'Ring1425.marked_cells_248_249' does not depend on any axioms
'Ring1425.marked_cells_250_251' does not depend on any axioms
'Ring1425.marked_cells_252_253' does not depend on any axioms
'Ring1425.marked_cells_254_255' does not depend on any axioms
'Ring1425.marked_cells_256_257' does not depend on any axioms
'Ring1425.marked_cells_258_259' does not depend on any axioms
'Ring1425.marked_cells_260_261' does not depend on any axioms
'Ring1425.marked_cells_262_263' does not depend on any axioms
'Ring1425.marked_cells_264_265' does not depend on any axioms
'Ring1425.marked_cells_266_267' does not depend on any axioms
'Ring1425.marked_cells_268_269' does not depend on any axioms
'Ring1425.marked_cells_270_271' does not depend on any axioms
'Ring1425.marked_cells_272_273' does not depend on any axioms
'Ring1425.marked_cells_274_275' does not depend on any axioms
'Ring1425.marked_cells_276_277' does not depend on any axioms
'Ring1425.marked_cells_278_279' does not depend on any axioms
'Ring1425.marked_cells_280_281' does not depend on any axioms
'Ring1425.marked_cells_282_283' does not depend on any axioms
'Ring1425.marked_cells_284_285' does not depend on any axioms
'Ring1425.marked_cells_286_287' does not depend on any axioms
'Ring1425.marked_cells_288_289' does not depend on any axioms
'Ring1425.marked_cells_290_291' does not depend on any axioms
'Ring1425.marked_cells_292_293' does not depend on any axioms
'Ring1425.marked_cells_294_295' does not depend on any axioms
'Ring1425.marked_cells_296_297' does not depend on any axioms
'Ring1425.marked_cells_298_299' does not depend on any axioms
'Ring1425.marked_cells_300_301' does not depend on any axioms
'Ring1425.marked_cells_302_303' does not depend on any axioms
'Ring1425.marked_cells_304_305' does not depend on any axioms
'Ring1425.marked_cells_306_307' does not depend on any axioms
'Ring1425.marked_cells_308_309' does not depend on any axioms
'Ring1425.marked_cells_310_311' does not depend on any axioms
'Ring1425.marked_cells_312_313' does not depend on any axioms
'Ring1425.marked_cells_314_315' does not depend on any axioms
'Ring1425.marked_cells_316_317' does not depend on any axioms
'Ring1425.marked_cells_318_319' does not depend on any axioms
'Ring1425.marked_cells_320_321' does not depend on any axioms
'Ring1425.marked_cells_322_323' does not depend on any axioms
'Ring1425.marked_cells_324_325' does not depend on any axioms
'Ring1425.marked_cells_326_327' does not depend on any axioms
'Ring1425.marked_cells_328_329' does not depend on any axioms
'Ring1425.marked_cells_330_331' does not depend on any axioms
'Ring1425.marked_cells_332_333' does not depend on any axioms
'Ring1425.marked_cells_334_335' does not depend on any axioms
'Ring1425.marked_cells_336_337' does not depend on any axioms
'Ring1425.marked_cells_338_339' does not depend on any axioms
'Ring1425.marked_cells_340_341' does not depend on any axioms
'Ring1425.marked_cells_342_343' does not depend on any axioms
'Ring1425.marked_cells_344_345' does not depend on any axioms
'Ring1425.marked_cells_346_347' does not depend on any axioms
'Ring1425.marked_cells_348_349' does not depend on any axioms
'Ring1425.marked_cells_350_351' does not depend on any axioms
'Ring1425.marked_cells_352_353' does not depend on any axioms
'Ring1425.marked_cells_354_355' does not depend on any axioms
'Ring1425.marked_cells_356_357' does not depend on any axioms
'Ring1425.marked_cells_358_359' does not depend on any axioms
'Ring1425.marked_cells_360_361' does not depend on any axioms
'Ring1425.marked_cells_362_363' does not depend on any axioms
'Ring1425.marked_cells_364_365' does not depend on any axioms
'Ring1425.marked_cells_366_367' does not depend on any axioms
'Ring1425.marked_cells_368_369' does not depend on any axioms
'Ring1425.marked_cells_370_371' does not depend on any axioms
'Ring1425.marked_cells_372_373' does not depend on any axioms
'Ring1425.marked_cells_374_375' does not depend on any axioms
'Ring1425.marked_cells_376_377' does not depend on any axioms
'Ring1425.marked_cells_378_379' does not depend on any axioms
'Ring1425.marked_cells_380_381' does not depend on any axioms
'Ring1425.marked_cells_382_383' does not depend on any axioms
'Ring1425.marked_cells_384_385' does not depend on any axioms
'Ring1425.marked_cells_386_387' does not depend on any axioms
'Ring1425.marked_cells_388_389' does not depend on any axioms
'Ring1425.marked_cells_390_391' does not depend on any axioms
'Ring1425.marked_cells_392_393' does not depend on any axioms
'Ring1425.marked_cells_394_395' does not depend on any axioms
'Ring1425.marked_cells_396_397' does not depend on any axioms
'Ring1425.marked_cells_398_399' does not depend on any axioms
'Ring1425.marked_cells_400_401' does not depend on any axioms
'Ring1425.marked_cells_402_403' does not depend on any axioms
'Ring1425.marked_cells_404_405' does not depend on any axioms
'Ring1425.marked_cells_406_407' does not depend on any axioms
'Ring1425.marked_cells_408_409' does not depend on any axioms
'Ring1425.marked_cells_410_411' does not depend on any axioms
'Ring1425.marked_cells_412_413' does not depend on any axioms
'Ring1425.marked_cells_414_415' does not depend on any axioms
'Ring1425.marked_cells_416_417' does not depend on any axioms
'Ring1425.marked_cells_418_419' does not depend on any axioms
'Ring1425.marked_cells_420_421' does not depend on any axioms
'Ring1425.marked_cells_422_423' does not depend on any axioms
'Ring1425.marked_cells_424_425' does not depend on any axioms
'Ring1425.marked_cells_426_427' does not depend on any axioms
'Ring1425.marked_cells_428_429' does not depend on any axioms
'Ring1425.marked_cells_430_431' does not depend on any axioms
'Ring1425.marked_cells_432_433' does not depend on any axioms
'Ring1425.marked_cells_434_435' does not depend on any axioms
'Ring1425.marked_cells_436_437' does not depend on any axioms
'Ring1425.marked_cells_438_439' does not depend on any axioms
'Ring1425.marked_cells_440_441' does not depend on any axioms
'Ring1425.marked_cells_442_443' does not depend on any axioms
'Ring1425.marked_cells_444_445' does not depend on any axioms
'Ring1425.marked_cells_446_447' does not depend on any axioms
'Ring1425.marked_cells_448_449' does not depend on any axioms
'Ring1425.marked_cells_450_451' does not depend on any axioms
'Ring1425.marked_cells_452_453' does not depend on any axioms
'Ring1425.marked_cells_454_455' does not depend on any axioms
'Ring1425.marked_cells_456_457' does not depend on any axioms
'Ring1425.marked_cells_458_459' does not depend on any axioms
'Ring1425.marked_cells_460_461' does not depend on any axioms
'Ring1425.marked_cells_462_463' does not depend on any axioms
'Ring1425.marked_cells_464_465' does not depend on any axioms
'Ring1425.marked_cells_466_467' does not depend on any axioms
'Ring1425.marked_cells_468_469' does not depend on any axioms
'Ring1425.marked_cells_470_471' does not depend on any axioms
'Ring1425.marked_cells_472_473' does not depend on any axioms
'Ring1425.marked_cells_474_475' does not depend on any axioms
'Ring1425.marked_cells_476_477' does not depend on any axioms
'Ring1425.marked_cells_478_479' does not depend on any axioms
'Ring1425.marked_cells_480_481' does not depend on any axioms
'Ring1425.marked_cells_482_483' does not depend on any axioms
'Ring1425.marked_cells_484_485' does not depend on any axioms
'Ring1425.marked_cells_486_487' does not depend on any axioms
'Ring1425.marked_cells_488_489' does not depend on any axioms
'Ring1425.marked_cells_490_491' does not depend on any axioms
'Ring1425.marked_cells_492_493' does not depend on any axioms
'Ring1425.marked_cells_494_495' does not depend on any axioms
'Ring1425.marked_cells_496_497' does not depend on any axioms
'Ring1425.marked_cells_498_499' does not depend on any axioms
'Ring1425.marked_cells_500_501' does not depend on any axioms
'Ring1425.marked_cells_502_503' does not depend on any axioms
'Ring1425.marked_cells_504_505' does not depend on any axioms
'Ring1425.marked_cells_506_507' does not depend on any axioms
'Ring1425.marked_cells_508_509' does not depend on any axioms
'Ring1425.marked_cells_510_511' does not depend on any axioms
'Ring1425.marked_core_mesh' does not depend on any axioms
'Ring1425.vacuum_cells_0_7' does not depend on any axioms
'Ring1425.vacuum_cells_8_15' does not depend on any axioms
'Ring1425.vacuum_cells_16_23' does not depend on any axioms
'Ring1425.vacuum_cells_24_31' does not depend on any axioms
'Ring1425.vacuum_cells_32_39' does not depend on any axioms
'Ring1425.vacuum_cells_40_47' does not depend on any axioms
'Ring1425.vacuum_cells_48_55' does not depend on any axioms
'Ring1425.vacuum_cells_56_63' does not depend on any axioms
'Ring1425.vacuum_cells_64_71' does not depend on any axioms
'Ring1425.vacuum_cells_72_79' does not depend on any axioms
'Ring1425.vacuum_cells_80_87' does not depend on any axioms
'Ring1425.vacuum_cells_88_95' does not depend on any axioms
'Ring1425.vacuum_cells_96_103' does not depend on any axioms
'Ring1425.vacuum_cells_104_111' does not depend on any axioms
'Ring1425.vacuum_cells_112_119' does not depend on any axioms
'Ring1425.vacuum_cells_120_127' does not depend on any axioms
'Ring1425.vacuum_core_mesh' does not depend on any axioms
'Ring1425.marked_core_extrema' does not depend on any axioms
'Ring1425.vacuum_core_extrema' does not depend on any axioms
'Ring1425.reject_one_histogram_sign' does not depend on any axioms
'Ring1425.one_plaquette_band' does not depend on any axioms
'Ring1425.fixed_charge_scalar_arithmetic' does not depend on any axioms
'Ring1425.frozen_signs' does not depend on any axioms
'Ring1425.conditional_input_tables' does not depend on any axioms
'Ring1425.angles_0_63' does not depend on any axioms
'Ring1425.angles_64_127' does not depend on any axioms
'Ring1425.angles_128_191' does not depend on any axioms
'Ring1425.angles_192_255' does not depend on any axioms
'Ring1425.angles_256_319' does not depend on any axioms
'Ring1425.angles_320_383' does not depend on any axioms
'Ring1425.angles_384_415' does not depend on any axioms
'Ring1425.angles_416_447' does not depend on any axioms
'Ring1425.angles_448_479' does not depend on any axioms
'Ring1425.angles_480_511' does not depend on any axioms
'Ring1425.angles_512_527' does not depend on any axioms
'Ring1425.angles_528_543' does not depend on any axioms
'Ring1425.angles_544_559' does not depend on any axioms
'Ring1425.angles_560_575' does not depend on any axioms
'Ring1425.angles_576_591' does not depend on any axioms
'Ring1425.angles_592_599' does not depend on any axioms
'Ring1425.angles_600_607' does not depend on any axioms
'Ring1425.angles_608_615' does not depend on any axioms
'Ring1425.angles_616_623' does not depend on any axioms
'Ring1425.angles_624_631' does not depend on any axioms
'Ring1425.angles_632_639' does not depend on any axioms
'Ring1425.angles_640_647' does not depend on any axioms
'Ring1425.angles_648_651' does not depend on any axioms
'Ring1425.angles_652_655' does not depend on any axioms
'Ring1425.angles_656_659' does not depend on any axioms
'Ring1425.angles_660_663' does not depend on any axioms
'Ring1425.angles_664_667' does not depend on any axioms
'Ring1425.angles_668_671' does not depend on any axioms
'Ring1425.angles_672_675' does not depend on any axioms
'Ring1425.angles_676_679' does not depend on any axioms
'Ring1425.angles_680_683' does not depend on any axioms
'Ring1425.angles_684_687' does not depend on any axioms
'Ring1425.angles_688_689' does not depend on any axioms
'Ring1425.angles_690_691' does not depend on any axioms
'Ring1425.angles_692_693' does not depend on any axioms
'Ring1425.angles_694_695' does not depend on any axioms
'Ring1425.angles_696_697' does not depend on any axioms
'Ring1425.angles_698_699' does not depend on any axioms
'Ring1425.angles_700_701' does not depend on any axioms
'Ring1425.angles_702_703' does not depend on any axioms
'Ring1425.angles_704_705' does not depend on any axioms
'Ring1425.angles_706_707' does not depend on any axioms
'Ring1425.angles_708_709' does not depend on any axioms
'Ring1425.angles_710_711' does not depend on any axioms
'Ring1425.angles_712_713' does not depend on any axioms
'Ring1425.angles_714_715' does not depend on any axioms
'Ring1425.angles_716_717' does not depend on any axioms
'Ring1425.angles_718_719' does not depend on any axioms
'Ring1425.angles_720_720' does not depend on any axioms
'Ring1425.angles_721_721' does not depend on any axioms
'Ring1425.angles_722_722' does not depend on any axioms
'Ring1425.angles_723_723' does not depend on any axioms
'Ring1425.angles_724_724' does not depend on any axioms
'Ring1425.angles_725_725' does not depend on any axioms
'Ring1425.angles_726_726' does not depend on any axioms
'Ring1425.angles_727_727' does not depend on any axioms
'Ring1425.angles_728_728' does not depend on any axioms
'Ring1425.angles_729_729' does not depend on any axioms
'Ring1425.angles_730_730' does not depend on any axioms
'Ring1425.angles_731_731' does not depend on any axioms
'Ring1425.angles_732_732' does not depend on any axioms
'Ring1425.angles_733_733' does not depend on any axioms
'Ring1425.angles_734_734' does not depend on any axioms
'Ring1425.angles_735_735' does not depend on any axioms
'Ring1425.angles_736_736' does not depend on any axioms
'Ring1425.angles_737_737' does not depend on any axioms
'Ring1425.angles_738_738' does not depend on any axioms
'Ring1425.angles_739_739' does not depend on any axioms
'Ring1425.angles_740_740' does not depend on any axioms
'Ring1425.angles_741_741' does not depend on any axioms
'Ring1425.angles_742_742' does not depend on any axioms
'Ring1425.angles_743_743' does not depend on any axioms
'Ring1425.angles_744_744' does not depend on any axioms
'Ring1425.angles_745_745' does not depend on any axioms
'Ring1425.angles_746_746' does not depend on any axioms
'Ring1425.angles_747_747' does not depend on any axioms
'Ring1425.angles_748_748' does not depend on any axioms
'Ring1425.angles_749_749' does not depend on any axioms
'Ring1425.angles_750_750' does not depend on any axioms
'Ring1425.angles_751_751' does not depend on any axioms
'Ring1425.angles_752_752' does not depend on any axioms
'Ring1425.angles_753_753' does not depend on any axioms
'Ring1425.angles_754_754' does not depend on any axioms
'Ring1425.angles_755_755' does not depend on any axioms
'Ring1425.angles_756_756' does not depend on any axioms
'Ring1425.angles_757_757' does not depend on any axioms
'Ring1425.angles_758_758' does not depend on any axioms
'Ring1425.angles_759_759' does not depend on any axioms
'Ring1425.angles_760_760' does not depend on any axioms
'Ring1425.angles_761_761' does not depend on any axioms
'Ring1425.angles_762_762' does not depend on any axioms
'Ring1425.angles_763_763' does not depend on any axioms
'Ring1425.angles_764_764' does not depend on any axioms
'Ring1425.angles_765_765' does not depend on any axioms
'Ring1425.angles_766_766' does not depend on any axioms
'Ring1425.angles_767_767' does not depend on any axioms
'Ring1425.angles_768_768' does not depend on any axioms
'Ring1425.angles_769_769' does not depend on any axioms
'Ring1425.angles_770_770' does not depend on any axioms
'Ring1425.angles_771_771' does not depend on any axioms
'Ring1425.angles_772_772' does not depend on any axioms
'Ring1425.angles_773_773' does not depend on any axioms
'Ring1425.angles_774_774' does not depend on any axioms
'Ring1425.angles_775_775' does not depend on any axioms
'Ring1425.angles_776_776' does not depend on any axioms
'Ring1425.angles_777_777' does not depend on any axioms
'Ring1425.angles_778_778' does not depend on any axioms
'Ring1425.angles_779_779' does not depend on any axioms
'Ring1425.angles_780_780' does not depend on any axioms
'Ring1425.angles_781_781' does not depend on any axioms
'Ring1425.angles_782_782' does not depend on any axioms
'Ring1425.angles_783_783' does not depend on any axioms
'Ring1425.angles_784_784' does not depend on any axioms
'Ring1425.angles_785_785' does not depend on any axioms
'Ring1425.angles_786_786' does not depend on any axioms
'Ring1425.angles_787_787' does not depend on any axioms
'Ring1425.angles_788_788' does not depend on any axioms
'Ring1425.angles_789_789' does not depend on any axioms
'Ring1425.angles_790_790' does not depend on any axioms
'Ring1425.angles_791_791' does not depend on any axioms
'Ring1425.angles_792_792' does not depend on any axioms
'Ring1425.angles_793_793' does not depend on any axioms
'Ring1425.angles_794_794' does not depend on any axioms
'Ring1425.angles_795_795' does not depend on any axioms
'Ring1425.angles_796_796' does not depend on any axioms
'Ring1425.angles_797_797' does not depend on any axioms
'Ring1425.angles_798_798' does not depend on any axioms
'Ring1425.angles_799_799' does not depend on any axioms
'Ring1425.angles_800_800' does not depend on any axioms
'Ring1425.angles_801_801' does not depend on any axioms
'Ring1425.angles_802_802' does not depend on any axioms
'Ring1425.angles_803_803' does not depend on any axioms
'Ring1425.angles_804_804' does not depend on any axioms
'Ring1425.angles_805_805' does not depend on any axioms
'Ring1425.angles_806_806' does not depend on any axioms
'Ring1425.angles_807_807' does not depend on any axioms
'Ring1425.angles_808_808' does not depend on any axioms
'Ring1425.angles_809_809' does not depend on any axioms
'Ring1425.angles_810_811' does not depend on any axioms
'Ring1425.angles_812_813' does not depend on any axioms
'Ring1425.angles_814_815' does not depend on any axioms
'Ring1425.angles_816_817' does not depend on any axioms
'Ring1425.angles_818_819' does not depend on any axioms
'Ring1425.angles_820_821' does not depend on any axioms
'Ring1425.angles_822_823' does not depend on any axioms
'Ring1425.angles_824_825' does not depend on any axioms
'Ring1425.angles_826_827' does not depend on any axioms
'Ring1425.angles_828_829' does not depend on any axioms
'Ring1425.angles_830_831' does not depend on any axioms
'Ring1425.angles_832_833' does not depend on any axioms
'Ring1425.angles_834_835' does not depend on any axioms
'Ring1425.angles_836_837' does not depend on any axioms
'Ring1425.angles_838_839' does not depend on any axioms
'Ring1425.angles_840_841' does not depend on any axioms
'Ring1425.angles_842_843' does not depend on any axioms
'Ring1425.angles_844_845' does not depend on any axioms
'Ring1425.angles_846_846' does not depend on any axioms
'Ring1425.angles_847_847' does not depend on any axioms
'Ring1425.angles_848_848' does not depend on any axioms
'Ring1425.angles_849_849' does not depend on any axioms
'Ring1425.angles_850_850' does not depend on any axioms
'Ring1425.angles_851_851' does not depend on any axioms
'Ring1425.angles_852_852' does not depend on any axioms
'Ring1425.angles_853_853' does not depend on any axioms
'Ring1425.angles_854_854' does not depend on any axioms
'Ring1425.angles_855_855' does not depend on any axioms
'Ring1425.angles_856_856' does not depend on any axioms
'Ring1425.angles_857_857' does not depend on any axioms
'Ring1425.angles_858_858' does not depend on any axioms
'Ring1425.angles_859_859' does not depend on any axioms
'Ring1425.angles_860_860' does not depend on any axioms
'Ring1425.angles_861_861' does not depend on any axioms
'Ring1425.angles_862_862' does not depend on any axioms
'Ring1425.angles_863_863' does not depend on any axioms
'Ring1425.angles_864_864' does not depend on any axioms
'Ring1425.angles_865_865' does not depend on any axioms
'Ring1425.angles_866_866' does not depend on any axioms
'Ring1425.angles_867_867' does not depend on any axioms
'Ring1425.angles_868_868' does not depend on any axioms
'Ring1425.angles_869_869' does not depend on any axioms
'Ring1425.angles_870_870' does not depend on any axioms
'Ring1425.angles_871_871' does not depend on any axioms
'Ring1425.angles_872_872' does not depend on any axioms
'Ring1425.angles_873_873' does not depend on any axioms
'Ring1425.angles_874_874' does not depend on any axioms
'Ring1425.angles_875_875' does not depend on any axioms
'Ring1425.angles_876_876' does not depend on any axioms
'Ring1425.angles_877_877' does not depend on any axioms
'Ring1425.angles_878_878' does not depend on any axioms
'Ring1425.angles_879_879' does not depend on any axioms
'Ring1425.angles_880_880' does not depend on any axioms
'Ring1425.angles_881_881' does not depend on any axioms
'Ring1425.angles_882_882' does not depend on any axioms
'Ring1425.angles_883_883' does not depend on any axioms
'Ring1425.angles_884_884' does not depend on any axioms
'Ring1425.angles_885_885' does not depend on any axioms
'Ring1425.angles_886_886' does not depend on any axioms
'Ring1425.angles_887_887' does not depend on any axioms
'Ring1425.angles_888_888' does not depend on any axioms
'Ring1425.angles_889_889' does not depend on any axioms
'Ring1425.angles_890_890' does not depend on any axioms
'Ring1425.angles_891_891' does not depend on any axioms
'Ring1425.angles_892_892' does not depend on any axioms
'Ring1425.angles_893_893' does not depend on any axioms
'Ring1425.angles_894_894' does not depend on any axioms
'Ring1425.angles_895_895' does not depend on any axioms
'Ring1425.angles_896_896' does not depend on any axioms
'Ring1425.angles_897_897' does not depend on any axioms
'Ring1425.angles_898_898' does not depend on any axioms
'Ring1425.angles_899_899' does not depend on any axioms
'Ring1425.angles_900_900' does not depend on any axioms
'Ring1425.angles_901_901' does not depend on any axioms
'Ring1425.angles_902_902' does not depend on any axioms
'Ring1425.angles_903_903' does not depend on any axioms
'Ring1425.angles_904_904' does not depend on any axioms
'Ring1425.angles_905_905' does not depend on any axioms
'Ring1425.angles_906_906' does not depend on any axioms
'Ring1425.angles_907_907' does not depend on any axioms
'Ring1425.angles_908_908' does not depend on any axioms
'Ring1425.angles_909_909' does not depend on any axioms
'Ring1425.angles_910_910' does not depend on any axioms
'Ring1425.angles_911_911' does not depend on any axioms
'Ring1425.angles_912_912' does not depend on any axioms
'Ring1425.angles_913_913' does not depend on any axioms
'Ring1425.angles_914_915' does not depend on any axioms
'Ring1425.angles_916_917' does not depend on any axioms
'Ring1425.angles_918_919' does not depend on any axioms
'Ring1425.angles_920_921' does not depend on any axioms
'Ring1425.angles_922_923' does not depend on any axioms
'Ring1425.angles_924_925' does not depend on any axioms
'Ring1425.angles_926_927' does not depend on any axioms
'Ring1425.angles_928_929' does not depend on any axioms
'Ring1425.angles_930_931' does not depend on any axioms
'Ring1425.angles_932_933' does not depend on any axioms
'Ring1425.angles_934_935' does not depend on any axioms
'Ring1425.angles_936_937' does not depend on any axioms
'Ring1425.angles_938_939' does not depend on any axioms
'Ring1425.angles_940_943' does not depend on any axioms
'Ring1425.angles_944_947' does not depend on any axioms
'Ring1425.angles_948_951' does not depend on any axioms
'Ring1425.angles_952_955' does not depend on any axioms
'Ring1425.angles_956_959' does not depend on any axioms
'Ring1425.angles_960_963' does not depend on any axioms
'Ring1425.angles_964_967' does not depend on any axioms
'Ring1425.angles_968_975' does not depend on any axioms
'Ring1425.angles_976_983' does not depend on any axioms
'Ring1425.angles_984_991' does not depend on any axioms
'Ring1425.angles_992_999' does not depend on any axioms
'Ring1425.angles_1000_1007' does not depend on any axioms
'Ring1425.angles_1008_1023' does not depend on any axioms
'Ring1425.angles_1024_1039' does not depend on any axioms
'Ring1425.angles_1040_1055' does not depend on any axioms
'Ring1425.angles_1056_1087' does not depend on any axioms
'Ring1425.angles_1088_1119' does not depend on any axioms
'Ring1425.angles_1120_1151' does not depend on any axioms
'Ring1425.angles_1152_1215' does not depend on any axioms
'Ring1425.angles_1216_1279' does not depend on any axioms
'Ring1425.angles_1280_1407' does not depend on any axioms
'Ring1425.angles_1408_1535' does not depend on any axioms
'Ring1425.angles_1536_1663' does not depend on any axioms
'Ring1425.angles_1664_1791' does not depend on any axioms
'Ring1425.angles_1792_1855' does not depend on any axioms
'Ring1425.angles_1856_1919' does not depend on any axioms
'Ring1425.angles_1920_1983' does not depend on any axioms
'Ring1425.angles_1984_2015' does not depend on any axioms
'Ring1425.angles_2016_2031' does not depend on any axioms
'Ring1425.angles_2032_2039' does not depend on any axioms
'Ring1425.angles_2040_2043' does not depend on any axioms
'Ring1425.angles_2044_2045' does not depend on any axioms
'Ring1425.angles_2046_2046' does not depend on any axioms
'Ring1425.angles_2047_2047' does not depend on any axioms
'Ring1425.all_conditional_boxes' does not depend on any axioms
'Ring1425.finite_ring_replay' does not depend on any axioms
```

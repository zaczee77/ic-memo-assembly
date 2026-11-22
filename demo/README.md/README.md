# Demo: IC memo assembly

A small reference demo of the IC memo idea behind Txvni: a memo is assembled only from blocks that name a section and a source, blocks with no source or an unknown section are rejected with a reason, and a readiness check names every section that is still empty.

## How to run it

From the repository root, or from this folder:

```
python3 demo/ic_memo_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. It feeds 7 invented blocks into the assembler, covering overview, KPIs, benchmarks, risks, and recommendation, plus one block for an unknown section.
2. It accepts 5 blocks and rejects 2: one risks block with no source, and one block whose section is not in the fixed list.
3. It reports 4 of 5 sections covered, names risks as the missing section, and marks the memo as not ready.
4. It renders the memo in fixed section order, with the source printed under each block and the risks section shown as empty.

## What it printed when it was tested

7 blocks received, 5 accepted, 2 rejected with reasons missing source and unknown section, 4 of 5 sections covered, missing sections risks, memo ready false, and all checks passed.

## What the sample data is

Every company name, document name, and figure in `ic_memo_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real user, or a real memo. A real system would build blocks from real ingested documents and keep human review before any memo is used. None of that is modeled here.

## Files

1. `ic_memo_demo.py`: the demo. The fixed section list, the sample blocks, the assembler, the rejection rules, the readiness check, the rendering, and the built in assertions.
2. `README.md`: this file.

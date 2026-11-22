# The IC memo assembly pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description lists document and spreadsheet ingestion, cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. The IC memo sits near the end of that chain. It is the place where the earlier steps become one document a committee can read, so it is the place where keeping the source attached matters most.

The same need appears wherever a summary is built from many sources. If the source name travels with each claim into the final document, a reader can check any claim in one step. If it does not, checking means redoing the research.

## The block

A block holds a section name, a short text, and a source name. The section name says where the block belongs in the memo. The text is the claim or figure in plain words. The source name is the document the text came from, named exactly as it was ingested, so a reader can find it again.

A block is the smallest unit the assembler trusts. The assembler never writes text of its own, never merges two blocks into new wording, and never moves a block into a different section. What the memo says is exactly what the blocks said.

## The four rules

1. A source is required. A block with an empty source is rejected and the rejection is recorded with its reason. A claim that cannot be traced is not included quietly and is not fixed by guessing a source.
2. Sections are fixed in advance. The assembler holds the ordered list of section names. A block naming a section outside that list is rejected, so the memo keeps the shape the committee expects and new headings cannot appear by accident.
3. Order is fixed. Sections print in the order the assembler holds them, and blocks inside a section print in the order they arrived. The reader sees the same shape every time, and a missing section is easy to spot.
4. Empty means not ready. The readiness check walks the required sections and lists each one that holds no accepted block. The memo is ready only when that list is empty. A draft with a named gap is honest. A draft that hides its gap is not.

## Design principles

1. Assembly is not authorship. The assembler arranges sourced blocks. It does not summarize, infer, or fill gaps. Those steps belong to the people and tools that produce the blocks, where the source is still in view.
2. Rejection is information. The rejected list, with reasons, tells the team exactly what work remains: find a source for one claim, or decide whether a new section is truly needed.
3. Readiness is a narrow claim. A ready memo means every required section holds at least one sourced block. It does not mean the figures are correct, the risks are complete, or the recommendation is sound. Those judgments stay with human review.
4. The source stays visible in the output. Printing the source under each block makes checking cheap for the reader and keeps the habit of sourcing strong for the writer.

## What the demo shows, and what it does not show

The demo shows the pattern at miniature scale: 7 invented blocks, 5 accepted, 2 rejected with reasons, 4 of 5 sections covered, and a readiness check that names the one missing section. It does not show real documents, real extraction, real figures, or the Txvni product, and it claims no accuracy or outcome result. It is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao

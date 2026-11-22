# IC memo assembly pattern

A reference pattern and a small runnable demo for assembling an investment committee memo from parts that each carry a source. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

A deal team reads many source documents and then writes one memo. The writing step is where numbers lose their sources. A figure gets copied from a spreadsheet, a risk gets summarized from memory, and a benchmark gets stated with no record of where it came from. When the committee asks where a claim came from, the answer takes a fresh search through the source files.

Assembly from sourced parts prevents that loss. Each part of the memo arrives as a small block with its text, its section, and the name of the source it came from. The memo is built only from those blocks, and any section with no block stays visibly empty instead of being filled from memory.

## What the pattern does

1. Every memo section is named in advance, in a fixed order.
2. Every content block names the section it belongs to and the source document it came from.
3. A block with no source is rejected and recorded as rejected, not quietly included.
4. A block for an unknown section is rejected, so new sections cannot appear by accident.
5. The assembled memo prints each section in order, with the source named under each block.
6. A readiness check lists every section that is still empty, and the memo is marked as a draft until no required section is empty.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It feeds 7 invented blocks into the assembler. Five blocks are accepted, one block is rejected because it has no source, and one block is rejected because its section is unknown. The assembled memo covers 4 of the 5 sections, the risks section stays empty after its only block was rejected, and the readiness check reports the memo as not ready and names risks as the missing section.

The docs folder describes the pattern in full: what a block contains, why a source is required, why section order is fixed, and what readiness can and cannot prove.

## What this is not

This demo is not the Txvni product. It models the IC memo idea Txvni lists among its features, at miniature scale, with invented sample data. No real documents, deals, users, or outcomes appear here, and no accuracy or outcome number is claimed. A real system would add the steps this demo does not model, such as reading real documents, extracting real figures, checking figures against sources, access rules, and human review before any memo is used. None of those are modeled here.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao

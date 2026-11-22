"""Reference demo: assembling an IC memo from sourced blocks.

Every sample name, document, and figure in this file is invented.
The demo models the IC memo step described for Txvni, an AI deal
workspace that lists IC memos among its features. It is not the
Txvni product and it makes no claim about real usage or outcomes.
"""

SECTIONS = ["overview", "kpis", "benchmarks", "risks", "recommendation"]


class MemoAssembler:
    def __init__(self, sections):
        self.sections = list(sections)
        self.blocks = {name: [] for name in self.sections}
        self.rejected = []

    def add_block(self, section, text, source):
        if section not in self.blocks:
            self.rejected.append((section, text, "unknown section"))
            return False
        if not source or not source.strip():
            self.rejected.append((section, text, "missing source"))
            return False
        if not text or not text.strip():
            self.rejected.append((section, text, "empty text"))
            return False
        self.blocks[section].append((text, source))
        return True

    def missing_sections(self):
        return [name for name in self.sections if not self.blocks[name]]

    def is_ready(self):
        return not self.missing_sections()

    def render(self):
        lines = []
        for name in self.sections:
            lines.append(f"## {name}")
            if not self.blocks[name]:
                lines.append("(empty)")
            for text, source in self.blocks[name]:
                lines.append(f"- {text}")
                lines.append(f"  source: {source}")
        return "\n".join(lines)


SAMPLE_BLOCKS = [
    ("overview", "Fictional Company A sells inventory software to small retailers.", "company_overview.txt"),
    ("kpis", "Revenue grew from 100 to 125 in the sample spreadsheet.", "sample_financials.csv"),
    ("kpis", "Gross margin in the sample spreadsheet is 44 percent.", "sample_financials.csv"),
    ("benchmarks", "Sample peer median gross margin is 40 percent.", "sample_peers.csv"),
    ("risks", "Customer concentration is high in the sample notes.", ""),
    ("recommendation", "Proceed to a deeper review of the sample file.", "review_notes.txt"),
    ("market", "The wider market is growing in the sample report.", "sample_report.txt"),
]


def main():
    memo = MemoAssembler(SECTIONS)
    accepted = 0
    for section, text, source in SAMPLE_BLOCKS:
        if memo.add_block(section, text, source):
            accepted += 1

    total = len(SAMPLE_BLOCKS)
    print(f"{total} blocks received, {accepted} accepted, {len(memo.rejected)} rejected")
    assert total == 7 and accepted == 5 and len(memo.rejected) == 2

    reasons = sorted(reason for _, _, reason in memo.rejected)
    print(f"rejection reasons: {reasons}")
    assert reasons == ["missing source", "unknown section"]

    covered = len(SECTIONS) - len(memo.missing_sections())
    print(f"sections covered: {covered} of {len(SECTIONS)}")
    assert covered == 4

    missing = memo.missing_sections()
    print(f"missing sections: {missing}")
    assert missing == ["risks"]

    ready = memo.is_ready()
    print(f"memo ready: {ready}")
    assert ready is False

    rendered = memo.render()
    print(rendered)
    assert "source: sample_financials.csv" in rendered
    assert "## risks\n(empty)" in rendered

    print("all checks passed")


if __name__ == "__main__":
    main()

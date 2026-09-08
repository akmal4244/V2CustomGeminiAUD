"""Static invariants for the public training site; Python standard library only."""
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    "Tiada Mandat", "Tadbir Urus", "Kesilapan / Isu Teknikal", "Kecuaian",
    "Pembaziran", "Pemborosan", "Penyelewengan / Ketirisan",
]
DOWNLOADS = [
    "Arahan_Gem_v4.4.1.md", "Panduan_Format_Analisis_Audit_v4.4.1.md",
    "Panduan_7_Kategori_Isu_Audit_v4.4.1.md", "Rangka_Pembentangan_v4.4.1.md",
    "Contoh_Latihan_Sintetik_v4.4.1.md",
]


class Site(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.slides, self.copy_targets, self.urls = [], [], [], []
        self.text = []

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "section" and a.get("data-slide"):
            self.slides.append(a["data-slide"])
        if a.get("data-copy-target"):
            self.copy_targets.append(a["data-copy-target"])
        for name in ("href", "src"):
            if a.get(name):
                self.urls.append(a[name])

    def handle_data(self, text):
        self.text.append(text)


html = (ROOT / "index.html").read_text(encoding="utf-8")
p = Site()
p.feed(html)
assert p.slides == [str(n) for n in range(1, 12)], p.slides
assert not [k for k, v in Counter(p.ids).items() if v > 1], "Duplicate HTML IDs"
assert set(p.copy_targets) <= set(p.ids), "Missing clipboard target"
assert "prompt-full" in p.copy_targets
assert all(f"bonus-prompt-{n}" in p.copy_targets for n in range(1, 11))

text = unescape(" ".join(p.text))
for name in CATEGORIES:
    assert name in text, f"Category missing: {name}"
assert not re.search(r"(?<![\d.])\b5\s+[Kk]ategori\b", text), "Obsolete taxonomy"
assert "13soyVBmExhzZiL88kbKawhKt1rzceJrF" not in html, "Legacy Gem URL"
assert "/gems/edit/" not in html, "Owner editor URL must not be advertised"
assert not re.search(r"Rendah\s*[:=(]?\s*1\s*[-–]\s*3\b", text), "Wrong Low band"
assert not re.search(r"Sederhana\s*[:=(]?\s*4\s*[-–]\s*8\b", text), "Wrong Moderate band"

for url in p.urls:
    if url.startswith(("http:", "https:", "mailto:", "tel:", "data:")):
        continue
    if url.startswith("#"):
        assert url[1:] in p.ids or url[1:].isdigit(), f"Unknown anchor: {url}"
        continue
    path = url.split("#")[0].split("?")[0]
    assert not path.startswith("/"), f"Project Pages needs relative path: {url}"
    assert (ROOT / path).is_file(), f"Missing local resource: {url}"

for name in DOWNLOADS:
    path = ROOT / "downloads" / name
    assert path.is_file() and path.stat().st_size > 100
    assert f"downloads/{name}" in p.urls, f"Download not linked: {name}"
    content = path.read_text(encoding="utf-8")
    for category in CATEGORIES:
        assert category in content, f"{name}: missing {category}"

canonical = (ROOT / "downloads" / DOWNLOADS[0]).read_text(encoding="utf-8")
format_guide = (ROOT / "downloads" / DOWNLOADS[1]).read_text(encoding="utf-8")
assert canonical == format_guide, "Format knowledge drifted from canonical instructions"

workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
assert "path: _site" in workflow and "include-hidden-files: true" not in workflow
for name in DOWNLOADS:
    assert name in workflow, f"Download omitted from deployment: {name}"

print(f"PASS: 11 slides; {len(p.ids)} unique IDs; {len(p.copy_targets)} clipboard controls")
print("PASS: seven-category terminology, risk bands, resources and five downloads")
print("PASS: canonical knowledge equality and allowlisted Pages artifact")

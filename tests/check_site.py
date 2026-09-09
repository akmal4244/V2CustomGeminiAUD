"""Static invariants for the public training site; Python standard library only."""
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
GEM_URL = "https://gemini.google.com/gem/1V-Tcts6MVW--dL2D6SRqQ4YIxiX-flui?usp=sharing"
CATEGORIES = [
    "Tadbir Urus", "Tiada Mandat", "Kesilapan / Isu Teknikal", "Kecuaian",
    "Pembaziran", "Pemborosan", "Penyelewengan / Ketirisan",
]
DOWNLOADS = [
    "Markah_Risiko_4x4.pdf", "Panduan_Format_Analisis_Audit_V6_Kod_Tajuk.txt",
    "Panduan_7_Kategori_Isu_Audit_V6.txt", "Instruction_Gem_Penganalisis_Audit_V6_Kod_Tajuk.txt",
    "Prompt_Kali_Pertama_Analisis_V6_Kod_Tajuk.txt", "Templat_Fokus_Pengurusan_V6.md",
    "Contoh_Latihan_Sintetik_V6.md",
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
assert "/gems/view" not in html and "gemini.google.com/u/" not in html, "Use participant share link"
assert "10xOZ5ybA6Eqc0A9xzykmgTHPl_rq9sBK" not in html, "Obsolete shared V4.4.1 Gem"
assert p.urls.count(GEM_URL) == 3, "All three reference-layout Gem links must use the official V6 share URL"
assert re.search(r'<pre\b[^>]*id="gem-link"[^>]*>' + re.escape(GEM_URL) + r'</pre>', html), "Copied Gem URL differs"
slide_one = re.search(r'<section\b[^>]*data-slide="1".*?</section>', html, re.S).group()
assert 'class="hero-grid"' in slide_one and 'class="gemini-badge gemini-link"' in slide_one
assert "Buka Custom Gemini V6" in text
assert not re.search(r'<details\b[^>]*id="gem-downloads"[^>]*\bopen\b', html), "Optional downloads must start collapsed"
for obsolete in ("Bina Gem sendiri", "bina Gem,", "Gem baharu / New Gem", "Buka pengurus Gems"):
    assert obsolete not in text, f"Obsolete participant setup step: {obsolete}"
readme = (ROOT / "README.md").read_text(encoding="utf-8")
assert GEM_URL in readme and "menyediakan Gem sendiri" not in readme
# The supplied image prompt explicitly forbids the old band. Validate its
# structured mapping below; check the remaining slide text independently.
without_image = Site()
without_image.feed(re.sub(r'<pre id="image-prompt"[^>]*>.*?</pre>', '', html, flags=re.S))
assert not re.search(r"Rendah\s*[:=(]?\s*1\s*[-–]\s*3\b", ' '.join(without_image.text)), "Wrong Low band"
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
    if path.suffix == ".pdf":
        assert path.read_bytes().startswith(b"%PDF-"), "Invalid risk PDF"
        continue
    content = path.read_text(encoding="utf-8")
    for category in CATEGORIES:
        assert category in content, f"{name}: missing {category}"

manifest = json.loads((ROOT / "downloads/manifest-v6.json").read_text(encoding="utf-8"))
assert manifest["version"] == "V6" and len(manifest["files"]) == 5
assert manifest["revision"] == "Kod Tajuk"
for source in manifest["files"]:
    assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"], f"Source artifact changed: {source['path']}"

prompt = re.search(r'<pre id="prompt-full"[^>]*>(.*?)</pre>', html, re.S).group(1)
assert unescape(prompt).strip() == (ROOT / "downloads/Prompt_Kali_Pertama_Analisis_V6_Kod_Tajuk.txt").read_text(encoding="utf-8").strip(), "Copied prompt differs from V6 source"
assert re.findall(r'<dt>(.*?)</dt>', html) == [f"K{i} — {name}" for i, name in enumerate(CATEGORIES, 1)], "Wrong category order"
structure = re.search(r'<ol[^>]*id="report-structure".*?</ol>', html, re.S).group()
assert structure.count("<li>") == 6, "V6 has six report sections"
assert "N_sah + N_belum = N" in text
assert 'id="title-code-guide"' in html
assert "PU-[KOD TAJUK]-[NN]" in unescape(prompt)
assert "Bahagian 2A" in unescape(prompt)
assert not re.search(r"PU-\d+-\d+", text), "Obsolete numeric-only title IDs"
assert "STATUS PENILAIAN RISIKO KESELURUHAN: SEPARA — BELUM LENGKAP" in text
for obsolete in (r"[vV]4\.4\.1", r"\b[Hh]ibrid\b", r"[Mm]aksimum tiga", r"Bahagian 7", r"K1\s*[—–-]\s*Tiada Mandat", r"K2\s*[—–-]\s*Tadbir Urus"):
    assert not re.search(obsolete, text), f"Outdated V4 rule: {obsolete}"

# Preserve the original training journey while the methodology follows V6.
sections = {int(n): body for n, body in re.findall(r'<section\b[^>]*data-slide="(\d+)"[^>]*>(.*?)</section>', html, re.S)}
assert 'class="two-col"' in sections[3], "Reference access slide has two columns"
assert "Custom Gemini langkah demi langkah" in sections[2]
assert "Tanya Custom Gemini untuk memecahkan maklumat" in sections[7]
assert sections[7].count('class="prompt-box"') == 10 and '<details' not in sections[7], "Keep all ten bonus examples visible"
template_url = "https://docs.google.com/presentation/d/1qAY56GkkvYxQsKS5fhZaSlzfs1uqvOBn/edit?usp=sharing&ouid=105726279532383248637&rtpof=true&sd=true"
assert template_url in p.urls and "Templat asal ialah rujukan susun atur" in sections[9]
assert "K1–K7 V6, Kod Tajuk" in sections[9]
assert "Buat rumusan visual menggunakan Gemini Image" in sections[10]
assert "sembang Gemini baharu" in sections[7] and "sembang Gemini baharu" in sections[10]
assert "sedia dimasukkan ke templat slaid" in sections[1]
assert "templat slaid" in sections[11] and "rumusan visual" in sections[11]

image_prompt = unescape(re.search(r'<pre id="image-prompt"[^>]*>(.*?)</pre>', html, re.S).group(1))
raw_image_json = image_prompt.removeprefix('```json\n').removesuffix('\n```')
visual = json.loads(raw_image_json)
# Exact user-supplied image prompt, with line endings normalized to LF.
assert hashlib.sha256(raw_image_json.encode('utf-8')).hexdigest() == '82451f61c5278c187f36095d2dc543785e04ae9c47f8c728c038a9fa56202681'
assert visual['versi_templat'] == '6.0_dinamik_7kategori_risiko4x4_kodtajuk'
assert visual['taburan_kategori_isu_v6']['kategori_standard'] == [f'K{i} {c.upper()}' for i, c in enumerate(CATEGORIES, 1)]
assert visual['peraturan_risiko_4x4_v6']['pemetaan_tahap_risiko'] == {'RENDAH': '1 hingga 4', 'SEDERHANA': '5 hingga 8', 'TINGGI': '9 hingga 12', 'KRITIKAL': '13 hingga 16'}
assert visual['logik_kelengkapan_risiko_v6']['formula'] == 'N_sah + N_belum = N'
assert visual['panel_risiko_keseluruhan_dinamik']['jika_penilaian_separa']['visual'] == 'kad_status_bukan_tolok'
assert visual['panel_risiko_keseluruhan_dinamik']['jika_penilaian_separa']['status'] == 'SEPARA — BELUM LENGKAP'
assert visual['tajuk_imej']['subtajuk_dinamik']['jika_tiada_markah_rasmi_langsung'] == 'PENEMUAN & RISIKO AUDIT'
assert "Jika markah atau penarafan rasmi tidak wujud, buang terus medan Prestasi daripada kad." in visual['kad_dinamik_tajuk_audit']['logik_paparan_prestasi']

workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
assert "path: _site" in workflow and "include-hidden-files: true" not in workflow
for name in DOWNLOADS:
    assert name in workflow, f"Download omitted from deployment: {name}"
assert "manifest-v6.json" in workflow

print(f"PASS: 11 slides; {len(p.ids)} unique IDs; {len(p.copy_targets)} clipboard controls")
print("PASS: V6 category order, six report sections, risk bands and seven downloads")
print("PASS: original 11-slide journey, template link, visible bonus prompts and valid V6 image JSON")
print("PASS: official Gem share URL and optional reference downloads")
print("PASS: original source hashes, exact V6 clipboard prompt and allowlisted Pages artifact")
print("PASS: latest Kod Tajuk source revision and meaningful finding IDs")

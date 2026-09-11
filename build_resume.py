from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(
    TTFont("ResumeSerif", "/usr/share/fonts/noto/NotoSerif-Regular.ttf")
)
pdfmetrics.registerFont(
    TTFont("ResumeSerif-Bold", "/usr/share/fonts/noto/NotoSerif-Bold.ttf")
)
pdfmetrics.registerFont(
    TTFont("ResumeSerif-Italic", "/usr/share/fonts/noto/NotoSerif-Italic.ttf")
)
pdfmetrics.registerFontFamily(
    "ResumeSerif",
    normal="ResumeSerif",
    bold="ResumeSerif-Bold",
    italic="ResumeSerif-Italic",
    boldItalic="ResumeSerif-Bold",
)

OUT = "output/pdf/Utkarsh_Solanki_Resume.pdf"
NAVY = HexColor("#17365D")
GRAY = HexColor("#6E6E6E")

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Name",
        parent=styles["Normal"],
        fontName="ResumeSerif-Bold",
        fontSize=23,
        leading=27,
        alignment=TA_CENTER,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Tagline",
        parent=styles["Normal"],
        fontName="ResumeSerif",
        fontSize=12.2,
        leading=15,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Contact",
        parent=styles["Normal"],
        fontName="ResumeSerif",
        textColor=NAVY,
        fontSize=9.7,
        leading=13,
        alignment=TA_CENTER,
        spaceAfter=13,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        parent=styles["Normal"],
        fontName="ResumeSerif-Bold",
        textColor=NAVY,
        fontSize=13.1,
        leading=16,
        spaceBefore=6,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontName="ResumeSerif",
        fontSize=11.1,
        leading=14.4,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="ResumeBullet",
        parent=styles["Body"],
        leftIndent=17,
        firstLineIndent=-10,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="ItemTitle",
        parent=styles["Normal"],
        fontName="ResumeSerif-Bold",
        textColor=NAVY,
        fontSize=10.9,
        leading=13.3,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="Date",
        parent=styles["Normal"],
        fontName="ResumeSerif-Italic",
        fontSize=10.8,
        leading=13.3,
        alignment=2,
    )
)


def section(title):
    return [
        Paragraph(title.upper(), styles["Section"]),
        Table(
            [[""]],
            colWidths=[6.45 * inch],
            rowHeights=[0.35],
            style=TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.45, GRAY)]),
        ),
    ]


def bullets(items):
    return [Paragraph("• " + item, styles["ResumeBullet"]) for item in items]


def heading(left, right=""):
    row = Table(
        [[Paragraph(left, styles["ItemTitle"]), Paragraph(right, styles["Date"])]],
        colWidths=[4.85 * inch, 1.60 * inch],
    )
    row.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return row


story = [
    Paragraph("Utkarsh Solanki", styles["Name"]),
    Paragraph(
        "Cybersecurity Student | Web Application Security &amp; Penetration Testing",
        styles["Tagline"],
    ),
    Paragraph(
        "utkarshsolanki776@gmail.com  |  github.com/Utkarsh464  |  linkedin.com/in/utkarsh-solanki-337806252  |  tryhackme.com/p/utkarsshh  |  India",
        styles["Contact"],
    ),
]

story += section("Summary")
story.append(
    Paragraph(
        "Final-year BCA student focused on cybersecurity, with hands-on experience in web application security and penetration "
        "testing through self-directed labs. Completed 85+ TryHackMe rooms and 34 PortSwigger Web Security Academy labs, "
        "and built Python-based security tooling — an HTTP proxy, a directory brute-forcer, and a penetration-testing toolkit "
        "— to understand vulnerabilities at the protocol level. Seeking a cybersecurity internship in web application security / "
        "penetration testing.",
        styles["Body"],
    )
)

story += section("Education")
story.append(
    heading(
        "Bachelor of Computer Applications (BCA) — Galgotias University",
        "Final-Year Student",
    )
)

story += section("Technical Skills")
story += bullets(
    [
        "<b>Security:</b> Web Application Security, Penetration Testing, OWASP Top 10, SQL Injection (UNION-based, blind, error-based), Cross-Site Scripting (XSS), Access Control Vulnerabilities, SSRF, Path Traversal",
        "<b>Tools:</b> Burp Suite, Nmap, Metasploit Framework, Hydra, Netcat, Git/GitHub",
        "<b>Networking:</b> TCP/IP, HTTP, DNS, Sockets, Subnetting",
        "<b>Programming:</b> Python (security tooling, sockets, threading, automation), Bash",
        "<b>Platforms:</b> Linux (Kali Linux), Metasploitable 2, DVWA, WebGoat, TryHackMe, PortSwigger Web Security Academy",
    ]
)

story += section("Projects — Python Security Tooling")

story.append(
    heading("HTTP Proxy &amp; Parser — http-proxy-lab", "Python (Standard Library)")
)
story += bullets(
    [
        "Built a forward HTTP proxy and request/response parser from raw TCP sockets (no frameworks) to study HTTP internals end-to-end.",
        "Implemented Content-Length-driven body reads and origin-form path rewriting; documented the proxy's own attack surface (open-proxy/SSRF exposure, unbounded-buffer DoS).",
    ]
)

story.append(heading("pentools — Python Security Toolkit", "Python, requests, pypdf"))
story += bullets(
    [
        "Built five standalone CLI security tools: a TCP port scanner, hash identifier/cracker, password hasher (MD5–SHA512), PDF password auditor, and blind SQL injection extractor.",
        "The blind SQLi tool automates a PortSwigger lab exploit (Oracle conditional-error oracle), extracting data character-by-character via HTTP response codes.",
    ]
)

story.append(
    heading(
        "dir-brute — Directory Brute-Forcer &amp; Crawler",
        "Python, threading, argparse",
    )
)
story += bullets(
    [
        "Built a multithreaded content-discovery tool that brute-forces hidden directories from a wordlist, filters by HTTP status code, and supports recursive re-scanning.",
        "Added URL normalization and a crawl mode; validated end-to-end in a documented lab writeup against a local test server.",
    ]
)

story += section("Hands-On Cybersecurity Experience")

story.append(heading("PortSwigger Web Security Academy — 34 Labs Solved"))
story += bullets(
    [
        "Solved 34 labs across five vulnerability classes: Access Control (13/13), SQL Injection (15/18 — UNION, blind, and error-based, across MySQL, Oracle &amp; MSSQL), Path Traversal, XSS, and SSRF.",
        "Documented each lab with recon, exploitation steps, payloads, root cause, and mitigation.",
    ]
)

story.append(heading("Metasploitable 2 / DVWA / WebGoat — 10 Documented Labs"))
story += bullets(
    [
        "Exploited 4 CVEs on Metasploitable 2 with the Metasploit Framework (vsFTPd backdoor, PHP CGI argument injection, Samba usermap_script, UnrealIRCd backdoor), plus SSH and Telnet credential brute-forcing.",
        "Performed a Hydra-driven brute-force and a blacklist-bypass reflected-XSS attack on DVWA, and an SSRF parameter-tampering attack on WebGoat via Burp Suite.",
    ]
)

story.append(heading("TryHackMe — 85+ Rooms, SEC0 Certified"))
story += bullets(
    [
        "Completed the Pre-Security path (SEC0 Professional Certification) and Cyber Security 101 (14/14 modules); currently working through the Jr Penetration Tester path.",
        "Authored structured writeups (commands, concepts, tools) for 85+ rooms across networking, Linux, cryptography, exploitation, and web security.",
    ]
)

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=0.72 * inch,
    leftMargin=0.72 * inch,
    topMargin=0.52 * inch,
    bottomMargin=0.50 * inch,
)
doc.build(story)
print(OUT)

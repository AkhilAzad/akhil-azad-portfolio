#!/usr/bin/env python3
"""Generate a clean, professional one-page resume PDF for Akhil Azad.
Pure reportlab (no browser needed). Light, ATS-friendly, restrained blue accent."""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, FrameBreak, NextPageTemplate,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---- Palette (print-appropriate) ----
INK        = HexColor("#15181d")   # near-black body
SUBINK     = HexColor("#3a4048")   # secondary text
MUTE       = HexColor("#6a7079")   # muted labels/dates
ACCENT     = HexColor("#2f5fd0")   # restrained blue (echoes the site accent)
RULE       = HexColor("#d7dbe0")   # hairline rules
LIGHTRULE  = HexColor("#e8eaee")

FONT       = "Helvetica"
FONT_B     = "Helvetica-Bold"
FONT_I     = "Helvetica-Oblique"

PAGE_W, PAGE_H = LETTER
MARGIN = 0.62 * inch

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "Akhil-Azad-Resume.pdf")

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(fontName=FONT, fontSize=9.3, leading=13.2, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

body      = S("body")
body_sub  = S("body_sub", textColor=SUBINK)
name      = S("name", fontName=FONT_B, fontSize=23, leading=25, textColor=INK, spaceAfter=0)
title     = S("title", fontName=FONT, fontSize=10.5, leading=14, textColor=ACCENT, spaceBefore=3)
contact   = S("contact", fontName=FONT, fontSize=8.6, leading=12.6, textColor=MUTE, alignment=TA_RIGHT)
section   = S("section", fontName=FONT_B, fontSize=8.2, leading=11, textColor=ACCENT, spaceBefore=2, spaceAfter=0)
role      = S("role", fontName=FONT_B, fontSize=9.7, leading=12.6, textColor=INK)
role_meta = S("role_meta", fontName=FONT, fontSize=8.4, leading=12.6, textColor=MUTE, alignment=TA_RIGHT)
bullet    = S("bullet", fontName=FONT, fontSize=9.1, leading=12.8, textColor=SUBINK, leftIndent=11, firstLineIndent=-11)
skill     = S("skill", fontName=FONT, fontSize=9.1, leading=13.4, textColor=SUBINK)

def section_header(text, story):
    story.append(Spacer(1, 9))
    story.append(Paragraph(text.upper(), ParagraphStyle(
        "sh", fontName=FONT_B, fontSize=8.4, leading=10, textColor=ACCENT,
        tracking=1)))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE,
                            spaceBefore=1, spaceAfter=6))

def bullets(items, story):
    for it in items:
        story.append(Paragraph("<font color='#2f5fd0'>▪</font>&nbsp;&nbsp;" + it, bullet))
        story.append(Spacer(1, 1.5))

# ---------------------------------------------------------------- doc
doc = BaseDocTemplate(
    OUT, pagesize=LETTER,
    leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
    title="Akhil Azad — Resume", author="Akhil Azad",
    subject="Software Developer / AI-ML Engineer", creator="akhilazad.dev",
)
frame = Frame(MARGIN, MARGIN, PAGE_W - 2*MARGIN, PAGE_H - 2*MARGIN,
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="main")

def decorate(canvas, d):
    # thin accent bar down the left margin edge — subtle brand echo
    canvas.saveState()
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 0.0, 0, 0, fill=1, stroke=0)  # no-op guard
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2.4)
    canvas.line(MARGIN, PAGE_H - MARGIN + 20, MARGIN + 34, PAGE_H - MARGIN + 20)
    canvas.restoreState()

doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])

story = []

# ---- Header: name + title (left)  |  contact (right) ----
left = [
    Paragraph("AKHIL AZAD", name),
    Paragraph("Software Developer &nbsp;·&nbsp; AI / ML Engineer", title),
]
right = [
    Paragraph("akhilazad9623@gmail.com", contact),
    Paragraph("github.com/AkhilAzad", contact),
    Paragraph("linkedin.com/in/akhil-azad-378147325", contact),
]
head = Table([[left, right]], colWidths=[(PAGE_W-2*MARGIN)*0.62, (PAGE_W-2*MARGIN)*0.38])
head.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (1,0), (1,0), 4),
]))
story.append(head)
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1.4, color=INK, spaceAfter=2))

# ---- Summary ----
section_header("Summary", story)
story.append(Paragraph(
    "Third-year Computer Science Engineering student with a strong foundation in artificial "
    "intelligence, machine learning and software engineering, plus a genuine interest in robotics "
    "and intelligent systems. Independently architected a modular AI assistant with natural language "
    "understanding, computer vision and voice interaction, alongside full-stack development across the SDLC.",
    body_sub))

# ---- Education ----
section_header("Education", story)
edu = Table([[
    Paragraph("<b>Chitkara University</b> &nbsp;—&nbsp; B.E. Computer Science", role),
    Paragraph("Expected June 2028", role_meta),
]], colWidths=[(PAGE_W-2*MARGIN)*0.72, (PAGE_W-2*MARGIN)*0.28])
edu.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story.append(edu)

# ---- Technical Skills ----
section_header("Technical Skills", story)
skills = [
    ("AI / ML", "Local LLM integration, Ollama, Llama-based models, natural language understanding, reasoning pipelines"),
    ("Computer Vision", "OpenCV, YOLO, object detection, face recognition"),
    ("Voice / Speech", "Speech recognition, text-to-speech"),
    ("Programming", "Python, Java, C, SQL, JavaScript"),
    ("Engineering", "OOP, modular architecture, data structures &amp; algorithms, SDLC"),
    ("Frameworks &amp; Tools", "React, Node.js, Express, MongoDB, Git, GitHub, VS Code, Vercel, Render"),
]
rows = []
for label, val in skills:
    rows.append([
        Paragraph(label, ParagraphStyle("sk_l", fontName=FONT_B, fontSize=9.1, leading=13.4, textColor=INK)),
        Paragraph(val, skill),
    ])
sk_tbl = Table(rows, colWidths=[(PAGE_W-2*MARGIN)*0.24, (PAGE_W-2*MARGIN)*0.76])
sk_tbl.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,-1),8),
    ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),1.5),
]))
story.append(sk_tbl)

# ---- Projects ----
section_header("Projects", story)

def project(nametxt, meta, desc, story):
    t = Table([[
        Paragraph(nametxt, role),
        Paragraph(meta, role_meta),
    ]], colWidths=[(PAGE_W-2*MARGIN)*0.72, (PAGE_W-2*MARGIN)*0.28])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1),
    ]))
    story.append(t)
    story.append(Paragraph(desc, body_sub))
    story.append(Spacer(1, 5))

project("Project HALO",
        "AI Assistant · Python",
        "Modular local AI operating system with natural-language understanding, computer vision, voice "
        "interaction, local LLMs, planning and intelligent automation — designed as an extensible platform.",
        story)
project("Conclave",
        "Multi-Agent Framework · Python",
        "Modular multi-agent orchestration framework for building autonomous AI teams and coordinating "
        "specialized agents with shared knowledge and agent components.",
        story)
project("Become Fit",
        "Full-Stack · Web",
        "Full-stack fitness coaching platform with Razorpay payment integration and automated PDF program delivery.",
        story)
project("SARA AI",
        "Voice Assistant · Python",
        "Local voice assistant combining speech recognition, text-to-speech, computer vision, contextual "
        "memory and task automation.",
        story)

# ---- Certifications ----
section_header("Certifications", story)
certs = [
    "Machine Learning, Generative AI &amp; Prompt Engineering — Coursera",
    "AI and Disaster Management — DeepLearning.AI",
    "The Rudiments of AI, ChatGPT, DeepSeek, Grok &amp; the Metaverse — Coursera",
    "Technical Communication — Coursera",
]
for c in certs:
    story.append(Paragraph("<font color='#2f5fd0'>▪</font>&nbsp;&nbsp;" + c, bullet))
    story.append(Spacer(1, 1.5))

doc.build(story)
print("PDF written:", OUT)

from pptx import Presentation
from pptx.util import Inches

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

slides_content = [
    ("Laser-Based Additive Manufacturing", "Overview, process fundamentals and research insights"),
    ("Introduction", "Definition, evolution and advantages of LBAM"),
    ("Working Principle", "Laser–powder interaction, thermal cycle and melt pool formation"),
    ("Materials Used", "Metals–Ni, Ti, Al, Stainless Steel; Ceramic & Composite research"),
    ("Process Parameters", "Laser power, hatch spacing, scan speed, layer thickness"),
    ("Microstructure Development", "Solidification, grain boundary evolution, anisotropy"),
    ("Defects & Challenges", "Porosity, balling, cracking, residual stress"),
    ("Mechanical Properties", "Tensile, fatigue, density & hardness performance"),
    ("Applications", "Aerospace, medical implants, automotive, energy"),
    ("Future Scope", "In-situ monitoring, AI for optimization, multi-material printing"),
    ("Conclusion", "LBAM enables advanced manufacturing with exceptional freedom"),
    ("References", "IEEE, Elsevier, Springer research papers")
]

for title, content in slides_content:
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

prs.save("Laser-Based Additive Manufacturing.pptx")
print("PPT successfully generated!")


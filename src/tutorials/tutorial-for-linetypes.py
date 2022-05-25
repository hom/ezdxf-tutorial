import ezdxf
from ezdxf.tools.standards import linetypes  # some predefined linetypes

'''
doc = ezdxf.new()
msp = doc.modelspace()

my_line_types = [
    (
        "DOTTED",
        "Dotted .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .",
        [0.2, 0.0, -0.2],
    ),
    (
        "DOTTEDX2",
        "Dotted (2x) .    .    .    .    .    .    .    . ",
        [0.4, 0.0, -0.4],
    ),
    (
        "DOTTED2",
        "Dotted (.5) . . . . . . . . . . . . . . . . . . . ",
        [0.1, 0.0, -0.1],
    ),
]
for name, desc, pattern in my_line_types:
    if name not in doc.linetypes:
        doc.linetypes.add(
            name=name,
            pattern=pattern,
            description=desc,
        )

for name, desc, pattern in linetypes():
    if name not in doc.linetypes:
        doc.linetypes.add(
            name=name,
            pattern= pattern,
            description=desc,
        )

# iteration
print("available linetypes:")
for lt in doc.linetypes:
    print(f"{lt.dxf.name}: {lt.dxf.description}")

# check for existing linetype
if "DOTTED" in doc.linetypes:
    pass

count = len(doc.linetypes) # total count of linetypes
'''

doc = ezdxf.new("R2018")  # DXF R13 or later is required

doc.linetypes.add(
    name="GASLEITUNG2",
    # linetype definition string from acad.lin:
    pattern='A,.5,-.2,["GAS",STANDARD,S=.1,U=0.0,X=-0.1,Y=-.05],-.25',
    description= "Gasleitung2 ----GAS----GAS----GAS----GAS----GAS----",
    length=1,  # required for complex line types
)

doc.linetypes.add("GRENZE2",
    # linetype definition in acad.lin:
    # A,.25,-.1,[BOX,ltypeshp.shx,x=-.1,s=.1],-.1,1
    # replacing BOX by shape index 132 (got index from an AutoCAD file),
    # ezdxf can't get shape index from ltypeshp.shx
    pattern="A,.25,-.1,[132,ltypeshp.shx,x=-.1,s=.1],-.1,1",
    description="Grenze eckig ----[]-----[]----[]-----[]----[]--",
    length= 1.45,  # required for complex line types
)

doc.saveas('output/linetypes.dxf')

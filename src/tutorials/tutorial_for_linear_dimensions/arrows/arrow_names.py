import ezdxf
from enum import Enum, auto

arrow = [
    "", "DOT", "DOTSMALL", "DOTBLANK", "ORIGIN", "ORIGIN2", "OPEN", "OPEN90",
    "OPEN30", "CLOSED", "SMALL", "NONE", "OBLIQUE", "BOXFILLED", "BOXBLANK",
    "CLOSEDBLANK", "DATUMFILLED", "DATUMBLANK", "INTEGRAL", "ARCHTICK",
    "EZ_ARROW", "EZ_ARROW_BLANK", "EZ_ARROW_FILLED"
]

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

for i in range(len(arrow)):
    msp.add_linear_dim(
        base=(i * 3 + i, 2),
        p1=(i * 3 + i, 0),
        p2=((i + 1) * 3 + i, 0),
        override={
            "dimtsz": 0,  # set tick size to 0 to enable arrow usage
            "dimasz": 0.25,  # arrow size in drawing units
            "dimblk": arrow[i],  # arrow block name
        }).render()

doc.saveas("output/arrow_names.dxf")

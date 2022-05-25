import ezdxf
import os

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_linear_dim(base=(3, 1),
                   p1=(3, 0),
                   p2=(6, 0),
                   override={
                       "dimclrd": 1,
                       "dimdle": 0.5,
                       "dimltype": "DASHED2",
                       "dimlwd": 35,
                   }
                   ).render()

dim = msp.add_linear_dim(base=(3, 2),
                   p1=(3, 0),
                   p2=(6, 0),
                   )

dim.set_dimline_format(
    color=2, linetype="DASHED2", lineweight=35, extension=0.25
)
dim.render()

doc.saveas("output/dimension_line_properties.dxf")

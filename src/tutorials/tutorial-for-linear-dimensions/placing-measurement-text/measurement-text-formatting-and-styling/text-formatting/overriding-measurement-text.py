import ezdxf
import os

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_linear_dim(base=(3, 1),
                   p1=(3, 0),
                   p2=(6, 0),
                   text="<>"
                   ).render()

msp.add_linear_dim(base=(3, 2),
                   p1=(3, 0),
                   p2=(6, 0),
                   text=">1m"
                   ).render()

msp.add_linear_dim(base=(3, 3),
                   p1=(3, 0),
                   p2=(6, 0),
                   text="~<>cm"
                   ).render()

doc.saveas("output/overriding_measurement_text.dxf")

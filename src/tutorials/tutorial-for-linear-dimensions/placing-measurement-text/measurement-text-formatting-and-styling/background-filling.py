import ezdxf
import os

doc = ezdxf.new('R2018', setup=True)
msp = doc.modelspace()

msp.add_linear_dim(base=(3, 1),
                   p1=(3, 0),
                   p2=(6, 0),
                   override={
                       "dimtfill": 2,
                       "dimtfillclr": 1,
                   }).render()

msp.add_linear_dim(base=(3, 2),
                   p1=(3, 0),
                   p2=(6, 0),
                   override={
                       "dimtfill": 2,
                       "dimtfillclr": 2
                   }).render()

msp.add_linear_dim(base=(3, 3),
                   p1=(3, 0),
                   p2=(6, 0),
                   override={
                       "dimtfill": 2,
                       "dimtfillclr": 3
                   }).render()

print(os.getcwd())
doc.saveas("output/background_filling.dxf")

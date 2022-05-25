import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_linear_dim(
    base=(3, 2), p1=(3, 0), p2=(6, 0), location=(4, 4)
).render()
msp.add_linear_dim(
    base=(3, 1), p1=(3, 0), p2=(6, 0), location=(3, 1)
).render()

doc.saveas('output/location_relative_to_origin.dxf')

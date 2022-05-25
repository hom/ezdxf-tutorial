import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

dim = msp.add_linear_dim(base=(3, 2), p1=(3, 0), p2=(6, 0))
dim.shift_text(dh=1, dv=1)
dim.render()

dim1 = msp.add_linear_dim(base=(7, 2), p1=(7, 0), p2=(10, 0))
dim1.set_text_align(halign="center")
dim1.render()

doc.saveas('output/location_relative_to_default_location.dxf')

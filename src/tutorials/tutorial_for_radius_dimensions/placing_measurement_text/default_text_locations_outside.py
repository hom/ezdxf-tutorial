import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

dim = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=45,
    dimstyle="EZ_RADIUS"
)
dim.render()  # always required, but not shown in the following examples

doc.saveas("output/default_text_locations_outside.dxf")

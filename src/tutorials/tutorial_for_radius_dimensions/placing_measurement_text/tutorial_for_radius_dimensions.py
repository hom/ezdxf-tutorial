import ezdxf

# DXF R2010 drawing, official DXF version name: 'AC1024',
# setup=True setups the default dimension styles
doc = ezdxf.new("R2010", setup=True)

msp = doc.modelspace()  # add new dimension entities to the modelspace
msp.add_circle((0, 0), radius=3)  # add a CIRCLE entity, not required
# add default radius dimension, measurement text is located outside
dim = msp.add_radius_dim(
    center=(0, 0), radius=3, angle=45, dimstyle="EZ_RADIUS"
)
# necessary second step, to create the BLOCK entity with the dimension geometry.
dim.render()
doc.saveas("tutorial_for_radius_dimensions.dxf")

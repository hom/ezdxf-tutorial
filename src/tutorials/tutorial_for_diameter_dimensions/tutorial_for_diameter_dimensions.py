import ezdxf

# setup=True setups the default dimension styles
doc = ezdxf.new("R2010", setup=True)

msp = doc.modelspace()  # add new dimension entities to the modelspace
msp.add_circle((0, 0), radius=3)  # add a CIRCLE entity, not required
# add default diameter dimension, measurement text is located outside
dim = msp.add_diameter_dim(
    center=(0, 0),
    radius=3,
    angle=45,
    dimstyle="EZ_RADIUS"
)
dim.render()
doc.saveas("output/tutorial_for_diameter_dimensions.dxf")

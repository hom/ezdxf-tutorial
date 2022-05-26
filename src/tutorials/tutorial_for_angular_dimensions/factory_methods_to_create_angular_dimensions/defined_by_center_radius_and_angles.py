import ezdxf

# Create a DXF R2010 document:
# Use argument setup=True to setup the default dimension styles.
doc = ezdxf.new("R2010", setup=True)

# Add new entities to the modelspace:
msp = doc.modelspace()

# Add an angular DIMENSION defined by the center point, start- and end angles,
# the measurement text is placed at the default location above the dimension
# line:
dim = msp.add_angular_dim_cra(
    center=(5, 5),  # center point of the angle
    radius= 7,  # distance from center point to the start of the extension lines
    start_angle=60,  # start angle in degrees
    end_angle=120,  # end angle in degrees
    distance=3,  # distance from start of the extension lines to the dimension line
    dimstyle="EZ_CURVED",  # default angular dimension style
)

# Necessary second step to create the BLOCK entity with the dimension geometry.
# Additional processing of the DIMENSION entity could happen between adding
# the entity and the rendering call.
dim.render()
doc.saveas("output/defined_by_center_radius_and-angles.dxf")

import ezdxf

# Create a DXF R2010 document:
# Use argument setup=True to setup the default dimension styles.
doc = ezdxf.new("R2010", setup=True)

# Add new dimension entities to the modelspace:
msp = doc.modelspace()

# Add a LINE entity for visualization, not required to create the DIMENSION
# entity:
msp.add_line((0, 0), (3, 0))

# Add a horizontal linear DIMENSION entity:
dim1 = msp.add_linear_dim(
    base=(3, 2),  # location of the dimension line
    p1=(0, 0),  # 1st measurement point
    p2=(3, 0),  # 2nd measurement point
    dimstyle="EZDXF",  # default dimension style
)
dim2 = msp.add_linear_dim(
    base=(3, 1),  # location of the dimension line
    p1=(0, 0),  # 1st measurement point
    p2=(1.5, 0),  # 2nd measurement point
    dimstyle="EZDXF",  # default dimension style
)

# Necessary second step to create the BLOCK entity with the dimension geometry.
# Additional processing of the DIMENSION entity could happen between adding
# the entity and the rendering call.
dim1.render()
dim2.render()

doc.saveas("output/dim_linear_horiz.dxf")

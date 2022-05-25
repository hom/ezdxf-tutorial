import ezdxf

# Create a DXF R2010 document:
# Use argument setup=True to setup the default dimension styles.
doc = ezdxf.new("R2010", setup=True)

# Add new dimension entities to the modelspace:
msp = doc.modelspace()

# Add a LINE entity for visualization, not required to create the DIMENSION
# entity:
msp.add_line((0, 0), (3, 0))

# assignment to dim is not necessary, if no additional processing happens
msp.add_linear_dim(base=(3, 2), p1=(0, 0), p2=(3, 0), angle=-30).render()
doc.saveas("output/dim_linear_rotated.dxf")


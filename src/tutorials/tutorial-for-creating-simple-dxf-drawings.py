import ezdxf

# Create a new DXF R2010 drawing, official DXF version name: "AC1024"
doc = ezdxf.new('R2010')

# Add new entities to the modelspace:
msp = doc.modelspace()
# Add a LINE entity
msp.add_line((0, 0), (10, 0))
doc.saveas("output/line.dxf")

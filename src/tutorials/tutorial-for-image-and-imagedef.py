import ezdxf

# The IMAGE entity requires the DXF R2000 format or later.
doc = ezdxf.new('R2000')

# The IMAGEDEF entity is like a block definition, it just defines the image.
my_image_def = doc.add_image_def(
    filename='t012d05f033d8032c19.png', size_in_pixel=(300, 300)
)


msp = doc.modelspace()
# The IMAGE entity is like the INSERT entity, it's just an image reference,
# and there can be multiple references to the same picture in a DXF document.

# 1st image reference
msp.add_image(
    insert=(2, 1),
    size_in_units=(6.4, 3.6),
    image_def=my_image_def,
    rotation=0
)
# 2nd image reference
msp.add_image(
    insert=(4, 5),
    size_in_units=(3.2, 1.8),
    image_def=my_image_def,
    rotation=30
)

# Get existing image definitions from the OBJECTS section:
image_defs = doc.objects.query('IMAGEDEF')

doc.saveas('../output/dxf_with_cat.dxf')

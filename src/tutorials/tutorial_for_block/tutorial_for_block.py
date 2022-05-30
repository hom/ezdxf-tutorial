import ezdxf
import random


def get_random_point():
    """Return random x, y coordinates."""
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    return x, y


doc = ezdxf.new('R2018', setup=True)

flag = doc.blocks.new(name='FLAG')

flag.add_lwpolyline([(0, 0), (0, 5), (4, 3), (0, 3)])
flag.add_circle((0, 0), .4, dxfattribs={'color': 2})

# Get the modelspace of the drawing.
msp = doc.modelspace()

# Get 50 random placing points.
placing_points = [get_random_point() for _ in range(50)]

for point in placing_points:
    # Every flag has a different scaling and a rotation of -15 deg.
    random_scale = 0.5 + random.random() * 2.0
    # Add a block reference to the block named 'FLAG' at the coordinates 'point'.
    msp.add_blockref('FLAG',
                     point,
                     dxfattribs={
                         'xscale': random_scale,
                         'yscale': random_scale,
                         'rotation': -15
                     })

for flag_ref in msp.query('INSERT[name=="FLAG"]'):
    print(str(flag_ref))
# Save the drawing.
# doc.saveas("output/blockref_tutorial.dxf")

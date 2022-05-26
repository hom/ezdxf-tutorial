import ezdxf

doc = ezdxf.new(setup=True)
msp = doc.modelspace()

msp.add_angular_dim_3p(
    base=(0, 7),  # location of the dimension line
    center=(0, 0),  # center point
    p1=(-3, 5),  # end point of 1st leg = start angle
    p2=(3, 5),  # end point of 2nd leg = end angle
).render()

doc.saveas("output/angle_by_3_points.dxf")


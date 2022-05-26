import ezdxf

doc = ezdxf.new(setup=True)
msp = doc.modelspace()

# Setup the geometric parameters for the DIMENSION entity:
base = (5.8833, -6.3408)  # location of the dimension line
p1 = (2.0101, -7.5156)  # start point of 1st leg
p2 = (2.7865, -11.4133)  # end point of 1st leg
p3 = (6.7054, -7.5156)  # start point of 2nd leg
p4 = (5.9289, -11.4133)  # end point of 2nd leg

# Draw the lines for visualization, not required to create the
# DIMENSION entity:
msp.add_line(p1, p2)
msp.add_line(p3, p4)

# Add an angular DIMENSION defined by two lines, the measurement text is
# placed at the default location above the dimension line:
dim = msp.add_angular_dim_2l(
    base=base,  # defines the location of the dimension line
    line1=(p1, p2),  # start leg of the angle
    line2=(p3, p4),  # end leg of the angle
    dimstyle="EZ_CURVED",  # default angular dimension style
)

# Necessary second step to create the dimension line geometry:
dim.render()
doc.saveas("output/angular_dimension_2l.dxf")

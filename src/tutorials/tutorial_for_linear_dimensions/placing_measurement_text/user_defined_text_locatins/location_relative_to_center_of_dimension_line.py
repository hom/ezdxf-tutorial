import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

dim1 = msp.add_linear_dim(
    base=(3, 2), p1=(3, 0), p2=(6, 0)
)
dim1.set_location(location=(-1, 1), leader=True, relative=True)
dim1.render()

dim2 = msp.add_linear_dim(
    base=(3, 2), p1=(7, 0), p2=(10, 0)
)
dim2.set_location(location=(-1, 2), leader=False, relative=True)
dim2.render()

dim3 = msp.add_linear_dim(
    base=(3, 2), p1=(11, 0), p2=(14, 0)
)
dim3.set_location(location=(-1, 1), leader=True, relative=False)
dim3.render()

doc.saveas('output/location_relative_to_center_of_dimension_line.dxf')

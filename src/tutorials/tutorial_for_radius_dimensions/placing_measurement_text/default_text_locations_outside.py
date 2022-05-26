import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_circle((0, 0), radius=2.5)  # add a CIRCLE entity, not required

dim = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=0,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 0},
)
dim.render()  # always required, but not shown in the following examples

dim1 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=15,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 1},
)
dim1.render()  # always required, but not shown in the following examples

dim2 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 2}
)
dim2.render()  # always required, but not shown in the following examples

dim3 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=45,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 3}
)
dim3.render()  # always required, but not shown in the following examples

dim4 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=60,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 4}
)
dim4.render()  # always required, but not shown in the following examples

# dimtoh
dim5 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-15,
    dimstyle="EZ_RADIUS",
    override={"dimtoh": 1, "dimtad": 0}
)
dim5.render()

dim6 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-30,
    dimstyle="EZ_RADIUS",
    override={"dimtoh": 1, "dimtad": 1}
)
dim6.render()

dim7 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-45,
    dimstyle="EZ_RADIUS",
    override={"dimtoh": 1, "dimtad": 2}
)
dim7.render()

dim8 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-60,
    dimstyle="EZ_RADIUS",
    override={"dimtoh": 1, "dimtad": 3}
)
dim8.render()

dim9 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-75,
    dimstyle="EZ_RADIUS",
    override={"dimtoh": 1, "dimtad": 4}
)
dim9.render()

doc.saveas("output/default_text_locations_outside.dxf")

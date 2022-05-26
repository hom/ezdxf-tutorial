import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_circle((0, 0), radius=2.5)  # add a CIRCLE entity, not required

dim = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=0,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 0},
)
dim.render()  # always required, but not shown in the following examples

dim1 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 1},
)
dim1.render()  # always required, but not shown in the following examples

dim2 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=60,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 2}
)
dim2.render()  # always required, but not shown in the following examples

dim3 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=90,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 3}
)
dim3.render()  # always required, but not shown in the following examples

dim4 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=120,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 4}
)
dim4.render()  # always required, but not shown in the following examples

dim5 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=120,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 4, "dimtih": 1,}
)
dim5.render()  # always required, but not shown in the following examples

# dimtmove
dim6 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 0}
)
dim6.render()

dim7 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-60,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 1}
)
dim7.render()

dim8 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-90,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 2}
)
dim8.render()

dim9 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-120,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 3}
)
dim9.render()

dim10 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-150,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 4}
)
dim10.render()

dim11 = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=-150,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 4, "dimtih": 1,}
)
dim11.render()

doc.saveas("output/default_text_locations_inside.dxf")

import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_line((0, 0), (3, 0))
# 测试属性
msp.add_linear_dim(base=(3, 1), p1=(0, 0), p2=(3, 0), override={"dimjust": 0}).render()
msp.add_linear_dim(base=(3, 2), p1=(0, 0), p2=(3, 0), override={"dimjust": 1}).render()
msp.add_linear_dim(base=(3, 3), p1=(0, 0), p2=(3, 0), override={"dimjust": 2}).render()
msp.add_linear_dim(base=(3, 4), p1=(0, 0), p2=(3, 0), override={"dimjust": 3}).render()
msp.add_linear_dim(base=(3, 5), p1=(0, 0), p2=(3, 0), override={"dimjust": 4}).render()
msp.add_linear_dim(base=(3, 6), p1=(0, 0), p2=(3, 0), text='Custom Text', angle=30, text_rotation=30, override={"dimjust": 0}).render()

msp.add_line((4, 0), (7, 0))
# 测试属性
msp.add_linear_dim(base=(7, 1), p1=(4, 0), p2=(7, 0), override={"dimtad": 0}).render()
msp.add_linear_dim(base=(7, 2), p1=(4, 0), p2=(7, 0), override={"dimtad": 1}).render()
msp.add_linear_dim(base=(7, 3), p1=(4, 0), p2=(7, 0), override={"dimtad": 2}).render()
msp.add_linear_dim(base=(7, 4), p1=(4, 0), p2=(7, 0), override={"dimtad": 3}).render()
msp.add_linear_dim(base=(7, 5), p1=(4, 0), p2=(7, 0), override={"dimtad": 4}).render()
msp.add_linear_dim(base=(7, 6), p1=(4, 0), p2=(7, 0), text='Custom Text', angle=30, text_rotation=30, override={"dimtad": 0}).render()


msp.add_line((8, 0), (12, 0))
# 测试属性
msp.add_linear_dim(base=(12, 1), p1=(8, 0), p2=(12, 0), override={"dimtad": 0, "dimgap": 0}).render()
msp.add_linear_dim(base=(12, 2), p1=(8, 0), p2=(12, 0), override={"dimtad": 1, "dimgap": 1}).render()
msp.add_linear_dim(base=(12, 3), p1=(8, 0), p2=(12, 0), override={"dimtad": 2, "dimgap": 2}).render()
msp.add_linear_dim(base=(12, 4), p1=(8, 0), p2=(12, 0), override={"dimtad": 3, "dimgap": 3}).render()
msp.add_linear_dim(base=(12, 5), p1=(8, 0), p2=(12, 0), override={"dimtad": 4}).render()
msp.add_linear_dim(base=(12, 6), p1=(8, 0), p2=(12, 0), text='Custom Text', angle=-30, text_rotation=-30, override={"dimtad": 0}).render()

msp.add_line((13, 0), (17, 0))
dim = msp.add_linear_dim(base=(17, 1), p1=(13, 0), p2=(17, 0))
dim.set_text_align(halign="center", valign="center")
dim.render()


doc.saveas('output/default_text_locations.dxf')

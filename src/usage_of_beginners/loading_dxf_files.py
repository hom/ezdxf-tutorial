import ezdxf

doc = ezdxf.readfile('../example.dxf')

doc.saveas('../output/saved.dxf')

# Minecraft function generation functions

import blocks

def fill(out, xyz_tuple1, xyz_tuple2, material, blockstate_dict=None):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]
		out.write(str.format('fill {} {} {} {} {} {} {} replace\n', x1, y1, z1, x2, y2, z2, material))
def fill_hollow(out, xyz_tuple1, xyz_tuple2, material):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]
	out.write(str.format('fill {} {} {} {} {} {} {} outline\n', x1, y1, z1, x2, y2, z2, material))

def fill_replace(out, xyz_tuple1, xyz_tuple2, old_material, new_material):
	x1 = xyz_tuple1[0]
	x2 = xyz_tuple2[0]
	y1 = xyz_tuple1[1]
	y2 = xyz_tuple2[1]
	z1 = xyz_tuple1[2]
	z2 = xyz_tuple2[2]
	out.write(str.format('fill {} {} {} {} {} {} {} replace {}\n', x1, y1, z1, x2, y2, z2, new_material, old_material))

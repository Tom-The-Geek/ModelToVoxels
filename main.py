import json
import sys


if len(sys.argv) < 2:
	print("Usage: " + sys.argv[0] + " <INPUT>")
	exit()

INPUT = sys.argv[1]

print("Reading: {}...".format(INPUT))

with open(INPUT) as f:
	data = json.load(f)

cubes = data["elements"]

output = []
output.append("public static VoxelShape SHAPE = VoxelShapes.or(")

for cube in cubes:
	ln = "\tBlock.makeCuboidShape({}, {}, {}, {}, {}, {}),"
	x1, y1, z1 = cube["from"]
	x2, y2, z2 = cube["to"]
	output.append(ln.format(x1, y1, z1, x2, y2, z2))

output.append(");")

result = "\n".join(output)

print("\n" * 4)
print(result)

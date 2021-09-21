from PIL import Image

image = Image.open("427.png")
rgb = image.convert('RGB')

coordinates = []
for x in range(image.size[0]): 
	for y in range(image.size[1]): 
		r, g, b = image.getpixel((x, y))
		if r == 0 and g == 0 and b == 0: 
			coordinates.append((x, y))

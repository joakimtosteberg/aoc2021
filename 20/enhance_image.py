import sys

image = {}
width = 0
height = 0
current_empty_value = '.'

with open(sys.argv[1]) as f:
    enhancement_table = f.readline().strip()
    f.readline()
    y = 0
    for line in f:
        x = 0
        for pixel in line.strip():
            image[(x,y)] = pixel
            x = x + 1
        width = x
        y = y + 1
    height = y

def get_enhancement_index(image, coord, current_empty_value):
    value = 0
    weight = 8
    for y in range(-1,2):
        for x in range(-1,2):
            read_coord = (coord[0]+x,coord[1]+y)
            pixel = image.get(read_coord,current_empty_value)
            value += (0 if pixel=='.' else 1)*(2**weight)
            weight -= 1
    return value


def print_image(image, width, height):
    for y in range(0,width):
        for x in range(0,height):
            print(image[(x,y)],end='')
        print()
    print()

def enhance_image(image, width, height, current_empty_value, enhancement_table):
    new_image = {}
    for y in range(0,width+4):
        for x in range(0,height+4):
            new_image[(x,y)] = enhancement_table[get_enhancement_index(image,(x-2,y-2),current_empty_value)]
    next_empty_value = enhancement_table[get_enhancement_index(image,(-10,-10),current_empty_value)]
    return (new_image,width+4,height+4,next_empty_value)

def count_active(image):
    count = 0
    for pixel in image:
        if image[pixel] == '#':
            count += 1
    return count

#print_image(image, width, height)
for i in range(0,50):
    (image,width,height,current_empty_value) = enhance_image(image, width, height, current_empty_value, enhancement_table)
    if i==1:
        print(count_active(image))
print(count_active(image))
#    print_image(image, width, height)



from PIL import Image


width, height = 1024, 1024
image = Image.new('1', (width, height), 1)
x, y = 512, 512
direction = 0
black_count = 0

while 0 <= x < width and 0 <= y < height:
    pixel_value = image.getpixel((x, y))
    direction_change = 1 if pixel_value == 1 else -1
    image.putpixel((x, y), 1 - pixel_value)
    direction = (direction + direction_change) % 4
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1
    black_count += direction_change

image.save('ant_path.png', 'PNG')
print(f'Количество черных клеток: {black_count}')

import numba as nb
import numpy as np
from PIL import Image

@nb.njit
def simulate(field, ant_x, ant_y, direction):
    height, width = field.shape
    
    while 0 <= ant_x < width and 0 <= ant_y < height:
        
        current_value = field[ant_y, ant_x]
        
        if current_value == 1:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
            
        field[ant_y, ant_x] = 1 - current_value
        
        if direction == 0:
            ant_y += 1  # Перемещение вниз
        elif direction == 1:
            ant_x += 1  # Перемещение вправо
        elif direction == 2:
            ant_y -= 1  # Перемещение вверх
        elif direction == 3:
            ant_x -= 1  # Перемещение влево

    return field

# Инициализация 
width, height = 1024, 1024
field = np.ones((width, height), np.uint8)
ant_x, ant_y = 512, 512 
direction = 0

# Симуляция
field = simulate(field, ant_x, ant_y, direction)

# Подсчет черных клеток
black_cells = np.count_nonzero(field == 0)

# Сохранение результата
img = Image.fromarray(field * 255)
img.save("ant_field.png")

print(f"Черных клеток: {black_cells}")

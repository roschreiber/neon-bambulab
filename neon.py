import time
import board
import displayio
import os
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

# Initialize Display
displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=4,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1
)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# Load a small bitmap font
font = bitmap_font.load_font("font5x8.bdf")  # Ensure you have this font file

# Load home icon
home_icon = displayio.OnDiskBitmap("gifs/home_icon.bmp")

# Create display group
splash = displayio.Group()
display.root_group = splash

def update_display(status, bed_temp, nozzle_temp):
    # Clear previous text
    while len(splash) > 0:
        splash.pop()
    
    # Add home icon
    home_tilegrid = displayio.TileGrid(home_icon, pixel_shader=home_icon.pixel_shader, x=40, y=0)
    splash.append(home_tilegrid)
    
    # Use bitmap font for text
    status_text = label.Label(
        font,
        text=f"S:{status}",
        color=0xFFFFFF,
        x=2,
        y=8
    )
    splash.append(status_text)
    
    temp_text = label.Label(
        font,
        text=f"B{bed_temp}",
        color=0xFF0000,
        x=2,
        y=24
    )
    splash.append(temp_text)
    
    nozzle_text = label.Label(
        font,
        text=f"N{nozzle_temp}",
        color=0x00FF00,
        x=34,
        y=24
    )
    splash.append(nozzle_text)
    
    nozzle_text = label.Label(
        font,
        text=f"N{nozzle_temp}",  # Use placeholder text
        color=0x00FF00,
        x=34,
        y=24
    )
    splash.append(nozzle_text)

if __name__ == '__main__':
    print('Starting Display Monitor')

    try:
        while True:
            # Use placeholder values
            status = "OK"
            bed_temp = 60
            nozzle_temp = 200
            
            update_display(status, bed_temp, nozzle_temp)
            display.refresh()
            
            print(f'Status: {status}, Bed: {bed_temp}, Nozzle: {nozzle_temp}')
            
            time.sleep(5)
    
    finally:
        print('Stopping Display Monitor')
# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon,draw_horizontal_gradient, draw_vertical_gradient, draw_text, finish_drawing




def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    #draw_rectangle(canvas, 0, scene_height / 3,scene_width, scene_height, width=0, fill="sky blue")
    draw_vertical_gradient(canvas,0,int(scene_height*.25),[229,107,26],scene_width,int(scene_height/1),[25,25,75])

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    #draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="tan4")
    draw_vertical_gradient(canvas,0,int(scene_height*0),[84,56,34],scene_width,int(scene_height*.33),[128,64,0])
    
def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height * .2
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

def main():
    scene_width = 1920
    scene_height = 1080
    
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    for i in range(50,scene_width,(random.randint(50,125))):
        print(i,random.randint(50,150))
        draw_pine_tree(canvas,i,random.randint(int(scene_width*.01),int(scene_width*.025)),random.randint(int(scene_height*.05),int(scene_height*.1)))


    # Call the finish_drawing function
    # in the draw2d.py library.
    draw_grid(canvas,scene_width,scene_height,50,color="black")
    finish_drawing(canvas)
    
# Call the main function so that
# this program will start executing.
main()
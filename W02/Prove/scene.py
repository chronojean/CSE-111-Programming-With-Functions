#user defined functions: draw sky, draw sun, draw ground, Draw tree, draw cloud
#called multiple times with random values: clouds, trees
#functions have default params, every run of this program is different from the previous one
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon,draw_horizontal_gradient, draw_vertical_gradient, draw_text, finish_drawing, draw_circle_with_vert_grad

def draw_sky(canvas, scene_width,scene_height,sky_ground_ratio=.5,start_color= [229,107,26],end_color=[25,25,75]):
    """Draw the sky and all the objects in the sky."""
    #draw_rectangle(canvas, 0, scene_height / 3,scene_width, scene_height, width=0, fill="sky blue")
    draw_vertical_gradient(canvas,0,int(scene_height*sky_ground_ratio),start_color,scene_width,scene_height,end_color)
    
def draw_sun(canvas,scene_width, scene_height,sky_ground_ratio):
    draw_circle_with_vert_grad(canvas,scene_width/2,int(scene_height*sky_ground_ratio-45),150,[255,180,90],[125,125,0])
    
def draw_cloud(canvas,scene_width,scene_height,start_screen_ratio_y=.33,end_screen_ratio_y = .7):
    start_x = random.randint(-100,scene_width+100)
    start_y = random.randint(int(scene_height*start_screen_ratio_y),int(scene_height*end_screen_ratio_y))
    for i in range(random.randint(2,5)):
        #Center
        draw_circle_with_vert_grad(canvas,start_x+i*40,start_y,35,[255,255,255],[255,125,0])
        draw_circle_with_vert_grad(canvas,start_x+i*40,start_y+15,35,[255,255,255],[255,125,0])
        draw_circle_with_vert_grad(canvas,start_x+i*40,start_y+30,35,[255,255,255],[255,255,255])
        draw_circle_with_vert_grad(canvas,start_x+i*40,start_y+45,35,[255,255,255],[255,255,255])

        #Left Border
        draw_circle_with_vert_grad(canvas,start_x+i*40-35,start_y+15,35,[255,255,255],[255,125,0])
        draw_circle_with_vert_grad(canvas,start_x+i*40-35,start_y+30,35,[255,255,255],[255,255,255])
        #Right Border
        draw_circle_with_vert_grad(canvas,start_x+i*40+35,start_y+15,35,[255,255,255],[255,125,0])
        draw_circle_with_vert_grad(canvas,start_x+i*40+35,start_y+30,35,[255,255,255],[255,255,255])
    
def draw_ground(canvas, start_x, start_y, end_x, end_y,screen_ratio_x = 1, screen_ratio_y = 1,start_color= [84,56,34],end_color=[128,64,0]):
    """Draw the ground and all the objects on the ground."""
    draw_vertical_gradient(canvas,start_x,start_y,start_color,int(end_x*screen_ratio_x),int(end_y*screen_ratio_y),end_color)
    
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

def main():
    scene_width = 1920
    scene_height = 1080
    sky_ground_ratio = .33
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas,scene_width,scene_height,sky_ground_ratio)
    draw_sun(canvas,scene_width,scene_height,sky_ground_ratio)
    for j in range(-50,scene_width+random.randint(50,75),random.randint(5,15)):
            #print(j,random.randint(50,150))
            #draw_pine_tree(canvas,j,random.randint(int(scene_width*.01),int(scene_width*.025)+scene_height),random.randint(int(scene_height*.05),int(scene_height*.1)))
            draw_pine_tree(canvas,j,int(scene_height*sky_ground_ratio-random.randint(15,35)),random.randint(30,75))
    draw_ground(canvas, 0, 0, scene_width,scene_height, screen_ratio_y=sky_ground_ratio)
    
    for i in range(5,25):
        draw_cloud(canvas,scene_width,scene_height,sky_ground_ratio+.1,end_screen_ratio_y=1)
    for count,i in enumerate(range(int(scene_height*sky_ground_ratio),-50,-40)):
        for j in range(-50,scene_width+random.randint(50,75),random.randint(20,35)):
            #print(j,random.randint(50,150))
            #draw_pine_tree(canvas,j,random.randint(int(scene_width*.01),int(scene_width*.025)+scene_height),random.randint(int(scene_height*.05),int(scene_height*.1)))
            draw_pine_tree(canvas,j,i-random.randint(15,35),random.randint(30+count*5,75+count*15))
        print(count)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)
# Call the main function so that
# this program will start executing.
main()
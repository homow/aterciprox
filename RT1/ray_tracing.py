import taichi as ti
import ray_tracing_models

ti.init(arch=ti.cuda)

# image
aspect_ratio = 18/9
image_width = 512
image_height = image_width * aspect_ratio
pixels = ti.Vector.field(3, ti.f32, shape=(image_width, image_height))
# camera
viewport_height = 2
viewport


@ti.kernel
def render(t: ti.f32):
    for i, j in pixels:
        color = ti.Vector([i/image_width, j/image_height, (ti.sin(t)+1)/2])
        pixels[i, j] = color


t = 0
gui = ti.GUI('Hello World!', (image_width, image_height))
while gui.running:
    t += 0.001
    render(t)
    gui.set_image(pixels)
    gui.show()

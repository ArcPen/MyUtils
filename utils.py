# Here's a list of files that might come in handy.


__all__ = [
    "display_image_list",
]


### IMAGE ###

## Generate a list of images ##

from matplotlib import pyplot as plt
def display_image_list(image_list, name_list=None, save_path=None, comment=None):
    '''Display a list of images'''
    if name_list is None:
        name_list = [f'Image {i+1}' for i in range(len(image_list))]
    else:
        if len(name_list) != len(image_list):
            # add default names
            name_list += [f'Image {i+1}' for i in range(len(image_list) - len(name_list))]

    fig, axs = plt.subplots(len(image_list), 1)#, figsize=(15, 10))
    for i, img in enumerate(image_list):
        axs[i].imshow(img, cmap='gray')
        axs[i].set_title(name_list[i])
        axs[i].axis('off')

    if comment: # Add comment
        plt.suptitle(comment)
        
    # plt.tight_layout() # Use this to adjust layout

    if not save_path:
        plt.show()
    else:
        plt.savefig(save_path)
    plt.close()

# another fancy way
def display_image_matrix(image_list, ncols=3, title=None, save_path=None):
    '''Display a list of images. With full resolution.
    args:
        image_list: 1D list of np arrays
    '''
    ncols = 4
    while not len(image_list) % ncols == 0:
        image_list.append(np.zeros_like(image_list[0]))
    stack_list = [np.hstack(image_list[i:i+ncols]) for i in range(0, len(image_list), ncols)]
    vis = np.vstack(stack_list)

    if title:
        cv2.putText(vis, img_path.name, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if not save_path:
        display(PILImage.fromarray(vis))
    else:
        cv2.imsave(save_path, vis)
        
## Generate color palette ##

from matplotlib import pyplot as plt

def RGB_to_Hex(rgb):
    """
    RGB格式颜色转换为16进制颜色格式
    Args:
        rgb: tuple

    Returns:
        color: str
    """
    RGB = list(rgb)
    color = '#'
    for i in RGB:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color
    
def generate_colors(N=12,colormap='hsv'):
    """
    生成颜色列表
    Args:
        N: 生成颜色列表中的颜色个数
        colormap: plt中的色表 (https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)

    Returns:
        rgb_list: list, 每个值(r,g,b)在0~255范围
        hex_list: list, 每个值为十六进制颜色码类似：#FAEBD7
    """
    step = max(int(255/N),1)
    cmap = plt.get_cmap(colormap)
    rgb_list = []
    hex_list = []
    for i in range(N):
        id = step*i # cmap(int)->(r,g,b,a) in 0~1
        id = 255 if id>255 else id
        rgba_color = cmap(id)
        rgb = [int(d*255) for d in rgba_color[:3]]
        rgb_list.append(tuple(rgb))
        hex_list.append(RGB_to_Hex(rgb))
    return rgb_list,hex_list
    
# 生成 6个冷色调的颜色
rgb_list,hex_list = generate_colors(6,'cool')
print(rgb_list)
print(hex_list)


# Here's a list of files that might come in handy.


__all__ = [
    "display_image_list",
]


### IMAGE ###
from matplotlib import pyplot as plt

def display_image_list(imgage_list, name_list=None, save_path=None, comment=None):
    '''Display a list of images'''
    if name_list is None:
        name_list = [f'Image {i+1}' for i in range(len(imgage_list))]
    else:
        if len(name_list) != len(imgage_list):
            # add default names
            name_list += [f'Image {i+1}' for i in range(len(imgage_list) - len(name_list))]

    fig, axs = plt.subplots(len(imgage_list), 1)#, figsize=(15, 10))
    for i, img in enumerate(imgage_list):
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

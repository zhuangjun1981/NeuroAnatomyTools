import numpy as np
import cv2


def resize_z_cv2(img, new_z, **kwargs):
    """
    use open cv to rescale the z dimension of an input
    3d array. Most useful to convert a volume to isotropic.

    :param img: 3d array, shape = (x, y, z)
    :param new_z: int, number of z planes in output image
    :param kwargs: inputs to cv2.resize function
                   interpolation = cv2.INTER_AREA
                                   cv2.INTER_CUBIC
                                   cv2.INTER_LINEAR
                                   cv2.INTER_NEAREST
    :return: 3d array
    """

    if len(img.shape) != 3:
        raise ValueError('input image file should be 3d.')

    x, y, z = img.shape

    img2 = np.empty((x, y, new_z), dtype=img.dtype)
    for xi in range(img.shape[0]):
        img2[xi, :, :] = cv2.resize(
            src=img[xi, :, :],
            dsize=(y, new_z),
            **kwargs)

    return img2.astype(img.dtype)


def equalize_hist_z_cv2(img):
    """
    use open cv to equalize histogram of each z plane
    input should be np.uint8

    :param img: 3d array, shape = (x, y, z)
    :return: 3d array
    """

    if len(img.shape) != 3:
        raise ValueError('input image file should be 3d.')

    img2 = np.empty(img.shape, dtype=img.dtype)

    for zi in range(img.shape[2]):
        img2[:, :, zi] = cv2.equalizeHist(img[:, :, zi])

    return img2

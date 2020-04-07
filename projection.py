import argparse
import os

import numpy as np
import scipy.misc as ssc
import imageio
#import kitti_util
import matplotlib.pyplot as plt
from coordinate_conversion import Trans
#from pypcd import pypcd



def generate_dispariy_from_velo(pc_velo,labels, height, width):
    a =Trans()
    pts_2d = a.project_lidar_to_image(pc_velo)
    fov_inds = (pts_2d[:, 0] < width - 1) & (pts_2d[:, 0] >= 0) & \
               (pts_2d[:, 1] < height - 1) & (pts_2d[:, 1] >= 0)
    fov_inds = fov_inds & (pc_velo[:, 0] > 2)
    imgfov_pc_velo = pc_velo[fov_inds, :]
    imgfov_pts_2d = pts_2d[fov_inds, :]



    #imgfov_pc_rect = calib.project_velo_to_rect(imgfov_pc_velo) # segmented pointcloud in image
    depth_map = np.zeros((height, width)) - 1
    gt_depth_map =np.zeros((height, width)) - 1
    imgfov_pts_2d = np.round(imgfov_pts_2d).astype(int) # segmented position in image.(pixel)
    road_point = []
    road_pos = []

    '''
    for i in range(imgfov_pts_2d.shape[0]):
        depth = imgfov_pc_rect[i, 2]
        depth_map[int(imgfov_pts_2d[i, 1]), int(imgfov_pts_2d[i, 0])] = depth
        if labels[int(imgfov_pts_2d[i,1]),int(imgfov_pts_2d[i, 0])] == 255 :
            gt_depth_map[int(imgfov_pts_2d[i, 1]), int(imgfov_pts_2d[i, 0])] = depth
            road_point.append(imgfov_pc_velo[i,:])
            road_pos.append(imgfov_pts_2d[i,:])

    road_point = np.array(road_point)
    road_pos = np.array(road_pos)


    np.save('/mrtstorage/users/chli/pseudo_lidar/seg_points/gt_umm_05', road_point)
    np.save('/mrtstorage/users/chli/pseudo_lidar/seg_points/gt_pos_umm_05', road_pos)

    baseline = 0.54

    disp_map = (calib.f_u * baseline) / depth_map
    gt_disp_map = (calib.f_u * baseline) / gt_depth_map
    #im2 = plt.imshow(gt_disp_map)
    #plt.show()

    print(calib.f_u)
    return disp_map, gt_disp_map

    '''

if __name__ == '__main__':
    ## the path of code

    lidar_dir = "/mrtstorage/users/chli/real_data/"
    image_dir = "/mrtstorage/users/chli/real_data/crop_image2/"
    gt_image_dir = "/mrtstorage/users/chli/real_data/gt_image2/"
    fn ="1571220343.044698000"

    # load point cloud
    #lidar = np.fromfile(lidar_dir+"1_seg.txt")
    lidar = np.loadtxt(lidar_dir+"1_seg.txt")

    gt_image = imageio.imread(gt_image_dir+fn+".png")

    #could = pypcd.PointCloud.from_path(lidar_dir+"1571220343.060393000.pcd")


    gt_labels = gt_image
    height, width = gt_image.shape
    generate_dispariy_from_velo(lidar, gt_labels, height, width)
    #print(disp.shape)

    #im2 = plt.imshow(disp, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear')

    #plt.show()
    #im2 = plt.imshow(gt_disp, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear')
    #plt.show()

    #np.save(disparity_dir + '/' + predix, gt_disp)
    #np.save(gt_disparity_dir + '/' + predix, gt_disp)
    #print('Finish Disparity {}'.format(predix))



import numpy as np
import imageio
from coordinate_conversion import Trans




def generate_disparity_from_velo(pc_velo,labels, height, width):
    a =Trans()
    pts_2d = a.project_lidar_to_image(pc_velo)
    pc_velo2 = a.project_lidar_to_vehicle(pc_velo)
    #pts_2d_2 = a.project_lidar_to_image2(pc_velo)
    #fov_inds = (pts_2d[:, 0] < 3000 - 1) & (pts_2d[:, 0] >= 1000) & \
               #(pts_2d[:, 1] < 1500 - 1) & (pts_2d[:, 1] >= 900)
    fov_inds = (pts_2d[:, 0] < 3000 - 1) & (pts_2d[:, 0] >= 1000) & \
               (pts_2d[:, 1] < 2400 - 1) & (pts_2d[:, 1] >= 900)
    fov_inds = fov_inds & (pc_velo[:, 0] > 0)& (pc_velo[:, 0] < 30)
    imgfov_pc_velo = pc_velo[fov_inds, :]    # points in image
    imgfov_pc_velo2 = pc_velo2[fov_inds, :]

    imgfov_pts_2d = pts_2d[fov_inds, :]
    x2 = imgfov_pc_velo[:,0]

    np.savetxt("/mrtstorage/users/chli/real_data/test_data3/lidar_new.txt", imgfov_pc_velo)


    imgfov_pts_2d = np.round(imgfov_pts_2d).astype(int) # segmented position in image.(pixel)
    road_point = []
    road_pos = []
    road_point2 = []

    print("i max = ",imgfov_pts_2d.shape[0])
    for i in range(imgfov_pts_2d.shape[0]):
        if int(imgfov_pts_2d[i,1])<1500:
            if labels[int(imgfov_pts_2d[i,1]-900),int(imgfov_pts_2d[i, 0]-1000)] == 0 :
                road_point.append(imgfov_pc_velo[i,:])
                road_point2.append(imgfov_pc_velo2[i, :3])
                road_pos.append(imgfov_pts_2d[i,:])
        else:
            if labels[589,int(imgfov_pts_2d[i, 0]-1000)] == 0 :
                road_point.append(imgfov_pc_velo[i,:])
                road_point2.append(imgfov_pc_velo2[i,:3])
                road_pos.append(imgfov_pts_2d[i,:])

    road_point = np.array(road_point)
    x = road_point[:,0]
    road_pos = np.array(road_pos)
    x1 = road_pos[:,1]
    road_point2 = np.array(road_point2)
    
    np.savetxt('/mrtstorage/users/chli/real_data/test_data3/0356_3_road_new.txt', road_point)
    np.savetxt('/mrtstorage/users/chli/real_data/test_data3/0356_3_road_new2.txt', road_point2)
    #np.savetxt('/mrtstorage/users/chli/real_data/test_data/pos_new.txt', road_pos)

    baseline = 0.54


    #im2 = plt.imshow(gt_disp_map)
    #plt.show()






if __name__ == '__main__':
    ## the path of code

    lidar_dir = "/mrtstorage/users/chli/real_data/"
    image_dir = "/mrtstorage/users/chli/real_data/crop_image2/"
    gt_image_dir = "/mrtstorage/users/chli/real_data/gt_image2/"
    fn ="1571220343.044698000"

    # load point cloud
    #lidar = np.fromfile(lidar_dir+"1_seg.txt")
    lidar = np.loadtxt("/mrtstorage/users/chli/real_data/test_data3/1571220356.36.txt")

    gt_image = imageio.imread("/mrtstorage/users/chli/real_data/gt_image2/1571220356.344702959.png")

    #could = pypcd.PointCloud.from_path(lidar_dir+"1571220343.060393000.pcd")


    gt_labels = gt_image
    height, width = gt_image.shape
    generate_disparity_from_velo(lidar, gt_labels, height, width)
    #print(disp.shape)

    #im2 = plt.imshow(disp, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear')

    #plt.show()
    #im2 = plt.imshow(gt_disp, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear')
    #plt.show()

    #np.save(disparity_dir + '/' + predix, gt_disp)
    #np.save(gt_disparity_dir + '/' + predix, gt_disp)
    #print('Finish Disparity {}'.format(predix))

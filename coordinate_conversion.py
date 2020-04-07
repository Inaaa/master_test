import numpy as np
from autolab_core import RigidTransform
class Trans():
    def __init__(self):

        self.P = [1700.0, 0.0, 2047.0, -0.0, 0.0, 1700.0, 1015.0, -0.0, 0.0, 0.0, 1.0, 0.0 ]
        self.P = np.reshape(self.P, [3, 4])
        self.R0 = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.R0 = np.reshape(self.R0, [3, 3])






    def trans_matrix(self,rotation_quaternion,trans, points=[1,1,1]):
        T_qua2rota = RigidTransform(rotation_quaternion, points)
        rot = T_qua2rota.rotation
        trans_matrix = np.vstack(((np.hstack((rot, trans))), [0, 0, 0, 1]))
        return trans_matrix
    def lidarfl_to_vehicle(self):
        orientation = {'y': -0.000730548134847, 'x': -0.000366438796854, 'z': 0.0407824679138, 'w': 0.999167712926}
        rotation_quaternion = np.asarray([orientation['w'], orientation['x'], orientation['y'], orientation['z']])
        trans = [[1.46054280291], [0.557635077922], [1.49213371609]]

        lidarfl_to_vehicle = self.trans_matrix(rotation_quaternion, trans)
        return lidarfl_to_vehicle

    def camera_to_vehicle(self):
        rotation_quaternion =[0.510227778268, -0.479599719025, 0.484929413309, -0.523922876681]
        trans =[[1.82781872652],[0.317004405987],[1.24662527497]]
        camera_to_vehicle = self.trans_matrix(rotation_quaternion, trans)
        return camera_to_vehicle

    def lidarfl_to_camera(self):
        return np.dot(self.lidarfl_to_vehicle(), np.linalg.inv(self.camera_to_vehicle()))

    def cart2hom(self, pts_3d):
        ''' Input: nx3 points in Cartesian
            Oupput: nx4 points in Homogeneous by pending 1
        '''
        n = pts_3d.shape[0]
        pts_3d_hom = np.hstack((pts_3d, np.ones((n, 1))))
        return pts_3d_hom

    def project_lidar_to_camera(self,pc_velo):
        pts_3d_velo = self.cart2hom(pc_velo)  # nx4
        matrix =self.lidarfl_to_camera()
        return np.dot(pts_3d_velo, np.transpose(matrix))

    def project_lidar_to_image(self,pc_velo):
        pts_3d_ref = self.project_lidar_to_camera(pc_velo)
        pts_3d_ref = pts_3d_ref[:,0:3]
        pts_3d_rect = np.transpose(np.dot(self.R0, np.transpose(pts_3d_ref)))
        pts_3d = pts_3d_rect

        n = pts_3d.shape[0]
        pts_3d_hom = np.hstack((pts_3d, np.ones((n, 1))))

        pts_3d_rect = pts_3d_hom

        print("self.p = \n", self.P)

        pts_2d = np.dot(pts_3d_rect, np.transpose(self.P))  # nx3
        pts_2d[:, 0] /= pts_2d[:, 2]
        pts_2d[:, 1] /= pts_2d[:, 2]
        result = pts_2d[:, 0:2]
        return result




a =Trans()
print(a.lidarfl_to_camera())




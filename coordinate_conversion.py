import numpy as np
from autolab_core import RigidTransform
class Trans():

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

    def project_lidar_to_image(self,pc_velo):
        return self.lidarfl_to_camera()*pc_velo

a =Trans()
print(a.lidarfl_to_camera())




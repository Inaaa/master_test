import numpy as np
pts_3d = lidar
n = pts_3d.shape[0]
pts_3d_hom = np.hstack((pts_3d, np.ones((n, 1))))
pts_3d_velo = pts_3d_hom
pts_3d_ref = np.dot(pts_3d_velo, np.transpose(self.V2C))   # velo to ref
pts_3d_rect = np.transpose(np.dot(self.R0, np.transpose(pts_3d_ref)))   # ref to rect

pts_3d = pts_3d_rect

n = pts_3d.shape[0]
pts_3d_hom = np.hstack((pts_3d, np.ones((n, 1))))

pts_3d_rect=pts_3d_hom

pts_2d = np.dot(pts_3d_rect, np.transpose(self.P))  # nx3
pts_2d[:, 0] /= pts_2d[:, 2]
pts_2d[:, 1] /= pts_2d[:, 2]
result = pts_2d[:, 0:2]
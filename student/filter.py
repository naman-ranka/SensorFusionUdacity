# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dt = params.dt
        F = np.identity(params.dim_state)
        F[0,3] = dt
        F[1,4] = dt
        F[2,5] = dt
        return F
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        var1 = 1/3*(params.dt**3)*params.sigma_p44
        var2 = 1/2*(params.dt**2)*params.sigma_p44

        var3 = 1/3*(params.dt**3)*params.sigma_p55
        var4 = 1/2*(params.dt**2)*params.sigma_p55

        var5 = 1/3*(params.dt**3)*params.sigma_p66
        var6 = 1/2*(params.dt**2)*params.sigma_p66

        var7 = 1/2*(params.dt**2)*params.sigma_p44
        var8 = params.dt*params.sigma_p44

        var9 = 1/2*(params.dt**2)*params.sigma_p55
        var10 = params.dt*params.sigma_p55

        var11 = 1/2*(params.dt**2)*params.sigma_p66
        var12 = params.dt*params.sigma_p66

        Q = np.matrix([[var1,0,0,var2,0,0],
                    [0,var3,0,0,var4,0],
                    [0,0,var5,0,0,var6],
                    [var7,0,0,var8,0,0],
                    [0,var9,0,0,var10,0],
                    [0,0,var11,0,0,var12]])
      
        return Q
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        F = self.F()
        Q = self.Q()
        x_pred = F*track.x 
        P_pred = F*track.P*F.transpose() + Q
        track.set_x(x_pred)
        track.set_P(P_pred)
        pass
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        H = meas.sensor.get_H(track.x)
        gamma = self.gamma(track,meas)
        
        S = self.S(track,meas,H)

        K = track.P * H.transpose() *np.linalg.inv(S)
        x_update = track.x + K*gamma
        I = np.identity(params.dim_state)
        P_update = (I - K*H) + track.P
        
        track.set_x(x_update)
        track.set_P(P_update)
        
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        H = meas.sensor.get_H(track.x)
        return meas.z - H*track.x
              
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        return H * track.P * H.transpose() + meas.R
        
        ############
        # END student code
        ############ 
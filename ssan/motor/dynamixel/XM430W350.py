from numpy import interp

from robotis_def import COMM_SUCCESS
from port_handler import PortHandler
from packet_handler import PacketHandler
from numpy import interp

class XM430W350:
    '''
    XM430-W350 reference - http://emanual.robotis.com/docs/kr/dxl/x/xm430-w350/
    '''

    # define motor control address
    ADDR_PRO_TORQUE_ENABLE      = 64
    ADDR_PROFILE_ACCELERATION   = 108
    ADDR_PROFILE_VELOCITY       = 112
    ADDR_PRO_GOAL_POSITION      = 116
    ADDR_PRO_PRESENT_POSITION   = 132

    # Protocol version
    PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel

    # const setting value
    TORQUE_ENABLE               = 1                 # Value for enabling the torque
    TORQUE_DISABLE              = 0                 # Value for disabling the torque

    DXL_MOVING_STATUS_THRESHOLD = 20

    MINMUM_MOTOR_POSITION       = 0
    MAX_MOTOR_POSITION          = 4095

    MIN_ANGLE                   = 0
    MAX_ANGLE                   = 359

    def __init__(self, device_path = None, baud_rate = 57600):
        self.device_path = device_path
        self.baud_rate = baud_rate
        self.portHandler = PortHandler(self.device_path, baudrate = self.baud_rate)
        self.portHandler.openPort()
        self.packetHandler = PacketHandler(XM430W350.PROTOCOL_VERSION)

    def connectionTest(self, motor_id = 1):
        '''
        @deprecated:
        to check motor device path is valid and motor connection is vaild
        '''
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PRO_TORQUE_ENABLE, XM430W350.TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "connectionTest Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "connectionTest Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)

    def connection_test(self, motor_id = 1):
        '''
        to check motor device path is valid and motor connection is vaild
        '''
        self.connectionTest(motor_id)

    def setToqueEnable(self, motor_id = 1, torqueEnable = True):
        '''
        @deprecated:
        motor의 토크를 활성화 한다
        '''
        torqueState = int(torqueEnable)
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PRO_TORQUE_ENABLE, torqueState)
        error_msg = None
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "setToqueEnable Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "setToqueEnable Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)

    def set_toque_enable(self, motor_id = 1, torqueEnable = True):
        '''
        motor의 토크를 활성화 한다
        '''
        self.setToqueEnable(motor_id, torqueEnable)

    def setProfileVelocity(self, motor_id = 1, profileVelocity = 50):
        '''
        @deprecated:
        0 is unlimited
        value range 0 ~ 32767
        max value 32767
        '''
        if profileVelocity < 0:
            profileVelocity = 0

        if profileVelocity > 32767:
            profileVelocity = 32767

        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PROFILE_VELOCITY, profileVelocity)
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "setProfileVelocity Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "setProfileVelocity Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)

    def set_profile_velocity(self, motor_id = 1, profile_velocity = 50):
        '''
        0 is unlimited
        value range 0 ~ 32767
        max value 32767
        '''
        self.setProfileVelocity(motor_id, profile_velocity)

    def setProfileAcceleration(self, motor_id = 1, profileAcceleration = 50):
        '''
        @deprecated:
        0 is unlimited
        value range 0 ~ 32767
        max value 32767
        '''
        if profileAcceleration < -1:
            profileAcceleration = 0

        if profileAcceleration > 32767:
            profileAcceleration = 32767

        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PROFILE_ACCELERATION, profileAcceleration)
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "setProfileVelocity Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "setProfileVelocity Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)

    def set_profile_acceleration(self, motor_id = 1, profile_acceleration = 50):
        '''
        0 is unlimited
        value range 0 ~ 32767
        max value 32767
        '''
        self.setProfileAcceleration(motor_id, profile_acceleration)

    def setMotorAngle(self, motor_id = 1, angle = 0, angleReverse = False):
        '''
        @deprecated:
        set motor angle range -180 ~ 179
        angleReverse is rotate direction
        '''
        if angleReverse:
            angle = angle * -1

        if angle < -180:
            angle = -180
        if angle > 179:
            angle = 179

        transformAngle = angle + 180
        robotisAngle = int(interp(transformAngle, [XM430W350.MIN_ANGLE, XM430W350.MAX_ANGLE], [XM430W350.MINMUM_MOTOR_POSITION, XM430W350.MAX_MOTOR_POSITION]))
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PRO_GOAL_POSITION, robotisAngle)
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "setMotorAngle Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "setMotorAngle Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)

        while True:
            # Read present position
            dxl_present_position, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PRO_PRESENT_POSITION)
            if dxl_comm_result != COMM_SUCCESS:
                error_msg = "while moving motor, error occured - {0}, device_path : {1}, and motor id : {2}, input angle : {3}, robotis angle : {4}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id, angle, robotisAngle)
                raise Exception(error_msg)
            elif dxl_error != 0:
                error_msg = "while moving motor, error occured - {0}, device_path : {1}, and motor id : {2}, input angle : {3}, robotis angle : {4}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id, angle, robotisAngle)
                raise Exception(error_msg)
            # waiting for reach robotisAngle
            if not abs(robotisAngle - dxl_present_position) > XM430W350.DXL_MOVING_STATUS_THRESHOLD:
                break
    def set_motor_angle(self, motor_id = 1, angle = 0, angle_reverse = False):
        '''
        set motor angle range -180 ~ 179
        angle_reverse is rotate direction
        '''
        self.setMotorAngle(motor_id, angle, angle_reverse)

    def getPresentMotorAngle(self, motor_id = 1, angleReverse = False):
        '''
        @deprecated:
        get motor angle
        return value rangle -180 ~ 179
        angleReverse is rotate direction
        '''
        dxl_present_position, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, motor_id, XM430W350.ADDR_PRO_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            error_msg = "getPresentMotorAngle Error - {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getTxRxResult(dxl_comm_result),self.device_path, motor_id)
            raise Exception(error_msg)
        elif dxl_error != 0:
            error_msg = "getPresentMotorAngle Error- {0}, device_path : {1}, and motor id : {2}".format(self.packetHandler.getRxPacketError(dxl_error),self.device_path, motor_id)
            raise Exception(error_msg)
        angle = int(interp(dxl_present_position, [XM430W350.MINMUM_MOTOR_POSITION, XM430W350.MAX_MOTOR_POSITION], [XM430W350.MIN_ANGLE, XM430W350.MAX_ANGLE]))
        angle = angle - 180

        if angleReverse:
            angle = angle * -1
        return angle

    def get_present_motor_angle(self, motor_id = 1, angle_reverse = False):
        '''
        get motor angle
        return value rangle -180 ~ 179
        angle_reverse is rotate direction
        '''
        return self.getPresentMotorAngle(motor_id, angle_reverse)


#example
if __name__ == "__main__":
    motor = XM430W350('/dev/ttyUSB0', 57600)
    motor.connectionTest(motor_id = 1) # recommend !!!
    motor.setToqueEnable(motor_id = 1, torqueEnable = True) # necessary!!!
    motor.setToqueEnable(motor_id = 2, torqueEnable = True) # necessary!!!

    motor.setProfileAcceleration(motor_id = 1, profileAcceleration = 50)
    motor.setProfileVelocity(motor_id = 1, profileVelocity = 50)

    motor.setProfileAcceleration(motor_id = 2, profileAcceleration = 50)
    motor.setProfileVelocity(motor_id = 2, profileVelocity = 50)

    motor.setMotorAngle(2, 0)
    print(motor.getPresentMotorAngle(2))
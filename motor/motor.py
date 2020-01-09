import XM430W350


class Motor:
    def __init__(self, port, vel=20, acc=20, logger=None):
        self.logger = logger.getChild(type(self).__name__)
        self.logger.info("모터 세팅 시작")
        self.__pos = [0, 0]
        self.__vel = [0, 0]
        self.__acc = [0, 0]
        self.__dir = [False, True]
        self.__motor = XM430W350(port)

        self.__motor.connection_test(motor_id=1)

        self.vel = (vel, vel)
        self.acc = (acc, acc)
        self.__pos = [self.__motor.get_present_motor_angle(motor_id=1, angle_reverse=not self.__dir[0])]

        self.logger.info("모터 세팅 완료")

    @property
    def pos(self):
        return self.horz

    @pos.setter
    def pos(self, val):
        self.logger.info("모터 각도 : %3.0f" % val)
        self.__pos[:] = val[:]
        self.__motor.set_motor_angle(motor_id=1, angle=val[0], angle_reverse=not self.__dir[0])

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, val):
        self.logger.info("모터 속도 : %3.0f" % val)
        for i, v in enumerate(val):
            self.__vel[i] = v
            self.__motor.set_profile_velocity(motor_id=i + 1, profile_velocity=v)

    @property
    def acc(self):
        return self.__acc

    @acc.setter
    def acc(self, val):
        self.logger.info("모터 가속도 : %3.0f" % val)
        for i, v in enumerate(val):
            self.__acc[i] = v
            self.__motor.set_profile_acceleration(motor_id=i + 1, profile_acceleration=v)

    @property
    def horz(self):
        return self.__pos[0]

    @horz.setter
    def horz(self, val):
        self.logger.info("모터 각도 수평 : %3.0f" % val)
        self.__pos[0] = val
        self.__motor.set_motor_angle(motor_id=1, angle=val, angle_reverse=not self.__dir[0])

    @property
    def vert(self):
        return self.__pos[1]

    @vert.setter
    def vert(self, val):
        self.logger.info("모터 각도 수직 : %3.0f" % val)
        self.__pos[1] = val
        self.__motor.set_motor_angle(motor_id=2, angle=val, angle_reverse=not self.__dir[1])

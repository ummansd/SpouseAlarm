from abc import *
from common import *
from plyer import notification

class Detector:
    __metaclass__ = ABCMeta

    @abstractmethod
    def detect(self):
        pass

    @abstractmethod
    def alarm(self):
        pass

class DetectorByBroadCaster(Detector):
    def __init__(self):
        self.is_on = False

    def detect(self):
        if get_broadcasters() != []:
            if not self.is_on:
                self.is_on = True
                return True
        else:
            self.is_on = False

        return False
    
    def alarm(self):
        notification.notify(
            title='서방님알람기',
            message='브로드캐스터 ON',
            app_name='SpouseAlarm',
            app_icon='./icon/icon.ico',
            timeout = 3
        )

class DetectorByTitleChanged(Detector):
    def __init__(self):
        self.title = get_title()

    def detect(self):
        temp_title = get_title()

        if self.title != temp_title:
            self.title = temp_title
            return True
        
        return False
    
    def alarm(self):
        notification.notify(
            title='서방님알람기',
            message='방제 변경됨',
            app_name='SpouseAlarm',
            app_icon='./icon/icon.ico',
            timeout = 3
        )

class DetectorByStream(Detector):
    def __init__(self):
        self.is_stream = False

    def detect(self):
        if get_stream() != None:
            if not self.is_stream:
                self.is_stream = True
                return True
        else:
            self.is_stream = False
        
        return False
    
    def alarm(self):
        notification.notify(
            title='서방님알람기',
            message='방송 시작',
            app_name='SpouseAlarm',
            app_icon='./icon/icon.ico',
            timeout = 3
        )
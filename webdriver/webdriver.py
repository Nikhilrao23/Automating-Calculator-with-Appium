from appium import webdriver


class driver:

    def __int__(self):

        desired_caps = {

            'platformName': 'android',
            'deviceName': 'Pixel 2 XL',
            'appPackage': 'com.android.calculator',
            'appActivity': 'com.android.calculator2.Calculator'
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)


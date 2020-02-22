from abc import ABCMeta, abstractmethod


class USBPower():
    def __init__(self):
        pass

    def chargefromPower(self, plug_to):
        if plug_to == 'USB':
            print('USB電源から充電します')
        else:
            print('plugが合わないので電源から充電ができませんでした')

class Power():
    def __init__(self):
        pass

    def chargefromPower(self, plug_to):
        if plug_to == 'Outlet':
            print('電源から充電します')
        else:
            print('plugが合わないので電源から充電ができませんでした')

class Adapter(metaclass=ABCMeta):
    @abstractmethod
    def typeChange(self):
        pass

class UsbAdapter(Adapter):
    def __init__(self):
        pass

    def typeChange(self):
        self.from_male_parts_type = 'Outlet'

class LightningCable(metaclass=ABCMeta):
    def __init__(self):
        self.from_male_parts_type = 'USB'
        self.to_male_parts_type = 'lightning'

    def charge(self, power_type):
        if power_type == 'Power':
            power = Power()
        elif power_type == 'USBPower':
            power = USBPower()

        power.chargefromPower(self.from_male_parts_type)

class AdapterLightningCable(LightningCable, UsbAdapter):
    def __init__(self):
        LightningCable.__init__(self)
        self.typeChange()

    def charge(self, power_type):
        super().charge(power_type)


def my_iPhone():
    lightning_cable = LightningCable()
    lightning_cable.charge('Power')
    lightning_cable.charge('USBPower')

    adapter_lightning_cable = AdapterLightningCable()
    adapter_lightning_cable.charge('Power')
    adapter_lightning_cable.charge('USBPower')

if __name__ == '__main__':
    my_iPhone()

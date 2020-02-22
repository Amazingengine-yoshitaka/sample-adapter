import pytest


from app import LightningCable
from app import AdapterLightningCable

def test_LightningCable():
    lightning_cable = LightningCable()
    assert lightning_cable.from_male_parts_type == 'USB'
    assert lightning_cable.to_male_parts_type == 'lightning'

def test_LightningCable_charge(capfd):
    lightning_cable = LightningCable()
    lightning_cable.charge('Power')

    out, err = capfd.readouterr()
    assert out == 'plugが合わないので電源から充電ができませんでした\n'
    assert err is ''

    lightning_cable.charge('USBPower')

    out, err = capfd.readouterr()
    assert out == 'USB電源から充電します\n'
    assert err is ''

def test_AdapterLightningCable():
    adapter_lightning_cable = AdapterLightningCable()
    assert adapter_lightning_cable.from_male_parts_type == 'Outlet'
    assert adapter_lightning_cable.to_male_parts_type == 'lightning'
    adapter_lightning_cable.charge('Power')
    adapter_lightning_cable.charge('USBPower')

def test_AdapterLightningCable_charge(capfd):
    lightning_cable = AdapterLightningCable()
    lightning_cable.charge('Power')

    out, err = capfd.readouterr()
    assert out == '電源から充電します\n'
    assert err is ''

    lightning_cable.charge('USBPower')

    out, err = capfd.readouterr()
    assert out == 'plugが合わないので電源から充電ができませんでした\n'
    assert err is ''

"""PWMService integration test"""
import pytest
from edgepi_rpc_client.services.pwm.client_pwm_service import ClientPWMService
from edgepi_rpc_client.services.pwm.pwm_pb_enums import PWMPins, Polarity

@pytest.fixture(name="pwm_service")
def fixture_test_pwm_service():
    """Inits new PWM service client for testing"""
    return ClientPWMService('tcp://localhost:4444')

@pytest.mark.parametrize(
    "pwm_num",
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_set_config(pwm_service, pwm_num):
    """Test for set_config"""
    response_init = pwm_service.init_pwm(pwm_num)
    assert response_init == "Successfully intialized PWM"
    response_config = pwm_service.set_config(pwm_num)
    assert response_config == "Successfully applied pwm configurations"

@pytest.mark.parametrize(
    "pwm_num, frequency",
    [
        (PWMPins.PWM1, 1000),
        (PWMPins.PWM1, 10000),
    ]
)
def test_set_frequency(pwm_service, pwm_num, frequency):
    """Test for set_frequency"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.set_frequency(pwm_num, frequency)
    assert response == "Successfully set PWM frequency"

@pytest.mark.parametrize(
    "pwm_num, duty_cycle",
    [
        (PWMPins.PWM1, 0),
        (PWMPins.PWM1, 100),
    ]
)
def test_set_duty_cycle(pwm_service, pwm_num, duty_cycle):
    """Test for set_duty_cycle"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.set_duty_cycle(pwm_num, duty_cycle)
    assert response == "Successfully set PWM duty cycle"

@pytest.mark.parametrize(
    "pwm_num, polarity",
    [
        (PWMPins.PWM1, Polarity.NORMAL),
        (PWMPins.PWM1, Polarity.INVERSED),
    ]
)
def test_set_polarity(pwm_service, pwm_num, polarity):
    """Test for set_polarity"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.set_polarity(pwm_num, polarity)
    assert response == "Successfully set PWM polarity"

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_enable(pwm_service, pwm_num):
    """Test for set_enable"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.enable(pwm_num)
    assert response == "Successfully enabled PWM"

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_disable(pwm_service, pwm_num):
    """Test for set_disable"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.disable(pwm_num)
    assert response == "Successfully disabled PWM"

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_close(pwm_service, pwm_num):
    """Test for close"""
    pwm_service.init_pwm(pwm_num)
    response = pwm_service.close(pwm_num)
    assert response == "Successfully closed PWM"


@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_get_frequency(pwm_service, pwm_num):
    """Test for get_frequency"""
    pwm_service.init_pwm(pwm_num)
    frequency = pwm_service.get_frequency(pwm_num)
    assert isinstance(frequency, float)

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_get_duty_cycle(pwm_service, pwm_num):
    """Test for get_duty_cycle"""
    pwm_service.init_pwm(pwm_num)
    duty_cycle = pwm_service.get_duty_cycle(pwm_num)
    assert isinstance(duty_cycle, int)

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_get_polarity(pwm_service, pwm_num):
    """Test for get_polarity"""
    pwm_service.init_pwm(pwm_num)
    polarity = pwm_service.get_polarity(pwm_num)
    assert polarity in Polarity

@pytest.mark.parametrize(
    'pwm_num',
    [
        (PWMPins.PWM1),
        (PWMPins.PWM2),
    ]
)
def test_get_enabled(pwm_service, pwm_num):
    """Test for get_enabled"""
    pwm_service.init_pwm(pwm_num)
    enabled = pwm_service.get_enabled(pwm_num)
    assert isinstance(enabled, bool)

import pytest
from data_loader import MotorImageryDataset

def test_data_loader():
    # Test with subject 1, training session
    dataset = MotorImageryDataset('.', subject=1, session='T')
    trials, classes = dataset.get_trials()
    assert len(trials) == len(classes)
    assert len(trials) > 0

    # Test with subject 2, evaluation session
    dataset = MotorImageryDataset('.', subject=2, session='E')
    trials, classes = dataset.get_trials()
    assert len(trials) == len(classes)
    assert len(trials) > 0

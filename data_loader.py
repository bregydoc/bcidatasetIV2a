import numpy as np

class MotorImageryDataset:
    def __init__(self, data_path, subject, session='T'):
        """
        Initializes the Motor Imagery Dataset loader.

        Args:
            data_path (str): The path to the directory containing the dataset files.
            subject (int): The subject number (1-9).
            session (str): The session type, 'T' for training or 'E' for evaluation.
        """
        filename = f"A{subject:02d}{session}.npz"
        filepath = f"{data_path}/{filename}"
        self.data = np.load(filepath)

        self.Fs = 250  # 250Hz from original paper

        # keys of data ['s', 'etyp', 'epos', 'edur', 'artifacts']
        self.raw = self.data['s'].T
        self.events_type = self.data['etyp'].T
        self.events_position = self.data['epos'].T
        self.events_duration = self.data['edur'].T
        self.artifacts = self.data['artifacts'].T

        # Types of motor imagery
        self.mi_types = {769: 'left', 770: 'right',
                         771: 'foot', 772: 'tongue', 783: 'unknown'}

    def get_trials(self, channels=None):
        """
        Extracts trials from the dataset for the specified channels.

        Args:
            channels (list of int, optional): A list of channel indices to extract.
                                             If None, all channels are extracted.
                                             Defaults to None.

        Returns:
            tuple: A tuple containing:
                - trials (list of np.ndarray): A list of trials. Each trial is a
                                               NumPy array of shape (n_channels, n_samples).
                - classes (list of str): A list of class labels for each trial.
        """
        if channels is None:
            channels = list(range(self.raw.shape[0]))

        startrial_code = 768
        starttrial_events = self.events_type == startrial_code
        idxs = [i for i, x in enumerate(starttrial_events[0]) if x]

        trials = []
        classes = []

        for index in idxs:
            try:
                type_e = self.events_type[0, index + 1]
                class_e = self.mi_types[type_e]

                start = self.events_position[0, index]
                stop = start + self.events_duration[0, index]
                trial = self.raw[channels, start:stop]
                trials.append(trial)
                classes.append(class_e)

            except KeyError:
                # This happens when the event type is not in mi_types
                continue
            except IndexError:
                # This happens at the end of the events list
                continue

        return trials, classes

import os
import subprocess


class TestingSystem:
    """
    This class provides testing system, that tests algorithms sent by users
    """

    def __init__(self):
        self.scores_dir = './scores'

    def run_test(self, path):
        """
        Evaluate scripts sent by users and save results to corresponding files

        Args:
            path: path to folder with user scripts
        """
        files = [os.path.abspath(f) for f in os.listdir(path)]
        for file in files:
            fname = os.path.basename(file)
            output_path = os.path.join(self.scores_dir, fname)
            with open(output_path, 'w') as f:
                subprocess.run(['python3', file], stdout=f)

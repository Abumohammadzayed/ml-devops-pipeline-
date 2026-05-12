import os
import subprocess

def test_training_script_runs():
    # Run the training script
    result = subprocess.run(["python", "src/train.py"], capture_output=True, text=True)
    # Check exit code
    assert result.returncode == 0
    # Check that the model file was created
    assert os.path.exists("models/iris_model.pkl")

# Import monai and ITK
import monai
import itk
import numpy as np


from monai.apps import DecathlonDataset

# Set the directory where you want to download the dataset
root_dir = "./data"

# Download the dataset
DecathlonDataset(root_dir=root_dir, task="Task08_HepaticVessel", section="training", download=True)

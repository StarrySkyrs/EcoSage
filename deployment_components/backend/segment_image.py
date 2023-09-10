import os
from image_processing.image_segmentation import main_segmentation
from image_processing.image_labeling import query
import argparse
import sys
from pathlib import Path 


def segment_images(image_path:str,segment_images_dir:str)->list:
        # Define the variable arguments as variables
        weight = "./weights/FastSAM-s.pt"
        output_dir = segment_images_dir

        # Create an argparse.Namespace object with the defined variables
        args = argparse.Namespace(
        weight=weight,
        image_path=image_path,
        output_dir=output_dir
        )
        # Call the main function with the parsed arguments
        list_of_images=main_segmentation(args)

        return list_of_images

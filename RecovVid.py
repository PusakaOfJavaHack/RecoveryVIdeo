import imageio_ffmpeg as ffmpeg
import cv2
import numpy as np

def fix_corrupt_video(input_path, output_path):
    try:
        # Read the corrupted video using imageio_ffmpeg
        video = ffmpeg.get_reader(input_path)
        
        # Get video properties
        fps = video.get_meta_data()['fps']
        width, height = video.get_meta_data()['size']
        
        # Create a writer object for the output video
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
        
        # Read frames and write to the output video
        for frame in video:
            out.write(frame)
        
        # Release the writer object
        out.release()
        
        print("Video fix successful!")
    except Exception as e:
        print(f"Error fixing video: {e}")

# Replace 'corrupted_input.mp4' and 'fixed_output.avi' with your file names
fix_corrupt_video('corrupted_input.mp4', 'fixed_output.avi')

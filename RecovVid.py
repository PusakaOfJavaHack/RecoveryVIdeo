import imageio
import cv2
import os

def fix_corrupt_video(input_path, output_path):
    try:
        # Extract input video file extension
        input_extension = os.path.splitext(input_path)[1][1:].lower()

        # Read the corrupted video using imageio
        video = imageio.get_reader(input_path)

        # Get video properties
        fps = video.get_meta_data()['fps']
        width, height = video.get_meta_data()['size']

        # Create a writer object for the output video
        output_extension = os.path.splitext(output_path)[1][1:].lower()
        fourcc = 'XVID' if output_extension == 'avi' else 'mp4v'  # Adjust as needed
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*fourcc), fps, (width, height))

        # Read frames and write to the output video
        for frame in video:
            out.write(frame)

        # Release the writer object
        out.release()

        print("Video fix successful!")
    except Exception as e:
        print(f"Error fixing video: {e}")

# Replace 'corrupted_input.mp4' and 'fixed_output.mp4' with your file names
fix_corrupt_video('corrupted_input.mp4', 'fixed_output.mp4')

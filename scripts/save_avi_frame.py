import cv2
import os

def extract_frame(video_path, frame_number):
    # Check if the video file exists
    if not os.path.isfile(video_path):
        print("File not found.")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Check if the specified frame number is valid
    if frame_number < 0 or frame_number >= total_frames:
        print(f"Frame number should be between 0 and {total_frames - 1}.")
        cap.release()
        return

    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if ret:
        # Get the directory of the video file
        directory = os.path.dirname(video_path)

        # Save the frame as a JPEG image
        frame_path = os.path.join(directory, f"frame_{frame_number}.jpeg")
        cv2.imwrite(frame_path, frame)
        print(f"Frame {frame_number} saved as {frame_path}")
    else:
        print("Error reading frame.")

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    # Get user inputs
    video_file = input("Enter the path to the video file (e.g., video.avi): ")
    frame_num = int(input("Enter the frame number you want to extract: "))

    # Extract the frame
    extract_frame(video_file, frame_num)

import cv2
import os

def detect_and_track_dark_objects(video_filename, start_frame, end_frame, min_area, max_area, sensitivity):
    cap = cv2.VideoCapture(video_filename)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Output video file path
    output_path = os.path.dirname(video_filename)
    output_filename = os.path.join(output_path, 'tracked_video.mp4')

    out = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    # Set start and end frames
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Background subtraction
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
            break

        # Apply background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Threshold to detect dark objects
        _, thresh = cv2.threshold(fg_mask, 50, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Filter contours based on area
            area = cv2.contourArea(contour)
            if min_area < area < max_area:  # Adjust the area thresholds as needed
                # Get bounding box and center
                x, y, w, h = cv2.boundingRect(contour)
                center = (int(x + w / 2), int(y + h / 2))

                # Draw semi-transparent green marker
                cv2.circle(frame, center, 10, (0, 255, 0), -1, lineType=cv2.LINE_AA)

        # Write frame to output video
        out.write(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Example usage:
video_filename = '/Users/jamescrall/Desktop/vulturebee/Cebo2_Arboleda/vulturebee2_2024-01-09_09-30-01.mjpeg'
start_frame = 100  # Specify start frame
end_frame = 300  # Specify end frame
min_area_threshold = 200  # Specify minimum area threshold
max_area_threshold = 1500  # Specify maximum area threshold
sensitivity_threshold = 30  # Specify sensitivity threshold for object difference from background
detect_and_track_dark_objects(video_filename, start_frame, end_frame, min_area_threshold, max_area_threshold, sensitivity_threshold)

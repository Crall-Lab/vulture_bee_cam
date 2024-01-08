import cv2

def display_every_tenth_frame(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        if frame_count % 1 == 0:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def main():
    video_path = input("Enter the path to the MJPEG video file: ")
    display_every_tenth_frame(video_path)

if __name__ == "__main__":
    main()

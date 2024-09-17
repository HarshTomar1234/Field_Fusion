# import cv2

# def read_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frames.append(frame)
#     cap.release()
#     print(f"Read {len(frames)} frames from {video_path}")
#     return frames

# def save_video(output_video_frames, output_video_path):
#     if not output_video_frames:
#         print("Error: output_video_frames is empty")
#         return

#     if output_video_frames[0] is None:
#         print("Error: First frame is None")
#         return

#     height, width = output_video_frames[0].shape[:2]
#     print(f"Frame dimensions: {width}x{height}")

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

#     for i, frame in enumerate(output_video_frames):
#         if frame is not None:
#             out.write(frame)
#         else:
#             print(f"Warning: Frame {i} is None, skipping")

#     out.release()
#     print(f"Saved {len(output_video_frames)} frames to {output_video_path}")

# # Example usage
# video_path = 'input_videos/08fd33_4.mp4'
# output_path = 'output_videos/output_video.avi'

# frames = read_video(video_path)
# save_video(frames, output_path)



# import cv2

# def read_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frames.append(frame)
#     return frames

# def save_video(output_video_frames,output_video_path):
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
#     for frame in output_video_frames:
#         out.write(frame)
#     out.release()



import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return []

    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame is not None:
            frames.append(frame)
            frame_count += 1
        else:
            print(f"Warning: Frame {frame_count} is None, skipping")

    cap.release()
    print(f"Read {len(frames)} valid frames out of {frame_count} total frames from {video_path}")
    
    if not frames:
        print("Error: No valid frames read from the video")
    elif frames[0] is None:
        print("Error: First frame is None, this shouldn't happen")
    
    return frames

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        print("No frames to save. The output video frames list is empty.")
        return
        
    first_frame = next((frame for frame in output_video_frames if frame is not None), None)
    if first_frame is None:
        print("All frames are None. Cannot save the video.")
        return
        
    height, width = first_frame.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))
    
    for frame in output_video_frames:
        if frame is not None:
            out.write(frame)
    
    out.release()
    print(f"Saved video with {len(output_video_frames)} frames to {output_video_path}")

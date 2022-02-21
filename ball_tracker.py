import cv2
import csv

"""
function to detect the ball and save the ball postion in a csv
"""
def get_ball_trajectory(video_path):

    storage_file_name = video_path.split('/')[1]

    # capturing the video file
    ball_vid_capture = cv2.VideoCapture(video_path + ".mp4")

    # Check if file opened successfully
    if ball_vid_capture.isOpened == False:
        print("Error processing the file!!")

    red_upper_limit = (179, 255, 255)
    red_lower_limit = (0, 50, 50)

    trajectory_pos = []

    save_img_array = []

    while (ball_vid_capture):
        _, frame = ball_vid_capture.read()

        try:           
            frame_resized = cv2.resize(frame, (600, 600)) 

            hsv = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2HSV)
            
            mask = cv2.inRange(hsv, red_lower_limit, red_upper_limit)
            cntrs = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            center = None

            if len(cntrs) > 0:
                cnt = max(cntrs, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                trajectory_pos.append((round(x), 600-round(y)))
                if radius > 10:
                    cv2.circle(frame_resized, (int(x), int(y)), int(radius), (255,255,0), 2)
            
            save_img_array.append(frame_resized)
            cv2.imshow("Frame", frame_resized)
            cv2.imshow("Mask", mask)
            if cv2.waitKey(150) & 0xFF == ord('q'):
                break
        
        except:
            break

    # writing postion data of the ball to a CSV
    with open(storage_file_name+"pos.csv", 'w') as f:
        writer = csv.writer(f)
        for pos in trajectory_pos:
            writer.writerow(pos)

    out = cv2.VideoWriter(storage_file_name+'.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, (600, 600))
 
    for i in range(len(save_img_array)):
        out.write(save_img_array[i])
    out.release()

    ball_vid_capture.release()
    cv2.destroyAllWindows()






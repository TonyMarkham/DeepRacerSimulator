from point import Point
from line import Line
from track import Track
import tkinter
import csv
import math

# TrackFile = "./tracks/China_track.csv"
TrackFile = "./tracks/Mexico_track.csv"
window_width = 1920
window_height = 1080
map_padding = 20
track_scale = 1.0
track_width = 0.64

episode_value = 0
step_value = 0
x_value = 0.0
y_value = 0.0
heading_value = 0.0
steering_angle_value = 0.0
speed_value = 0.0
action_taken_value = 0
reward_value = 0.0
job_completed_value = False
all_wheels_on_track_value = True
progress_value = 0.0
closest_waypoint_value = 0
track_length_value = 0.0
time_value = 0.0

track = Track()


def scale():
    global track_scale, map_canvas

    map_canvas.update()
    x_scale = (map_canvas.winfo_width() - (2 * map_padding)) / track.width
    y_scale = (map_canvas.winfo_height() - (2 * map_padding)) / track.height
    if x_scale < y_scale:
        track_scale = x_scale
    else:
        track_scale = y_scale


def draw_line(p1x_in, p1y_in, p2x_in, p2y_in, thickness, colour):
    global map_canvas

    x1 = (p1x_in - track.minimum_x + map_padding / track_scale) * track_scale
    y1 = (p1y_in - track.maximum_y - map_padding / track_scale) * track_scale * -1
    x2 = (p2x_in - track.minimum_x + map_padding / track_scale) * track_scale
    y2 = (p2y_in - track.maximum_y - map_padding / track_scale) * track_scale * -1

    map_canvas.create_line(x1, y1, x2, y2, fill=colour, width=thickness)


def load_track_data():
    previous_point = Point(math.inf, math.inf)
    with open(TrackFile) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            x = float(line[0])
            y = float(line[1])
            p = Point(x, y)
            if p.x != previous_point.x and p.y != previous_point.y:
                track.center_points.append(p)
            previous_point = p
    track.setup(track_width)
    scale()


def draw_track():
    draw_centerline()
    draw_inside_line()
    draw_outside_line()


def draw_centerline():
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    for line in track.center_lines:
        p1 = line.P1
        p2 = line.P2
        draw_line(p1.x, p1.y, p2.x, p2.y, 2.0, 'yellow')


def draw_inside_line():
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    for line in track.inside_lines:
        p1 = line.P1
        p2 = line.P2
        draw_line(p1.x, p1.y, p2.x, p2.y, 2.0, 'black')


def draw_outside_line():
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    for line in track.outside_lines:
        p1 = line.P1
        p2 = line.P2
        draw_line(p1.x, p1.y, p2.x, p2.y, 2.0, 'black')


def draw_data_frame():
    global data_canvas

    data_canvas = tkinter.Canvas(
        main_window,
        borderwidth=2
    )
    data_canvas.pack(side='right', fill=tkinter.Y, padx=(5, 5), pady=(5, 5))

    episode_frame = tkinter.LabelFrame(data_canvas, text="Episode")
    episode_frame.pack(side='top', fill=tkinter.X)
    episode_data = tkinter.Label(episode_frame, text=episode_value)
    episode_data.pack(side='right', fill=tkinter.X)

    step_frame = tkinter.LabelFrame(data_canvas, text="Step")
    step_frame.pack(side='top', fill=tkinter.X)
    step_data = tkinter.Label(step_frame, text=step_value)
    step_data.pack(side='right', fill=tkinter.X)

    x_frame = tkinter.LabelFrame(data_canvas, text="X Position")
    x_frame.pack(side='top', fill=tkinter.X)
    x_data = tkinter.Label(x_frame, text=x_value)
    x_data.pack(side='right', fill=tkinter.X)

    y_frame = tkinter.LabelFrame(data_canvas, text="y Position")
    y_frame.pack(side='top', fill=tkinter.X)
    y_data = tkinter.Label(y_frame, text=y_value)
    y_data.pack(side='right', fill=tkinter.X)

    heading_frame = tkinter.LabelFrame(data_canvas, text="Heading")
    heading_frame.pack(side='top', fill=tkinter.X)
    heading_data = tkinter.Label(heading_frame, text=heading_value)
    heading_data.pack(side='right', fill=tkinter.X)

    steering_angle_frame = tkinter.LabelFrame(data_canvas, text="Steering Angle")
    steering_angle_frame.pack(side='top', fill=tkinter.X)
    steering_angle_data = tkinter.Label(steering_angle_frame, text=steering_angle_value)
    steering_angle_data.pack(side='right', fill=tkinter.X)

    speed_frame = tkinter.LabelFrame(data_canvas, text="Speed")
    speed_frame.pack(side='top', fill=tkinter.X)
    speed_data = tkinter.Label(speed_frame, text=speed_value)
    speed_data.pack(side='right', fill=tkinter.X)

    action_taken_frame = tkinter.LabelFrame(data_canvas, text="Action Taken")
    action_taken_frame.pack(side='top', fill=tkinter.X)
    action_taken_data = tkinter.Label(action_taken_frame, text=action_taken_value)
    action_taken_data.pack(side='right', fill=tkinter.X)

    reward_frame = tkinter.LabelFrame(data_canvas, text="Reward")
    reward_frame.pack(side='top', fill=tkinter.X)
    reward_data = tkinter.Label(reward_frame, text=reward_value)
    reward_data.pack(side='right', fill=tkinter.X)

    job_completed_frame = tkinter.LabelFrame(data_canvas, text="Job Completed")
    job_completed_frame.pack(side='top', fill=tkinter.X)
    job_completed_data = tkinter.Label(job_completed_frame, text=job_completed_value)
    job_completed_data.pack(side='right', fill=tkinter.X)

    all_wheels_on_track_frame = tkinter.LabelFrame(data_canvas, text="All Wheels On Track")
    all_wheels_on_track_frame.pack(side='top', fill=tkinter.X)
    all_wheels_on_track_data = tkinter.Label(all_wheels_on_track_frame, text=all_wheels_on_track_value)
    all_wheels_on_track_data.pack(side='right', fill=tkinter.X)

    progress_frame = tkinter.LabelFrame(data_canvas, text="Progress")
    progress_frame.pack(side='top', fill=tkinter.X)
    progress_data = tkinter.Label(progress_frame, text=progress_value)
    progress_data.pack(side='right', fill=tkinter.X)

    closest_waypoint_index_frame = tkinter.LabelFrame(data_canvas, text="Closest Waypoint Index")
    closest_waypoint_index_frame.pack(side='top', fill=tkinter.X)
    closest_waypoint_index_data = tkinter.Label(closest_waypoint_index_frame, text=y_value)
    closest_waypoint_index_data.pack(side='right', fill=tkinter.X)

    track_length_frame = tkinter.LabelFrame(data_canvas, text="Track Length")
    track_length_frame.pack(side='top', fill=tkinter.X)
    track_length_data = tkinter.Label(track_length_frame, text=track_length_value)
    track_length_data.pack(side='right', fill=tkinter.X)

    time_frame = tkinter.LabelFrame(data_canvas, text="Time")
    time_frame.pack(side='top', fill=tkinter.X)
    time_data = tkinter.Label(time_frame, text=time_value)
    time_data.pack(side='right', fill=tkinter.X)


# 1280x800, 1440x900, 1680x1050
# 1280x720, 1366x768, 1920x1080
main_window = tkinter.Tk()
main_window.title("DeepRacer - Track Simulator")
data_canvas = tkinter.Canvas(main_window)

# map_frame_width = 1260
window_width = 1550
window_height = 1050

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

window_left_position = (screen_width / 2) - (window_width / 2)
window_top_position = (screen_height / 2) - (window_height / 2)

main_window.geometry('%dx%d+%d+%d' % (window_width, window_height, window_left_position, window_top_position))
main_window.resizable(False, False)

draw_data_frame()
data_canvas.update()
main_window.update()
available_x = main_window.winfo_width() - data_canvas.winfo_width()
available_y = main_window.winfo_height() - data_canvas.winfo_height()

map_canvas = tkinter.Canvas(main_window, width=available_x, height=available_y)
map_canvas.pack(side='right', fill=tkinter.Y)

load_track_data()
draw_track()








main_window.mainloop()
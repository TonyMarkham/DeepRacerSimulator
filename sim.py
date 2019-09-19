from point import Point
from line import Line
from track import Track
from race_car import Racecar
from ray import Ray
import tkinter
import csv
import math

# TrackFile = "./tracks/China_track.csv"
TrackFile = "./tracks/Mexico_track.csv"
map_padding = 20
track_scale = 1.0
track_width = 0.64
position_index = 0

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

ray_centre = Ray()
ray_front_right_00 = Ray()
ray_front_left_00 = Ray()

track = Track()
racecar = Racecar()


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


def create_line(p1x_in, p1y_in, p2x_in, p2y_in, thickness, colour):
    global map_canvas

    x1 = (p1x_in - track.minimum_x + map_padding / track_scale) * track_scale
    y1 = (p1y_in - track.maximum_y - map_padding / track_scale) * track_scale * -1
    x2 = (p2x_in - track.minimum_x + map_padding / track_scale) * track_scale
    y2 = (p2y_in - track.maximum_y - map_padding / track_scale) * track_scale * -1

    return map_canvas.create_line(x1, y1, x2, y2, fill=colour, width=thickness)


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
    # Start / Finish Line
    draw_line(
        track.inside_points[0].x,
        track.inside_points[0].y,
        track.outside_points[0].x,
        track.outside_points[0].y,
        2.0,
        'red'
    )


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


def adjust_polygon(polygon_in):
    i = 0
    while i < len(polygon_in):
        j = i + 1
        polygon_in[i] = (polygon_in[i] - track.minimum_x + map_padding / track_scale) * track_scale
        polygon_in[j] = (polygon_in[j] - track.maximum_y - map_padding / track_scale) * track_scale * -1
        i += 2
    return polygon_in


def draw_racecar(x_in, y_in, heading_in, steering_angle_in):
    global racecar_chassis, racecar_right_front_wheel, racecar_right_rear_wheel
    global racecar_left_front_wheel, racecar_left_rear_wheel
    global camera_circle, centre_ray_line, right_ray_line_00, left_ray_line_00
    global ray_centre, ray_front_right_00, ray_front_left_00

    racecar.update_car(x_in, y_in, heading_in, steering_angle_in)

    map_canvas.delete(racecar_chassis)
    map_canvas.delete(racecar_right_front_wheel)
    map_canvas.delete(racecar_right_rear_wheel)
    map_canvas.delete(racecar_left_front_wheel)
    map_canvas.delete(racecar_left_rear_wheel)
    map_canvas.delete(camera_circle)
    map_canvas.delete(centre_ray_line)
    map_canvas.delete(right_ray_line_00)
    map_canvas.delete(left_ray_line_00)

    chassis = racecar.chassis_polygon.copy()
    right_front = racecar.right_front_wheel_polygon.copy()
    right_rear = racecar.right_rear_wheel_polygon.copy()
    left_front = racecar.left_front_wheel_polygon.copy()
    left_rear = racecar.left_rear_wheel_polygon.copy()

    racecar_chassis = map_canvas.create_polygon(
        adjust_polygon(chassis),
        outline='black',
        width=0.5,
        fill='red'
    )
    racecar_right_front_wheel = map_canvas.create_polygon(
        adjust_polygon(right_front),
        outline='black',
        width=0.5,
        fill='black'
    )
    racecar_right_rear_wheel = map_canvas.create_polygon(
        adjust_polygon(right_rear),
        outline='black',
        width=0.5,
        fill='black'
    )
    racecar_left_front_wheel = map_canvas.create_polygon(
        adjust_polygon(left_front),
        outline='black',
        width=0.5,
        fill='black'
    )
    racecar_left_rear_wheel = map_canvas.create_polygon(
        adjust_polygon(left_rear),
        outline='black',
        width=0.5,
        fill='black'
    )
    # Draw Centre Ray
    v = Point(-math.sin(heading_in * math.pi / 180), math.cos(heading_in * math.pi / 180))
    ray_centre.define(racecar.camera, v)
    p1_x = (ray_centre.P1.x - 0.025 - track.minimum_x + map_padding / track_scale) * track_scale
    p1_y = (ray_centre.P1.y - 0.025 - track.maximum_y - map_padding / track_scale) * track_scale * -1
    p2_x = (ray_centre.P1.x + 0.025 - track.minimum_x + map_padding / track_scale) * track_scale
    p2_y = (ray_centre.P1.y + 0.025 - track.maximum_y - map_padding / track_scale) * track_scale * -1
    camera_circle = map_canvas.create_oval(p1_x, p1_y, p2_x, p2_y, outline='blue')
    lines = []
    for inside_line in track.inside_lines:
        point = ray_centre.find_intersection(inside_line)
        if ray_centre.find_intersection(inside_line):
            lines.append(Line(racecar.camera, point))
    for outside_line in track.outside_lines:
        point = ray_centre.find_intersection(outside_line)
        if ray_centre.find_intersection(outside_line):
            lines.append(Line(racecar.camera, point))
    shortest = math.inf
    shortest_index = -1
    for i, l in enumerate(lines):
        if l.Length < shortest:
            shortest = l.Length
            shortest_index = i
    if i > -1:
        centre_ray_line = create_line(
            lines[shortest_index].P1.x,
            lines[shortest_index].P1.y,
            lines[shortest_index].P2.x,
            lines[shortest_index].P2.y,
            0.5,
            'blue'
        )
    # Draw Right Wheel Ray
    ray_front_right_00.define(racecar.ray_right_front_00, v)
    lines = []
    for inside_line in track.inside_lines:
        point = ray_front_right_00.find_intersection(inside_line)
        if point:
            lines.append(Line(racecar.ray_right_front_00, point))
    for outside_line in track.outside_lines:
        point = ray_front_right_00.find_intersection(outside_line)
        if point:
            lines.append(Line(racecar.ray_right_front_00, point))
    shortest = math.inf
    shortest_index = -1
    for i, l in enumerate(lines):
        if l.Length < shortest:
            shortest = l.Length
            shortest_index = i
    if i > -1:
        right_ray_line_00 = create_line(
            lines[shortest_index].P1.x,
            lines[shortest_index].P1.y,
            lines[shortest_index].P2.x,
            lines[shortest_index].P2.y,
            0.5,
            'blue'
        )
    # Draw Left Wheel Ray
    ray_front_left_00.define(racecar.ray_left_front_00, v)
    lines = []
    for inside_line in track.inside_lines:
        point = ray_front_left_00.find_intersection(inside_line)
        if point:
            lines.append(Line(racecar.ray_left_front_00, point))
    for outside_line in track.outside_lines:
        point = ray_front_left_00.find_intersection(outside_line)
        if point:
            lines.append(Line(racecar.ray_left_front_00, point))
    shortest = math.inf
    shortest_index = -1
    for i, l in enumerate(lines):
        if l.Length < shortest:
            shortest = l.Length
            shortest_index = i
    if i > -1:
        left_ray_line_00 = create_line(
            lines[shortest_index].P1.x,
            lines[shortest_index].P1.y,
            lines[shortest_index].P2.x,
            lines[shortest_index].P2.y,
            0.5,
            'blue'
        )


def up_pressed(event):
    global position_index

    position_index += 1
    if position_index == len(track.center_points):
        position_index = position_index - len(track.center_points) + 1
    next_index = position_index + 1
    if next_index == len(track.center_points):
        next_index = next_index - len(track.center_points) + 1
    if track.center_points[position_index] == track.center_points[next_index]:
        position_index += 1
        next_index = position_index + 1
    draw_racecar(
        track.center_points[position_index].x,
        track.center_points[position_index].y,
        calculate_heading(position_index, next_index),
        0
    )


def down_pressed(event):
    global position_index

    position_index -= 1
    if position_index == 0:
        position_index = len(track.center_points) - 1
    next_index = position_index + 1
    if next_index == len(track.center_points):
        next_index = next_index - len(track.center_points) + 1
    if track.center_points[position_index] == track.center_points[next_index]:
        position_index -= 1
        next_index = position_index + 1
    draw_racecar(
        track.center_points[position_index].x,
        track.center_points[position_index].y,
        calculate_heading(position_index, next_index),
        0
    )


def calculate_heading(index_1, index_2):
    p1 = track.center_points[index_1]
    p2 = track.center_points[index_2]
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return (math.atan2(dy, dx) - math.pi / 2) * 180 / math.pi


# 1280x800, 1440x900, 1680x1050
# 1280x720, 1366x768, 1920x1080
main_window = tkinter.Tk()
main_window.title("DeepRacer - Track Simulator")
main_window.bind("<Up>", up_pressed)
main_window.bind("<Down>", down_pressed)
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

pts = [0, 0, -1, 1, 1, 1]
racecar_chassis = map_canvas.create_polygon(pts, outline='black', width=0.5, fill='red')
racecar_right_front_wheel = map_canvas.create_polygon(pts, outline='black', width=0.5, fill='black')
racecar_right_rear_wheel = map_canvas.create_polygon(pts, outline='black', width=0.5, fill='black')
racecar_left_front_wheel = map_canvas.create_polygon(pts, outline='black', width=0.5, fill='black')
racecar_left_rear_wheel = map_canvas.create_polygon(pts, outline='black', width=0.5, fill='black')
camera_circle = map_canvas.create_oval(-1, -1, 1, 1, outline='blue')
centre_ray_line = create_line(0, 0, 1, 1, 0.5, 'blue')
right_ray_line_00 = create_line(0, 0, 1, 1, 0.5, 'blue')
left_ray_line_00 = create_line(0, 0, 1, 1, 0.5, 'blue')

load_track_data()
draw_track()
draw_racecar(
    track.center_points[0].x,
    track.center_points[0].y,
    calculate_heading(0, 1),
    0
)

main_window.mainloop()

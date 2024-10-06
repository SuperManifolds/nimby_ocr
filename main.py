import cv2
import pytesseract
import re
from datetime import timedelta, time
import numpy as np
import argparse
import csv

distance_pattern = (
    r"\+((?:\d{1,2}(?::)?)?\d{2}(?::)?\d{2}) ([\d,]+)m at (\d+) km\/h avg."
)
name_pattern = r"^([\do]{1,2}.[\do]{2}.[\do]{2}) (.*) (\w+)"
waypoint_pattern = r"^([\do]{1,2}.[\do]{2}.[\do]{2}) .*(Waypoint \d+) @"
region_pattern = r"^([\do]{1,2}.[\do]{2}.[\do]{2}) (.*)"


class Stop:
    def __init__(
        self,
        duration: timedelta,
        distance: int,
        speed: int,
        arrive_time: time,
        depart_time: time,
        name: str,
        platform: str,
        region: str,
    ):
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.arrive_time = arrive_time
        self.depart_time = depart_time
        self.name = name
        self.platform = platform
        self.region = region

    def __str__(self):
        return f"Stop at {self.name} in {self.region} at {self.arrive_time} on platform {self.platform}. Departing at {self.depart_time}. Distance: {self.distance}m, Duration: {self.duration}, Speed: {self.speed} km/h"

    def set_distance_info(self, duration: timedelta, distance: int, speed: int):
        self.duration = duration
        self.distance = distance
        self.speed = speed

    def set_name_info(self, arrive_time: time, name: str, platform: str):
        self.arrive_time = arrive_time
        self.name = name
        self.platform = platform

    def set_region_info(self, depart_time: time, region: str):
        self.depart_time = depart_time
        self.region = region

    def is_valid(self) -> bool:
        if self.name.startswith("Waypoint"):
            return (
                self.duration is not None
                and self.distance is not None
                and self.speed is not None
                and self.arrive_time is not None
                and self.depart_time is not None
                and self.name is not None
                and self.region is None
                and self.platform is None
            )
        return (
            self.duration is not None
            and self.distance is not None
            and self.speed is not None
            and self.arrive_time is not None
            and self.depart_time is not None
            and self.name is not None
            and self.platform is not None
            and self.region is not None
        )


def stops_from_text(text: str) -> [Stop]:
    lines = text.split("\n")
    stops = []
    current_stop = None
    for line in lines:
        if current_stop is None:
            if extract_distance_line(line):
                current_stop = Stop(None, None, None, None, None, None, None, None)
                current_stop.set_distance_info(*extract_distance_line(line))
            elif extract_name_line(line):
                current_stop = Stop(None, None, None, None, None, None, None, None)
                current_stop.set_name_info(*extract_name_line(line))
            else:
                continue
        else:
            if extract_distance_line(line):
                if current_stop.is_valid() and not has_stop(
                    current_stop.name, current_stop.arrive_time, stops
                ):
                    stops.append(current_stop)
                current_stop = Stop(None, None, None, None, None, None, None, None)
                current_stop.set_distance_info(*extract_distance_line(line))
            elif extract_waypoint_line(line) and current_stop.name is None:
                (time, waypoint) = extract_waypoint_line(line)
                current_stop.set_name_info(time, waypoint, None)
            elif extract_name_line(line) and current_stop.name is None:
                current_stop.set_name_info(*extract_name_line(line))
            elif extract_region_line(line):
                current_stop.set_region_info(*extract_region_line(line))
                if current_stop.name.startswith("Waypoint"):
                    current_stop.region = None

                if current_stop.is_valid() and not has_stop(
                    current_stop.name, current_stop.arrive_time, stops
                ):
                    stops.append(current_stop)
                current_stop = None
            else:
                continue

    return stops


def extract_distance_line(line: str) -> (timedelta, int, int):
    matches = re.search(distance_pattern, line)
    if matches:
        duration_text = matches.group(1)
        distance_text = matches.group(2)
        speed_text = matches.group(3)

        duration = timestamp_to_timedelta(duration_text)
        distance = distance_to_int(distance_text)
        speed = int(speed_text)
        return duration, distance, speed
    return None


def extract_name_line(line: str) -> (time, str, str):
    matches = re.search(name_pattern, line)
    if matches:
        time_text = matches.group(1)
        name_text = matches.group(2)
        platform_text = matches.group(3)

        time = timestamp_to_datetime(time_text)
        return time, name_text, platform_text

    return None


def extract_waypoint_line(line: str) -> (time, str):
    matches = re.search(waypoint_pattern, line)
    if matches:
        time_text = matches.group(1)
        waypoint_text = matches.group(2)

        time = timestamp_to_datetime(time_text)
        return time, waypoint_text

    return None


def extract_region_line(line: str) -> (str, str):
    matches = re.search(region_pattern, line)
    if matches:
        time_text = matches.group(1)
        region_text = matches.group(2)

        time = timestamp_to_datetime(time_text)
        return time, region_text

    return None


def timestamp_to_timedelta(timestamp: str) -> timedelta:
    secs = timestamp[-2:].replace("o", "0")
    mins = timestamp[-5:-3].replace("o", "0")
    hours = "0"
    if len(timestamp) > 5:
        hours = timestamp[:-6].replace("o", "0")

    return timedelta(hours=int(hours), minutes=int(mins), seconds=int(secs))


def timestamp_to_datetime(timestamp: str) -> time:
    secs = timestamp[-2:].replace("o", "0")
    mins = timestamp[-5:-3].replace("o", "0")
    hours = "0"
    if len(timestamp) > 5:
        hours = timestamp[:-6].replace("o", "0")

    return time(hour=int(hours), minute=int(mins), second=int(secs))


def distance_to_int(distance: str) -> int:
    return int(distance.replace(",", ""))


def has_stop(name: str, time: time, stops: [Stop]) -> bool:
    for stop in stops:
        if stop.arrive_time == time:
            return True
    return False


def write_csv(stops: [Stop], output_file: str):
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "name",
                "platform",
                "region",
                "arrival",
                "departure",
                "duration",
                "distance",
                "speed",
            ]
        )
        for stop in stops:
            writer.writerow(
                [
                    stop.name,
                    stop.platform,
                    stop.region,
                    stop.arrive_time,
                    stop.depart_time,
                    stop.duration,
                    stop.distance,
                    stop.speed,
                ]
            )


def main():
    parser = argparse.ArgumentParser(
        description="Processes a screen recording of a NIMBY rails line stop list and exports a CSV"
    )
    parser.add_argument(
        "--in",
        dest="input_file",
        required=True,
        help="Path to the input screen recording",
    )
    parser.add_argument(
        "--out", dest="output_file", required=True, help="Path to the output csv file"
    )
    args = parser.parse_args()

    output_file = "output.txt"

    # Open video file
    cap = cv2.VideoCapture(args.input_file)
    if not cap.isOpened():
        print(f"Failed to open the video file: {args.input_file}")
        return

    frame_number = 0
    all_text = []
    all_stops = []
    prev_frame = None
    similarity_threshold = 1000

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Process every 10th frame
        if frame_number % 10 == 0:
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if prev_frame is not None:
                diff = cv2.absdiff(gray_frame, prev_frame)
                non_zero_count = np.count_nonzero(diff)

                # Skip processing if the frame is too similar to the previous one
                if non_zero_count < similarity_threshold:
                    frame_number += 1
                    continue

            # Update previous frame
            prev_frame = gray_frame

            # Extract text from the frame using OCR
            text = pytesseract.image_to_string(gray_frame, config="--psm 6")
            all_text.append(text)

            # Process text for stops
            stops = stops_from_text(text)
            for stop in stops:
                if not has_stop(stop.name, stop.arrive_time, all_stops):
                    all_stops.append(stop)

        frame_number += 1
    #

    all_stops.sort(key=lambda x: x.arrive_time)

    cap.release()

    write_csv(all_stops, args.output_file)

    print("num stops: ", len(all_stops))
    for stop in all_stops:
        print(stop)


if __name__ == "__main__":
    main()

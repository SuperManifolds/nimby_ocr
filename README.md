# Nimby OCR

Uses optical character recognition to read stop timings from NIMBY Rails lines and generates a csv

## Example


https://github.com/user-attachments/assets/061abde5-d986-4ed8-a9b9-b4171fec8fd9


```
name,platform,region,arrival,departure,duration,distance,speed
North Brunswick,3N,North Brunswick Township,00:00:00,00:00:30,0:04:28,6774,91
Jersey Avenue,2N,New Brunswick,00:03:40,00:04:10,0:03:10,4852,92
New Brunswick,2N,New Brunswick,00:06:23,00:06:53,0:02:13,2995,81
Edison,1E,Edison,00:09:28,00:09:58,0:02:35,3731,87
Metuchen,1E,Metuchen,00:13:16,00:13:46,0:03:18,5122,93
Metro Park,2E,Woodbridge Township,00:16:35,00:17:05,0:02:49,4187,89
Rahway,3N,Rahway,00:20:53,00:21:23,0:03:48,6093,96
Linden,4N,Linden,00:23:46,00:24:16,0:02:23,3329,84
Elizabeth,2N,Elizabeth,00:27:40,00:28:10,0:03:24,5304,94
North Elizabeth,2N,Flizabeth,00:29:38,00:30:08,0:01:28,1554,64

```

## Dependencies
* numpy
* pytesseract
* opencv

## How to use
Set UI scaling to 200%
Make a screen recording of the stops list in a NIMBY rails line as you scroll from the top to the bottom at a casual pace.
Now run the Python script passing in the path to the screen recording

```python main.py --in input-recording.mp4 --out output-file.csv```

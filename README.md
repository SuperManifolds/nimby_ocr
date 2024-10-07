# Nimby OCR

Uses optical character recognition to read stop timings from NIMBY Rails lines and generates a csv

## Example


https://github.com/user-attachments/assets/061abde5-d986-4ed8-a9b9-b4171fec8fd9

<details>
<summary>Show output</summary>
  
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
Newark Liberty,6N,Newark,00:32:23,00:32:53,0:02:15,3064,82
Newark Penn Station,3E,Newark,00:35:37,00:36:07,0:02:44,4015,88
Hoboken,5E,Hoboken,00:44:44,00:45:14,0:08:37,11510,80
Fulton St.,1S,Manhattan,00:48:21,00:48:51,0:03:07,4478,86
Atlantic Terminal,17E,Brooklyn,00:52:11,00:52:41,0:03:20,5201,94
Nostrand Av,1E,Brooklyn,00:54:46,00:55:16,0:02:05,2268,65
East New York,2E,Brooklyn,00:57:57,00:58:27,0:02:41,3809,85
Woodhaven,4E,Queens,01:01:56,01:02:26,0:03:29,5251,90
Jamaica,6,Queens,01:04:53,01:05:23,0:02:27,3224,79
pl Waypoint 1421200@0.318 ©,Pass,Stop 20,01:06:09,01:06:09,0:00:46,611,48
St. Albans,1S,Queens,01:08:38,01:09:08,0:02:29,3953,95
Waypoint 9505100,,,01:11:29,01:11:29,0:02:21,3670,94
Lynbrook,3E,Village of Lynbrook,01:14:40,01:15:10,0:03:11,5764,109
Rockville Centre,1E,Village of Rockville Centre,01:17:07,01:17:37,0:00:57,2500,77
Baldwin,1E,Baldwin,01:20:00,01:20:30,0:02:23,3327,84
Freeport,1E,Village of Freeport,01:22:15,01:22:45,0:01:45,2087,72
Merrick,1E,Merrick,01:24:51,01:25:21,0:02:06,2792,80
Bellmore,1E,Bellmore,01:27:00,01:27:30,0:01:39,1901,69
Wantagh,1E,Wantagh,01:29:05,01:29:35,0:01:35,1766,67
Seaford,1E,Seaford,01:31:14,01:31:44,0:01:39,1898,69
Massapequa,1E,Massapequa,01:33:07,01:33:37,0:01:23,1426,62
Massapequa Park,1E,Village of Massapequa Park,01:34:52,01:35:22,0:01:15,1200,58
Amityville,1E,Village of Amityville,01:37:34,01:38:04,0:02:12,2995,82
Copiague,1E,Copiague,01:39:40,01:40:10,0:01:36,1820,68
Lindenhurst,1E,Village of Lindenhurst,01:42:12,01:42:42,0:02:02,2640,78
Babylon,1E,Village of Babylon,01:45:27,01:45:57,0:02:45,4053,88
Babylon,3W,Village of Babylon,01:49:18,01:49:48,0:03:21,3017,54
Lindenhurst,2W,Village of Lindenhurst,01:52:33,01:53:03,0:02:45,4046,88
Copiague,2W,Copiague,01:55:06,01:55:36,0:02:03,2618,77
Amityville,2W,Village of Amityville,01:57:13,01:57:43,0:01:37,1828,68
Massapequa Park,2W,Village of Massapequa Park,01:59:54,02:00:24,0:02:11,2950,81
Massapequa,2W,Massapequa,02:01:38,02:02:08,0:01:14,1163,57
Seaford,2W,Seaford,02:03:34,02:04:04,0:01:26,1521,64
Wantagh,2W,Wantagh,02:05:43,02:06:13,0:01:39,1915,70
Bellmore,2W,Bellmore,02:07:48,02:08:18,0:01:35,1763,67
Merrick,2W,Merrick,02:09:57,02:10:27,0:01:39,1900,69
Freeport,2W,Village of Freeport,02:12:34,02:13:04,0:02:07,2813,80
Baldwin,2W,Baldwin,02:14:47,02:15:17,0:01:43,2044,71
Rockville Centre,2W,Village of Rockville Centre,02:17:40,02:18:10,0:02:23,3342,84
Lynbrook,4W,Village of Lynbrook,02:20:07,02:20:37,0:00:57,2493,77
St. Albans,2N,Queens,02:26:05,02:26:35,0:05:28,9310,102
\pl Waypoint 1430400@0.765 ©,Pass,Stop 52,02:28:48,02:28:48,0:02:13,3246,88
Waypoint 1430800,,,02:29:05,02:29:05,0:00:17,478,101
Jamaica,3,Queens,02:29:55,02:30:25,0:00:50,921,66
Woodhaven,3W,Queens,02:32:49,02:33:19,0:02:24,3204,80
East New York,3W,Brooklyn,02:36:47,02:37:17,0:03:28,5227,90
Nostrand Av,2W,Brooklyn,02:39:56,02:40:26,0:02:39,3734,85
Atlantic Terminal,18W,Brooklyn,02:42:36,02:43:06,0:02:10,2358,65
Fulton St.,2N,Manhattan,02:46:27,02:46:57,0:03:21,5212,93
Hoboken,7W,Hoboken,02:50:07,02:50:37,0:03:10,4674,89
Newark Penn Station,8S,Newark,02:57:17,02:57:47,0:06:40,11365,102
Newark Liberty,1S,Newark,03:00:32,03:01:02,0:02:45,4061,89
North Elizabeth,1S,Elizabeth,03:03:14,03:03:44,0:02:12,2976,81
Elizabeth,1S,Elizabeth,03:05:12,03:05:42,0:01:28,1557,64
Linden,1S,Linden,03:09:06,03:09:36,0:03:24,5328,94
Rahway,1S,Rahway,03:11:57,03:12:27,0:02:21,3272,84
Metro Park,1S,Woodbridge Township,03:16:19,03:16:49,0:03:52,6238,97
Metuchen,2W,Metuchen,03:19:34,03:20:04,0:02:45,4052,88
Edison,2W,Edison,03:23:22,03:23:52,0:03:18,5128,93
New Brunswick,1S,New Brunswick,03:26:27,03:26:57,0:02:35,3731,87
Jersey Avenue,1S,New Brunswick,03:29:08,03:29:38,0:02:11,2947,81
North Brunswick,1S,North Brunswick Township |#| 02:10,03:32:52,03:35:32,0:03:14,4999,93
```
  
</details>


## Dependencies
* numpy
* pytesseract
* opencv

## How to use
Set UI scaling to 200%
Make a screen recording of the stops list in a NIMBY rails line as you scroll from the top to the bottom at a casual pace.
Now run the Python script passing in the path to the screen recording

```python main.py --in input-recording.mp4 --out output-file.csv```

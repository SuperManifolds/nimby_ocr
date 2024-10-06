# Nimby OCR

Uses optical character recognition to read stop timings from NIMBY Rails lines and generates a csv

## Dependencies
* numpy
* pytesseract
* opencv

## How to use
Make a screen recording of the stops list in a NIMBY rails line as you scroll from the top to the bottom at a casual pace.
Now run the Python script passing in the path to the screen recording

```python main.py --in input-recording.mp4 --out output-file.csv```

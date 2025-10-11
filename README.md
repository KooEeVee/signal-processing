# Pitch detection with FFT

## Peer Review 2
Use Flask UI in the browser to test the program. Project and the dependencies are managed with Poetry, so the libraries should be easy to install with poetry install.

To open the UI in the browser, go to src folder and type (console): poetry run python app.py

Features:
- choose the test signal with or without noise
- plot the test signal in time-domain or frequency domain
- detect the pitch from the test signal (Hz or note) - correct values for test signal are 440Hz and A4

Documentation work is in progress, but you can run the tests typing: poetry run pytest -v.

## Peer Review 1
Check the src/app.py for code documentation and instructions how to test the program. If you choose to try to run it, go to src: poetry run python app.py

Features:
- test the pitch detection with synthetic signals
- plot and listen the test signals - play_sound is commented off by default
- compare the pitch detection results achieved with numpy fft functions and fft algorithm
- change the test signals' pitch and see how it shows in the results
- add or reduce noise in the test signals to see how it interferes with the pitch detection

## Documentation

[Specification](https://github.com/KooEeVee/signal-processing/blob/main/documentation/specification.md)

## Weekly Reports

[Week 1](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week1.md)

[Week 2](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week2.md)

[Week 3](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week3.md)

[Week 4](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week4.md)

[Week 5](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week5.md)

[Week 6](https://github.com/KooEeVee/signal-processing/blob/main/documentation/weekly-reports/week6.md)

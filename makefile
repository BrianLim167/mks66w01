ppm: picmaker.py
	python3 picmaker.py

convert: picmaker.ppm
	convert picmaker.ppm picmaker.png

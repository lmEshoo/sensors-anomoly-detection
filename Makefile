

all: run

build:
	docker build --no-cache -t lmestar/armv71-torch-py3.6:0.1 .

run:
	docker run -it --rm \
		-v $(PWD):/app \
		--name final lmestar/armv71-torch-py3.6:0.1 \
		bash -c "cd /app/src/ && python3 test.py"
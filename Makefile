

all: run

build:
	docker build --no-cache -t lmestar/sklearn-alpine:2 .

build_arm:
	docker build --no-cache -t lmestar/armv71-torch-py3.6:0.1 -f Dockerfile.arm

run_arm:
	docker run -it --rm --cap-add SYS_RAWIO --device /dev/gpiomem \
	-v $(PWD):/app --name final lmestar/armv71-torch-py3.6:0.1 \
	bash -c "cd /app/src/ && python3 testing.py"

run:
	rm -rf outputs/*.png
	rm -rf outputs/*.html
	docker run -it \
	-v $(PWD):/app  lmestar/sklearn-alpine:2 \
	sh -c "cd /app/src/ && python3 one_class_svm_with_visualization.py && python3 kmeans_pca.py && python3 cluster_percentile.py"

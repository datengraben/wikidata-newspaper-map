#raw-data.csv: download-sparql-data.py
#	python3 download-sparql-data.py > raw-data.csv
#

all: show.html 

data:
	mkdir data

scripts/test-p291.rq scripts/test.rq scripts/test-hq.rq scripts/test-hq2.rq scripts/all_bdzv_papers_with_location_properties.rq: data query.sh

data/test-p291.data.csv: scripts/test-p291.rq
	sh query.sh scripts/test-p291.rq > data/test-p291.data.csv

data/test.data.csv: scripts/test.rq
	sh query.sh scripts/test.rq > data/test.data.csv

data/test-hq.data.csv: scripts/test-hq.rq
	sh query.sh scripts/test-hq.rq > data/test-hq.data.csv

data/test-hq2.data.csv: scripts/test-hq2.rq
	sh query.sh scripts/test-hq2.rq > data/test-hq2.data.csv

data/all_bdzv_papers_with_location_properties.data.csv: scripts/all_bdzv_papers_with_location_properties.rq
	sh query.sh scripts/all_bdzv_papers_with_location_properties.rq > data/all_bdzv_papers_with_location_properties.data.csv

nuts-merged-count.csv zeitungen-mit-nuts.csv generated-changelog.md: main.py data/test.data.csv data/test-hq.data.csv data/test-hq2.data.csv data/test-p291.data.csv data/all_bdzv_papers_with_location_properties.data.csv
	python3 main.py --verbose

changelog.md: generated-changelog.md
	cat changelog.md >> generated-changelog.md
	cp generated-changelog.md changelog.md

show.html: zeitungen-mit-nuts.csv nuts-merged-count.csv generate.sh generate-table.py head.html scripts.html header.html
	python3 generate-table.py > generated-index.html
	sh generate.sh
	
changelog.html: changelog.md
	pandoc -f markdown -t html -o changelog.html --standalone --metadata pagetitle="Changelog" changelog.md

clean:
	rm generated-changelog.md
	rm generated-index.html

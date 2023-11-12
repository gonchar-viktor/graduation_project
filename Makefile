test_chrome:
	pytest -s -v --reruns 1 -n 4 --headless=false --browser=chrome
test_chrome_headless:
	pytest -s -v --reruns 1 -n 4 --headless=true --browser=chrome
test_firefox:
	pytest -s -v --reruns 1 -n 4 --headless=false --browser=firefox
test_firefox_headless:
	pytest -s -v --reruns 1 -n 4 --headless=true --browser=firefox
test_edge:
	pytest -s -v --reruns 1 -n 4 --headless=false --browser=edge
test_edge_headless:
	pytest -s -v --reruns 1 -n 4 --headless=true --browser=edge


bind ?= localhost
port ?= 3000
serve:
	python -m http.server dist --bind $(bind) $(port)
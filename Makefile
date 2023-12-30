test_chrome:
	pytest -s -v --reruns 2 -n 4 --headless=false --browser=chrome --alluredir allure_results_chrome
test_chrome_headless:
	pytest -s -v --reruns 2 -n 4 --headless=true --browser=chrome --alluredir allure_results_chrome
test_edge:
	pytest -s -v --reruns 2 -n 4 --headless=false --browser=edge --alluredir allure_results_edge
test_edge_headless:
	pytest -s -v --reruns 2 -n 4 --headless=true --browser=edge --alluredir allure_results_edge

serve_results_chrome:
	allure serve allure_results_chrome
serve_results_edge:
	allure serve allure_results_edge

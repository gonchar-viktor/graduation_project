test_chrome:
	pytest -s -v --reruns 5 -n 4 --headless=false --browser=chrome --alluredir my_allure_results
test_chrome_headless:
	pytest -s -v --reruns 5 -n 4 --headless=true --browser=chrome --alluredir my_allure_results
test_edge:
	pytest -s -v --reruns 5 -n 4 --headless=false --browser=edge --alluredir my_allure_results
test_edge_headless:
	pytest -s -v --reruns 5 -n 4 --headless=true --browser=edge --alluredir my_allure_results
serve_results:
	allure serve my_allure_results

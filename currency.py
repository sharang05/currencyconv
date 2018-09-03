import requests


def Convert():
	res = requests.get("http://data.fixer.io/api/latest?access_key=18bfa087d7e77b59f23e3d7a3857d46a")
	if res.status_code != 200:
		raise Exception("Error: API Request unsuccessful")
	data = res.json()
	#print(data)
	rate = data["rates"]["USD"]
	print(type(rate))


def main():
	Convert()
	


if __name__ == '__main__':
	main()
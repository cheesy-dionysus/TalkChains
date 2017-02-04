setup:
	(npm -g install embark;
	npm -g install ethereumjs-testrpc;
	embark blockchain)

server:
	(cd app; python -m SimpleHTTPServer 3000;)
